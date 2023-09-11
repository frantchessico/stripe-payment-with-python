from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import stripe
import os

# Configure Stripe
stripe.api_key = "your_secret_key_here"  # Replace with your Stripe secret

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: int

@app.post("/create-payment-intent")
async def create_payment_intent(payment_request: PaymentRequest):
    try:
        intent = stripe.PaymentIntent.create(
            amount=payment_request.amount,
            currency="usd"
        )
        return {"message": "Payment intent created successfully", "payment_intent_id": intent.id, "amount": intent.amount}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/process-payment")
async def process_payment(request: Request):
    try:
        data = await request.json()
        token = data.get("token")
        amount = data.get("amount")

        if not token or not amount:
            raise HTTPException(status_code=400, detail="Invalid request data")

        intent = stripe.PaymentIntent.confirm(
            token,
            amount=amount,
            currency="usd"
        )

        return {"message": "Payment processed successfully"}

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

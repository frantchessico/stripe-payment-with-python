
# Stripe Payment API with FastAPI

This is an example of a FastAPI-based API in Python that allows you to create a payment intent with Stripe and process payments. The API is configured to accept POST requests and respond with details about the created payment intent or payment processing status.

## Prerequisites

- Python installed in your environment.
- FastAPI library installed. You can install it using pip: `pip install fastapi`.
- Stripe library installed. You can install it using pip: `pip install stripe`.

## Configuration

1. Set your Stripe secret key in the code. Replace `"your_secret_key_here"` with your actual Stripe secret key.

2. Run the FastAPI server:

   ```shell
   uvicorn app:app --host 0.0.0.0 --port 8080
   ```

The server will be running on port 8080.

## Endpoints

### 1. Create Payment Intent

- **URL:** `/create-payment-intent`
- **Method:** `POST`
- **Request Body (JSON):** 

  ```json
  {
      "amount": 1000
  }
  ```

- **Example Response:**

  ```json
  {
      "message": "Payment intent created successfully",
      "payment_intent_id": "pi_1234567890",
      "amount": 1000
  }
  ```

### 2. Process Payment

- **URL:** `/process-payment`
- **Method:** `POST`
- **Request Body (JSON):** 

  ```json
  {
      "token": "stripe_payment_token",
      "amount": 1000
  }
  ```

- **Example Response:**

  ```json
  {
      "message": "Payment processed successfully"
  }
  ```

## Workflow

1. To create a payment intent, make a POST request to `/create-payment-intent` with the desired payment amount in the request body.

2. The API will create a payment intent with Stripe based on the provided data and respond with the intent ID.

3. To process an actual payment, you should implement the client-side Stripe logic (e.g., in JavaScript) to collect card information and create a payment token. Then, make a POST request to `/process-payment` with the token and payment amount.

4. The API will confirm the payment intent using the received token and respond with a payment confirmation.

Ensure that you follow best security practices when handling sensitive information and payment details.

---

This is a simple example of a Stripe payment API with FastAPI in Python. Customize and enhance this code as needed to meet the specific requirements of your project.

## Developer By:

**Francisco Inoque**
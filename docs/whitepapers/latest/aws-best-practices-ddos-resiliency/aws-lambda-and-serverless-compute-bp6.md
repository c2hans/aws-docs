---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/aws-lambda-and-serverless-compute-bp6.html
---

# AWS Lambda and Serverless Compute (BP6)
<a name="aws-lambda-and-serverless-compute-bp6"></a>

 AWS Lambda automatically scales by running additional instances of your functions in response to incoming requests. Each function instance handles one request at a time, and Lambda can scale to thousands of concurrent executions within seconds.

 For DDoS resilience considerations with Lambda:
+ **[Reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)** – Set a reserved concurrency limit to help ensure your function has capacity available, even if other functions in the account are consuming concurrency.
+ **[Provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)** – Pre-initialize function instances to reduce cold start latency during traffic surges. This is particularly useful for latency-sensitive applications that might experience sudden traffic increases.
+ *Function URL throttling* – If using [Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html#urls-throttling), configure reserved concurrency to act as a throttle against excessive requests.
+ *[Amazon API Gateway](https://aws.amazon.com/api-gateway/) integration* – When Lambda is behind API Gateway, you benefit from the API Gateway built-in throttling (default 10,000 requests per second per Region) and can add AWS WAF for additional protection.

 Be aware that Lambda has account-level concurrency limits. A DDoS attack targeting one function could consume concurrency needed by other functions. Use reserved concurrency to isolate critical functions.

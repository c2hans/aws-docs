---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/function-urls.html
---

# AWS Lambda function URLs
<a name="function-urls"></a>

With [AWS Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html), you can simply attach an HTTPS endpoint to a Lambda function. Although Application Load Balancer and Amazon API Gateway cover a wide range of use cases, Lambda function URLs can be more efficient for some specific use cases.

## Lambda function URL use cases
<a name="function-url-use-cases"></a>

Consider Lambda function URLs for the following use cases:
+ **Lightweight microservices and webhooks** – Lambda function URLs are well-suited for handling discrete, independent microservices that can be fulfilled over simple HTTP requests. Examples of such tasks include webhook handlers that trigger actions, form validations, mobile payment processing, advertisement placements, and machine learning inference. The underlying principle is to use function URLs for lightweight and specific event-driven tasks where a single function can fulfill your requirements.
+ **Simplified deployment for single functions** – Implementing a single-function microservice with a public endpoint might not require the routing and security options available with Application Load Balancer and API Gateway. Instead, Lambda function URLs provide a streamlined path to getting your service up and running.

The following diagram demonstrates the direct link between HTTPS endpoints and a Lambda function that uses function URLs. The function URL makes the Lambda function accessible as an HTTP endpoint. The Lambda function contains the core logic to do the following:
+ Call external APIs, for example, Slack.
+ Integrate with other AWS services, for example, AWS Step Functions.
+ Generate a response, for example, uploading an object in Amazon Simple Storage Service (Amazon S3).

This capability enables creating HTTP-based endpoints with Lambda functions and function URLs without needing to configure and manage web servers. It highlights the simplicity and efficiency of using function URLs to expose Lambda functions as HTTP endpoints.

![Lambda function made available as HTTPs endpoint using Function URL feature.](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/images/guide-img/45387eb1-39dc-4dd7-a6b2-e3cd572b2949/images/43b20120-0b8b-4343-a8b1-eef9a3e022b2.png)

The following is an example of a POST request to a Lambda function URL using cURL:

`curl -v 'https://abcdefg.lambda-url.us-east-1.on.aws/?message=HelloWorld' -H 'content-type: application/json' -d '{ "example": "test" }'`

This example includes:
+ A JSON payload: `{"example": "test"}`
+ A query parameter: `message=HelloWorld`
+ Verbose output for request/response details

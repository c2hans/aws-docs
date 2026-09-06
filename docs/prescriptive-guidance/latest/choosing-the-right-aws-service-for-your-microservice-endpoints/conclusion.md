---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-the-right-aws-service-for-your-microservice-endpoints/conclusion.html
---

# Conclusion and resources
<a name="conclusion"></a>

This guide discusses Application Load Balancer, Amazon API Gateway, and AWS Lambda function URLs and their capabilities for creating HTTP endpoints. To choose the right AWS service for your microservices endpoints, carefully consider the capabilities and design considerations described in this guide.

Each service excels in specific scenarios. Application Load Balancer is ideal for scenarios such as hosting a scalable e-commerce website. In that scenario, Application Load Balancer efficiently distributes incoming traffic across multiple EC2 instances to ensure reliability and performance.

In contrast, API Gateway is used to create RESTful APIs for applications like a ride-booking app. In that scenario, API Gateway can seamlessly integrate with AWS Lambda functions and Amazon DynamoDB to handle backend logic and data storage.

For lightweight use cases such as exposing a webhook to process Stripe payment events, a Lambda function URL can be a good choice. In the lightweight use case, a function URL provides a simple and direct way to trigger Lambda functions without the overhead of a full API Gateway setup.

## Resources
<a name="resources"></a>

For additional information, see the following AWS service documentation and resources.

### AWS service documentation
<a name="9999999999999999aws-service--documentation.b715c4e7-f141-5a87-82fe-f2bfd9a8c2b8"></a>

For detailed guides, best practices, and hands-on tutorials, see the following AWS service documentation:
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+ [AWS Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)

### Other AWS resources
<a name="other-9999999999999999aws--resources.27fd1cce-16b4-58cf-82ff-0f2c26406a64"></a>

For more insights into microservices, see the following AWS resources:
+ [Architecting for scale with Amazon API Gateway private integrations](https://aws.amazon.com/blogs/compute/architecting-for-scale-with-amazon-api-gateway-private-integrations/)
+ [Comparing design approaches for building serverless microservices](https://aws.amazon.com/blogs/compute/comparing-design-approaches-for-building-serverless-microservices/)
+ [Implementing microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
+ [Microservices](https://aws.amazon.com/microservices/)
+ [What's the difference between monolithic and microservices architecture?](https://aws.amazon.com/compare/the-difference-between-monolithic-and-microservices-architecture/)

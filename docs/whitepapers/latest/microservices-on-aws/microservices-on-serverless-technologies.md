---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-serverless-technologies.html
---

# Microservices on serverless technologies
<a name="microservices-on-serverless-technologies"></a>

 Using microservices with serverless technologies can greatly decrease operational complexity. AWS Lambda and AWS Fargate, integrated with API Gateway, allows for the creation of fully serverless applications. As of [April 7, 2023](https://aws.amazon.com/about-aws/whats-new/2023/04/aws-lambda-response-payload-streaming/), Lambda functions can progressively stream response payloads back to the client, enhancing performance for web and mobile applications. Prior to this, Lambda-based applications using the traditional request-response invocation model had to generate and buffer the response before returning it to the client, which could delay the time to first byte. With response streaming, functions can send partial responses back to the client as they become ready, significantly improving the time to first byte, which web and mobile applications are especially sensitive to.

 Figure 4 demonstrates a serverless microservice architecture using AWS Lambda and managed services. This serverless architecture mitigates the need to design for scale and high availability, and reduces the effort needed for running and monitoring the underlying infrastructure.

![Diagram showing Serverless microservice using AWS Lambda](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/serverless-microservice-using-lambda.png)

 Figure 5 displays a similar serverless implementation using containers with AWS Fargate, removing concerns about underlying infrastructure. It also features Amazon Aurora Serverless, an on-demand, auto-scaling database that automatically adjusts capacity based on your application's requirements.

![Diagram showing serverless microservice using AWS Fargate](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/serverless-microservice-fargate.png)

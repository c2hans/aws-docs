---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/microservices-with-lambda.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Microservices with Lambda
<a name="microservices-with-lambda"></a>

![Cross-account architecture with API Gateways and Lambda functions in two AWS accounts.](https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/images/microservices-with-lambda.png)

* Architectural pattern for microservices with Lambda *

 The microservice architecture pattern is not bound to the typical three-tier architecture; however, this popular pattern can realize significant benefits from the use of serverless resources.

 In this architecture, each of the application components are decoupled and independently deployed and operated. An API created with Amazon API Gateway, and functions subsequently launched by AWS Lambda, is all that you need to build a microservice. Your team can use these services to decouple and fragment your environment to the level of granularity desired.

 In general, a microservices environment can introduce the following difficulties: repeated overhead for creating each new microservice, issues with optimizing server density and utilization, complexity of running multiple versions of multiple microservices simultaneously, and proliferation of client-side code requirements to integrate with many separate services.

 When you create microservices using serverless resources, these problems become less difficult to solve and, in some cases, simply disappear. The serverless microservices pattern lowers the barrier for the creation of each subsequent microservice (API Gateway even allows for the cloning of existing APIs, and usage of Lambda functions in other accounts). Optimizing server utilization is no longer relevant with this pattern. Finally, Amazon API Gateway provides programmatically generated client SDKs in a number of popular languages to reduce integration overhead.

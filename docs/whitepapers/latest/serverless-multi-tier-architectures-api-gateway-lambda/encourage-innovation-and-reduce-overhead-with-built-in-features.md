---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/encourage-innovation-and-reduce-overhead-with-built-in-features.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Encourage innovation and reduce overhead with built-in features
<a name="encourage-innovation-and-reduce-overhead-with-built-in-features"></a>

 The development cost to build any new application is an investment. Using API Gateway can reduce the amount of time required for certain development tasks and lower the total development cost, enabling organizations to more freely experiment and innovate.

 During initial application development phases, implementation of logging and metrics gathering are often neglected to deliver a new application more quickly. This can lead to technical debt and operational risk when deploying these features to an application running in production. Amazon API Gateway integrates seamlessly with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), which collects and processes raw data from API Gateway into readable, near real-time metrics for monitoring API execution. API Gateway also supports access logging with configurable reports, and [AWS X-Ray](https://aws.amazon.com/xray/) tracing for debugging. Each of these features requires no code to be written, and can be adjusted in applications running in production without risk to the core business logic.

 The overall lifetime of an application might be unknown, or it might be known to be short-lived. Creating a business case for building such applications can be made easier if your starting point already includes the managed features that API Gateway provides, and if you only incur infrastructure costs after your APIs begin receiving requests. For more information, refer to [Amazon API Gateway pricing](https://aws.amazon.com/api-gateway/pricing/).

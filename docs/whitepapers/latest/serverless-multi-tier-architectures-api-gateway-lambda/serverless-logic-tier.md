---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/serverless-logic-tier.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Serverless logic tier
<a name="serverless-logic-tier"></a>

 The logic tier of the three-tier architecture represents the brains of the application. This is where using Amazon API Gateway and AWS Lambda can have the most impact compared to a traditional, server-based implementation. The features of these two services enable you to build a serverless application that is highly available, scalable, and secure. In a traditional model, your application could require thousands of servers; however, by using Amazon API Gateway and AWS Lambda you are not responsible for server management in any capacity. In addition, by using these managed services together, you gain the following benefits:
+  **AWS Lambda:**
  +  No OS to choose, secure, patch, or manage
  +  No servers to right size, monitor, or scale
  +  Reduced risk to your cost from over-provisioning
  +  Reduced risk to your performance from under-provisioning
+  **Amazon API Gateway:**
  +  Simplified mechanisms to deploy, monitor, and secure APIs
  +  Improved API performance through caching and content delivery

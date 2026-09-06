---
source_url: https://docs.aws.amazon.com/whitepapers/latest/next-generation-oss/integration-enablement.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Integration enablement
<a name="integration-enablement"></a>

 Integration enablement aligns with the increasing focus of implementing modular OSS applications exposed via Open APIs, and the need to support dynamic exposure of network-as-a-service constructs towards enterprise or ecosystem partners. Collectively, this is enabled by [Amazon API Gateway](https://aws.amazon.com/api-gateway), which simplifies the development and deployment lifecycle of both internal and external APIs.

 The integration framework is enhanced by using [AWS Step Functions](https://aws.amazon.com/step-functions), which enables a coordinated state-machine implementation, and [Amazon EventBridge](https://aws.amazon.com/eventbridge) (EventBridge), which enables event-driven integration with other BSS/external applications as part of the OSS value-chain transaction. To enable a consistent, common, consumption layer, network operation or product/business teams can extract business insights via [Amazon Quick](https://aws.amazon.com/quicksight) (QuickSight), [Amazon Athena](https://aws.amazon.com/athena) and [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service). [Amazon S3](https://aws.amazon.com/s3) can be leveraged as common object storage across all OSS applications that can handle different network data formats, and serve as a foundation of a shared data unification layer.

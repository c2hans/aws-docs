---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_GatewayElbAccessLogDestination.html
---

# GatewayElbAccessLogDestination
<a name="API_GatewayElbAccessLogDestination"></a>

The destination where the access logs for a gateway's load balancers are delivered.

## Contents
<a name="API_GatewayElbAccessLogDestination_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="ECS-Type-GatewayElbAccessLogDestination-s3"></a>
The Amazon S3 destination for access logs.
Type: [GatewayElbAccessLogS3Destination](API_GatewayElbAccessLogS3Destination.md) object
Required: No

## See Also
<a name="API_GatewayElbAccessLogDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/GatewayElbAccessLogDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/GatewayElbAccessLogDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/GatewayElbAccessLogDestination)

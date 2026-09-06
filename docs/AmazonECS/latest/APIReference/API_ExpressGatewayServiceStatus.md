---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ExpressGatewayServiceStatus.html
---

# ExpressGatewayServiceStatus
<a name="API_ExpressGatewayServiceStatus"></a>

An object that defines the status of Express service creation and information about the status of the service.

## Contents
<a name="API_ExpressGatewayServiceStatus_Contents"></a>

 ** statusCode **   <a name="ECS-Type-ExpressGatewayServiceStatus-statusCode"></a>
The status of the Express service.
Type: String
Valid Values: `ACTIVE | DRAINING | INACTIVE`
Required: No

 ** statusReason **   <a name="ECS-Type-ExpressGatewayServiceStatus-statusReason"></a>
Information about why the Express service is in the current status.
Type: String
Required: No

## See Also
<a name="API_ExpressGatewayServiceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ExpressGatewayServiceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ExpressGatewayServiceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ExpressGatewayServiceStatus)

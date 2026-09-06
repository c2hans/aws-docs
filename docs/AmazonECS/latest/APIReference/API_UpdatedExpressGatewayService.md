---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdatedExpressGatewayService.html
---

# UpdatedExpressGatewayService
<a name="API_UpdatedExpressGatewayService"></a>

An object that describes an Express service to be updated.

## Contents
<a name="API_UpdatedExpressGatewayService_Contents"></a>

 ** cluster **   <a name="ECS-Type-UpdatedExpressGatewayService-cluster"></a>
The cluster associated with the Express service that is being updated.
Type: String
Required: No

 ** createdAt **   <a name="ECS-Type-UpdatedExpressGatewayService-createdAt"></a>
The Unix timestamp for when the Express service that is being updated was created.
Type: Timestamp
Required: No

 ** serviceArn **   <a name="ECS-Type-UpdatedExpressGatewayService-serviceArn"></a>
The ARN of the Express service that is being updated.
Type: String
Required: No

 ** serviceName **   <a name="ECS-Type-UpdatedExpressGatewayService-serviceName"></a>
The name of the Express service that is being updated.
Type: String
Required: No

 ** status **   <a name="ECS-Type-UpdatedExpressGatewayService-status"></a>
The status of the Express service that is being updated.
Type: [ExpressGatewayServiceStatus](API_ExpressGatewayServiceStatus.md) object
Required: No

 ** targetConfiguration **   <a name="ECS-Type-UpdatedExpressGatewayService-targetConfiguration"></a>
The configuration to which the current Express service is being updated to.
Type: [ExpressGatewayServiceConfiguration](API_ExpressGatewayServiceConfiguration.md) object
Required: No

 ** updatedAt **   <a name="ECS-Type-UpdatedExpressGatewayService-updatedAt"></a>
The Unix timestamp for when the Express service that is being updated was most recently updated.
Type: Timestamp
Required: No

## See Also
<a name="API_UpdatedExpressGatewayService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/UpdatedExpressGatewayService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/UpdatedExpressGatewayService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/UpdatedExpressGatewayService)

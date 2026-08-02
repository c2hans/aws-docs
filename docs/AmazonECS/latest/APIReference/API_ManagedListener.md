---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedListener.html
---

# ManagedListener
<a name="API_ManagedListener"></a>

The listeners associated with the Express service's Application Load Balancer.

## Contents
<a name="API_ManagedListener_Contents"></a>

 ** status **   <a name="ECS-Type-ManagedListener-status"></a>
The status of the load balancer listener.
Type: String
Valid Values: `PROVISIONING | ACTIVE | DEPROVISIONING | DELETED | FAILED`
Required: Yes

 ** updatedAt **   <a name="ECS-Type-ManagedListener-updatedAt"></a>
The Unix timestamp for when this listener was most recently updated.
Type: Timestamp
Required: Yes

 ** arn **   <a name="ECS-Type-ManagedListener-arn"></a>
The Amazon Resource Name (ARN) of the load balancer listener.
Type: String
Required: No

 ** statusReason **   <a name="ECS-Type-ManagedListener-statusReason"></a>
Informaion about why the load balancer listener is in the current status.
Type: String
Required: No

## See Also
<a name="API_ManagedListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ManagedListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ManagedListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ManagedListener)

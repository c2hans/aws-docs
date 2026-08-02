---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectTestTrafficRules.html
---

# ServiceConnectTestTrafficRules
<a name="API_ServiceConnectTestTrafficRules"></a>

The test traffic routing configuration for Amazon ECS blue/green deployments. This configuration allows you to define rules for routing specific traffic to the new service revision during the deployment process, allowing for safe testing before full production traffic shift.

For more information, see [Service Connect for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-blue-green.html) in the * Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_ServiceConnectTestTrafficRules_Contents"></a>

 ** header **   <a name="ECS-Type-ServiceConnectTestTrafficRules-header"></a>
The HTTP header-based routing rules that determine which requests should be routed to the new service version during blue/green deployment testing. These rules provide fine-grained control over test traffic routing based on request headers.
Type: [ServiceConnectTestTrafficHeaderRules](API_ServiceConnectTestTrafficHeaderRules.md) object
Required: Yes

## See Also
<a name="API_ServiceConnectTestTrafficRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectTestTrafficRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectTestTrafficRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectTestTrafficRules)

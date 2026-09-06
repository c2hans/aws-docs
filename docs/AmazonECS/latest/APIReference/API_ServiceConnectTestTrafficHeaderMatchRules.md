---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectTestTrafficHeaderMatchRules.html
---

# ServiceConnectTestTrafficHeaderMatchRules
<a name="API_ServiceConnectTestTrafficHeaderMatchRules"></a>

The header matching rules for test traffic routing in Amazon ECS blue/green deployments. These rules determine how incoming requests are matched based on HTTP headers to route test traffic to the new service revision.

## Contents
<a name="API_ServiceConnectTestTrafficHeaderMatchRules_Contents"></a>

 ** exact **   <a name="ECS-Type-ServiceConnectTestTrafficHeaderMatchRules-exact"></a>
The exact value that the HTTP header must match for the test traffic routing rule to apply. This provides precise control over which requests are routed to the new service revision during blue/green deployments.
Type: String
Required: Yes

## See Also
<a name="API_ServiceConnectTestTrafficHeaderMatchRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectTestTrafficHeaderMatchRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectTestTrafficHeaderMatchRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectTestTrafficHeaderMatchRules)

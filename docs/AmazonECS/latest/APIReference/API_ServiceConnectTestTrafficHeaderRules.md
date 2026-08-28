---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ServiceConnectTestTrafficHeaderRules.html
---

# ServiceConnectTestTrafficHeaderRules
<a name="API_ServiceConnectTestTrafficHeaderRules"></a>

The HTTP header rules used to identify and route test traffic during Amazon ECS blue/green deployments. These rules specify which HTTP headers to examine and what values to match for routing decisions.

For more information, see [Service Connect for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect-blue-green.html) in the * Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_ServiceConnectTestTrafficHeaderRules_Contents"></a>

 ** name **   <a name="ECS-Type-ServiceConnectTestTrafficHeaderRules-name"></a>
The name of the HTTP header to examine for test traffic routing. Common examples include custom headers like `X-Test-Version` or `X-Canary-Request` that can be used to identify test traffic.
Type: String
Required: Yes

 ** value **   <a name="ECS-Type-ServiceConnectTestTrafficHeaderRules-value"></a>
The header value matching configuration that determines how the HTTP header value is evaluated for test traffic routing decisions.
Type: [ServiceConnectTestTrafficHeaderMatchRules](API_ServiceConnectTestTrafficHeaderMatchRules.md) object
Required: No

## See Also
<a name="API_ServiceConnectTestTrafficHeaderRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ServiceConnectTestTrafficHeaderRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ServiceConnectTestTrafficHeaderRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ServiceConnectTestTrafficHeaderRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

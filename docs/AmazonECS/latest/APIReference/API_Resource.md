---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Describes the resources available for a container instance.

## Contents
<a name="API_Resource_Contents"></a>

 ** doubleValue **   <a name="ECS-Type-Resource-doubleValue"></a>
When the `doubleValue` type is set, the value of the resource must be a double precision floating-point type.
Type: Double
Required: No

 ** integerValue **   <a name="ECS-Type-Resource-integerValue"></a>
When the `integerValue` type is set, the value of the resource must be an integer.
Type: Integer
Required: No

 ** longValue **   <a name="ECS-Type-Resource-longValue"></a>
When the `longValue` type is set, the value of the resource must be an extended precision floating-point type.
Type: Long
Required: No

 ** name **   <a name="ECS-Type-Resource-name"></a>
The name of the resource, such as `CPU`, `MEMORY`, `PORTS`, `PORTS_UDP`, or a user-defined resource.
Type: String
Required: No

 ** stringSetValue **   <a name="ECS-Type-Resource-stringSetValue"></a>
When the `stringSetValue` type is set, the value of the resource must be a string type.
Type: Array of strings
Required: No

 ** type **   <a name="ECS-Type-Resource-type"></a>
The type of the resource. Valid values: `INTEGER`, `DOUBLE`, `LONG`, or `STRINGSET`.
Type: String
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

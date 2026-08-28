---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_UnsupportedResource.html
---

# UnsupportedResource
<a name="API_UnsupportedResource"></a>

Defines a resource that is not supported by AWS Resilience Hub.

## Contents
<a name="API_UnsupportedResource_Contents"></a>

 ** logicalResourceId **   <a name="resiliencehub-Type-UnsupportedResource-logicalResourceId"></a>
Logical resource identifier for the unsupported resource.
Type: [LogicalResourceId](API_LogicalResourceId.md) object
Required: Yes

 ** physicalResourceId **   <a name="resiliencehub-Type-UnsupportedResource-physicalResourceId"></a>
Physical resource identifier for the unsupported resource.
Type: [PhysicalResourceId](API_PhysicalResourceId.md) object
Required: Yes

 ** resourceType **   <a name="resiliencehub-Type-UnsupportedResource-resourceType"></a>
The type of resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** unsupportedResourceStatus **   <a name="resiliencehub-Type-UnsupportedResource-unsupportedResourceStatus"></a>
The status of the unsupported resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_UnsupportedResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/UnsupportedResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/UnsupportedResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/UnsupportedResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

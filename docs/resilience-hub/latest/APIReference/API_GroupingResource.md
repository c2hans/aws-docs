---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_GroupingResource.html
---

# GroupingResource
<a name="API_GroupingResource"></a>

Indicates the resource that will be grouped in the recommended Application Component (AppComponent).

## Contents
<a name="API_GroupingResource_Contents"></a>

 ** logicalResourceId **   <a name="resiliencehub-Type-GroupingResource-logicalResourceId"></a>
Indicates the logical identifier of the resource.
Type: [LogicalResourceId](API_LogicalResourceId.md) object
Required: Yes

 ** physicalResourceId **   <a name="resiliencehub-Type-GroupingResource-physicalResourceId"></a>
Indicates the physical identifier of the resource.
Type: [PhysicalResourceId](API_PhysicalResourceId.md) object
Required: Yes

 ** resourceName **   <a name="resiliencehub-Type-GroupingResource-resourceName"></a>
Indicates the resource name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** resourceType **   <a name="resiliencehub-Type-GroupingResource-resourceType"></a>
Indicates the resource type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** sourceAppComponentIds **   <a name="resiliencehub-Type-GroupingResource-sourceAppComponentIds"></a>
Indicates the identifier of the source AppComponents in which the resources were previously grouped into.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_GroupingResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/GroupingResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/GroupingResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/GroupingResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTarget.html
---

# ExperimentTarget
<a name="API_ExperimentTarget"></a>

Describes a target for an experiment.

## Contents
<a name="API_ExperimentTarget_Contents"></a>

 ** filters **   <a name="fis-Type-ExperimentTarget-filters"></a>
The filters to apply to identify target resources using specific attributes.
Type: Array of [ExperimentTargetFilter](API_ExperimentTargetFilter.md) objects
Required: No

 ** parameters **   <a name="fis-Type-ExperimentTarget-parameters"></a>
The resource type parameters.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** resourceArns **   <a name="fis-Type-ExperimentTarget-resourceArns"></a>
The Amazon Resource Names (ARNs) of the resources.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** resourceTags **   <a name="fis-Type-ExperimentTarget-resourceTags"></a>
The tags for the target resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** resourceType **   <a name="fis-Type-ExperimentTarget-resourceType"></a>
The resource type.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** selectionMode **   <a name="fis-Type-ExperimentTarget-selectionMode"></a>
Scopes the identified resources to a specific count or percentage.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

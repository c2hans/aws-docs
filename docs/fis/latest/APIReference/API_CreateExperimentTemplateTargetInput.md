---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplateTargetInput.html
---

# CreateExperimentTemplateTargetInput
<a name="API_CreateExperimentTemplateTargetInput"></a>

Specifies a target for an experiment. You must specify at least one Amazon Resource Name (ARN) or at least one resource tag. You cannot specify both ARNs and tags.

For more information, see [Targets](https://docs.aws.amazon.com/fis/latest/userguide/targets.html) in the * AWS Fault Injection Service User Guide*.

## Contents
<a name="API_CreateExperimentTemplateTargetInput_Contents"></a>

 ** resourceType **   <a name="fis-Type-CreateExperimentTemplateTargetInput-resourceType"></a>
The resource type. The resource type must be supported for the specified action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: Yes

 ** selectionMode **   <a name="fis-Type-CreateExperimentTemplateTargetInput-selectionMode"></a>
Scopes the identified resources to a specific count of the resources at random, or a percentage of the resources. All identified resources are included in the target.
+ ALL - Run the action on all identified targets. This is the default.
+ COUNT(n) - Run the action on the specified number of targets, chosen from the identified targets at random. For example, COUNT(1) selects one of the targets.
+ PERCENT(n) - Run the action on the specified percentage of targets, chosen from the identified targets at random. For example, PERCENT(25) selects 25% of the targets.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: Yes

 ** filters **   <a name="fis-Type-CreateExperimentTemplateTargetInput-filters"></a>
The filters to apply to identify target resources using specific attributes.
Type: Array of [ExperimentTemplateTargetInputFilter](API_ExperimentTemplateTargetInputFilter.md) objects
Required: No

 ** parameters **   <a name="fis-Type-CreateExperimentTemplateTargetInput-parameters"></a>
The resource type parameters.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]+$`
Required: No

 ** resourceArns **   <a name="fis-Type-CreateExperimentTemplateTargetInput-resourceArns"></a>
The Amazon Resource Names (ARNs) of the resources.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** resourceTags **   <a name="fis-Type-CreateExperimentTemplateTargetInput-resourceTags"></a>
The tags for the target resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_CreateExperimentTemplateTargetInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/CreateExperimentTemplateTargetInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/CreateExperimentTemplateTargetInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/CreateExperimentTemplateTargetInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

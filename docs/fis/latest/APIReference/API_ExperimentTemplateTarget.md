---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplateTarget.html
---

# ExperimentTemplateTarget
<a name="API_ExperimentTemplateTarget"></a>

Describes a target for an experiment template.

## Contents
<a name="API_ExperimentTemplateTarget_Contents"></a>

 ** filters **   <a name="fis-Type-ExperimentTemplateTarget-filters"></a>
The filters to apply to identify target resources using specific attributes.
Type: Array of [ExperimentTemplateTargetFilter](API_ExperimentTemplateTargetFilter.md) objects
Required: No

 ** parameters **   <a name="fis-Type-ExperimentTemplateTarget-parameters"></a>
The resource type parameters.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]+$`
Required: No

 ** resourceArns **   <a name="fis-Type-ExperimentTemplateTarget-resourceArns"></a>
The Amazon Resource Names (ARNs) of the targets.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

 ** resourceTags **   <a name="fis-Type-ExperimentTemplateTarget-resourceTags"></a>
The tags for the target resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 128.
Key Pattern: `[\s\S]+`
Value Length Constraints: Maximum length of 256.
Value Pattern: `[\s\S]*`
Required: No

 ** resourceType **   <a name="fis-Type-ExperimentTemplateTarget-resourceType"></a>
The resource type.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** selectionMode **   <a name="fis-Type-ExperimentTemplateTarget-selectionMode"></a>
Scopes the identified resources to a specific count or percentage.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ExperimentTemplateTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ExperimentTemplateTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ExperimentTemplateTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ExperimentTemplateTarget)

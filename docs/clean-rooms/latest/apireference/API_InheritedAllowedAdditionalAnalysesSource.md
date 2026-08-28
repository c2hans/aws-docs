---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedAllowedAdditionalAnalysesSource.html
---

# InheritedAllowedAdditionalAnalysesSource
<a name="API_InheritedAllowedAdditionalAnalysesSource"></a>

Contains information about a parent table that contributes an allowed additional analyses constraint.

## Contents
<a name="API_InheritedAllowedAdditionalAnalysesSource_Contents"></a>

 ** id **   <a name="API-Type-InheritedAllowedAdditionalAnalysesSource-id"></a>
The unique identifier of the parent table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-InheritedAllowedAdditionalAnalysesSource-name"></a>
The name of the parent table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** sourceAccountId **   <a name="API-Type-InheritedAllowedAdditionalAnalysesSource-sourceAccountId"></a>
The AWS account ID of the member who owns the parent table.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** type **   <a name="API-Type-InheritedAllowedAdditionalAnalysesSource-type"></a>
The type of the parent table.
Type: String
Valid Values: `TABLE | INTERMEDIATE_TABLE | ID_MAPPING_TABLE`
Required: Yes

 ** value **   <a name="API-Type-InheritedAllowedAdditionalAnalysesSource-value"></a>
The allowed additional analyses defined on the parent table.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:([\d]{12}|\*):membership\/[\*\d\w-]+\/configuredaudiencemodelassociation\/[\*\d\w-]+$|^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:([0-9]{12}|\*):membership\/[\*\d\w-]+\/configured-model-algorithm-association\/([-a-zA-Z0-9_\/.]+|\*)`
Required: Yes

## See Also
<a name="API_InheritedAllowedAdditionalAnalysesSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalysesSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalysesSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedAllowedAdditionalAnalysesSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_InheritedAdditionalAnalysesSource.html
---

# InheritedAdditionalAnalysesSource
<a name="API_InheritedAdditionalAnalysesSource"></a>

Contains information about a parent table that contributes an additional analyses constraint.

## Contents
<a name="API_InheritedAdditionalAnalysesSource_Contents"></a>

 ** id **   <a name="API-Type-InheritedAdditionalAnalysesSource-id"></a>
The unique identifier of the parent table.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-InheritedAdditionalAnalysesSource-name"></a>
The name of the parent table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** sourceAccountId **   <a name="API-Type-InheritedAdditionalAnalysesSource-sourceAccountId"></a>
The AWS account ID of the member who owns the parent table.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** type **   <a name="API-Type-InheritedAdditionalAnalysesSource-type"></a>
The type of the parent table.
Type: String
Valid Values: `TABLE | INTERMEDIATE_TABLE | ID_MAPPING_TABLE`
Required: Yes

 ** value **   <a name="API-Type-InheritedAdditionalAnalysesSource-value"></a>
The additional analyses setting defined on the parent table.
Type: String
Valid Values: `ALLOWED | REQUIRED | NOT_ALLOWED`
Required: Yes

## See Also
<a name="API_InheritedAdditionalAnalysesSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/InheritedAdditionalAnalysesSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/InheritedAdditionalAnalysesSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/InheritedAdditionalAnalysesSource)

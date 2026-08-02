---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisTemplateSummary.html
---

# AnalysisTemplateSummary
<a name="API_AnalysisTemplateSummary"></a>

The metadata of the analysis template.

## Contents
<a name="API_AnalysisTemplateSummary_Contents"></a>

 ** arn **   <a name="API-Type-AnalysisTemplateSummary-arn"></a>
The Amazon Resource Name (ARN) of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-AnalysisTemplateSummary-collaborationArn"></a>
The unique ARN for the analysis template summary’s associated collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-AnalysisTemplateSummary-collaborationId"></a>
A unique identifier for the collaboration that the analysis template summary belongs to. Currently accepts collaboration ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-AnalysisTemplateSummary-createTime"></a>
The time that the analysis template summary was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="API-Type-AnalysisTemplateSummary-id"></a>
The identifier of the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-AnalysisTemplateSummary-membershipArn"></a>
The Amazon Resource Name (ARN) of the member who created the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-AnalysisTemplateSummary-membershipId"></a>
The identifier for a membership resource.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-AnalysisTemplateSummary-name"></a>
The name of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** updateTime **   <a name="API-Type-AnalysisTemplateSummary-updateTime"></a>
The time that the analysis template summary was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-AnalysisTemplateSummary-description"></a>
The description of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** isSyntheticData **   <a name="API-Type-AnalysisTemplateSummary-isSyntheticData"></a>
Indicates if this analysis template summary generated synthetic data.
Type: Boolean
Required: No

## See Also
<a name="API_AnalysisTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisTemplateSummary)

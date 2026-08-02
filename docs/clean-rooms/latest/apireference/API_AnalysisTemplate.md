---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisTemplate.html
---

# AnalysisTemplate
<a name="API_AnalysisTemplate"></a>

The analysis template.

## Contents
<a name="API_AnalysisTemplate_Contents"></a>

 ** arn **   <a name="API-Type-AnalysisTemplate-arn"></a>
The Amazon Resource Name (ARN) of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-AnalysisTemplate-collaborationArn"></a>
The unique ARN for the analysis template’s associated collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-AnalysisTemplate-collaborationId"></a>
The unique ID for the associated collaboration of the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-AnalysisTemplate-createTime"></a>
The time that the analysis template was created.
Type: Timestamp
Required: Yes

 ** format **   <a name="API-Type-AnalysisTemplate-format"></a>
The format of the analysis template.
Type: String
Valid Values: `SQL | PYSPARK_1_0`
Required: Yes

 ** id **   <a name="API-Type-AnalysisTemplate-id"></a>
The identifier for the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** membershipArn **   <a name="API-Type-AnalysisTemplate-membershipArn"></a>
The Amazon Resource Name (ARN) of the member who created the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+`
Required: Yes

 ** membershipId **   <a name="API-Type-AnalysisTemplate-membershipId"></a>
The identifier of a member who created the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-AnalysisTemplate-name"></a>
The name of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** schema **   <a name="API-Type-AnalysisTemplate-schema"></a>
The entire schema object.
Type: [AnalysisSchema](API_AnalysisSchema.md) object
Required: Yes

 ** source **   <a name="API-Type-AnalysisTemplate-source"></a>
The source of the analysis template.
Type: [AnalysisSource](API_AnalysisSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** updateTime **   <a name="API-Type-AnalysisTemplate-updateTime"></a>
The time that the analysis template was last updated.
Type: Timestamp
Required: Yes

 ** analysisParameters **   <a name="API-Type-AnalysisTemplate-analysisParameters"></a>
The parameters of the analysis template.
Type: Array of [AnalysisParameter](API_AnalysisParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** description **   <a name="API-Type-AnalysisTemplate-description"></a>
The description of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** errorMessageConfiguration **   <a name="API-Type-AnalysisTemplate-errorMessageConfiguration"></a>
The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to `DETAILED`, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.
Type: [ErrorMessageConfiguration](API_ErrorMessageConfiguration.md) object
Required: No

 ** sourceMetadata **   <a name="API-Type-AnalysisTemplate-sourceMetadata"></a>
 The source metadata for the analysis template.
Type: [AnalysisSourceMetadata](API_AnalysisSourceMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** syntheticDataParameters **   <a name="API-Type-AnalysisTemplate-syntheticDataParameters"></a>
The parameters used to generate synthetic data for this analysis template.
Type: [SyntheticDataParameters](API_SyntheticDataParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** validations **   <a name="API-Type-AnalysisTemplate-validations"></a>
Information about the validations performed on the analysis template.
Type: Array of [AnalysisTemplateValidationStatusDetail](API_AnalysisTemplateValidationStatusDetail.md) objects
Required: No

## See Also
<a name="API_AnalysisTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisTemplate)

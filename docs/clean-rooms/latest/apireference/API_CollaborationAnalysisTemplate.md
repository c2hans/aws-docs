---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationAnalysisTemplate.html
---

# CollaborationAnalysisTemplate
<a name="API_CollaborationAnalysisTemplate"></a>

The analysis template within a collaboration.

## Contents
<a name="API_CollaborationAnalysisTemplate_Contents"></a>

 ** arn **   <a name="API-Type-CollaborationAnalysisTemplate-arn"></a>
The Amazon Resource Name (ARN) of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-CollaborationAnalysisTemplate-collaborationArn"></a>
The unique ARN for the analysis template’s associated collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationAnalysisTemplate-collaborationId"></a>
A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationAnalysisTemplate-createTime"></a>
The time that the analysis template within a collaboration was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationAnalysisTemplate-creatorAccountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** format **   <a name="API-Type-CollaborationAnalysisTemplate-format"></a>
The format of the analysis template in the collaboration.
Type: String
Valid Values: `SQL | PYSPARK_1_0`
Required: Yes

 ** id **   <a name="API-Type-CollaborationAnalysisTemplate-id"></a>
The identifier of the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-CollaborationAnalysisTemplate-name"></a>
The name of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** schema **   <a name="API-Type-CollaborationAnalysisTemplate-schema"></a>
The entire schema object.
Type: [AnalysisSchema](API_AnalysisSchema.md) object
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationAnalysisTemplate-updateTime"></a>
The time that the analysis template in the collaboration was last updated.
Type: Timestamp
Required: Yes

 ** analysisParameters **   <a name="API-Type-CollaborationAnalysisTemplate-analysisParameters"></a>
The analysis parameters that have been specified in the analysis template.
Type: Array of [AnalysisParameter](API_AnalysisParameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** description **   <a name="API-Type-CollaborationAnalysisTemplate-description"></a>
The description of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** errorMessageConfiguration **   <a name="API-Type-CollaborationAnalysisTemplate-errorMessageConfiguration"></a>
The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to `DETAILED`, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.
Type: [ErrorMessageConfiguration](API_ErrorMessageConfiguration.md) object
Required: No

 ** source **   <a name="API-Type-CollaborationAnalysisTemplate-source"></a>
The source of the analysis template within a collaboration.
Type: [AnalysisSource](API_AnalysisSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** sourceMetadata **   <a name="API-Type-CollaborationAnalysisTemplate-sourceMetadata"></a>
 The source metadata for the collaboration analysis template.
Type: [AnalysisSourceMetadata](API_AnalysisSourceMetadata.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** syntheticDataParameters **   <a name="API-Type-CollaborationAnalysisTemplate-syntheticDataParameters"></a>
The synthetic data generation parameters configured for this collaboration analysis template.
Type: [SyntheticDataParameters](API_SyntheticDataParameters.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** validations **   <a name="API-Type-CollaborationAnalysisTemplate-validations"></a>
The validations that were performed.
Type: Array of [AnalysisTemplateValidationStatusDetail](API_AnalysisTemplateValidationStatusDetail.md) objects
Required: No

## See Also
<a name="API_CollaborationAnalysisTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationAnalysisTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationAnalysisTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationAnalysisTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

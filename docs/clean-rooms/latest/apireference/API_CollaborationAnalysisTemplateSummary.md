---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CollaborationAnalysisTemplateSummary.html
---

# CollaborationAnalysisTemplateSummary
<a name="API_CollaborationAnalysisTemplateSummary"></a>

The metadata of the analysis template within a collaboration.

## Contents
<a name="API_CollaborationAnalysisTemplateSummary_Contents"></a>

 ** arn **   <a name="API-Type-CollaborationAnalysisTemplateSummary-arn"></a>
The Amazon Resource Name (ARN) of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** collaborationArn **   <a name="API-Type-CollaborationAnalysisTemplateSummary-collaborationArn"></a>
The unique ARN for the analysis template’s associated collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `arn:aws:[\w]+:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:collaboration/[\d\w-]+`
Required: Yes

 ** collaborationId **   <a name="API-Type-CollaborationAnalysisTemplateSummary-collaborationId"></a>
A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationAnalysisTemplateSummary-createTime"></a>
The time that the summary of the analysis template in a collaboration was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationAnalysisTemplateSummary-creatorAccountId"></a>
The identifier used to reference members of the collaboration. Currently only supports AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** id **   <a name="API-Type-CollaborationAnalysisTemplateSummary-id"></a>
The identifier of the analysis template.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-CollaborationAnalysisTemplateSummary-name"></a>
The name of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationAnalysisTemplateSummary-updateTime"></a>
The time that the summary of the analysis template in the collaboration was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-CollaborationAnalysisTemplateSummary-description"></a>
The description of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** isSyntheticData **   <a name="API-Type-CollaborationAnalysisTemplateSummary-isSyntheticData"></a>
Indicates if this collaboration analysis template uses synthetic data generation.
Type: Boolean
Required: No

## See Also
<a name="API_CollaborationAnalysisTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/CollaborationAnalysisTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/CollaborationAnalysisTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/CollaborationAnalysisTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetCollaborationAnalysisTemplateError.html
---

# BatchGetCollaborationAnalysisTemplateError
<a name="API_BatchGetCollaborationAnalysisTemplateError"></a>

Details of errors thrown by the call to retrieve multiple analysis templates within a collaboration by their identifiers.

## Contents
<a name="API_BatchGetCollaborationAnalysisTemplateError_Contents"></a>

 ** arn **   <a name="API-Type-BatchGetCollaborationAnalysisTemplateError-arn"></a>
The Amazon Resource Name (ARN) of the analysis template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: Yes

 ** code **   <a name="API-Type-BatchGetCollaborationAnalysisTemplateError-code"></a>
An error code for the error.
Type: String
Required: Yes

 ** message **   <a name="API-Type-BatchGetCollaborationAnalysisTemplateError-message"></a>
A description of why the call failed.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetCollaborationAnalysisTemplateError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/BatchGetCollaborationAnalysisTemplateError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/BatchGetCollaborationAnalysisTemplateError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/BatchGetCollaborationAnalysisTemplateError)

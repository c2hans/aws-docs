---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisTemplateArtifacts.html
---

# AnalysisTemplateArtifacts
<a name="API_AnalysisTemplateArtifacts"></a>

The analysis template artifacts.

## Contents
<a name="API_AnalysisTemplateArtifacts_Contents"></a>

 ** entryPoint **   <a name="API-Type-AnalysisTemplateArtifacts-entryPoint"></a>
 The entry point for the analysis template artifacts.
Type: [AnalysisTemplateArtifact](API_AnalysisTemplateArtifact.md) object
Required: Yes

 ** roleArn **   <a name="API-Type-AnalysisTemplateArtifacts-roleArn"></a>
 The role ARN for the analysis template artifacts.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
Required: Yes

 ** additionalArtifacts **   <a name="API-Type-AnalysisTemplateArtifacts-additionalArtifacts"></a>
 Additional artifacts for the analysis template.
Type: Array of [AnalysisTemplateArtifact](API_AnalysisTemplateArtifact.md) objects
Array Members: Fixed number of 1 item.
Required: No

## See Also
<a name="API_AnalysisTemplateArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisTemplateArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisTemplateArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisTemplateArtifacts)

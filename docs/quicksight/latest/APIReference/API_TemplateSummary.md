---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateSummary.html
---

# TemplateSummary
<a name="API_TemplateSummary"></a>

The template summary.

## Contents
<a name="API_TemplateSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-TemplateSummary-Arn"></a>
A summary of a template.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-TemplateSummary-CreatedTime"></a>
The last time that this template was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-TemplateSummary-LastUpdatedTime"></a>
The last time that this template was updated.
Type: Timestamp
Required: No

 ** LatestVersionNumber **   <a name="QS-Type-TemplateSummary-LatestVersionNumber"></a>
A structure containing a list of version numbers for the template summary.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** Name **   <a name="QS-Type-TemplateSummary-Name"></a>
A display name for the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** TemplateId **   <a name="QS-Type-TemplateSummary-TemplateId"></a>
The ID of the template. This ID is unique per AWS Region for each AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

## See Also
<a name="API_TemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateSummary)

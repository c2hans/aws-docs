---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation_VideoExtractionCategory.html
---

# VideoExtractionCategory
<a name="API_data-automation_VideoExtractionCategory"></a>

Settings for generating categorical data from video.

## Contents
<a name="API_data-automation_VideoExtractionCategory_Contents"></a>

 ** state **   <a name="bedrock-Type-data-automation_VideoExtractionCategory-state"></a>
Whether generating categorical data from video is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** types **   <a name="bedrock-Type-data-automation_VideoExtractionCategory-types"></a>
The types of data to generate.
Type: Array of strings
Valid Values: `CONTENT_MODERATION | TEXT_DETECTION | TRANSCRIPT | LOGOS`
Required: No

## See Also
<a name="API_data-automation_VideoExtractionCategory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/VideoExtractionCategory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/VideoExtractionCategory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/VideoExtractionCategory)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

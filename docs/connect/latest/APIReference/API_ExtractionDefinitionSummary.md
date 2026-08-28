---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ExtractionDefinitionSummary.html
---

# ExtractionDefinitionSummary
<a name="API_ExtractionDefinitionSummary"></a>

Summary information about an extraction definition.

## Contents
<a name="API_ExtractionDefinitionSummary_Contents"></a>

 ** CreatedTime **   <a name="connect-Type-ExtractionDefinitionSummary-CreatedTime"></a>
The timestamp when the extraction definition was created.
Type: Timestamp
Required: Yes

 ** ExtractionDefinitionArn **   <a name="connect-Type-ExtractionDefinitionSummary-ExtractionDefinitionArn"></a>
The Amazon Resource Name (ARN) of the extraction definition.
Type: String
Required: Yes

 ** ExtractionDefinitionId **   <a name="connect-Type-ExtractionDefinitionSummary-ExtractionDefinitionId"></a>
The identifier of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastUpdatedBy **   <a name="connect-Type-ExtractionDefinitionSummary-LastUpdatedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the extraction definition.
Type: String
Required: Yes

 ** LastUpdatedTime **   <a name="connect-Type-ExtractionDefinitionSummary-LastUpdatedTime"></a>
The timestamp when the extraction definition was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-ExtractionDefinitionSummary-Name"></a>
The name of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

## See Also
<a name="API_ExtractionDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ExtractionDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ExtractionDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ExtractionDefinitionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ExtractionDefinition.html
---

# ExtractionDefinition
<a name="API_ExtractionDefinition"></a>

Information about an extraction definition.

## Contents
<a name="API_ExtractionDefinition_Contents"></a>

 ** CreatedTime **   <a name="connect-Type-ExtractionDefinition-CreatedTime"></a>
The timestamp when the extraction definition was created.
Type: Timestamp
Required: Yes

 ** ExtractionConfiguration **   <a name="connect-Type-ExtractionDefinition-ExtractionConfiguration"></a>
The configuration that defines how data is extracted.
Type: [ExtractionConfiguration](API_ExtractionConfiguration.md) object
Required: Yes

 ** ExtractionDefinitionArn **   <a name="connect-Type-ExtractionDefinition-ExtractionDefinitionArn"></a>
The Amazon Resource Name (ARN) of the extraction definition.
Type: String
Required: Yes

 ** ExtractionDefinitionId **   <a name="connect-Type-ExtractionDefinition-ExtractionDefinitionId"></a>
The identifier of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** LastUpdatedBy **   <a name="connect-Type-ExtractionDefinition-LastUpdatedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the extraction definition.
Type: String
Required: Yes

 ** LastUpdatedTime **   <a name="connect-Type-ExtractionDefinition-LastUpdatedTime"></a>
The timestamp when the extraction definition was last updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="connect-Type-ExtractionDefinition-Name"></a>
The name of the extraction definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** Display **   <a name="connect-Type-ExtractionDefinition-Display"></a>
The display settings for the extraction definition.
Type: [ExtractionDefinitionDisplay](API_ExtractionDefinitionDisplay.md) object
Required: No

 ** Tags **   <a name="connect-Type-ExtractionDefinition-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_ExtractionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ExtractionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ExtractionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ExtractionDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Prompt.html
---

# Prompt
<a name="API_Prompt"></a>

Information about a prompt.

## Contents
<a name="API_Prompt_Contents"></a>

 ** Description **   <a name="connect-Type-Prompt-Description"></a>
The description of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-Prompt-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-Prompt-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-Prompt-Name"></a>
The name of the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: No

 ** PromptARN **   <a name="connect-Type-Prompt-PromptARN"></a>
The Amazon Resource Name (ARN) of the prompt.
Type: String
Required: No

 ** PromptId **   <a name="connect-Type-Prompt-PromptId"></a>
A unique identifier for the prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Tags **   <a name="connect-Type-Prompt-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Prompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Prompt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Prompt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Prompt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

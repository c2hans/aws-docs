---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_StatusReason.html
---

# StatusReason
<a name="API_StatusReason"></a>

Provide additional context about the status of a command execution using a reason code and description.

## Contents
<a name="API_StatusReason_Contents"></a>

 ** reasonCode **   <a name="iot-Type-StatusReason-reasonCode"></a>
A code that provides additional context for the command execution status.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[A-Z0-9_-]+`
Required: Yes

 ** reasonDescription **   <a name="iot-Type-StatusReason-reasonDescription"></a>
A literal string for devices to optionally provide additional information about the reason code for a command execution status.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[^\p{C}]*`
Required: No

## See Also
<a name="API_StatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/StatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/StatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/StatusReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

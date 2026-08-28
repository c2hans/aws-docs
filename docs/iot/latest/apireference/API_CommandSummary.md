---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CommandSummary.html
---

# CommandSummary
<a name="API_CommandSummary"></a>

Summary information about a particular command resource.

## Contents
<a name="API_CommandSummary_Contents"></a>

 ** commandArn **   <a name="iot-Type-CommandSummary-commandArn"></a>
The Amazon Resource Name (ARN) of the command.
Type: String
Required: No

 ** commandId **   <a name="iot-Type-CommandSummary-commandId"></a>
The unique identifier of the command.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** createdAt **   <a name="iot-Type-CommandSummary-createdAt"></a>
The timestamp, when the command was created.
Type: Timestamp
Required: No

 ** deprecated **   <a name="iot-Type-CommandSummary-deprecated"></a>
Indicates whether the command has been deprecated.
Type: Boolean
Required: No

 ** displayName **   <a name="iot-Type-CommandSummary-displayName"></a>
The display name of the command.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[^\p{C}]*`
Required: No

 ** lastUpdatedAt **   <a name="iot-Type-CommandSummary-lastUpdatedAt"></a>
The timestamp, when the command was last updated.
Type: Timestamp
Required: No

 ** pendingDeletion **   <a name="iot-Type-CommandSummary-pendingDeletion"></a>
Indicates whether the command is pending deletion.
Type: Boolean
Required: No

## See Also
<a name="API_CommandSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CommandSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CommandSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CommandSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

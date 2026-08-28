---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_MessageMetadata.html
---

# MessageMetadata
<a name="API_connect-participant_MessageMetadata"></a>

Contains metadata related to a message.

## Contents
<a name="API_connect-participant_MessageMetadata_Contents"></a>

 ** MessageId **   <a name="connect-Type-connect-participant_MessageMetadata-MessageId"></a>
The identifier of the message that contains the metadata information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MessageProcessingStatus **   <a name="connect-Type-connect-participant_MessageMetadata-MessageProcessingStatus"></a>
The status of Message Processing for the message.
Type: String
Valid Values: `PROCESSING | FAILED | REJECTED`
Required: No

 ** Receipts **   <a name="connect-Type-connect-participant_MessageMetadata-Receipts"></a>
The list of receipt information for a message for different recipients.
Type: Array of [Receipt](API_connect-participant_Receipt.md) objects
Required: No

## See Also
<a name="API_connect-participant_MessageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/MessageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/MessageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/MessageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

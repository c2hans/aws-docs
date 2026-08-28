---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_NetworkSettings.html
---

# NetworkSettings
<a name="API_NetworkSettings"></a>

Contains network-level configuration settings that apply to all users and security groups within a Wickr network.

## Contents
<a name="API_NetworkSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** consentPopup **   <a name="wickr-Type-NetworkSettings-consentPopup"></a>
Consent popup configuration for the network, displayed to users on login.
Type: [ConsentPopupConfig](API_ConsentPopupConfig.md) object
Required: No

 ** dataRetention **   <a name="wickr-Type-NetworkSettings-dataRetention"></a>
Indicates whether the data retention feature is enabled for the network. When true, messages are captured by the data retention bot for compliance and archiving purposes.
Type: Boolean
Required: No

 ** enableClientMetrics **   <a name="wickr-Type-NetworkSettings-enableClientMetrics"></a>
Allows Wickr clients to send anonymized performance and usage metrics to the Wickr backend server for service improvement and troubleshooting.
Type: Boolean
Required: No

 ** enableTrustedDataFormat **   <a name="wickr-Type-NetworkSettings-enableTrustedDataFormat"></a>
Configuration for OpenTDF integration at the network level, enforcing ABAC decision making when operating in TDF enabled rooms.
Type: Boolean
Required: No

 ** readReceiptConfig **   <a name="wickr-Type-NetworkSettings-readReceiptConfig"></a>
Configuration for read receipts at the network level, controlling the default behavior for whether senders can see when their messages have been read.
Type: [ReadReceiptConfig](API_ReadReceiptConfig.md) object
Required: No

## See Also
<a name="API_NetworkSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/NetworkSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/NetworkSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/NetworkSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

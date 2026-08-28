---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_Receiver.html
---

# Receiver
<a name="API_Receiver"></a>

Represents the entity that received the Engagement Invitation, including account and company details. This field is essential for tracking the partner who is being invited to collaborate.

## Contents
<a name="API_Receiver_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Account **   <a name="AWSPartnerCentral-Type-Receiver-Account"></a>
Specifies the AWS account of the partner who received the Engagement Invitation. This field is used to track the invitation recipient within the AWS ecosystem.
Type: [AccountReceiver](API_AccountReceiver.md) object
Required: No

## See Also
<a name="API_Receiver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/Receiver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/Receiver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/Receiver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

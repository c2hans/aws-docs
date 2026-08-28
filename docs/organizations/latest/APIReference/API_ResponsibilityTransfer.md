---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_ResponsibilityTransfer.html
---

# ResponsibilityTransfer
<a name="API_ResponsibilityTransfer"></a>

Contains details for a transfer. A *transfer* is the arrangement between two management accounts where one account designates the other with specified responsibilities for their organization.

## Contents
<a name="API_ResponsibilityTransfer_Contents"></a>

 ** ActiveHandshakeId **   <a name="organizations-Type-ResponsibilityTransfer-ActiveHandshakeId"></a>
ID for the handshake of the transfer.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^h-[0-9a-z]{8,32}$`
Required: No

 ** Arn **   <a name="organizations-Type-ResponsibilityTransfer-Arn"></a>
Amazon Resource Name (ARN) for the transfer.
Type: String
Pattern: `^arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer\/o-[a-z0-9]{10,32}\/(billing)\/(inbound|outbound)\/rt-[0-9a-z]{8,32}$`
Required: No

 ** EndTimestamp **   <a name="organizations-Type-ResponsibilityTransfer-EndTimestamp"></a>
Timestamp when the transfer ends.
Type: Timestamp
Required: No

 ** Id **   <a name="organizations-Type-ResponsibilityTransfer-Id"></a>
ID for the transfer.
Type: String
Pattern: `^rt-[0-9a-z]{8,32}$`
Required: No

 ** Name **   <a name="organizations-Type-ResponsibilityTransfer-Name"></a>
Name assigned to the transfer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[ -~]+$`
Required: No

 ** Source **   <a name="organizations-Type-ResponsibilityTransfer-Source"></a>
Account that allows another account external to its organization to manage the specified responsibilities for the organization.
Type: [TransferParticipant](API_TransferParticipant.md) object
Required: No

 ** StartTimestamp **   <a name="organizations-Type-ResponsibilityTransfer-StartTimestamp"></a>
Timestamp when the transfer starts.
Type: Timestamp
Required: No

 ** Status **   <a name="organizations-Type-ResponsibilityTransfer-Status"></a>
Status for the transfer.
Type: String
Valid Values: `REQUESTED | DECLINED | CANCELED | EXPIRED | ACCEPTED | WITHDRAWN`
Required: No

 ** Target **   <a name="organizations-Type-ResponsibilityTransfer-Target"></a>
Account that manages the specified responsibilities for another organization.
Type: [TransferParticipant](API_TransferParticipant.md) object
Required: No

 ** Type **   <a name="organizations-Type-ResponsibilityTransfer-Type"></a>
The type of transfer. Currently, only `BILLING` is supported.
Type: String
Valid Values: `BILLING`
Required: No

## See Also
<a name="API_ResponsibilityTransfer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/ResponsibilityTransfer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/ResponsibilityTransfer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/ResponsibilityTransfer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

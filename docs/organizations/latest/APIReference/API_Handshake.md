---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_Handshake.html
---

# Handshake
<a name="API_Handshake"></a>

Contains details for a handshake. A handshake is the secure exchange of information between two AWS accounts: a sender and a recipient.

 **Note:** Handshakes that are `CANCELED`, `ACCEPTED`, `DECLINED`, or `EXPIRED` show up in lists for only 30 days after entering that state After that they are deleted.

## Contents
<a name="API_Handshake_Contents"></a>

 ** Action **   <a name="organizations-Type-Handshake-Action"></a>
The type of handshake:
+  **INVITE**: Handshake sent to a standalone account requesting that it to join the sender's organization.
+  **ENABLE\_ALL\_FEATURES**: Handshake sent to invited member accounts to enable all features for the organization.
+  **APPROVE\_ALL\_FEATURES**: Handshake sent to the management account when all invited member accounts have approved to enable all features.
+  **TRANSFER\_RESPONSIBILITY**: Handshake sent to another organization's management account requesting that it designate the sender with the specified responsibilities for recipient's organization.
Type: String
Valid Values: `INVITE | ENABLE_ALL_FEATURES | APPROVE_ALL_FEATURES | ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE | TRANSFER_RESPONSIBILITY`
Required: No

 ** Arn **   <a name="organizations-Type-Handshake-Arn"></a>
Amazon Resource Name (ARN) for the handshake.
For more information about ARNs in Organizations, see [ARN Formats Supported by Organizations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies) in the * AWS Service Authorization Reference*.
Type: String
Pattern: `^arn:aws:organizations::\d{12}:handshake\/o-[a-z0-9]{10,32}\/[a-z_]{1,32}\/h-[0-9a-z]{8,32}`
Required: No

 ** ExpirationTimestamp **   <a name="organizations-Type-Handshake-ExpirationTimestamp"></a>
Timestamp when the handshake expires.
Type: Timestamp
Required: No

 ** Id **   <a name="organizations-Type-Handshake-Id"></a>
ID for the handshake.
The [regex pattern](http://wikipedia.org/wiki/regex) for handshake ID string requires "h-" followed by from 8 to 32 lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 34.
Pattern: `^h-[0-9a-z]{8,32}$`
Required: No

 ** Parties **   <a name="organizations-Type-Handshake-Parties"></a>
An array of `HandshakeParty` objects. Contains details for participant in a handshake.
Type: Array of [HandshakeParty](API_HandshakeParty.md) objects
Required: No

 ** RequestedTimestamp **   <a name="organizations-Type-Handshake-RequestedTimestamp"></a>
Timestamp when the handshake request was made.
Type: Timestamp
Required: No

 ** Resources **   <a name="organizations-Type-Handshake-Resources"></a>
An array of `HandshakeResource` objects. When needed, contains additional details for a handshake. For example, the email address for the sender.
Type: Array of [HandshakeResource](API_HandshakeResource.md) objects
Required: No

 ** State **   <a name="organizations-Type-Handshake-State"></a>
Current state for the handshake.
+  **REQUESTED**: Handshake awaiting a response from the recipient.
+  **OPEN**: Handshake sent to multiple recipients and all recipients have responded. The sender can now complete the handshake action.
+  **CANCELED**: Handshake canceled by the sender.
+  **ACCEPTED**: Handshake accepted by the recipient.
+  **DECLINED**: Handshake declined by the recipient.
+  **EXPIRED**: Handshake has expired.
Type: String
Valid Values: `REQUESTED | OPEN | CANCELED | ACCEPTED | DECLINED | EXPIRED`
Required: No

## See Also
<a name="API_Handshake_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/Handshake)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/Handshake)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/Handshake)

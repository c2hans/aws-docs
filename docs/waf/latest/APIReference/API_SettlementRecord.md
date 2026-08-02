---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_SettlementRecord.html
---

# SettlementRecord
<a name="API_SettlementRecord"></a>

A single settlement transaction record for AI bot monetization. Contains details about the payment including timestamp, amount, status, and the parties involved.

## Contents
<a name="API_SettlementRecord_Contents"></a>

 ** Amount **   <a name="WAF-Type-SettlementRecord-Amount"></a>
The payment amount in the specified currency.
Type: String
Required: Yes

 ** Status **   <a name="WAF-Type-SettlementRecord-Status"></a>
The status of the settlement. Possible values:
+  `SETTLED` - The payment was successfully settled on the blockchain and the transfer from the payer's wallet to the publisher's wallet is confirmed. The `TransactionId` field contains the on-chain transaction hash. Content is served to the client.
+  `PENDING` - The blockchain transaction has been submitted but not yet confirmed on-chain. This is a transient state that automatically resolves to either `SETTLED` or `FAILED`. No action is required. While pending, content is not served and the API returns a 402 response. Clients can retry the request.
+  `FAILED` - The payment settlement was attempted but failed. Possible causes include insufficient funds, an expired payment authorization, or a reverted blockchain transaction. The `failureReason` field contains a machine-readable error code. Content is not served.
+  `SERVICE_ERROR` - Settlement could not be completed due to an internal service issue or an issue with the payment network. Content is not served. The client's payment authorization remains valid and the request can be retried.
+  `SKIPPED_ORIGIN_ERROR` - The origin returned a non-2xx response, so settlement was intentionally skipped. The client is not charged.
+  `DUPLICATE` - A prior request with the same payment payload has already been settled. This status typically appears when a previous attempt timed out but the payment was ultimately processed. The client is not charged again.
Type: String
Valid Values: `SETTLED | PENDING | FAILED | SERVICE_ERROR | SKIPPED_ORIGIN_ERROR | DUPLICATE`
Required: Yes

 ** Timestamp **   <a name="WAF-Type-SettlementRecord-Timestamp"></a>
The timestamp when the settlement was recorded.
Type: Timestamp
Required: Yes

 ** ContentPath **   <a name="WAF-Type-SettlementRecord-ContentPath"></a>
The content path that was accessed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Currency **   <a name="WAF-Type-SettlementRecord-Currency"></a>
The currency of the payment amount.
Type: String
Valid Values: `USDC`
Required: No

 ** Intent **   <a name="WAF-Type-SettlementRecord-Intent"></a>
The declared intent of the AI bot request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** Network **   <a name="WAF-Type-SettlementRecord-Network"></a>
The blockchain network on which the settlement occurred.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
Required: No

 ** Organization **   <a name="WAF-Type-SettlementRecord-Organization"></a>
The organization associated with the AI bot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** PayerAddress **   <a name="WAF-Type-SettlementRecord-PayerAddress"></a>
The blockchain wallet address of the paying AI agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
Required: No

 ** RequestId **   <a name="WAF-Type-SettlementRecord-RequestId"></a>
The AWS WAF request ID associated with this settlement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
Required: No

 ** RequestTimestamp **   <a name="WAF-Type-SettlementRecord-RequestTimestamp"></a>
The timestamp of the original web request.
Type: Timestamp
Required: No

 ** SourceCategory **   <a name="WAF-Type-SettlementRecord-SourceCategory"></a>
The category of the AI bot source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** SourceName **   <a name="WAF-Type-SettlementRecord-SourceName"></a>
The name of the AI bot that made the payment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** TransactionId **   <a name="WAF-Type-SettlementRecord-TransactionId"></a>
The blockchain transaction identifier. You can use this to verify the transaction on a blockchain explorer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Verified **   <a name="WAF-Type-SettlementRecord-Verified"></a>
Whether the AI bot's identity was verified.
Type: Boolean
Required: No

 ** WalletAddress **   <a name="WAF-Type-SettlementRecord-WalletAddress"></a>
Your receiving wallet address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9:._\-=+/]+$`
Required: No

 ** WebAclArn **   <a name="WAF-Type-SettlementRecord-WebAclArn"></a>
The ARN of the web ACL that processed the request.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SettlementRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/SettlementRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/SettlementRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/SettlementRecord)

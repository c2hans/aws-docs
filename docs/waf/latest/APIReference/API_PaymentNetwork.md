---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_PaymentNetwork.html
---

# PaymentNetwork
<a name="API_PaymentNetwork"></a>

A blockchain payment network configuration for receiving AI bot monetization payments. Specifies the blockchain chain, your wallet address on that chain, and the price per request.

## Contents
<a name="API_PaymentNetwork_Contents"></a>

 ** Chain **   <a name="WAF-Type-PaymentNetwork-Chain"></a>
The blockchain network for receiving payments. Production networks: `BASE` (Base mainnet), `SOLANA` (Solana mainnet). Test networks: `BASE_SEPOLIA` (Base Sepolia testnet), `SOLANA_DEVNET` (Solana Devnet).
Type: String
Valid Values: `BASE | SOLANA | BASE_SEPOLIA | SOLANA_DEVNET`
Required: Yes

 ** Prices **   <a name="WAF-Type-PaymentNetwork-Prices"></a>
The price configuration for this payment network. Currently supports a single price entry in USDC.
Type: Array of [Price](API_Price.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** WalletAddress **   <a name="WAF-Type-PaymentNetwork-WalletAddress"></a>
Your wallet address on the specified blockchain where payments are sent. For EVM chains (Base, Base Sepolia), provide a valid Ethereum address (42 characters including 0x prefix). For Solana chains, provide a valid Base58-encoded public key (32-44 characters).
For EVM addresses, AWS WAF performs EIP-55 checksum validation for typo detection when the address uses a mix of lower and upper case letters. You can bypass this validation by providing the address in all lowercase or all uppercase.
Type: String
Length Constraints: Minimum length of 26. Maximum length of 44.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_PaymentNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PaymentNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PaymentNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PaymentNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerAccountContext.html
---

# CustomerAccountContext

The customer account context for an account-planning engagement. It names the account the plan concerns. The identifying details can be supplied by the caller or derived by the service from the account identifier.

## Contents
<a name="API_CustomerAccountContext_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountIdentifier **   <a name="AWSPartnerCentral-Type-CustomerAccountContext-AccountIdentifier"></a>
The identifier of the customer account that the engagement concerns, as an Amazon Resource Name (ARN) or a customer account identifier.
Type: String
Pattern: `(arn:.*|cust-acc-[0-9a-z]{13})`
Required: No

 ** Customer **   <a name="AWSPartnerCentral-Type-CustomerAccountContext-Customer"></a>
A snapshot of the customer company's identity for the account. On read, the service populates this from the account identifier.
Type: [AccountCustomer](API_AccountCustomer.md) object
Required: No

## See Also
<a name="API_CustomerAccountContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerAccountContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerAccountContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerAccountContext)

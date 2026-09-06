---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_EndTimeBehavior.html
---

# EndTimeBehavior
<a name="API_marketplace-agreements_EndTimeBehavior"></a>

The behavior of an agreement when it reaches its end date. For example, whether the agreement renews, and if it doesn't, the reason why.

## Contents
<a name="API_marketplace-agreements_EndTimeBehavior_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** type **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EndTimeBehavior-type"></a>
The behavior of the agreement when it reaches its end date.
Types include:
+  `RENEW` – A new agreement is created from the accepted terms of this agreement.
+  `REPLACE` – A new agreement is created from a different offer than the one this agreement was created from. This happens, for example, when a private offer reaches its end date and the acceptor transitions to the public offer for the product.
+  `EXPIRE` – The agreement ends and isn't renewed or replaced.
Type: String
Valid Values: `RENEW | REPLACE | EXPIRE`
Required: Yes

 ** reasonCode **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EndTimeBehavior-reasonCode"></a>
The reason why the agreement doesn't renew at its end date. The field is `null` when the agreement renews.
More than one reason can apply to the same agreement. When that happens, the operation returns only one reason code, and `PROPOSER_RENEW_OPTED_OUT` takes precedence over all others.
The `EnableAutoRenew` field reflects only the acceptor's preference, and doesn't reflect the other reasons an agreement might not renew.
Reason codes include:
+  `PROPOSER_RENEW_OPTED_OUT` – The proposer opted out of renewing the agreement.
+  `ACCEPTOR_RENEW_OPTED_OUT` – The acceptor opted out of renewing the agreement.
+  `NO_RENEWAL_TERM` – The accepted terms of the agreement don't include a renewal term, which is required for an agreement to renew.
+  `RENEWAL_LIMIT_EXHAUSTED` – The agreement reached the maximum number of renewals allowed by its renewal term.
Type: String
Valid Values: `PROPOSER_RENEW_OPTED_OUT | ACCEPTOR_RENEW_OPTED_OUT | NO_RENEWAL_TERM | RENEWAL_LIMIT_EXHAUSTED`
Required: No

 ** renewalSummary **   <a name="AWSMarketplaceService-Type-marketplace-agreements_EndTimeBehavior-renewalSummary"></a>
The details of the renewal that applies at the end date of the agreement. This field is present when `Type` is `RENEW`. It is also present when `ReasonCode` is `PROPOSER_RENEW_OPTED_OUT` or `ACCEPTOR_RENEW_OPTED_OUT`. In those cases, it identifies the offer that the agreement would otherwise have renewed from. The field is `null` in all other cases.
Type: [RenewalSummary](API_marketplace-agreements_RenewalSummary.md) object
Required: No

## See Also
<a name="API_marketplace-agreements_EndTimeBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/EndTimeBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/EndTimeBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/EndTimeBehavior)

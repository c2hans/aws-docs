---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_OfferingTransaction.html
---

# OfferingTransaction
<a name="API_OfferingTransaction"></a>

Represents the metadata of an offering transaction.

## Contents
<a name="API_OfferingTransaction_Contents"></a>

 ** cost **   <a name="devicefarm-Type-OfferingTransaction-cost"></a>
The cost of an offering transaction.
Type: [MonetaryAmount](API_MonetaryAmount.md) object
Required: No

 ** createdOn **   <a name="devicefarm-Type-OfferingTransaction-createdOn"></a>
The date on which an offering transaction was created.
Type: Timestamp
Required: No

 ** offeringPromotionId **   <a name="devicefarm-Type-OfferingTransaction-offeringPromotionId"></a>
The ID that corresponds to a device offering promotion.
Type: String
Length Constraints: Minimum length of 4.
Required: No

 ** offeringStatus **   <a name="devicefarm-Type-OfferingTransaction-offeringStatus"></a>
The status of an offering transaction.
Type: [OfferingStatus](API_OfferingStatus.md) object
Required: No

 ** transactionId **   <a name="devicefarm-Type-OfferingTransaction-transactionId"></a>
The transaction ID of the offering transaction.
Type: String
Length Constraints: Minimum length of 32.
Required: No

## See Also
<a name="API_OfferingTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/OfferingTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/OfferingTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/OfferingTransaction)

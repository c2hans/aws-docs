---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_OfferingStatus.html
---

# OfferingStatus
<a name="API_OfferingStatus"></a>

The status of the offering.

## Contents
<a name="API_OfferingStatus_Contents"></a>

 ** effectiveOn **   <a name="devicefarm-Type-OfferingStatus-effectiveOn"></a>
The date on which the offering is effective.
Type: Timestamp
Required: No

 ** offering **   <a name="devicefarm-Type-OfferingStatus-offering"></a>
Represents the metadata of an offering status.
Type: [Offering](API_Offering.md) object
Required: No

 ** quantity **   <a name="devicefarm-Type-OfferingStatus-quantity"></a>
The number of available devices in the offering.
Type: Integer
Required: No

 ** type **   <a name="devicefarm-Type-OfferingStatus-type"></a>
The type specified for the offering status.
Type: String
Valid Values: `PURCHASE | RENEW | SYSTEM`
Required: No

## See Also
<a name="API_OfferingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/OfferingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/OfferingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/OfferingStatus)

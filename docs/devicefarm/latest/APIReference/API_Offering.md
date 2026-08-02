---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Offering.html
---

# Offering
<a name="API_Offering"></a>

Represents the metadata of a device offering.

## Contents
<a name="API_Offering_Contents"></a>

 ** description **   <a name="devicefarm-Type-Offering-description"></a>
A string that describes the offering.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** id **   <a name="devicefarm-Type-Offering-id"></a>
The ID that corresponds to a device offering.
Type: String
Length Constraints: Minimum length of 32.
Required: No

 ** platform **   <a name="devicefarm-Type-Offering-platform"></a>
The platform of the device (for example, `ANDROID` or `IOS`).
Type: String
Valid Values: `ANDROID | IOS`
Required: No

 ** recurringCharges **   <a name="devicefarm-Type-Offering-recurringCharges"></a>
Specifies whether there are recurring charges for the offering.
Type: Array of [RecurringCharge](API_RecurringCharge.md) objects
Required: No

 ** type **   <a name="devicefarm-Type-Offering-type"></a>
The type of offering (for example, `RECURRING`) for a device.
Type: String
Valid Values: `RECURRING`
Required: No

## See Also
<a name="API_Offering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Offering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Offering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Offering)

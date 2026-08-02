---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_PickupDetails.html
---

# PickupDetails
<a name="API_PickupDetails"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Information identifying the person picking up the device.

## Contents
<a name="API_PickupDetails_Contents"></a>

 ** DevicePickupId **   <a name="Snowball-Type-PickupDetails-DevicePickupId"></a>
The unique ID for a device that will be picked up.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `DPID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Email **   <a name="Snowball-Type-PickupDetails-Email"></a>
The email address of the person picking up the device.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 320.
Pattern: `^(?=.{3,100}$).+@.+[.].+$`
Required: No

 ** IdentificationExpirationDate **   <a name="Snowball-Type-PickupDetails-IdentificationExpirationDate"></a>
Expiration date of the credential identifying the person picking up the device.
Type: Timestamp
Required: No

 ** IdentificationIssuingOrg **   <a name="Snowball-Type-PickupDetails-IdentificationIssuingOrg"></a>
Organization that issued the credential identifying the person picking up the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** IdentificationNumber **   <a name="Snowball-Type-PickupDetails-IdentificationNumber"></a>
The number on the credential identifying the person picking up the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="Snowball-Type-PickupDetails-Name"></a>
The name of the person picking up the device.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PhoneNumber **   <a name="Snowball-Type-PickupDetails-PhoneNumber"></a>
The phone number of the person picking up the device.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 30.
Pattern: `^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$`
Required: No

## See Also
<a name="API_PickupDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/PickupDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/PickupDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/PickupDetails)

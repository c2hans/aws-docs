---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_Address.html
---

# Address
<a name="API_Address"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The address that you want the Snow device(s) associated with a specific job to be shipped to. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. Although no individual elements of the `Address` are required, if the address is invalid or unsupported, then an exception is thrown.

## Contents
<a name="API_Address_Contents"></a>

 ** AddressId **   <a name="Snowball-Type-Address-AddressId"></a>
The unique ID for an address.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `ADID[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** City **   <a name="Snowball-Type-Address-City"></a>
The city in an address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Company **   <a name="Snowball-Type-Address-Company"></a>
The name of the company to receive a Snow device at an address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Country **   <a name="Snowball-Type-Address-Country"></a>
The country in an address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** IsRestricted **   <a name="Snowball-Type-Address-IsRestricted"></a>
This field is not supported in your region.
Type: Boolean
Required: No

 ** Landmark **   <a name="Snowball-Type-Address-Landmark"></a>
This field is no longer used and the value is ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Name **   <a name="Snowball-Type-Address-Name"></a>
The name of a person to receive a Snow device at an address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PhoneNumber **   <a name="Snowball-Type-Address-PhoneNumber"></a>
The phone number associated with an address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PostalCode **   <a name="Snowball-Type-Address-PostalCode"></a>
The postal code in an address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PrefectureOrDistrict **   <a name="Snowball-Type-Address-PrefectureOrDistrict"></a>
This field is no longer used and the value is ignored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** StateOrProvince **   <a name="Snowball-Type-Address-StateOrProvince"></a>
The state or province in an address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Street1 **   <a name="Snowball-Type-Address-Street1"></a>
The first line in a street address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Street2 **   <a name="Snowball-Type-Address-Street2"></a>
The second line in a street address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Street3 **   <a name="Snowball-Type-Address-Street3"></a>
The third line in a street address that a Snow device is to be delivered to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Type **   <a name="Snowball-Type-Address-Type"></a>
Differentiates between delivery address and pickup address in the customer account. Provided at job creation.
Type: String
Valid Values: `CUST_PICKUP | AWS_SHIP`
Required: No

## See Also
<a name="API_Address_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/Address)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/Address)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/Address)

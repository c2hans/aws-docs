---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_CreateAddress.html
---

# CreateAddress
<a name="API_CreateAddress"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Creates an address for a Snow device to be shipped to. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown. If providing an address as a JSON file through the `cli-input-json` option, include the full file path. For example, `--cli-input-json file://create-address.json`.

## Request Syntax
<a name="API_CreateAddress_RequestSyntax"></a>

```
{
   "Address": {
      "AddressId": "{{string}}",
      "City": "{{string}}",
      "Company": "{{string}}",
      "Country": "{{string}}",
      "IsRestricted": {{boolean}},
      "Landmark": "{{string}}",
      "Name": "{{string}}",
      "PhoneNumber": "{{string}}",
      "PostalCode": "{{string}}",
      "PrefectureOrDistrict": "{{string}}",
      "StateOrProvince": "{{string}}",
      "Street1": "{{string}}",
      "Street2": "{{string}}",
      "Street3": "{{string}}",
      "Type": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateAddress_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Address](#API_CreateAddress_RequestSyntax) **   <a name="Snowball-CreateAddress-request-Address"></a>
The address that you want the Snow device shipped to.
Type: [Address](API_Address.md) object
Required: Yes

## Response Syntax
<a name="API_CreateAddress_ResponseSyntax"></a>

```
{
   "AddressId": "string"
}
```

## Response Elements
<a name="API_CreateAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddressId](#API_CreateAddress_ResponseSyntax) **   <a name="Snowball-CreateAddress-response-AddressId"></a>
The automatically generated ID for a specific address. You'll use this ID when you create a job to specify which address you want the Snow device for that job shipped to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`

## Errors
<a name="API_CreateAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidAddressException **
The address provided was invalid. Check the address with your region's carrier, and try again.
HTTP Status Code: 400

 ** UnsupportedAddressException **
The address is either outside the serviceable area for your region, or an error occurred. Check the address with your region's carrier and try again. If the issue persists, contact Support.
HTTP Status Code: 400

## See Also
<a name="API_CreateAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/snowball-2016-06-30/CreateAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/CreateAddress)

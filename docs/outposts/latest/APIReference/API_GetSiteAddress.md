---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSiteAddress.html
---

# GetSiteAddress
<a name="API_GetSiteAddress"></a>

 Gets the site address of the specified site.

## Request Syntax
<a name="API_GetSiteAddress_RequestSyntax"></a>

```
GET /sites/{{SiteId}}/address?AddressType={{AddressType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSiteAddress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AddressType](#API_GetSiteAddress_RequestSyntax) **   <a name="outposts-GetSiteAddress-request-uri-AddressType"></a>
The type of the address you request.
Valid Values: `SHIPPING_ADDRESS | OPERATING_ADDRESS`
Required: Yes

 ** [SiteId](#API_GetSiteAddress_RequestSyntax) **   <a name="outposts-GetSiteAddress-request-uri-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

## Request Body
<a name="API_GetSiteAddress_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSiteAddress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Address": {
      "AddressLine1": "string",
      "AddressLine2": "string",
      "AddressLine3": "string",
      "City": "string",
      "ContactName": "string",
      "ContactPhoneNumber": "string",
      "CountryCode": "string",
      "DistrictOrCounty": "string",
      "Municipality": "string",
      "PostalCode": "string",
      "StateOrRegion": "string"
   },
   "AddressType": "string",
   "SiteId": "string"
}
```

## Response Elements
<a name="API_GetSiteAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Address](#API_GetSiteAddress_ResponseSyntax) **   <a name="outposts-GetSiteAddress-response-Address"></a>
 Information about the address.
Type: [Address](API_Address.md) object

 ** [AddressType](#API_GetSiteAddress_ResponseSyntax) **   <a name="outposts-GetSiteAddress-response-AddressType"></a>
The type of the address you receive.
Type: String
Valid Values: `SHIPPING_ADDRESS | OPERATING_ADDRESS`

 ** [SiteId](#API_GetSiteAddress_ResponseSyntax) **   <a name="outposts-GetSiteAddress-response-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`

## Errors
<a name="API_GetSiteAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** NotFoundException **
The specified request is not valid.
HTTP Status Code: 404

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_GetSiteAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetSiteAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetSiteAddress)

---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteAddress.html
---

# UpdateSiteAddress
<a name="API_UpdateSiteAddress"></a>

Updates the address of the specified site.

You can't update a site address if there is an order in progress. You must wait for the order to complete or cancel the order.

You can update the operating address before you place an order at the site, or after all Outposts that belong to the site have been deactivated.

## Request Syntax
<a name="API_UpdateSiteAddress_RequestSyntax"></a>

```
PUT /sites/{{SiteId}}/address HTTP/1.1
Content-type: application/json

{
   "Address": {
      "AddressLine1": "{{string}}",
      "AddressLine2": "{{string}}",
      "AddressLine3": "{{string}}",
      "City": "{{string}}",
      "ContactName": "{{string}}",
      "ContactPhoneNumber": "{{string}}",
      "CountryCode": "{{string}}",
      "DistrictOrCounty": "{{string}}",
      "Municipality": "{{string}}",
      "PostalCode": "{{string}}",
      "StateOrRegion": "{{string}}"
   },
   "AddressType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSiteAddress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SiteId](#API_UpdateSiteAddress_RequestSyntax) **   <a name="outposts-UpdateSiteAddress-request-uri-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

## Request Body
<a name="API_UpdateSiteAddress_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Address](#API_UpdateSiteAddress_RequestSyntax) **   <a name="outposts-UpdateSiteAddress-request-Address"></a>
 The address for the site.
Type: [Address](API_Address.md) object
Required: Yes

 ** [AddressType](#API_UpdateSiteAddress_RequestSyntax) **   <a name="outposts-UpdateSiteAddress-request-AddressType"></a>
 The type of the address.
Type: String
Valid Values: `SHIPPING_ADDRESS | OPERATING_ADDRESS`
Required: Yes

## Response Syntax
<a name="API_UpdateSiteAddress_ResponseSyntax"></a>

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
   "AddressType": "string"
}
```

## Response Elements
<a name="API_UpdateSiteAddress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Address](#API_UpdateSiteAddress_ResponseSyntax) **   <a name="outposts-UpdateSiteAddress-response-Address"></a>
 Information about an address.
Type: [Address](API_Address.md) object

 ** [AddressType](#API_UpdateSiteAddress_ResponseSyntax) **   <a name="outposts-UpdateSiteAddress-response-AddressType"></a>
 The type of the address.
Type: String
Valid Values: `SHIPPING_ADDRESS | OPERATING_ADDRESS`

## Errors
<a name="API_UpdateSiteAddress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have permission to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource causing the conflict.
 ** ResourceType **
The type of the resource causing the conflict.
HTTP Status Code: 409

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
<a name="API_UpdateSiteAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/UpdateSiteAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/UpdateSiteAddress)

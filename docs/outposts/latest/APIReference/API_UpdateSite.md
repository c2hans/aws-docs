---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSite.html
---

# UpdateSite
<a name="API_UpdateSite"></a>

Updates the specified site.

## Request Syntax
<a name="API_UpdateSite_RequestSyntax"></a>

```
PATCH /sites/{{SiteId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Notes": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSite_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SiteId](#API_UpdateSite_RequestSyntax) **   <a name="outposts-UpdateSite-request-uri-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

## Request Body
<a name="API_UpdateSite_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateSite_RequestSyntax) **   <a name="outposts-UpdateSite-request-Description"></a>
The description of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1001.
Pattern: `^[\S ]+$`
Required: No

 ** [Name](#API_UpdateSite_RequestSyntax) **   <a name="outposts-UpdateSite-request-Name"></a>
The name of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S ]+$`
Required: No

 ** [Notes](#API_UpdateSite_RequestSyntax) **   <a name="outposts-UpdateSite-request-Notes"></a>
Notes about a site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^[\S \n]+$`
Required: No

## Response Syntax
<a name="API_UpdateSite_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Site": {
      "AccountId": "string",
      "Description": "string",
      "Name": "string",
      "Notes": "string",
      "OperatingAddressCity": "string",
      "OperatingAddressCountryCode": "string",
      "OperatingAddressStateOrRegion": "string",
      "RackPhysicalProperties": {
         "FiberOpticCableType": "string",
         "MaximumSupportedWeightLbs": "string",
         "OpticalStandard": "string",
         "PowerConnector": "string",
         "PowerDrawKva": "string",
         "PowerFeedDrop": "string",
         "PowerPhase": "string",
         "UplinkCount": "string",
         "UplinkGbps": "string"
      },
      "SiteArn": "string",
      "SiteId": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateSite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Site](#API_UpdateSite_ResponseSyntax) **   <a name="outposts-UpdateSite-response-Site"></a>
Information about a site.
Type: [Site](API_Site.md) object

## Errors
<a name="API_UpdateSite_Errors"></a>

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
<a name="API_UpdateSite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/UpdateSite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/UpdateSite)

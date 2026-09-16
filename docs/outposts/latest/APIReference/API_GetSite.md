---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSite.html
---

# GetSite
<a name="API_GetSite"></a>

Gets information about the specified Outpost site.

## Request Syntax
<a name="API_GetSite_RequestSyntax"></a>

```
GET /sites/{{SiteId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSite_RequestParameters"></a>

The request uses the following URI parameters.

 ** [SiteId](#API_GetSite_RequestSyntax) **   <a name="outposts-GetSite-request-uri-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

## Request Body
<a name="API_GetSite_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSite_ResponseSyntax"></a>

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
<a name="API_GetSite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Site](#API_GetSite_ResponseSyntax) **   <a name="outposts-GetSite-response-Site"></a>
Information about a site.
Type: [Site](API_Site.md) object

## Errors
<a name="API_GetSite_Errors"></a>

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
<a name="API_GetSite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/GetSite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/GetSite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/GetSite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/GetSite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/GetSite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/GetSite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/GetSite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/GetSite)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/GetSite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/GetSite)

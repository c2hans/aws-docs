---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateSite.html
---

# CreateSite
<a name="API_CreateSite"></a>

 Creates a site for an Outpost.

## Request Syntax
<a name="API_CreateSite_RequestSyntax"></a>

```
POST /sites HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Notes": "{{string}}",
   "OperatingAddress": {
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
   "RackPhysicalProperties": {
      "FiberOpticCableType": "{{string}}",
      "MaximumSupportedWeightLbs": "{{string}}",
      "OpticalStandard": "{{string}}",
      "PowerConnector": "{{string}}",
      "PowerDrawKva": "{{string}}",
      "PowerFeedDrop": "{{string}}",
      "PowerPhase": "{{string}}",
      "UplinkCount": "{{string}}",
      "UplinkGbps": "{{string}}"
   },
   "ShippingAddress": {
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
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSite_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSite_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-Description"></a>
The description of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1001.
Pattern: `^[\S ]+$`
Required: No

 ** [Name](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-Name"></a>
The name of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S ]+$`
Required: Yes

 ** [Notes](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-Notes"></a>
Additional information that you provide about site access requirements, electrician scheduling, personal protective equipment, or regulation of equipment materials that could affect your installation process.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^[\S \n]+$`
Required: No

 ** [OperatingAddress](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-OperatingAddress"></a>
 The location to install and power on the hardware. This address might be different from the shipping address.
Type: [Address](API_Address.md) object
Required: No

 ** [RackPhysicalProperties](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-RackPhysicalProperties"></a>
 Information about the physical and logistical details for the rack at this site. For more information about hardware requirements for racks, see [Network readiness checklist](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist) in the AWS Outposts User Guide.
Type: [RackPhysicalProperties](API_RackPhysicalProperties.md) object
Required: No

 ** [ShippingAddress](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-ShippingAddress"></a>
 The location to ship the hardware. This address might be different from the operating address.
Type: [Address](API_Address.md) object
Required: No

 ** [Tags](#API_CreateSite_RequestSyntax) **   <a name="outposts-CreateSite-request-Tags"></a>
 The tags to apply to a site.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^[\S \n]+$`
Required: No

## Response Syntax
<a name="API_CreateSite_ResponseSyntax"></a>

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
<a name="API_CreateSite_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Site](#API_CreateSite_ResponseSyntax) **   <a name="outposts-CreateSite-response-Site"></a>
Information about a site.
Type: [Site](API_Site.md) object

## Errors
<a name="API_CreateSite_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded a service quota.
HTTP Status Code: 402

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateSite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreateSite)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreateSite)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreateSite)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreateSite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreateSite)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreateSite)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreateSite)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreateSite)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreateSite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreateSite)

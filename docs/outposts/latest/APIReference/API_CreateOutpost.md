---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOutpost.html
---

# CreateOutpost
<a name="API_CreateOutpost"></a>

Creates an Outpost.

You can specify either an Availability one or an AZ ID.

## Request Syntax
<a name="API_CreateOutpost_RequestSyntax"></a>

```
POST /outposts HTTP/1.1
Content-type: application/json

{
   "AvailabilityZone": "{{string}}",
   "AvailabilityZoneId": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SiteId": "{{string}}",
   "SupportedHardwareType": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateOutpost_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateOutpost_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-AvailabilityZone"></a>
The Availability Zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^([a-zA-Z]+-){1,3}([a-zA-Z]+)?(\d+[a-zA-Z]?)?$`
Required: No

 ** [AvailabilityZoneId](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-AvailabilityZoneId"></a>
The ID of the Availability Zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+\d-[a-zA-Z]+\d$`
Required: No

 ** [Description](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-Description"></a>
The description of the Outpost.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^[\S ]*$`
Required: No

 ** [Name](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-Name"></a>
The name of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\S ]+$`
Required: Yes

 ** [SiteId](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-SiteId"></a>
 The ID or the Amazon Resource Name (ARN) of the site.
Despite the parameter name, you can make the request with an ARN. The parameter name is `SiteId` for backward compatibility.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: Yes

 ** [SupportedHardwareType](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-SupportedHardwareType"></a>
 The type of hardware for this Outpost.
Type: String
Valid Values: `RACK | SERVER`
Required: No

 ** [Tags](#API_CreateOutpost_RequestSyntax) **   <a name="outposts-CreateOutpost-request-Tags"></a>
The tags to apply to the Outpost.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^[\S \n]+$`
Required: No

## Response Syntax
<a name="API_CreateOutpost_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Outpost": {
      "AvailabilityZone": "string",
      "AvailabilityZoneId": "string",
      "Description": "string",
      "Generation": "string",
      "LifeCycleStatus": "string",
      "Name": "string",
      "OutpostArn": "string",
      "OutpostId": "string",
      "OwnerId": "string",
      "RackScalingType": "string",
      "SiteArn": "string",
      "SiteId": "string",
      "SupportedHardwareType": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateOutpost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Outpost](#API_CreateOutpost_ResponseSyntax) **   <a name="outposts-CreateOutpost-response-Outpost"></a>
Information about an Outpost.
Type: [Outpost](API_Outpost.md) object

## Errors
<a name="API_CreateOutpost_Errors"></a>

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

 ** ServiceQuotaExceededException **
You have exceeded a service quota.
HTTP Status Code: 402

 ** ValidationException **
A parameter is not valid.
HTTP Status Code: 400

## See Also
<a name="API_CreateOutpost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/CreateOutpost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CreateOutpost)

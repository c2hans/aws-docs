---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateOutpost.html
---

# UpdateOutpost
<a name="API_UpdateOutpost"></a>

 Updates an Outpost.

## Request Syntax
<a name="API_UpdateOutpost_RequestSyntax"></a>

```
PATCH /outposts/{{OutpostId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "SupportedHardwareType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateOutpost_RequestParameters"></a>

The request uses the following URI parameters.

 ** [OutpostId](#API_UpdateOutpost_RequestSyntax) **   <a name="outposts-UpdateOutpost-request-uri-OutpostId"></a>
 The ID or ARN of the Outpost.
Despite the parameter name, you can make the request with an ARN. The parameter name is `OutpostId` for backward compatibility.
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: Yes

## Request Body
<a name="API_UpdateOutpost_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateOutpost_RequestSyntax) **   <a name="outposts-UpdateOutpost-request-Description"></a>
The description of the Outpost.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^[\S ]*$`
Required: No

 ** [Name](#API_UpdateOutpost_RequestSyntax) **   <a name="outposts-UpdateOutpost-request-Name"></a>
The name of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\S ]+$`
Required: No

 ** [SupportedHardwareType](#API_UpdateOutpost_RequestSyntax) **   <a name="outposts-UpdateOutpost-request-SupportedHardwareType"></a>
 The type of hardware for this Outpost.
Type: String
Valid Values: `RACK | SERVER`
Required: No

## Response Syntax
<a name="API_UpdateOutpost_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Outpost": {
      "AvailabilityZone": "string",
      "AvailabilityZoneId": "string",
      "Description": "string",
      "LifeCycleStatus": "string",
      "Name": "string",
      "OutpostArn": "string",
      "OutpostId": "string",
      "OwnerId": "string",
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
<a name="API_UpdateOutpost_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Outpost](#API_UpdateOutpost_ResponseSyntax) **   <a name="outposts-UpdateOutpost-response-Outpost"></a>
Information about an Outpost.
Type: [Outpost](API_Outpost.md) object

## Errors
<a name="API_UpdateOutpost_Errors"></a>

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
<a name="API_UpdateOutpost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/outposts-2019-12-03/UpdateOutpost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/UpdateOutpost)

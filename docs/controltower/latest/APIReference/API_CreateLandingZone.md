---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_CreateLandingZone.html
---

# CreateLandingZone
<a name="API_CreateLandingZone"></a>

Creates a new landing zone. This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.

## Request Syntax
<a name="API_CreateLandingZone_RequestSyntax"></a>

```
POST /create-landingzone HTTP/1.1
Content-type: application/json

{
   "manifest": {{JSON value}},
   "remediationTypes": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "version": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateLandingZone_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLandingZone_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [manifest](#API_CreateLandingZone_RequestSyntax) **   <a name="controltower-CreateLandingZone-request-manifest"></a>
The manifest JSON file is a text file that describes your AWS resources. For examples, review [Launch your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch).
Type: JSON value
Required: Yes

 ** [remediationTypes](#API_CreateLandingZone_RequestSyntax) **   <a name="controltower-CreateLandingZone-request-remediationTypes"></a>
Specifies the types of remediation actions to apply when creating the landing zone, such as automatic drift correction or compliance enforcement.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `INHERITANCE_DRIFT`
Required: No

 ** [tags](#API_CreateLandingZone_RequestSyntax) **   <a name="controltower-CreateLandingZone-request-tags"></a>
Tags to be applied to the landing zone.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [version](#API_CreateLandingZone_RequestSyntax) **   <a name="controltower-CreateLandingZone-request-version"></a>
The landing zone version, for example, 3.0.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `\d+.\d+`
Required: Yes

## Response Syntax
<a name="API_CreateLandingZone_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "operationIdentifier": "string"
}
```

## Response Elements
<a name="API_CreateLandingZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateLandingZone_ResponseSyntax) **   <a name="controltower-CreateLandingZone-response-arn"></a>
The ARN of the landing zone resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`

 ** [operationIdentifier](#API_CreateLandingZone_ResponseSyntax) **   <a name="controltower-CreateLandingZone-response-operationIdentifier"></a>
A unique identifier assigned to a `CreateLandingZone` operation. You can use this identifier as an input of `GetLandingZoneOperation` to check the operation's status.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreateLandingZone_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting the resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateLandingZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/CreateLandingZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/CreateLandingZone)

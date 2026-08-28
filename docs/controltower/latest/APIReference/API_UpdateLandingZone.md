---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_UpdateLandingZone.html
---

# UpdateLandingZone
<a name="API_UpdateLandingZone"></a>

This API call updates the landing zone. It starts an asynchronous operation that updates the landing zone based on the new landing zone version, or on the changed parameters specified in the updated manifest file.

## Request Syntax
<a name="API_UpdateLandingZone_RequestSyntax"></a>

```
POST /update-landingzone HTTP/1.1
Content-type: application/json

{
   "landingZoneIdentifier": "{{string}}",
   "manifest": {{JSON value}},
   "remediationTypes": [ "{{string}}" ],
   "version": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLandingZone_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLandingZone_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [landingZoneIdentifier](#API_UpdateLandingZone_RequestSyntax) **   <a name="controltower-UpdateLandingZone-request-landingZoneIdentifier"></a>
The unique identifier of the landing zone.
Type: String
Required: Yes

 ** [manifest](#API_UpdateLandingZone_RequestSyntax) **   <a name="controltower-UpdateLandingZone-request-manifest"></a>
The manifest file (JSON) is a text file that describes your AWS resources. For an example, review [Launch your landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/lz-api-launch). The example manifest file contains each of the available parameters. The schema for the landing zone's JSON manifest file is not published, by design.
Type: JSON value
Required: Yes

 ** [remediationTypes](#API_UpdateLandingZone_RequestSyntax) **   <a name="controltower-UpdateLandingZone-request-remediationTypes"></a>
Specifies the types of remediation actions to apply when updating the landing zone configuration.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `INHERITANCE_DRIFT`
Required: No

 ** [version](#API_UpdateLandingZone_RequestSyntax) **   <a name="controltower-UpdateLandingZone-request-version"></a>
The landing zone version, for example, 3.2.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 10.
Pattern: `\d+.\d+`
Required: Yes

## Response Syntax
<a name="API_UpdateLandingZone_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "operationIdentifier": "string"
}
```

## Response Elements
<a name="API_UpdateLandingZone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [operationIdentifier](#API_UpdateLandingZone_ResponseSyntax) **   <a name="controltower-UpdateLandingZone-response-operationIdentifier"></a>
A unique identifier assigned to a `UpdateLandingZone` operation. You can use this identifier as an input of `GetLandingZoneOperation` to check the operation's status.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_UpdateLandingZone_Errors"></a>

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

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

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
<a name="API_UpdateLandingZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/UpdateLandingZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/UpdateLandingZone)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

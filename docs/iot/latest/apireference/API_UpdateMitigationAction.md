---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateMitigationAction.html
---

# UpdateMitigationAction
<a name="API_UpdateMitigationAction"></a>

Updates the definition for the specified mitigation action.

Requires permission to access the [UpdateMitigationAction](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateMitigationAction_RequestSyntax"></a>

```
PATCH /mitigationactions/actions/{{actionName}} HTTP/1.1
Content-type: application/json

{
   "actionParams": {
      "addThingsToThingGroupParams": {
         "overrideDynamicGroups": {{boolean}},
         "thingGroupNames": [ "{{string}}" ]
      },
      "enableIoTLoggingParams": {
         "logLevel": "{{string}}",
         "roleArnForLogging": "{{string}}"
      },
      "publishFindingToSnsParams": {
         "topicArn": "{{string}}"
      },
      "replaceDefaultPolicyVersionParams": {
         "templateName": "{{string}}"
      },
      "updateCACertificateParams": {
         "action": "{{string}}"
      },
      "updateDeviceCertificateParams": {
         "action": "{{string}}"
      }
   },
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateMitigationAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionName](#API_UpdateMitigationAction_RequestSyntax) **   <a name="iot-UpdateMitigationAction-request-uri-actionName"></a>
The friendly name for the mitigation action. You cannot change the name by using `UpdateMitigationAction`. Instead, you must delete and recreate the mitigation action with the new name.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_UpdateMitigationAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionParams](#API_UpdateMitigationAction_RequestSyntax) **   <a name="iot-UpdateMitigationAction-request-actionParams"></a>
Defines the type of action and the parameters for that action.
Type: [MitigationActionParams](API_MitigationActionParams.md) object
Required: No

 ** [roleArn](#API_UpdateMitigationAction_RequestSyntax) **   <a name="iot-UpdateMitigationAction-request-roleArn"></a>
The ARN of the IAM role that is used to apply the mitigation action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateMitigationAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionArn": "string",
   "actionId": "string"
}
```

## Response Elements
<a name="API_UpdateMitigationAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionArn](#API_UpdateMitigationAction_ResponseSyntax) **   <a name="iot-UpdateMitigationAction-response-actionArn"></a>
The ARN for the new mitigation action.
Type: String

 ** [actionId](#API_UpdateMitigationAction_ResponseSyntax) **   <a name="iot-UpdateMitigationAction-response-actionId"></a>
A unique identifier for the mitigation action.
Type: String

## Errors
<a name="API_UpdateMitigationAction_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateMitigationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateMitigationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateMitigationAction)

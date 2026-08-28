---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateMitigationAction.html
---

# CreateMitigationAction
<a name="API_CreateMitigationAction"></a>

Defines an action that can be applied to audit findings by using StartAuditMitigationActionsTask. Only certain types of mitigation actions can be applied to specific check names. For more information, see [Mitigation actions](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-mitigation-actions.html). Each mitigation action can apply only one type of change.

Requires permission to access the [CreateMitigationAction](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateMitigationAction_RequestSyntax"></a>

```
POST /mitigationactions/actions/{{actionName}} HTTP/1.1
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
   "roleArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMitigationAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionName](#API_CreateMitigationAction_RequestSyntax) **   <a name="iot-CreateMitigationAction-request-uri-actionName"></a>
A friendly name for the action. Choose a friendly name that accurately describes the action (for example, `EnableLoggingAction`).
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateMitigationAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actionParams](#API_CreateMitigationAction_RequestSyntax) **   <a name="iot-CreateMitigationAction-request-actionParams"></a>
Defines the type of action and the parameters for that action.
Type: [MitigationActionParams](API_MitigationActionParams.md) object
Required: Yes

 ** [roleArn](#API_CreateMitigationAction_RequestSyntax) **   <a name="iot-CreateMitigationAction-request-roleArn"></a>
The ARN of the IAM role that is used to apply the mitigation action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [tags](#API_CreateMitigationAction_RequestSyntax) **   <a name="iot-CreateMitigationAction-request-tags"></a>
Metadata that can be used to manage the mitigation action.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateMitigationAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionArn": "string",
   "actionId": "string"
}
```

## Response Elements
<a name="API_CreateMitigationAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionArn](#API_CreateMitigationAction_ResponseSyntax) **   <a name="iot-CreateMitigationAction-response-actionArn"></a>
The ARN for the new mitigation action.
Type: String

 ** [actionId](#API_CreateMitigationAction_ResponseSyntax) **   <a name="iot-CreateMitigationAction-response-actionId"></a>
A unique identifier for the new mitigation action.
Type: String

## Errors
<a name="API_CreateMitigationAction_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateMitigationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateMitigationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateMitigationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

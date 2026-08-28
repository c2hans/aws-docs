---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeMitigationAction.html
---

# DescribeMitigationAction
<a name="API_DescribeMitigationAction"></a>

Gets information about a mitigation action.

Requires permission to access the [DescribeMitigationAction](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeMitigationAction_RequestSyntax"></a>

```
GET /mitigationactions/actions/{{actionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeMitigationAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionName](#API_DescribeMitigationAction_RequestSyntax) **   <a name="iot-DescribeMitigationAction-request-uri-actionName"></a>
The friendly name that uniquely identifies the mitigation action.
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_DescribeMitigationAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeMitigationAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionArn": "string",
   "actionId": "string",
   "actionName": "string",
   "actionParams": {
      "addThingsToThingGroupParams": {
         "overrideDynamicGroups": boolean,
         "thingGroupNames": [ "string" ]
      },
      "enableIoTLoggingParams": {
         "logLevel": "string",
         "roleArnForLogging": "string"
      },
      "publishFindingToSnsParams": {
         "topicArn": "string"
      },
      "replaceDefaultPolicyVersionParams": {
         "templateName": "string"
      },
      "updateCACertificateParams": {
         "action": "string"
      },
      "updateDeviceCertificateParams": {
         "action": "string"
      }
   },
   "actionType": "string",
   "creationDate": number,
   "lastModifiedDate": number,
   "roleArn": "string"
}
```

## Response Elements
<a name="API_DescribeMitigationAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionArn](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-actionArn"></a>
The ARN that identifies this migration action.
Type: String

 ** [actionId](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-actionId"></a>
A unique identifier for this action.
Type: String

 ** [actionName](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-actionName"></a>
The friendly name that uniquely identifies the mitigation action.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [actionParams](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-actionParams"></a>
Parameters that control how the mitigation action is applied, specific to the type of mitigation action.
Type: [MitigationActionParams](API_MitigationActionParams.md) object

 ** [actionType](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-actionType"></a>
The type of mitigation action.
Type: String
Valid Values: `UPDATE_DEVICE_CERTIFICATE | UPDATE_CA_CERTIFICATE | ADD_THINGS_TO_THING_GROUP | REPLACE_DEFAULT_POLICY_VERSION | ENABLE_IOT_LOGGING | PUBLISH_FINDING_TO_SNS`

 ** [creationDate](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-creationDate"></a>
The date and time when the mitigation action was added to your AWS accounts.
Type: Timestamp

 ** [lastModifiedDate](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-lastModifiedDate"></a>
The date and time when the mitigation action was last changed.
Type: Timestamp

 ** [roleArn](#API_DescribeMitigationAction_ResponseSyntax) **   <a name="iot-DescribeMitigationAction-response-roleArn"></a>
The ARN of the IAM role used to apply this action.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_DescribeMitigationAction_Errors"></a>

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
<a name="API_DescribeMitigationAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeMitigationAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeMitigationAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

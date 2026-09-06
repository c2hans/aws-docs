---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateActionConnector.html
---

# UpdateActionConnector
<a name="API_UpdateActionConnector"></a>

Updates an existing action connector with new configuration details, authentication settings, or enabled actions. You can modify the connector's name, description, authentication configuration, and which actions are enabled. For more information, [https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-action-auth.html](https://docs.aws.amazon.com/quicksuite/latest/userguide/quick-action-auth.html).

## Request Syntax
<a name="API_UpdateActionConnector_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/action-connectors/{{ActionConnectorId}} HTTP/1.1
Content-type: application/json

{
   "AuthenticationConfig": {
      "AuthenticationMetadata": { ... },
      "AuthenticationType": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "VpcConnectionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateActionConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ActionConnectorId](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-uri-ActionConnectorId"></a>
The unique identifier of the action connector to update.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-uri-AwsAccountId"></a>
The AWS account ID that contains the action connector to update.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateActionConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AuthenticationConfig](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-AuthenticationConfig"></a>
The updated authentication configuration for connecting to the external service.
Type: [AuthConfig](API_AuthConfig.md) object
Required: Yes

 ** [Name](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-Name"></a>
The new name for the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9](?:[\w- ]*[A-Za-z0-9])?`
Required: Yes

 ** [Description](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-Description"></a>
The updated description of the action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[A-Za-z0-9 _.,!?-]*`
Required: No

 ** [VpcConnectionArn](#API_UpdateActionConnector_RequestSyntax) **   <a name="QS-UpdateActionConnector-request-VpcConnectionArn"></a>
The updated ARN of the VPC connection to use for secure connectivity.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateActionConnector_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActionConnectorId": "string",
   "Arn": "string",
   "RequestId": "string",
   "UpdateStatus": "string"
}
```

## Response Elements
<a name="API_UpdateActionConnector_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateActionConnector_ResponseSyntax) **   <a name="QS-UpdateActionConnector-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorId](#API_UpdateActionConnector_ResponseSyntax) **   <a name="QS-UpdateActionConnector-response-ActionConnectorId"></a>
The unique identifier of the updated action connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [Arn](#API_UpdateActionConnector_ResponseSyntax) **   <a name="QS-UpdateActionConnector-response-Arn"></a>
The Amazon Resource Name (ARN) of the updated action connector.
Type: String

 ** [RequestId](#API_UpdateActionConnector_ResponseSyntax) **   <a name="QS-UpdateActionConnector-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

 ** [UpdateStatus](#API_UpdateActionConnector_ResponseSyntax) **   <a name="QS-UpdateActionConnector-response-UpdateStatus"></a>
The status of the update operation.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`

## Errors
<a name="API_UpdateActionConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_UpdateActionConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateActionConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateActionConnector)

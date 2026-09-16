---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAgent.html
---

# UpdateAgent
<a name="API_UpdateAgent"></a>

Updates an existing agent.

## Request Syntax
<a name="API_UpdateAgent_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/agents/{{AgentId}} HTTP/1.1
Content-type: application/json

{
   "ActionConnectorsToAdd": [ "{{string}}" ],
   "ActionConnectorsToRemove": [ "{{string}}" ],
   "CustomPromptInput": { ... },
   "Description": "{{string}}",
   "IconId": "{{string}}",
   "Name": "{{string}}",
   "SpacesToAdd": [ "{{string}}" ],
   "SpacesToRemove": [ "{{string}}" ],
   "StarterPrompts": [ "{{string}}" ],
   "WelcomeMessage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAgent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AgentId](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-uri-AgentId"></a>
The unique identifier for the agent to update.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_.+]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the agent.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAgent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-Name"></a>
The name of the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `(?!\s*$).+`
Required: Yes

 ** [ActionConnectorsToAdd](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-ActionConnectorsToAdd"></a>
The Amazon Resource Names (ARNs) of the action connectors to attach to the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [ActionConnectorsToRemove](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-ActionConnectorsToRemove"></a>
The Amazon Resource Names (ARNs) of the action connectors to detach from the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [CustomPromptInput](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-CustomPromptInput"></a>
The custom prompt configuration for the agent.
Type: [CustomPromptInput](API_CustomPromptInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Description](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-Description"></a>
A description of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** [IconId](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-IconId"></a>
The icon identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** [SpacesToAdd](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-SpacesToAdd"></a>
The Amazon Resource Names (ARNs) of the spaces to attach to the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [SpacesToRemove](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-SpacesToRemove"></a>
The Amazon Resource Names (ARNs) of the spaces to detach from the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [StarterPrompts](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-StarterPrompts"></a>
A list of starter prompts that are displayed to users when they begin interacting with the agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** [WelcomeMessage](#API_UpdateAgent_RequestSyntax) **   <a name="QS-UpdateAgent-request-WelcomeMessage"></a>
The welcome message that is displayed when a user starts a conversation with the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Required: No

## Response Syntax
<a name="API_UpdateAgent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentId": "string",
   "AgentStatus": "string",
   "Arn": "string",
   "FailedToAddActionConnectors": [
      {
         "Arn": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "FailedToAddSpaces": [
      {
         "Arn": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "FailedToRemoveActionConnectors": [
      {
         "Arn": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "FailedToRemoveSpaces": [
      {
         "Arn": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateAgent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentId](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-AgentId"></a>
The unique identifier for the agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9a-zA-Z-_.+]+`

 ** [AgentStatus](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-AgentStatus"></a>
The status of the agent.
Type: String
Valid Values: `ACTIVE | UPDATING | FAILED | CREATING`

 ** [Arn](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-Arn"></a>
The Amazon Resource Name (ARN) of the agent.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [FailedToAddActionConnectors](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-FailedToAddActionConnectors"></a>
A list of per-ARN failures from the action connectors that were requested to be added.
Type: Array of [FailedToUpdateAssociation](API_FailedToUpdateAssociation.md) objects

 ** [FailedToAddSpaces](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-FailedToAddSpaces"></a>
A list of per-ARN failures from the spaces that were requested to be added.
Type: Array of [FailedToUpdateAssociation](API_FailedToUpdateAssociation.md) objects

 ** [FailedToRemoveActionConnectors](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-FailedToRemoveActionConnectors"></a>
A list of per-ARN failures from the action connectors that were requested to be removed.
Type: Array of [FailedToUpdateAssociation](API_FailedToUpdateAssociation.md) objects

 ** [FailedToRemoveSpaces](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-FailedToRemoveSpaces"></a>
A list of per-ARN failures from the spaces that were requested to be removed.
Type: Array of [FailedToUpdateAssociation](API_FailedToUpdateAssociation.md) objects

 ** [RequestId](#API_UpdateAgent_ResponseSyntax) **   <a name="QS-UpdateAgent-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateAgent_Errors"></a>

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

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** PreconditionNotMetException **
One or more preconditions aren't met.
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
<a name="API_UpdateAgent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAgent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAgent)

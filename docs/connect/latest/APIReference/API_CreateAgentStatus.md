---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateAgentStatus.html
---

# CreateAgentStatus
<a name="API_CreateAgentStatus"></a>

Creates an agent status for the specified Connect Customer instance.

## Request Syntax
<a name="API_CreateAgentStatus_RequestSyntax"></a>

```
PUT /agent-status/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "DisplayOrder": {{number}},
   "Name": "{{string}}",
   "State": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAgentStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateAgentStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-Description"></a>
The description of the status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [DisplayOrder](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-DisplayOrder"></a>
The display order of the status.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [Name](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-Name"></a>
The name of the status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [State](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-State"></a>
The state of the status.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** [Tags](#API_CreateAgentStatus_RequestSyntax) **   <a name="connect-CreateAgentStatus-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateAgentStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AgentStatusARN": "string",
   "AgentStatusId": "string"
}
```

## Response Elements
<a name="API_CreateAgentStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AgentStatusARN](#API_CreateAgentStatus_ResponseSyntax) **   <a name="connect-CreateAgentStatus-response-AgentStatusARN"></a>
The Amazon Resource Name (ARN) of the agent status.
Type: String

 ** [AgentStatusId](#API_CreateAgentStatus_ResponseSyntax) **   <a name="connect-CreateAgentStatus-response-AgentStatusId"></a>
The identifier of the agent status.
Type: String

## Errors
<a name="API_CreateAgentStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateAgentStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateAgentStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateAgentStatus)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateQuickConnect.html
---

# CreateQuickConnect
<a name="API_CreateQuickConnect"></a>

Creates a quick connect for the specified Connect Customer instance.

## Request Syntax
<a name="API_CreateQuickConnect_RequestSyntax"></a>

```
PUT /quick-connects/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "QuickConnectConfig": {
      "FlowConfig": {
         "ContactFlowId": "{{string}}"
      },
      "PhoneConfig": {
         "PhoneNumber": "{{string}}"
      },
      "QueueConfig": {
         "ContactFlowId": "{{string}}",
         "QueueId": "{{string}}"
      },
      "QuickConnectType": "{{string}}",
      "UserConfig": {
         "ContactFlowId": "{{string}}",
         "UserId": "{{string}}"
      }
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateQuickConnect_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateQuickConnect_RequestSyntax) **   <a name="connect-CreateQuickConnect-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateQuickConnect_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateQuickConnect_RequestSyntax) **   <a name="connect-CreateQuickConnect-request-Description"></a>
The description of the quick connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_CreateQuickConnect_RequestSyntax) **   <a name="connect-CreateQuickConnect-request-Name"></a>
A unique name of the quick connect.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

 ** [QuickConnectConfig](#API_CreateQuickConnect_RequestSyntax) **   <a name="connect-CreateQuickConnect-request-QuickConnectConfig"></a>
Configuration settings for the quick connect.
Type: [QuickConnectConfig](API_QuickConnectConfig.md) object
Required: Yes

 ** [Tags](#API_CreateQuickConnect_RequestSyntax) **   <a name="connect-CreateQuickConnect-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateQuickConnect_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "QuickConnectARN": "string",
   "QuickConnectId": "string"
}
```

## Response Elements
<a name="API_CreateQuickConnect_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [QuickConnectARN](#API_CreateQuickConnect_ResponseSyntax) **   <a name="connect-CreateQuickConnect-response-QuickConnectARN"></a>
The Amazon Resource Name (ARN) for the quick connect.
Type: String

 ** [QuickConnectId](#API_CreateQuickConnect_ResponseSyntax) **   <a name="connect-CreateQuickConnect-response-QuickConnectId"></a>
The identifier for the quick connect.
Type: String

## Errors
<a name="API_CreateQuickConnect_Errors"></a>

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
<a name="API_CreateQuickConnect_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateQuickConnect)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateQuickConnect)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

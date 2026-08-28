---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateContactFlowModule.html
---

# CreateContactFlowModule
<a name="API_CreateContactFlowModule"></a>

Creates a flow module for the specified Connect Customer instance.

## Request Syntax
<a name="API_CreateContactFlowModule_RequestSyntax"></a>

```
PUT /contact-flow-modules/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Content": "{{string}}",
   "Description": "{{string}}",
   "ExternalInvocationConfiguration": {
      "Enabled": {{boolean}}
   },
   "Name": "{{string}}",
   "Settings": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateContactFlowModule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateContactFlowModule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Content](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-Content"></a>
The JSON string that represents the content of the flow. For an example, see [Example flow in Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256000.
Required: Yes

 ** [Description](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-Description"></a>
The description of the flow module.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `.*\S.*`
Required: No

 ** [ExternalInvocationConfiguration](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-ExternalInvocationConfiguration"></a>
The external invocation configuration for the flow module.
Type: [ExternalInvocationConfiguration](API_ExternalInvocationConfiguration.md) object
Required: No

 ** [Name](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-Name"></a>
The name of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`
Required: Yes

 ** [Settings](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-Settings"></a>
The configuration settings for the flow module.
Type: String
Required: No

 ** [Tags](#API_CreateContactFlowModule_RequestSyntax) **   <a name="connect-CreateContactFlowModule-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateContactFlowModule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateContactFlowModule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateContactFlowModule_ResponseSyntax) **   <a name="connect-CreateContactFlowModule-response-Arn"></a>
The Amazon Resource Name (ARN) of the flow module.
Type: String

 ** [Id](#API_CreateContactFlowModule_ResponseSyntax) **   <a name="connect-CreateContactFlowModule-response-Id"></a>
The identifier of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_CreateContactFlowModule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidContactFlowModuleException **
The problems with the module. Please fix before trying again.
HTTP Status Code: 400

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
<a name="API_CreateContactFlowModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateContactFlowModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateContactFlowModule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

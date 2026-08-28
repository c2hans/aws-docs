---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactFlowModuleContent.html
---

# UpdateContactFlowModuleContent
<a name="API_UpdateContactFlowModuleContent"></a>

Updates specified flow module for the specified Connect Customer instance.

Use the `$SAVED` alias in the request to describe the `SAVED` content of a Flow. For example, `arn:aws:.../contact-flow/{id}:$SAVED`. After a flow is published, `$SAVED` needs to be supplied to view saved content that has not been published.

## Request Syntax
<a name="API_UpdateContactFlowModuleContent_RequestSyntax"></a>

```
POST /contact-flow-modules/{{InstanceId}}/{{ContactFlowModuleId}}/content HTTP/1.1
Content-type: application/json

{
   "Content": "{{string}}",
   "Settings": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateContactFlowModuleContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ContactFlowModuleId](#API_UpdateContactFlowModuleContent_RequestSyntax) **   <a name="connect-UpdateContactFlowModuleContent-request-uri-ContactFlowModuleId"></a>
The identifier of the flow module.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateContactFlowModuleContent_RequestSyntax) **   <a name="connect-UpdateContactFlowModuleContent-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateContactFlowModuleContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Content](#API_UpdateContactFlowModuleContent_RequestSyntax) **   <a name="connect-UpdateContactFlowModuleContent-request-Content"></a>
The JSON string that represents the content of the flow. For an example, see [Example flow in Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256000.
Required: No

 ** [Settings](#API_UpdateContactFlowModuleContent_RequestSyntax) **   <a name="connect-UpdateContactFlowModuleContent-request-Settings"></a>
Serialized JSON string of the flow module Settings schema.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateContactFlowModuleContent_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateContactFlowModuleContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateContactFlowModuleContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidContactFlowModuleException **
The problems with the module. Please fix before trying again.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateContactFlowModuleContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateContactFlowModuleContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateContactFlowModuleContent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

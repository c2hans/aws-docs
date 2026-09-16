---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContactTaskTemplate.html
---

# UpdateContactTaskTemplate
<a name="API_UpdateContactTaskTemplate"></a>

Updates the task template association on an existing task contact. You can update the task template on a contact before assignment to support tasks that are created without a template (for example [Rules](https://docs.aws.amazon.com/connect/latest/adminguide/connect-rules.html) or [disconnect flows](https://docs.aws.amazon.com/connect/latest/adminguide/set-disconnect-flow.html)) or change the agent interaction form to represent the latest task data (for example an initial request that was submitted as a refund gets updated to an account cancellation and requires a new template).

This operation can only be used with task contacts that are in progress and not connected to an agent. A task template can be updated a maximum of 5 times per contact.

The task's references must be compatible with the fields of the target task template. If the target template has a required field, the task must have a corresponding reference with a matching name and compatible type. The following task template field types map to reference types:
+  `TEXT`, `TEXT_AREA`, `BOOLEAN`, and `SINGLE_SELECT` map to references of type `STRING`.
+  `NUMBER` maps to references of type `NUMBER`.
+  `DATE_TIME` maps to references of type `DATE`.
+  `URL` maps to references of type `URL`.
+  `EMAIL` maps to references of type `EMAIL`.

References corresponding to `TEXT` fields must be fewer than 512 characters. `TEXT_AREA` fields must be fewer than 4,096 characters. `BOOLEAN` fields must have a value of `true` or `false`.

An `InvalidRequestException` occurs when `UpdateContactTaskTemplate` is called on a connected or terminated task, when it is called on non-task contacts, and when the task contact already uses the provided task template. A `PropertyValidationException` occurs when the task's references conflict with the task template's fields, for example if the task is missing a reference that matches a required field, or if the task has a reference that matches a required field's name but not its datatype.

## Request Syntax
<a name="API_UpdateContactTaskTemplate_RequestSyntax"></a>

```
POST /contact/task-template HTTP/1.1
Content-type: application/json

{
   "ContactId": "{{string}}",
   "InstanceId": "{{string}}",
   "TaskTemplateId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateContactTaskTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateContactTaskTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ContactId](#API_UpdateContactTaskTemplate_RequestSyntax) **   <a name="connect-UpdateContactTaskTemplate-request-ContactId"></a>
The identifier of the contact in this instance of Connect Customer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_UpdateContactTaskTemplate_RequestSyntax) **   <a name="connect-UpdateContactTaskTemplate-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [TaskTemplateId](#API_UpdateContactTaskTemplate_RequestSyntax) **   <a name="connect-UpdateContactTaskTemplate-request-TaskTemplateId"></a>
A unique identifier for the task template. For more information about task templates, see [Task templates](https://docs.aws.amazon.com/connect/latest/adminguide/task-templates.html) in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Response Syntax
<a name="API_UpdateContactTaskTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateContactTaskTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateContactTaskTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

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

 ** PropertyValidationException **
The property is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

## See Also
<a name="API_UpdateContactTaskTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateContactTaskTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateContactTaskTemplate)

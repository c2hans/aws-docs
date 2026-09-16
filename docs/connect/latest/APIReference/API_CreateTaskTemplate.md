---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTaskTemplate.html
---

# CreateTaskTemplate
<a name="API_CreateTaskTemplate"></a>

Creates a new task template in the specified Connect Customer instance.

## Request Syntax
<a name="API_CreateTaskTemplate_RequestSyntax"></a>

```
PUT /instance/{{InstanceId}}/task/template HTTP/1.1
Content-type: application/json

{
   "ClientToken": "{{string}}",
   "Constraints": {
      "InvisibleFields": [
         {
            "Id": {
               "Name": "{{string}}"
            }
         }
      ],
      "ReadOnlyFields": [
         {
            "Id": {
               "Name": "{{string}}"
            }
         }
      ],
      "RequiredFields": [
         {
            "Id": {
               "Name": "{{string}}"
            }
         }
      ]
   },
   "ContactFlowId": "{{string}}",
   "Defaults": {
      "DefaultFieldValues": [
         {
            "DefaultValue": "{{string}}",
            "Id": {
               "Name": "{{string}}"
            }
         }
      ]
   },
   "Description": "{{string}}",
   "Fields": [
      {
         "Description": "{{string}}",
         "Id": {
            "Name": "{{string}}"
         },
         "SingleSelectOptions": [ "{{string}}" ],
         "Type": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "SelfAssignFlowId": "{{string}}",
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTaskTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateTaskTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Constraints](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Constraints"></a>
Constraints that are applicable to the fields listed. Although this parameter is marked as optional in the API model, the service requires it when calling `CreateTaskTemplate` or `UpdateTaskTemplate`. The `RequiredFields` array must contain at least one element, and the field of type `NAME` must be included in `RequiredFields`.
Type: [TaskTemplateConstraints](API_TaskTemplateConstraints.md) object
Required: No

 ** [ContactFlowId](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-ContactFlowId"></a>
The identifier of the flow that runs by default when a task is created by referencing this template.
Although this parameter is marked as optional, the request must contain either a `ContactFlowId` or a field of type `QUICK_CONNECT`.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Defaults](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Defaults"></a>
The default values for fields when a task is created by referencing this template.
Type: [TaskTemplateDefaults](API_TaskTemplateDefaults.md) object
Required: No

 ** [Description](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Description"></a>
The description of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Fields](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Fields"></a>
Fields that are part of the template.
The request must contain exactly one field of type `NAME`. This field must also be listed in the `RequiredFields` array within the `Constraints` parameter.
Type: Array of [TaskTemplateField](API_TaskTemplateField.md) objects
Required: Yes

 ** [Name](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Name"></a>
The name of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [SelfAssignFlowId](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-SelfAssignFlowId"></a>
The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Status](#API_CreateTaskTemplate_RequestSyntax) **   <a name="connect-CreateTaskTemplate-request-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_CreateTaskTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string"
}
```

## Response Elements
<a name="API_CreateTaskTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateTaskTemplate_ResponseSyntax) **   <a name="connect-CreateTaskTemplate-response-Arn"></a>
The Amazon Resource Name (ARN) for the task template resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [Id](#API_CreateTaskTemplate_ResponseSyntax) **   <a name="connect-CreateTaskTemplate-response-Id"></a>
The identifier of the task template resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_CreateTaskTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateTaskTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateTaskTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateTaskTemplate)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTaskTemplate.html
---

# UpdateTaskTemplate
<a name="API_UpdateTaskTemplate"></a>

Updates details about a specific task template in the specified Connect Customer instance. This operation does not support partial updates. Instead it does a full update of template content.

## Request Syntax
<a name="API_UpdateTaskTemplate_RequestSyntax"></a>

```
POST /instance/{{InstanceId}}/task/template/{{TaskTemplateId}} HTTP/1.1
Content-type: application/json

{
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
<a name="API_UpdateTaskTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [TaskTemplateId](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-uri-TaskTemplateId"></a>
A unique identifier for the task template.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_UpdateTaskTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Constraints](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Constraints"></a>
Constraints that are applicable to the fields listed. Although this parameter is marked as optional in the API model, the service requires it when calling `CreateTaskTemplate` or `UpdateTaskTemplate`. The `RequiredFields` array must contain at least one element, and the field of type `NAME` must be included in `RequiredFields`.
Type: [TaskTemplateConstraints](API_TaskTemplateConstraints.md) object
Required: No

 ** [ContactFlowId](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-ContactFlowId"></a>
The identifier of the flow that runs by default when a task is created by referencing this template.
Although this parameter is marked as optional, the request must contain either a `ContactFlowId` or a field of type `QUICK_CONNECT`.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Defaults](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Defaults"></a>
The default values for fields when a task is created by referencing this template.
Type: [TaskTemplateDefaults](API_TaskTemplateDefaults.md) object
Required: No

 ** [Description](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Description"></a>
The description of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [Fields](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Fields"></a>
Fields that are part of the template.
The request must contain exactly one field of type `NAME`. This field must also be listed in the `RequiredFields` array within the `Constraints` parameter.
Type: Array of [TaskTemplateField](API_TaskTemplateField.md) objects
Required: No

 ** [Name](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Name"></a>
The name of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [SelfAssignFlowId](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-SelfAssignFlowId"></a>
The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** [Status](#API_UpdateTaskTemplate_RequestSyntax) **   <a name="connect-UpdateTaskTemplate-request-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Although this parameter is marked as optional, the service requires it when calling `UpdateTaskTemplate`.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

## Response Syntax
<a name="API_UpdateTaskTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Constraints": {
      "InvisibleFields": [
         {
            "Id": {
               "Name": "string"
            }
         }
      ],
      "ReadOnlyFields": [
         {
            "Id": {
               "Name": "string"
            }
         }
      ],
      "RequiredFields": [
         {
            "Id": {
               "Name": "string"
            }
         }
      ]
   },
   "ContactFlowId": "string",
   "CreatedTime": number,
   "Defaults": {
      "DefaultFieldValues": [
         {
            "DefaultValue": "string",
            "Id": {
               "Name": "string"
            }
         }
      ]
   },
   "Description": "string",
   "Fields": [
      {
         "Description": "string",
         "Id": {
            "Name": "string"
         },
         "SingleSelectOptions": [ "string" ],
         "Type": "string"
      }
   ],
   "Id": "string",
   "InstanceId": "string",
   "LastModifiedTime": number,
   "Name": "string",
   "SelfAssignFlowId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateTaskTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Arn"></a>
The Amazon Resource Name (ARN) for the task template resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [Constraints](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Constraints"></a>
Constraints that are applicable to the fields listed. Although this parameter is marked as optional in the API model, the service requires it when calling `CreateTaskTemplate` or `UpdateTaskTemplate`. The `RequiredFields` array must contain at least one element, and the field of type `NAME` must be included in `RequiredFields`.
Type: [TaskTemplateConstraints](API_TaskTemplateConstraints.md) object

 ** [ContactFlowId](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-ContactFlowId"></a>
The identifier of the flow that runs by default when a task is created by referencing this template.
Type: String
Length Constraints: Maximum length of 500.

 ** [CreatedTime](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-CreatedTime"></a>
The timestamp when the task template was created.
Type: Timestamp

 ** [Defaults](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Defaults"></a>
The default values for fields when a task is created by referencing this template.
Type: [TaskTemplateDefaults](API_TaskTemplateDefaults.md) object

 ** [Description](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Description"></a>
The description of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Fields](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Fields"></a>
Fields that are part of the template.
Type: Array of [TaskTemplateField](API_TaskTemplateField.md) objects

 ** [Id](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Id"></a>
The identifier of the task template resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [InstanceId](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [LastModifiedTime](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-LastModifiedTime"></a>
The timestamp when the task template was last modified.
Type: Timestamp

 ** [Name](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Name"></a>
The name of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [SelfAssignFlowId](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-SelfAssignFlowId"></a>
The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.
Type: String
Length Constraints: Maximum length of 500.

 ** [Status](#API_UpdateTaskTemplate_ResponseSyntax) **   <a name="connect-UpdateTaskTemplate-response-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Type: String
Valid Values: `ACTIVE | INACTIVE`

## Errors
<a name="API_UpdateTaskTemplate_Errors"></a>

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
<a name="API_UpdateTaskTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateTaskTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateTaskTemplate)

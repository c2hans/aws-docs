---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_GetTaskTemplate.html
---

# GetTaskTemplate
<a name="API_GetTaskTemplate"></a>

Gets details about a specific task template in the specified Connect Customer instance.

## Request Syntax
<a name="API_GetTaskTemplate_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/task/template/{{TaskTemplateId}}?snapshotVersion={{SnapshotVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetTaskTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_GetTaskTemplate_RequestSyntax) **   <a name="connect-GetTaskTemplate-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [SnapshotVersion](#API_GetTaskTemplate_RequestSyntax) **   <a name="connect-GetTaskTemplate-request-uri-SnapshotVersion"></a>
The system generated version of a task template that is associated with a task, when the task is created.

 ** [TaskTemplateId](#API_GetTaskTemplate_RequestSyntax) **   <a name="connect-GetTaskTemplate-request-uri-TaskTemplateId"></a>
A unique identifier for the task template.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_GetTaskTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetTaskTemplate_ResponseSyntax"></a>

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
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetTaskTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Arn"></a>
The Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [Constraints](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Constraints"></a>
Constraints that are applicable to the fields listed. Although this parameter is marked as optional in the API model, the service requires it when calling `CreateTaskTemplate` or `UpdateTaskTemplate`. The `RequiredFields` array must contain at least one element, and the field of type `NAME` must be included in `RequiredFields`.
Type: [TaskTemplateConstraints](API_TaskTemplateConstraints.md) object

 ** [ContactFlowId](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-ContactFlowId"></a>
The identifier of the flow that runs by default when a task is created by referencing this template.
Type: String
Length Constraints: Maximum length of 500.

 ** [CreatedTime](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-CreatedTime"></a>
The timestamp when the task template was created.
Type: Timestamp

 ** [Defaults](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Defaults"></a>
The default values for fields when a task is created by referencing this template.
Type: [TaskTemplateDefaults](API_TaskTemplateDefaults.md) object

 ** [Description](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Description"></a>
The description of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [Fields](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Fields"></a>
Fields that are part of the template.
Type: Array of [TaskTemplateField](API_TaskTemplateField.md) objects

 ** [Id](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Id"></a>
A unique identifier for the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [InstanceId](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [LastModifiedTime](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-LastModifiedTime"></a>
The timestamp when the task template was last modified.
Type: Timestamp

 ** [Name](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Name"></a>
The name of the task template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.

 ** [SelfAssignFlowId](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-SelfAssignFlowId"></a>
The ContactFlowId for the flow that will be run if this template is used to create a self-assigned task.
Type: String
Length Constraints: Maximum length of 500.

 ** [Status](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Status"></a>
Marks a template as `ACTIVE` or `INACTIVE` for a task to refer to it. Tasks can only be created from `ACTIVE` templates. If a template is marked as `INACTIVE`, then a task that refers to this template cannot be created.
Type: String
Valid Values: `ACTIVE | INACTIVE`

 ** [Tags](#API_GetTaskTemplate_ResponseSyntax) **   <a name="connect-GetTaskTemplate-response-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.

## Errors
<a name="API_GetTaskTemplate_Errors"></a>

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
<a name="API_GetTaskTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/GetTaskTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/GetTaskTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

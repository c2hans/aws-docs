---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_CreateIdMappingWorkflow.html
---

# CreateIdMappingWorkflow
<a name="API_CreateIdMappingWorkflow"></a>

Creates an `IdMappingWorkflow` object which stores the configuration of the data processing job to be run. Each `IdMappingWorkflow` must have a unique workflow name. To modify an existing workflow, use the UpdateIdMappingWorkflow API.

**Important**
Incremental processing is not supported for ID mapping workflows.

## Request Syntax
<a name="API_CreateIdMappingWorkflow_RequestSyntax"></a>

```
POST /idmappingworkflows HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "idMappingTechniques": {
      "idMappingType": "{{string}}",
      "providerProperties": {
         "intermediateSourceConfiguration": {
            "intermediateS3Path": "{{string}}"
         },
         "providerConfiguration": {{JSON value}},
         "providerServiceArn": "{{string}}"
      },
      "ruleBasedProperties": {
         "attributeMatchingModel": "{{string}}",
         "recordMatchingModel": "{{string}}",
         "ruleDefinitionType": "{{string}}",
         "rules": [
            {
               "matchingKeys": [ "{{string}}" ],
               "ruleName": "{{string}}"
            }
         ]
      }
   },
   "incrementalRunConfig": {
      "incrementalRunType": "{{string}}"
   },
   "inputSourceConfig": [
      {
         "inputSourceARN": "{{string}}",
         "schemaName": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "outputSourceConfig": [
      {
         "KMSArn": "{{string}}",
         "outputS3Path": "{{string}}"
      }
   ],
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "workflowName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIdMappingWorkflow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateIdMappingWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [idMappingTechniques](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-idMappingTechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
Type: [IdMappingTechniques](API_IdMappingTechniques.md) object
Required: Yes

 ** [incrementalRunConfig](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-incrementalRunConfig"></a>
 The incremental run configuration for the ID mapping workflow.
Type: [IdMappingIncrementalRunConfig](API_IdMappingIncrementalRunConfig.md) object
Required: No

 ** [inputSourceConfig](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdMappingWorkflowInputSource](API_IdMappingWorkflowInputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [outputSourceConfig](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-outputSourceConfig"></a>
A list of `IdMappingWorkflowOutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
Type: Array of [IdMappingWorkflowOutputSource](API_IdMappingWorkflowOutputSource.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [roleArn](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `$|^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** [tags](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workflowName](#API_CreateIdMappingWorkflow_RequestSyntax) **   <a name="API-CreateIdMappingWorkflow-request-workflowName"></a>
The name of the workflow. There can't be multiple `IdMappingWorkflows` with the same name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Response Syntax
<a name="API_CreateIdMappingWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "idMappingTechniques": {
      "idMappingType": "string",
      "providerProperties": {
         "intermediateSourceConfiguration": {
            "intermediateS3Path": "string"
         },
         "providerConfiguration": JSON value,
         "providerServiceArn": "string"
      },
      "ruleBasedProperties": {
         "attributeMatchingModel": "string",
         "recordMatchingModel": "string",
         "ruleDefinitionType": "string",
         "rules": [
            {
               "matchingKeys": [ "string" ],
               "ruleName": "string"
            }
         ]
      }
   },
   "incrementalRunConfig": {
      "incrementalRunType": "string"
   },
   "inputSourceConfig": [
      {
         "inputSourceARN": "string",
         "schemaName": "string",
         "type": "string"
      }
   ],
   "outputSourceConfig": [
      {
         "KMSArn": "string",
         "outputS3Path": "string"
      }
   ],
   "roleArn": "string",
   "workflowArn": "string",
   "workflowName": "string"
}
```

## Response Elements
<a name="API_CreateIdMappingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [idMappingTechniques](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-idMappingTechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
Type: [IdMappingTechniques](API_IdMappingTechniques.md) object

 ** [incrementalRunConfig](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-incrementalRunConfig"></a>
 The incremental run configuration for the ID mapping workflow.
Type: [IdMappingIncrementalRunConfig](API_IdMappingIncrementalRunConfig.md) object

 ** [inputSourceConfig](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdMappingWorkflowInputSource](API_IdMappingWorkflowInputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [outputSourceConfig](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-outputSourceConfig"></a>
A list of `IdMappingWorkflowOutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
Type: Array of [IdMappingWorkflowOutputSource](API_IdMappingWorkflowOutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [roleArn](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `$|^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [workflowArn](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-workflowArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `IDMappingWorkflow`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`

 ** [workflowName](#API_CreateIdMappingWorkflow_ResponseSyntax) **   <a name="API-CreateIdMappingWorkflow-response-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_CreateIdMappingWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request couldn't be processed because of conflict in the current state of the resource. Example: Workflow already exists, Schema already exists, Workflow is currently running, etc.
HTTP Status Code: 400

 ** ExceedsLimitException **
The request was rejected because it attempted to create resources beyond the current AWS Entity Resolution account limits. The error message describes the limit exceeded.
 ** quotaName **
The name of the quota that has been breached.
 ** quotaValue **
The current quota value for the customers.
HTTP Status Code: 402

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_CreateIdMappingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/CreateIdMappingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/CreateIdMappingWorkflow)

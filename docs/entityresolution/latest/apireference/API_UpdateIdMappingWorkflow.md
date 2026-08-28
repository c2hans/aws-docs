---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_UpdateIdMappingWorkflow.html
---

# UpdateIdMappingWorkflow
<a name="API_UpdateIdMappingWorkflow"></a>

Updates an existing `IdMappingWorkflow`. This method is identical to CreateIdMappingWorkflow, except it uses an HTTP `PUT` request instead of a `POST` request, and the `IdMappingWorkflow` must already exist for the method to succeed.

**Important**
Incremental processing is not supported for ID mapping workflows.

## Request Syntax
<a name="API_UpdateIdMappingWorkflow_RequestSyntax"></a>

```
PUT /idmappingworkflows/{{workflowName}} HTTP/1.1
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
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIdMappingWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_UpdateIdMappingWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [idMappingTechniques](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-idMappingTechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
Type: [IdMappingTechniques](API_IdMappingTechniques.md) object
Required: Yes

 ** [incrementalRunConfig](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-incrementalRunConfig"></a>
 The incremental run configuration for the update ID mapping workflow.
Type: [IdMappingIncrementalRunConfig](API_IdMappingIncrementalRunConfig.md) object
Required: No

 ** [inputSourceConfig](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdMappingWorkflowInputSource](API_IdMappingWorkflowInputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

 ** [outputSourceConfig](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
Type: Array of [IdMappingWorkflowOutputSource](API_IdMappingWorkflowOutputSource.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [roleArn](#API_UpdateIdMappingWorkflow_RequestSyntax) **   <a name="API-UpdateIdMappingWorkflow-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access AWS resources on your behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `$|^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## Response Syntax
<a name="API_UpdateIdMappingWorkflow_ResponseSyntax"></a>

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
<a name="API_UpdateIdMappingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [idMappingTechniques](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-idMappingTechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
Type: [IdMappingTechniques](API_IdMappingTechniques.md) object

 ** [incrementalRunConfig](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-incrementalRunConfig"></a>
 The incremental run configuration for the update ID mapping workflow output.
Type: [IdMappingIncrementalRunConfig](API_IdMappingIncrementalRunConfig.md) object

 ** [inputSourceConfig](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdMappingWorkflowInputSource](API_IdMappingWorkflowInputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [outputSourceConfig](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
Type: Array of [IdMappingWorkflowOutputSource](API_IdMappingWorkflowOutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [roleArn](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access AWS resources on your behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `$|^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [workflowArn](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-workflowArn"></a>
The Amazon Resource Name (ARN) of the workflow role. AWS Entity Resolution assumes this role to access AWS resources on your behalf.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`

 ** [workflowName](#API_UpdateIdMappingWorkflow_ResponseSyntax) **   <a name="API-UpdateIdMappingWorkflow-response-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_UpdateIdMappingWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Entity Resolution service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource couldn't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by AWS Entity Resolution.
HTTP Status Code: 400

## See Also
<a name="API_UpdateIdMappingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/UpdateIdMappingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/UpdateIdMappingWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetIdMappingWorkflow.html
---

# GetIdMappingWorkflow
<a name="API_GetIdMappingWorkflow"></a>

Returns the `IdMappingWorkflow` with a given name, if it exists.

## Request Syntax
<a name="API_GetIdMappingWorkflow_RequestSyntax"></a>

```
GET /idmappingworkflows/{{workflowName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetIdMappingWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_GetIdMappingWorkflow_RequestSyntax) **   <a name="API-GetIdMappingWorkflow-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GetIdMappingWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetIdMappingWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
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
   "tags": {
      "string" : "string"
   },
   "updatedAt": number,
   "workflowArn": "string",
   "workflowName": "string"
}
```

## Response Elements
<a name="API_GetIdMappingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-createdAt"></a>
The timestamp of when the workflow was created.
Type: Timestamp

 ** [description](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [idMappingTechniques](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-idMappingTechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
Type: [IdMappingTechniques](API_IdMappingTechniques.md) object

 ** [incrementalRunConfig](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-incrementalRunConfig"></a>
 The incremental run configuration for the ID mapping workflow.
Type: [IdMappingIncrementalRunConfig](API_IdMappingIncrementalRunConfig.md) object

 ** [inputSourceConfig](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [IdMappingWorkflowInputSource](API_IdMappingWorkflowInputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [outputSourceConfig](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
Type: Array of [IdMappingWorkflowOutputSource](API_IdMappingWorkflowOutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [roleArn](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access AWS resources on your behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `$|^arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [tags](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-updatedAt"></a>
The timestamp of when the workflow was last updated.
Type: Timestamp

 ** [workflowArn](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-workflowArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `IdMappingWorkflow` .
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(idmappingworkflow/[a-zA-Z_0-9-]{1,255})`

 ** [workflowName](#API_GetIdMappingWorkflow_ResponseSyntax) **   <a name="API-GetIdMappingWorkflow-response-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_GetIdMappingWorkflow_Errors"></a>

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
<a name="API_GetIdMappingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetIdMappingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetIdMappingWorkflow)

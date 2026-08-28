---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_GetMatchingWorkflow.html
---

# GetMatchingWorkflow
<a name="API_GetMatchingWorkflow"></a>

Returns the `MatchingWorkflow` with a given name, if it exists.

## Request Syntax
<a name="API_GetMatchingWorkflow_RequestSyntax"></a>

```
GET /matchingworkflows/{{workflowName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMatchingWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowName](#API_GetMatchingWorkflow_RequestSyntax) **   <a name="API-GetMatchingWorkflow-request-uri-workflowName"></a>
The name of the workflow.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`
Required: Yes

## Request Body
<a name="API_GetMatchingWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMatchingWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "description": "string",
   "incrementalRunConfig": {
      "incrementalRunType": "string"
   },
   "inputSourceConfig": [
      {
         "applyNormalization": boolean,
         "inputSourceARN": "string",
         "schemaName": "string"
      }
   ],
   "outputSourceConfig": [
      {
         "applyNormalization": boolean,
         "customerProfilesIntegrationConfig": {
            "domainArn": "string",
            "objectTypeArn": "string"
         },
         "KMSArn": "string",
         "output": [
            {
               "hashed": boolean,
               "name": "string"
            }
         ],
         "outputS3Path": "string"
      }
   ],
   "resolutionTechniques": {
      "enableRealTimeMatching": boolean,
      "providerProperties": {
         "intermediateSourceConfiguration": {
            "intermediateS3Path": "string"
         },
         "providerConfiguration": JSON value,
         "providerServiceArn": "string"
      },
      "resolutionType": "string",
      "ruleBasedProperties": {
         "attributeMatchingModel": "string",
         "matchPurpose": "string",
         "rules": [
            {
               "matchingKeys": [ "string" ],
               "ruleName": "string"
            }
         ]
      },
      "ruleConditionProperties": {
         "matchingConfig": {
            "enableTransitiveMatching": boolean
         },
         "rules": [
            {
               "condition": "string",
               "ruleName": "string"
            }
         ]
      }
   },
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
<a name="API_GetMatchingWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-createdAt"></a>
The timestamp of when the workflow was created.
Type: Timestamp

 ** [description](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-description"></a>
A description of the workflow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [incrementalRunConfig](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-incrementalRunConfig"></a>
An object which defines an incremental run type and has only `incrementalRunType` as a field.
Type: [IncrementalRunConfig](API_IncrementalRunConfig.md) object

 ** [inputSourceConfig](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-inputSourceConfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
Type: Array of [InputSource](API_InputSource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.

 ** [outputSourceConfig](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-outputSourceConfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path`, `applyNormalization`, `KMSArn`, and `output`.
Type: Array of [OutputSource](API_OutputSource.md) objects
Array Members: Fixed number of 1 item.

 ** [resolutionTechniques](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-resolutionTechniques"></a>
An object which defines the `resolutionType` and the `ruleBasedProperties`.
Type: [ResolutionTechniques](API_ResolutionTechniques.md) object

 ** [roleArn](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access AWS resources on your behalf.
Type: String

 ** [tags](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updatedAt](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-updatedAt"></a>
The timestamp of when the workflow was last updated.
Type: Timestamp

 ** [workflowArn](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-workflowArn"></a>
The ARN (Amazon Resource Name) that AWS Entity Resolution generated for the `MatchingWorkflow`.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn):entityresolution:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(matchingworkflow/[a-zA-Z_0-9-]{1,255})`

 ** [workflowName](#API_GetMatchingWorkflow_ResponseSyntax) **   <a name="API-GetMatchingWorkflow-response-workflowName"></a>
The name of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_0-9-]*`

## Errors
<a name="API_GetMatchingWorkflow_Errors"></a>

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
<a name="API_GetMatchingWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/entityresolution-2018-05-10/GetMatchingWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/GetMatchingWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

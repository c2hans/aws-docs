---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

Gets all information about a workflow using its ID.

If a workflow is shared with you, you cannot export the workflow.

For more information about your workflow status, see [Verify the workflow status](https://docs.aws.amazon.com/omics/latest/dev/using-get-workflow.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
GET /workflow/{{id}}?export={{export}}&type={{type}}&workflowOwnerId={{workflowOwnerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [export](#API_GetWorkflow_RequestSyntax) **   <a name="omics-GetWorkflow-request-uri-export"></a>
The export format for the workflow.
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `DEFINITION | README`

 ** [id](#API_GetWorkflow_RequestSyntax) **   <a name="omics-GetWorkflow-request-uri-id"></a>
The workflow's ID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [type](#API_GetWorkflow_RequestSyntax) **   <a name="omics-GetWorkflow-request-uri-type"></a>
The workflow's type.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [workflowOwnerId](#API_GetWorkflow_RequestSyntax) **   <a name="omics-GetWorkflow-request-uri-workflowOwnerId"></a>
The ID of the workflow owner.
Pattern: `[0-9]{12}`

## Request Body
<a name="API_GetWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accelerators": "string",
   "arn": "string",
   "containerRegistryMap": {
      "imageMappings": [
         {
            "destinationImage": "string",
            "sourceImage": "string"
         }
      ],
      "registryMappings": [
         {
            "ecrAccountId": "string",
            "ecrRepositoryPrefix": "string",
            "upstreamRegistryUrl": "string",
            "upstreamRepositoryPrefix": "string"
         }
      ]
   },
   "creationTime": "string",
   "definition": "string",
   "definitionRepositoryDetails": {
      "connectionArn": "string",
      "fullRepositoryId": "string",
      "providerEndpoint": "string",
      "providerType": "string",
      "sourceReference": {
         "type": "string",
         "value": "string"
      }
   },
   "description": "string",
   "digest": "string",
   "engine": "string",
   "id": "string",
   "main": "string",
   "metadata": {
      "string" : "string"
   },
   "name": "string",
   "parameterTemplate": {
      "string" : {
         "description": "string",
         "optional": boolean
      }
   },
   "profileParameterTemplates": {
      "string" : {
         "string" : {
            "description": "string",
            "optional": boolean
         }
      }
   },
   "profiles": [ "string" ],
   "readme": "string",
   "readmePath": "string",
   "status": "string",
   "statusMessage": "string",
   "storageCapacity": number,
   "storageType": "string",
   "tags": {
      "string" : "string"
   },
   "type": "string",
   "uuid": "string"
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accelerators](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-accelerators"></a>
The computational accelerator specified to run the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `GPU`

 ** [arn](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-arn"></a>
The workflow's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [containerRegistryMap](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-containerRegistryMap"></a>
The registry map that this workflow is using.
Type: [ContainerRegistryMap](API_ContainerRegistryMap.md) object

 ** [creationTime](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-creationTime"></a>
When the workflow was created.
Type: Timestamp

 ** [definition](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-definition"></a>
The workflow's definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [definitionRepositoryDetails](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-definitionRepositoryDetails"></a>
Details about the source code repository that hosts the workflow definition files.
Type: [DefinitionRepositoryDetails](API_DefinitionRepositoryDetails.md) object

 ** [description](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-description"></a>
The workflow's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [digest](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-digest"></a>
The workflow's digest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [engine](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-engine"></a>
The workflow's engine.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `WDL | NEXTFLOW | CWL | WDL_LENIENT`

 ** [id](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-id"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [main](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-main"></a>
The path of the main definition file for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [metadata](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-metadata"></a>
Gets metadata for the workflow.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [name](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-name"></a>
The workflow's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [parameterTemplate](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-parameterTemplate"></a>
The workflow's parameter template.
Type: String to [WorkflowParameter](API_WorkflowParameter.md) object map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [profileParameterTemplates](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-profileParameterTemplates"></a>
A mapping of profile names to their parameter templates. Each profile defines its own set of parameters that you can use when starting a run with that profile.
Type: String to string to [WorkflowParameter](API_WorkflowParameter.md) object map map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [profiles](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-profiles"></a>
The list of Nextflow profiles that are available for this workflow. Profiles allow you to select predefined configuration settings at runtime.
Type: Array of strings

 ** [readme](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-readme"></a>
The README content for the workflow, providing documentation and usage information.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [readmePath](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-readmePath"></a>
The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the `README.md` file from the root directory of the repository will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-status"></a>
The workflow's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`

 ** [statusMessage](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-statusMessage"></a>
The workflow's status message.
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [storageCapacity](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-storageCapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.

 ** [storageType](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-storageType"></a>
The default storage type for runs using this workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`

 ** [tags](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-tags"></a>
The workflow's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [type](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-type"></a>
The workflow's type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [uuid](#API_GetWorkflow_ResponseSyntax) **   <a name="omics-GetWorkflow-response-uuid"></a>
The universally unique identifier (UUID) value for this workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_GetWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetWorkflow)

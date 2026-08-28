---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetWorkflowVersion.html
---

# GetWorkflowVersion
<a name="API_GetWorkflowVersion"></a>

Gets information about a workflow version. For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_GetWorkflowVersion_RequestSyntax"></a>

```
GET /workflow/{{workflowId}}/version/{{versionName}}?export={{export}}&type={{type}}&workflowOwnerId={{workflowOwnerId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [export](#API_GetWorkflowVersion_RequestSyntax) **   <a name="omics-GetWorkflowVersion-request-uri-export"></a>
The export format for the workflow.
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `DEFINITION | README`

 ** [type](#API_GetWorkflowVersion_RequestSyntax) **   <a name="omics-GetWorkflowVersion-request-uri-type"></a>
The workflow's type.
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [versionName](#API_GetWorkflowVersion_RequestSyntax) **   <a name="omics-GetWorkflowVersion-request-uri-versionName"></a>
The workflow version name.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

 ** [workflowId](#API_GetWorkflowVersion_RequestSyntax) **   <a name="omics-GetWorkflowVersion-request-uri-workflowId"></a>
The workflow's ID. The `workflowId` is not the UUID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

 ** [workflowOwnerId](#API_GetWorkflowVersion_RequestSyntax) **   <a name="omics-GetWorkflowVersion-request-uri-workflowOwnerId"></a>
The 12-digit account ID of the workflow owner. The workflow owner ID can be retrieved using the `GetShare` API operation. If you are the workflow owner, you do not need to include this ID.
Pattern: `[0-9]{12}`

## Request Body
<a name="API_GetWorkflowVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflowVersion_ResponseSyntax"></a>

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
   "main": "string",
   "metadata": {
      "string" : "string"
   },
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
   "uuid": "string",
   "versionName": "string",
   "workflowBucketOwnerId": "string",
   "workflowId": "string"
}
```

## Response Elements
<a name="API_GetWorkflowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accelerators](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-accelerators"></a>
The accelerator for this workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `GPU`

 ** [arn](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-arn"></a>
ARN of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `arn:.+`

 ** [containerRegistryMap](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-containerRegistryMap"></a>
The registry map that this workflow version uses.
Type: [ContainerRegistryMap](API_ContainerRegistryMap.md) object

 ** [creationTime](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-creationTime"></a>
When the workflow version was created.
Type: Timestamp

 ** [definition](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-definition"></a>
Definition of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [definitionRepositoryDetails](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-definitionRepositoryDetails"></a>
Details about the source code repository that hosts the workflow version definition files.
Type: [DefinitionRepositoryDetails](API_DefinitionRepositoryDetails.md) object

 ** [description](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-description"></a>
Description of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [digest](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-digest"></a>
The workflow version's digest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [engine](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-engine"></a>
The workflow engine for this workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `WDL | NEXTFLOW | CWL | WDL_LENIENT`

 ** [main](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-main"></a>
The path of the main definition file for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [metadata](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-metadata"></a>
The metadata for the workflow version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [parameterTemplate](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-parameterTemplate"></a>
The parameter template for the workflow version.
Type: String to [WorkflowParameter](API_WorkflowParameter.md) object map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [profileParameterTemplates](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-profileParameterTemplates"></a>
A mapping of profile names to their parameter templates. Each profile defines its own set of parameters that you can use when starting a run with that profile.
Type: String to string to [WorkflowParameter](API_WorkflowParameter.md) object map map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [profiles](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-profiles"></a>
The list of Nextflow profiles that are available for this workflow version. Profiles allow you to select predefined configuration settings at runtime.
Type: Array of strings

 ** [readme](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-readme"></a>
The README content for the workflow version, providing documentation and usage information specific to this version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [readmePath](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-readmePath"></a>
The path to the workflow version README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the `README.md` file from the root directory of the repository will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [status](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-status"></a>
The workflow version status
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`

 ** [statusMessage](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-statusMessage"></a>
The workflow version status message
Type: String
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [storageCapacity](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-storageCapacity"></a>
The default run storage capacity for static storage.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.

 ** [storageType](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-storageType"></a>
The default storage type for the run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`

 ** [tags](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-tags"></a>
The workflow version tags
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [type](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-type"></a>
The workflow version type
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `PRIVATE | READY2RUN`

 ** [uuid](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-uuid"></a>
The universally unique identifier (UUID) value for this workflow version
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [versionName](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-versionName"></a>
The workflow version name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`

 ** [workflowBucketOwnerId](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-workflowBucketOwnerId"></a>
 AWS Id of the owner of the bucket.
Type: String
Pattern: `[0-9]{12}`

 ** [workflowId](#API_GetWorkflowVersion_ResponseSyntax) **   <a name="omics-GetWorkflowVersion-response-workflowId"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

## Errors
<a name="API_GetWorkflowVersion_Errors"></a>

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
<a name="API_GetWorkflowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetWorkflowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetWorkflowVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

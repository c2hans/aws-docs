---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateWorkflowVersion.html
---

# CreateWorkflowVersion
<a name="API_CreateWorkflowVersion"></a>

Creates a new workflow version for the workflow that you specify with the `workflowId` parameter.

When you create a new version of a workflow, you need to specify the configuration for the new version. It doesn't inherit any configuration values from the workflow.

Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.

**Note**
Don't include any personally identifiable information (PII) in the version name. Version names appear in the workflow version ARN.

For more information, see [Workflow versioning in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateWorkflowVersion_RequestSyntax"></a>

```
POST /workflow/{{workflowId}}/version HTTP/1.1
Content-type: application/json

{
   "accelerators": "{{string}}",
   "containerRegistryMap": {
      "imageMappings": [
         {
            "destinationImage": "{{string}}",
            "sourceImage": "{{string}}"
         }
      ],
      "registryMappings": [
         {
            "ecrAccountId": "{{string}}",
            "ecrRepositoryPrefix": "{{string}}",
            "upstreamRegistryUrl": "{{string}}",
            "upstreamRepositoryPrefix": "{{string}}"
         }
      ]
   },
   "containerRegistryMapUri": "{{string}}",
   "definitionRepository": {
      "connectionArn": "{{string}}",
      "excludeFilePatterns": [ "{{string}}" ],
      "fullRepositoryId": "{{string}}",
      "sourceReference": {
         "type": "{{string}}",
         "value": "{{string}}"
      }
   },
   "definitionUri": "{{string}}",
   "definitionZip": {{blob}},
   "description": "{{string}}",
   "engine": "{{string}}",
   "main": "{{string}}",
   "parameterTemplate": {
      "{{string}}" : {
         "description": "{{string}}",
         "optional": {{boolean}}
      }
   },
   "parameterTemplatePath": "{{string}}",
   "readmeMarkdown": "{{string}}",
   "readmePath": "{{string}}",
   "readmeUri": "{{string}}",
   "requestId": "{{string}}",
   "storageCapacity": {{number}},
   "storageType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "versionName": "{{string}}",
   "workflowBucketOwnerId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowId](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-uri-workflowId"></a>
The ID of the workflow where you are creating the new version. The `workflowId` is not the UUID.
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_CreateWorkflowVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accelerators](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-accelerators"></a>
The computational accelerator for this workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `GPU`
Required: No

 ** [containerRegistryMap](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-containerRegistryMap"></a>
(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the * AWS HealthOmics User Guide*.
Type: [ContainerRegistryMap](API_ContainerRegistryMap.md) object
Required: No

 ** [containerRegistryMapUri](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-containerRegistryMapUri"></a>
(Optional) URI of the S3 location for the registry mapping file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [definitionRepository](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-definitionRepository"></a>
The repository information for the workflow version definition. This allows you to source your workflow version definition directly from a code repository.
Type: [DefinitionRepository](API_DefinitionRepository.md) object
Required: No

 ** [definitionUri](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-definitionUri"></a>
The S3 URI of a definition for this workflow version. The S3 bucket must be in the same region as this workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [definitionZip](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-definitionZip"></a>
A ZIP archive containing the main workflow definition file and dependencies that it imports for this workflow version. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see Workflow definition requirements in the * AWS HealthOmics User Guide*.
Type: Base64-encoded binary data object
Required: No

 ** [description](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-description"></a>
A description for this workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [engine](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-engine"></a>
The workflow engine for this workflow version. This is only required if you have workflow definition files from more than one engine in your zip file. Otherwise, the service can detect the engine automatically from your workflow definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `WDL | NEXTFLOW | CWL | WDL_LENIENT`
Required: No

 ** [main](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-main"></a>
The path of the main definition file for this workflow version. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: `workflow-definition/main-file.wdl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [parameterTemplate](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-parameterTemplate"></a>
A parameter template for this workflow version. If this field is blank, AWS HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see [Parameter template files](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html) in the * AWS HealthOmics User Guide*.
Type: String to [WorkflowParameter](API_WorkflowParameter.md) object map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [parameterTemplatePath](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-parameterTemplatePath"></a>
The path to the workflow version parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow version. If not specified, the workflow version will be created without a parameter template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeMarkdown](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-readmeMarkdown"></a>
The markdown content for the workflow version's README file. This provides documentation and usage information for users of this specific workflow version.
Type: String
Required: No

 ** [readmePath](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-readmePath"></a>
The path to the workflow version README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the `README.md` file from the root directory of the repository will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeUri](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-readmeUri"></a>
The S3 URI of the README file for the workflow version. This file provides documentation and usage information for the workflow version. Requirements include:
+ The S3 URI must begin with `s3://USER-OWNED-BUCKET/`
+ The requester must have access to the S3 bucket and object.
+ The max README content length is 500 KiB.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/((.{1,1024}))`
Required: No

 ** [requestId](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-requestId"></a>
An idempotency token to ensure that duplicate workflows are not created when AWS HealthOmics submits retry requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [storageCapacity](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-storageCapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow version. The `storageCapacity` can be overwritten at run time. The storage capacity is not required for runs with a `DYNAMIC` storage type.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [storageType](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-storageType"></a>
The default storage type for runs that use this workflow version. The `storageType` can be overridden at run time. `DYNAMIC` storage dynamically scales the storage up or down, based on file system utilization. STATIC storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see [Run storage types](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** [tags](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-tags"></a>
Tags for this workflow version. You can define up to 50 tags for the workflow. For more information, see [Adding a tag](https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html) in the * AWS HealthOmics User Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [versionName](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-versionName"></a>
A name for the workflow version. Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.
The version name must start with a letter or number and it can include upper-case and lower-case letters, numbers, hyphens, periods and underscores. The maximum length is 64 characters. You can use a simple naming scheme, such as version1, version2, version3. You can also match your workflow versions with your own internal versioning conventions, such as 2.7.0, 2.7.1, 2.7.2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: Yes

 ** [workflowBucketOwnerId](#API_CreateWorkflowVersion_RequestSyntax) **   <a name="omics-CreateWorkflowVersion-request-workflowBucketOwnerId"></a>
 AWS Id of the owner of the S3 bucket that contains the workflow definition. You need to specify this parameter if your account is not the bucket owner.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_CreateWorkflowVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string",
   "versionName": "string",
   "workflowId": "string"
}
```

## Response Elements
<a name="API_CreateWorkflowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-arn"></a>
ARN of the workflow version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `arn:.+`

 ** [status](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-status"></a>
The workflow version status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`

 ** [tags](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-tags"></a>
The workflow version's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-uuid"></a>
The universally unique identifier (UUID) value for this workflow version.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

 ** [versionName](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-versionName"></a>
The workflow version name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`

 ** [workflowId](#API_CreateWorkflowVersion_ResponseSyntax) **   <a name="omics-CreateWorkflowVersion-response-workflowId"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

## Errors
<a name="API_CreateWorkflowVersion_Errors"></a>

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
<a name="API_CreateWorkflowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateWorkflowVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateWorkflowVersion)

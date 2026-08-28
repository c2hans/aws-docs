---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateWorkflow.html
---

# CreateWorkflow
<a name="API_CreateWorkflow"></a>

Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:
+  *Workflow definition file:* A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in `.zip` format. For more information, see [Workflow definition files](https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html) in AWS HealthOmics.
  + You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see [Example prompts for Amazon Q CLI](https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts) and the [AWS HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai) on GitHub.
+  *(Optional) Parameter template file:* A parameter template file written in JSON. Create the file to define the run parameters, or AWS HealthOmics generates the parameter template for you. For more information, see [Parameter template files for HealthOmics workflows](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html).
+  *ECR container images:* Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.
+  *(Optional) Sentieon licenses:* Request a Sentieon license to use the Sentieon software in private workflows.

For more information, see [Creating or updating a private workflow in AWS HealthOmics](https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_CreateWorkflow_RequestSyntax"></a>

```
POST /workflow HTTP/1.1
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
   "name": "{{string}}",
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
   "workflowBucketOwnerId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accelerators](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-accelerators"></a>
The computational accelerator specified to run the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `GPU`
Required: No

 ** [containerRegistryMap](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-containerRegistryMap"></a>
(Optional) Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see [Container images](https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html) in the * AWS HealthOmics User Guide*.
Type: [ContainerRegistryMap](API_ContainerRegistryMap.md) object
Required: No

 ** [containerRegistryMapUri](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-containerRegistryMapUri"></a>
(Optional) URI of the S3 location for the registry mapping file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 750.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [definitionRepository](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-definitionRepository"></a>
The repository information for the workflow definition. This allows you to source your workflow definition directly from a code repository.
Type: [DefinitionRepository](API_DefinitionRepository.md) object
Required: No

 ** [definitionUri](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-definitionUri"></a>
The S3 URI of a definition for the workflow. The S3 bucket must be in the same region as the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [definitionZip](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-definitionZip"></a>
A ZIP archive containing the main workflow definition file and dependencies that it imports for the workflow. You can use a file with a ://fileb prefix instead of the Base64 string. For more information, see [Workflow definition requirements](https://docs.aws.amazon.com/omics/latest/dev/workflow-defn-requirements.html) in the * AWS HealthOmics User Guide*.
Type: Base64-encoded binary data object
Required: No

 ** [description](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-description"></a>
A description for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [engine](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-engine"></a>
The workflow engine for the workflow. By default, AWS HealthOmics detects the engine automatically from your workflow definition. Provide a value if you have workflow definition files from more than one engine in your zip file, or to use WDL lenient.
WDL lenient is designed to handle workflows migrated from Cromwell. It supports customer Cromwell directives and some non-conformant logic. For details, see [Implicit type conversion in WDL lenient](https://docs.aws.amazon.com/omics/latest/dev/workflow-wdl-type-conversion.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `WDL | NEXTFLOW | CWL | WDL_LENIENT`
Required: No

 ** [main](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-main"></a>
The path of the main definition file for the workflow. This parameter is not required if the ZIP archive contains only one workflow definition file, or if the main definition file is named “main”. An example path is: `workflow-definition/main-file.wdl`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [name](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-name"></a>
Name (optional but highly recommended) for the workflow to locate relevant information in the CloudWatch logs and AWS HealthOmics console.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [parameterTemplate](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-parameterTemplate"></a>
A parameter template for the workflow. If this field is blank, AWS HealthOmics will automatically parse the parameter template values from your workflow definition file. To override these service generated default values, provide a parameter template. To view an example of a parameter template, see [Parameter template files](https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html) in the * AWS HealthOmics User Guide*.
Type: String to [WorkflowParameter](API_WorkflowParameter.md) object map
Map Entries: Maximum number of 2000 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [parameterTemplatePath](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-parameterTemplatePath"></a>
The path to the workflow parameter template JSON file within the repository. This file defines the input parameters for runs that use this workflow. If not specified, the workflow will be created without a parameter template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeMarkdown](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-readmeMarkdown"></a>
The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
Type: String
Required: No

 ** [readmePath](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-readmePath"></a>
The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the `README.md` file from the root directory of the repository will be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** [readmeUri](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-readmeUri"></a>
The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. Requirements include:
+ The S3 URI must begin with `s3://USER-OWNED-BUCKET/`
+ The requester must have access to the S3 bucket and object.
+ The max README content length is 500 KiB.
Type: String
Pattern: `s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/((.{1,1024}))`
Required: No

 ** [requestId](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-requestId"></a>
An idempotency token to ensure that duplicate workflows are not created when AWS HealthOmics submits retry requests.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: Yes

 ** [storageCapacity](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-storageCapacity"></a>
The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The `storageCapacity` can be overwritten at run time. The storage capacity is not required for runs with a `DYNAMIC` storage type.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100000.
Required: No

 ** [storageType](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-storageType"></a>
The default storage type for runs that use this workflow. The `storageType` can be overridden at run time. `DYNAMIC` storage dynamically scales the storage up or down, based on file system utilization. `STATIC` storage allocates a fixed amount of storage. For more information about dynamic and static storage types, see [Run storage types](https://docs.aws.amazon.com/omics/latest/dev/workflows-run-types.html) in the * AWS HealthOmics User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `STATIC | DYNAMIC`
Required: No

 ** [tags](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-tags"></a>
Tags for the workflow. You can define up to 50 tags for the workflow. For more information, see [Adding a tag](https://docs.aws.amazon.com/omics/latest/dev/add-a-tag.html) in the * AWS HealthOmics User Guide*.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [workflowBucketOwnerId](#API_CreateWorkflow_RequestSyntax) **   <a name="omics-CreateWorkflow-request-workflowBucketOwnerId"></a>
The AWS account ID of the expected owner of the S3 bucket that contains the workflow definition. If not specified, the service skips the validation.
Type: String
Pattern: `[0-9]{12}`
Required: No

## Response Syntax
<a name="API_CreateWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "status": "string",
   "tags": {
      "string" : "string"
   },
   "uuid": "string"
}
```

## Response Elements
<a name="API_CreateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateWorkflow_ResponseSyntax) **   <a name="omics-CreateWorkflow-response-arn"></a>
The workflow's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:.+`

 ** [id](#API_CreateWorkflow_ResponseSyntax) **   <a name="omics-CreateWorkflow-response-id"></a>
The workflow's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `[0-9]+`

 ** [status](#API_CreateWorkflow_ResponseSyntax) **   <a name="omics-CreateWorkflow-response-status"></a>
The workflow's status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Valid Values: `CREATING | ACTIVE | UPDATING | DELETED | FAILED | INACTIVE`

 ** [tags](#API_CreateWorkflow_ResponseSyntax) **   <a name="omics-CreateWorkflow-response-tags"></a>
The workflow's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [uuid](#API_CreateWorkflow_ResponseSyntax) **   <a name="omics-CreateWorkflow-response-uuid"></a>
The universally unique identifier (UUID) value for this workflow.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`

## Errors
<a name="API_CreateWorkflow_Errors"></a>

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
<a name="API_CreateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateWorkflow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateWorkflow.html
---

# CreateWorkflow
<a name="API_CreateWorkflow"></a>

Creates a new workflow or a new version of an existing workflow. If a workflow with the same name and semantic version already exists, and your request changes its configuration, Image Builder creates a new build version. If the configuration is identical to the latest build version, the request fails because that workflow configuration already exists.

## Request Syntax
<a name="API_CreateWorkflow_RequestSyntax"></a>

```
PUT /CreateWorkflow HTTP/1.1
Content-type: application/json

{
   "changeDescription": "{{string}}",
   "clientToken": "{{string}}",
   "data": "{{string}}",
   "description": "{{string}}",
   "dryRun": {{boolean}},
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "semanticVersion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "type": "{{string}}",
   "uri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateWorkflow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateWorkflow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [changeDescription](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-changeDescription"></a>
Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [clientToken](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-clientToken"></a>
A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) in the *Amazon EC2 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [data](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-data"></a>
The UTF-8 encoded YAML document content for the workflow, up to 16,000 characters. For larger documents, store the document in Amazon S3 and specify the `uri` property instead. You must specify exactly one of the `data` or `uri` properties.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16000.
Pattern: `[^\x00]+`
Required: No

 ** [description](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-description"></a>
Describes the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [dryRun](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-dryRun"></a>
Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a `DryRunOperationException` error response.
Type: Boolean
Required: No

 ** [kmsKeyId](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-kmsKeyId"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key used to encrypt this workflow resource. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the * AWS Key Management Service Developer Guide*. If you don't specify a key, Image Builder encrypts the workflow document with a KMS key that Image Builder owns.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-name"></a>
The name of the workflow to create. Image Builder generates the workflow ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. If a workflow with the same name and semantic version already exists in your account in the same AWS Region, the request creates a new build version for it. If the content is also identical to the latest build version, the request fails because the workflow already exists.
Type: String
Pattern: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
Required: Yes

 ** [semanticVersion](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-semanticVersion"></a>
The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.
The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.
 **Assignment:** For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.
 **Patterns:** You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
Type: String
Pattern: `^[0-9]+\.[0-9]+\.[0-9]+$`
Required: Yes

 ** [tags](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-tags"></a>
Tags that apply to the workflow resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z0-9\s_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [type](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-type"></a>
The image creation stage that this workflow applies to. Image Builder validates the workflow document steps against the stage you specify.
Type: String
Valid Values: `BUILD | TEST | DISTRIBUTION`
Required: Yes

 ** [uri](#API_CreateWorkflow_RequestSyntax) **   <a name="imagebuilder-CreateWorkflow-request-uri"></a>
The `uri` of a YAML workflow document file stored in Amazon S3. This must be an S3 URL (`s3://bucket/key`), and you must have permission to access the S3 bucket it points to. A workflow document that you provide from Amazon S3 can be up to your service quota for workflow size.
Alternatively, you can specify the YAML document inline, using the workflow `data` property. You must specify exactly one of the `data` or `uri` properties.
Type: String
Required: No

## Response Syntax
<a name="API_CreateWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "workflowBuildVersionArn": "string"
}
```

## Response Elements
<a name="API_CreateWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_CreateWorkflow_ResponseSyntax) **   <a name="imagebuilder-CreateWorkflow-response-clientToken"></a>
The client token that uniquely identifies the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [latestVersionReferences](#API_CreateWorkflow_ResponseSyntax) **   <a name="imagebuilder-CreateWorkflow-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [workflowBuildVersionArn](#API_CreateWorkflow_ResponseSyntax) **   <a name="imagebuilder-CreateWorkflow-response-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the workflow resource that the request created.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`

## Errors
<a name="API_CreateWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** DryRunOperationException **
The dry run operation of the resource was successful, and no resources or mutations were actually performed due to the dry run flag in the request.
HTTP Status Code: 412

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** IdempotentParameterMismatchException **
You have specified a client token for an operation using parameter values that differ from a previous request that used the same client token.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
You have specified a combination of parameters that isn't valid. For example, two mutually exclusive parameters, or a parameter without its required companion parameter. Review the error message for details.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** InvalidVersionNumberException **
Your version number is out of bounds or does not follow the required syntax.
HTTP Status Code: 400

 ** ResourceInUseException **
The resource that you are trying to operate on is currently in use. Review the message details and retry later.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded the number of permitted resources or operations for this service. For service quotas, see [EC2 Image Builder endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html#limits_imagebuilder).
HTTP Status Code: 402

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_CreateWorkflow_Examples"></a>

### Create a build workflow from an inline document
<a name="API_CreateWorkflow_Example_1"></a>

The following example creates a build workflow from a YAML workflow document provided inline in the request.

#### Sample Request
<a name="API_CreateWorkflow_Example_1_Request"></a>

```
PUT /CreateWorkflow HTTP/1.1
Content-type: application/json

{
    "name": "my-example-workflow",
    "semanticVersion": "1.0.0",
    "description": "Workflow to build an AMI",
    "type": "BUILD",
    "data": "name: my-example-workflow\ndescription: Workflow to build an AMI\nschemaVersion: 1.0\nsteps:\n  - name: LaunchBuildInstance\n    action: LaunchInstance\n    onFailure: Abort\n    inputs:\n      waitFor: ssmAgent\n  - name: ApplyBuildComponents\n    action: ExecuteComponents\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: CreateOutputAMI\n    action: CreateImage\n    onFailure: Abort\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n  - name: TerminateBuildInstance\n    action: TerminateInstance\n    onFailure: Continue\n    inputs:\n      instanceId.$: $.stepOutputs.LaunchBuildInstance.instanceId\n",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE54321"
}
```

#### Sample Response
<a name="API_CreateWorkflow_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE54321",
    "workflowBuildVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1",
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0"
    }
}
```

## See Also
<a name="API_CreateWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/CreateWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CreateWorkflow)

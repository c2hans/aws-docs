---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflow.html
---

# GetWorkflow
<a name="API_GetWorkflow"></a>

Retrieves a workflow resource object.

## Request Syntax
<a name="API_GetWorkflow_RequestSyntax"></a>

```
GET /GetWorkflow?workflowBuildVersionArn={{workflowBuildVersionArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetWorkflow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workflowBuildVersionArn](#API_GetWorkflow_RequestSyntax) **   <a name="imagebuilder-GetWorkflow-request-uri-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the workflow resource that you want to get. You can specify a build version ARN, or a version ARN with or without wildcards (`x`) in its version segments. Image Builder resolves version and wildcard ARNs to the most recent matching build version.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

## Request Body
<a name="API_GetWorkflow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetWorkflow_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "latestVersionReferences": {
      "latestMajorVersionArn": "string",
      "latestMinorVersionArn": "string",
      "latestPatchVersionArn": "string",
      "latestVersionArn": "string"
   },
   "workflow": {
      "arn": "string",
      "changeDescription": "string",
      "data": "string",
      "dateCreated": "string",
      "description": "string",
      "kmsKeyId": "string",
      "name": "string",
      "owner": "string",
      "parameters": [
         {
            "defaultValue": [ "string" ],
            "description": "string",
            "name": "string",
            "type": "string"
         }
      ],
      "state": {
         "reason": "string",
         "status": "string"
      },
      "tags": {
         "string" : "string"
      },
      "type": "string",
      "version": "string"
   }
}
```

## Response Elements
<a name="API_GetWorkflow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [latestVersionReferences](#API_GetWorkflow_ResponseSyntax) **   <a name="imagebuilder-GetWorkflow-response-latestVersionReferences"></a>
A set of wildcard version ARNs that always reference the latest version of the resource. ARNs are included for the latest version overall, and for the latest versions within the same major, minor, and patch levels.
Type: [LatestVersionReferences](API_LatestVersionReferences.md) object

 ** [workflow](#API_GetWorkflow_ResponseSyntax) **   <a name="imagebuilder-GetWorkflow-response-workflow"></a>
The workflow resource specified in the request.
Type: [Workflow](API_Workflow.md) object

## Errors
<a name="API_GetWorkflow_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CallRateLimitExceededException **
You have exceeded the permitted request rate for the Amazon EC2 APIs that Image Builder calls on your behalf. Retry with an increasing or variable delay between requests.
HTTP Status Code: 429

 ** ClientException **
A generic client error. This error usually indicates that the request failed a validation check, such as when a downstream service rejects a configured value.
HTTP Status Code: 400

 ** ForbiddenException **
You are not authorized to perform the requested operation.
HTTP Status Code: 403

 ** InvalidRequestException **
The request is malformed or otherwise invalid. Verify the request and try again.
HTTP Status Code: 400

 ** ServiceException **
An internal server error occurred while Image Builder processed the request. Retrying the request may succeed.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is unable to process your request at this time.
HTTP Status Code: 503

## Examples
<a name="API_GetWorkflow_Examples"></a>

### Get the details of a workflow build version
<a name="API_GetWorkflow_Example_1"></a>

The following example retrieves a workflow build version. The response includes the YAML workflow document in the `data` field and the parameters that Image Builder extracted from it when the workflow was created.

#### Sample Request
<a name="API_GetWorkflow_Example_1_Request"></a>

```
GET /GetWorkflow?workflowBuildVersionArn=arn%3Aaws%3Aimagebuilder%3Aus-west-2%3A111122223333%3Aworkflow%2Fbuild%2Fmy-example-workflow%2F1.0.0%2F1 HTTP/1.1
```

#### Sample Response
<a name="API_GetWorkflow_Example_1_Response"></a>

```
HTTP/1.1 200
Content-type: application/json

{
    "workflow": {
        "arn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0/1",
        "name": "my-example-workflow",
        "version": "1.0.0",
        "description": "Builds an AMI, and then waits for an external action before the workflow completes",
        "changeDescription": "Initial version",
        "type": "BUILD",
        "owner": "111122223333",
        "data": "name: my-example-workflow\ndescription: Workflow to build an AMI, then wait for an external action before it completes\nschemaVersion: 1.0\n\nparameters:\n  - name: waitForActionAtEnd\n    type: boolean\n    default: true\n\nsteps:\n  - name: LaunchBuildInstance\n    action: LaunchInstance\n    onFailure: Abort\n    inputs:\n      waitFor: \"ssmAgent\"\n\n  - name: ApplyBuildComponents\n    action: ExecuteComponents\n    onFailure: Abort\n    inputs:\n      instanceId.$: \"$.stepOutputs.LaunchBuildInstance.instanceId\"\n\n  - name: CreateOutputAMI\n    action: CreateImage\n    onFailure: Abort\n    inputs:\n      instanceId.$: \"$.stepOutputs.LaunchBuildInstance.instanceId\"\n\n  - name: TerminateBuildInstance\n    action: TerminateInstance\n    onFailure: Continue\n    inputs:\n      instanceId.$: \"$.stepOutputs.LaunchBuildInstance.instanceId\"\n\n  - name: WaitForActionAtEnd\n    action: WaitForAction\n    if:\n      booleanEquals: true\n      value: \"$.parameters.waitForActionAtEnd\"\n",
        "dateCreated": "2026-09-09T19:55:55.731Z",
        "tags": {},
        "parameters": [
            {
                "name": "waitForActionAtEnd",
                "type": "boolean",
                "defaultValue": [
                    "true"
                ]
            }
        ]
    },
    "latestVersionReferences": {
        "latestVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/x.x.x",
        "latestMajorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.x.x",
        "latestMinorVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.x",
        "latestPatchVersionArn": "arn:aws:imagebuilder:us-west-2:111122223333:workflow/build/my-example-workflow/1.0.0"
    }
}
```

## See Also
<a name="API_GetWorkflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/imagebuilder-2019-12-02/GetWorkflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/GetWorkflow)

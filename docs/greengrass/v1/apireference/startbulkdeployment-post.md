---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/startbulkdeployment-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# StartBulkDeployment
<a name="startbulkdeployment-post"></a>

Deploys multiple groups in one operation. This action starts the bulk deployment of a specified set of group versions. Each group version deployment is triggered with an adaptive rate that has a fixed upper limit. We recommend that you include an `X-Amzn-Client-Token` token in every `StartBulkDeployment` request. These requests are idempotent with respect to the token and the request parameters.

URI: `POST /greengrass/bulk/deployments`

Produces: application/json

## CLI:
<a name="startbulkdeployment-post-cli"></a>

```
aws greengrass start-bulk-deployment \
  [--input-file-uri <value>] \
  [--execution-role-arn <value>] \
  [--tags <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"InputFileUri": "string",
"ExecutionRoleArn": "string",
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
},
"AmznClientToken": "string"
}
```

## Parameters:
<a name="startbulkdeployment-post-params"></a>

[**StartBulkDeploymentRequestBody**](parameters-startbulkdeploymentrequestbody.md)

where used: body; required: true

```
{
"InputFileUri": "string",
"ExecutionRoleArn": "string",
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```
schema:
StartBulkDeploymentRequest
Information about a bulk deployment. You cannot start a new bulk deployment while another one is still running or in a non-terminal state.
type: object
required: ["InputFileUri", "ExecutionRoleArn"]
InputFileUri
The URI of the input file in the S3 bucket. The execution role must have `getObject` permissions on this bucket to access the input file. The input file is a JSON-serialized, line-delimited file with UTF-8 encoding that provides a list of group and version IDs and the deployment type. This file must be less than 100 MB. Currently, AWS IoT Greengrass supports only `NewDeployment` deployment types.

```
{"GroupId":"{{groupId1}}", "GroupVersionId":"{{groupVersionId1}}", "DeploymentType":"NewDeployment"}
{"GroupId":"{{groupId2}}", "GroupVersionId":"{{groupVersionId2}}", "DeploymentType":"NewDeployment"}
{"GroupId":"{{groupId3}}", "GroupVersionId":"{{groupVersionId3}}", "DeploymentType":"NewDeployment"}
...
```
For more information, including the input file format, see [Create Bulk Deployments For Groups](https://docs.aws.amazon.com/greengrass/latest/developerguide/bulk-deploy-cli.html).
type: string
ExecutionRoleArn
The ARN of the execution role to associate with the bulk deployment operation. This IAM role must allow the `greengrass:CreateDeployment` action for all group versions that are listed in the input file. This IAM role must have access to the S3 bucket that contains the input file.
type: string
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="startbulkdeployment-post-resp"></a>

**200**
Success.
 [ StartBulkDeploymentResponse](definitions-startbulkdeploymentresponse.md)

```
{
"BulkDeploymentId": "string",
"BulkDeploymentArn": "string"
}
```
StartBulkDeploymentResponse
type: object
BulkDeploymentId
The ID of the bulk deployment.
type: string
BulkDeploymentArn
The ARN of the bulk deployment.
type: string

**400**
Invalid request.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
type: string
ErrorDetails
A list of error details.
type: array
items: [ErrorDetail](definitions-errordetail.md)
ErrorDetail
Details about the error.
type: object
DetailedErrorCode
A detailed error code.
type: string
DetailedErrorMessage
A detailed error message.
type: string

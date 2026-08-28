---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-bulk-deployments.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/bulk/deployments
<a name="-greengrass-bulk-deployments"></a>

## POST
<a name="-greengrass-bulk-deployments-post"></a>

 `POST /greengrass/bulk/deployments`

Operation ID: [StartBulkDeployment](startbulkdeployment-post.md)

Deploys multiple groups in one operation. This action starts the bulk deployment of a specified set of group versions. Each group version deployment is triggered with an adaptive rate that has a fixed upper limit. We recommend that you include an `X-Amzn-Client-Token` token in every `StartBulkDeployment` request. These requests are idempotent with respect to the token and the request parameters.

Produces: application/json

### Body Parameters
<a name="-greengrass-bulk-deployments-post-body"></a>

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

### Header Parameters
<a name="-greengrass-bulk-deployments-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### CLI
<a name="-greengrass-bulk-deployments-post-cli"></a>

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

### Responses
<a name="-greengrass-bulk-deployments-post-responses"></a>

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

## GET
<a name="-greengrass-bulk-deployments-get"></a>

 `GET /greengrass/bulk/deployments`

Operation ID: [ListBulkDeployments](listbulkdeployments-get.md)

Returns a list of bulk deployments.

Produces: application/json

### Query Parameters
<a name="-greengrass-bulk-deployments-get-query"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-bulk-deployments-get-cli"></a>

```
aws greengrass list-bulk-deployments \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"MaxResults": "integer",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-bulk-deployments-get-responses"></a>

**200**
Success. The response body contains the list of bulk deployments.
 [ ListBulkDeploymentsResponse](definitions-listbulkdeploymentsresponse.md)

```
{
"BulkDeployments": [
  {
    "BulkDeploymentId": "string",
    "BulkDeploymentArn": "string",
    "CreatedAt": "string"
  }
],
"NextToken": "string"
}
```
ListBulkDeploymentsResponse
type: object
BulkDeployments
type: array
items: [BulkDeployment](definitions-bulkdeployment.md)
BulkDeployment
Information about a bulk deployment. You cannot start a new bulk deployment while another one is still running or in a non-terminal state.
type: object
BulkDeploymentId
The ID of the bulk deployment.
type: string
BulkDeploymentArn
The ARN of the bulk deployment.
type: string
CreatedAt
The time, in ISO format, when the deployment was created.
type: string
NextToken
The token for the next set of results, or `null` if there are no more results.
in: query
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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

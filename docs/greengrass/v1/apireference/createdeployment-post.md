---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createdeployment-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateDeployment
<a name="createdeployment-post"></a>

Creates a deployment. `CreateDeployment` requests are idempotent with respect to the `X-Amzn-Client-Token` token and the request parameters.

URI: `POST /greengrass/groups/{{GroupId}}/deployments`

Produces: application/json

## CLI:
<a name="createdeployment-post-cli"></a>

```
aws greengrass create-deployment \
  --group-id <value> \
  [--deployment-type <value>] \
  [--deployment-id <value>] \
  [--group-version-id <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
"DeploymentId": "string",
"GroupVersionId": "string",
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createdeployment-post-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**CreateDeploymentRequestBody**](parameters-createdeploymentrequestbody.md)

where used: body; required: true

```
{
"DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
"DeploymentId": "string",
"GroupVersionId": "string"
}
```
schema:
CreateDeploymentRequest
Information about a deployment.
type: object
required: ["DeploymentType"]
DeploymentType
The type of deployment. When used for `CreateDeployment`, only `NewDeployment` and `Redeployment` are valid.
type: string
enum: ["NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"]
DeploymentId
The ID of the previous deployment you want to redeploy.
type: string
GroupVersionId
The ID of the group version to be deployed.
type: string

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="createdeployment-post-resp"></a>

**200**
Success. The group was deployed.
 [ CreateDeploymentResponse](definitions-createdeploymentresponse.md)

```
{
"DeploymentArn": "string",
"DeploymentId": "string"
}
```
CreateDeploymentResponse
type: object
DeploymentArn
The ARN of the deployment.
type: string
DeploymentId
The ID of the deployment.
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

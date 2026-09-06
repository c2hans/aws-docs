---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-groups-groupid-deployments.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/groups/GroupId/deployments
<a name="-greengrass-groups-groupid-deployments"></a>

## POST
<a name="-greengrass-groups-groupid-deployments-post"></a>

 `POST /greengrass/groups/{{GroupId}}/deployments`

Operation ID: [CreateDeployment](createdeployment-post.md)

Creates a deployment. `CreateDeployment` requests are idempotent with respect to the `X-Amzn-Client-Token` token and the request parameters.

Produces: application/json

### Body Parameters
<a name="-greengrass-groups-groupid-deployments-post-body"></a>

[**CreateDeploymentRequestBody**](parameters-createdeploymentrequestbody.md)

where used: body; required: true

```
{
"DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
"DeploymentId": "string",
"GroupVersionId": "string"
}
```
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

### Header Parameters
<a name="-greengrass-groups-groupid-deployments-post-header"></a>

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

### Path Parameters
<a name="-greengrass-groups-groupid-deployments-post-path"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-groups-groupid-deployments-post-cli"></a>

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

### Responses
<a name="-greengrass-groups-groupid-deployments-post-responses"></a>

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

## GET
<a name="-greengrass-groups-groupid-deployments-get"></a>

 `GET /greengrass/groups/{{GroupId}}/deployments`

Operation ID: [ListDeployments](listdeployments-get.md)

Returns a history of deployments for the group.

Produces: application/json

### Path Parameters
<a name="-greengrass-groups-groupid-deployments-get-path"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

### Query Parameters
<a name="-greengrass-groups-groupid-deployments-get-query"></a>

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

### CLI
<a name="-greengrass-groups-groupid-deployments-get-cli"></a>

```
aws greengrass list-deployments \
  --group-id <value> \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"MaxResults": "integer",
"NextToken": "string"
}
```

### Responses
<a name="-greengrass-groups-groupid-deployments-get-responses"></a>

**200**
Success. The response body contains the list of deployments for the given group.
 [ ListDeploymentsResponse](definitions-listdeploymentsresponse.md)

```
{
"Deployments": [
  {
    "GroupArn": "string",
    "DeploymentId": "string",
    "DeploymentArn": "string",
    "DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
    "CreatedAt": "string"
  }
],
"NextToken": "string"
}
```
ListDeploymentsResponse
type: object
Deployments
type: array
items: [Deployment](definitions-deployment.md)
Deployment
Information about a deployment.
type: object
GroupArn
The ARN of the group for this deployment.
type: string
DeploymentId
The ID of the deployment.
type: string
DeploymentArn
The ARN of the deployment.
type: string
DeploymentType
The type of deployment. When used for `CreateDeployment`, only `NewDeployment` and `Redeployment` are valid.
type: string
enum: ["NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"]
CreatedAt
The time, in milliseconds since the epoch, when the deployment was created.
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

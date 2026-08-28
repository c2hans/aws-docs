---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/getdeploymentstatus-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetDeploymentStatus
<a name="getdeploymentstatus-get"></a>

Returns the status of a deployment.

URI: `GET /greengrass/groups/{{GroupId}}/deployments/{{DeploymentId}}/status`

Produces: application/json

## CLI:
<a name="getdeploymentstatus-get-cli"></a>

```
aws greengrass get-deployment-status \
  --group-id <value> \
  --deployment-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"GroupId": "string",
"DeploymentId": "string"
}
```

## Parameters:
<a name="getdeploymentstatus-get-params"></a>

[**GroupId**](parameters-groupidparam.md)
The ID of the Greengrass group.
where used: path; required: true
type: string

[**DeploymentId**](parameters-deploymentidparam.md)
The ID of the deployment.
where used: path; required: true
type: string

## Responses:
<a name="getdeploymentstatus-get-resp"></a>

**200**
Success. The response body contains the status of the deployment for the group.
 [ GetDeploymentStatusResponse](definitions-getdeploymentstatusresponse.md)

```
{
"DeploymentStatus": "string",
"DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
"UpdatedAt": "string",
"ErrorMessage": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GetDeploymentStatusResponse
Information about the status of a deployment for a group.
type: object
DeploymentStatus
The status of the deployment: `Building`, `InProgress`, `Success`, or `Failure`.
type: string
DeploymentType
The type of deployment. When used for `CreateDeployment`, only `NewDeployment` and `Redeployment` are valid.
type: string
enum: ["NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"]
UpdatedAt
The time, in milliseconds since the epoch, when the deployment status was updated.
type: string
ErrorMessage
Error message
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

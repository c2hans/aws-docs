---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/listbulkdeploymentdetailedreports-get.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListBulkDeploymentDetailedReports
<a name="listbulkdeploymentdetailedreports-get"></a>

Gets a paginated list of the deployments that have been started in a bulk deployment operation, and their current deployment status.

URI: `GET /greengrass/bulk/deployments/{{BulkDeploymentId}}/detailed-reports`

Produces: application/json

## CLI:
<a name="listbulkdeploymentdetailedreports-get-cli"></a>

```
aws greengrass list-bulk-deployment-detailed-reports \
  --bulk-deployment-id <value> \
  [--max-results <value>] \
  [--next-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"BulkDeploymentId": "string",
"MaxResults": "integer",
"NextToken": "string"
}
```

## Parameters:
<a name="listbulkdeploymentdetailedreports-get-params"></a>

[**BulkDeploymentId**](parameters-bulkdeploymentidparam.md)
The ID of the bulk deployment.
where used: path; required: true
type: string

[**MaxResults**](parameters-maxresultsparam.md)
The maximum number of results to be returned per request.
where used: query; required: false
type: integer

[**NextToken**](parameters-nexttokenparam.md)
The token for the next set of results, or `null` if there are no more results.
where used: query; required: false
type: string

## Responses:
<a name="listbulkdeploymentdetailedreports-get-resp"></a>

**200**
Success. The response body contains the list of deployments for the given group.
 [ ListBulkDeploymentDetailedReportsResponse](definitions-listbulkdeploymentdetailedreportsresponse.md)

```
{
"Deployments": [
  {
    "DeploymentId": "string",
    "DeploymentArn": "string",
    "GroupArn": "string",
    "DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
    "CreatedAt": "string",
    "DeploymentStatus": "string",
    "ErrorMessage": "string",
    "ErrorDetails": [
      {
        "DetailedErrorCode": "string",
        "DetailedErrorMessage": "string"
      }
    ]
  }
],
"NextToken": "string"
}
```
ListBulkDeploymentDetailedReportsResponse
type: object
Deployments
type: array
items: [BulkDeploymentResult](definitions-bulkdeploymentresult.md)
BulkDeploymentResult
Information about an individual group deployment in a bulk deployment operation.
type: object
DeploymentId
The ID of the group deployment.
type: string
DeploymentArn
The ARN of the group deployment.
type: string
GroupArn
The ARN of the Greengrass group.
type: string
DeploymentType
The type of deployment. When used for `CreateDeployment`, only `NewDeployment` and `Redeployment` are valid.
type: string
enum: ["NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"]
CreatedAt
The time, in ISO format, when the deployment was created.
type: string
DeploymentStatus
The current status of the group deployment: ` `Building`, `InProgress `, `Success `, or `Failure``.
type: string
ErrorMessage
The error message for a failed deployment.
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

---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-bulk-deployments-bulkdeploymentid-status.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/bulk/deployments/BulkDeploymentId/status
<a name="-greengrass-bulk-deployments-bulkdeploymentid-status"></a>

## GET
<a name="-greengrass-bulk-deployments-bulkdeploymentid-status-get"></a>

 `GET /greengrass/bulk/deployments/{{BulkDeploymentId}}/status`

Operation ID: [GetBulkDeploymentStatus](getbulkdeploymentstatus-get.md)

Returns the status of a bulk deployment.

Produces: application/json

### Path Parameters
<a name="-greengrass-bulk-deployments-bulkdeploymentid-status-get-path"></a>

[**BulkDeploymentId**](parameters-bulkdeploymentidparam.md)
The ID of the bulk deployment.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-bulk-deployments-bulkdeploymentid-status-get-cli"></a>

```
aws greengrass get-bulk-deployment-status \
  --bulk-deployment-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"BulkDeploymentId": "string"
}
```

### Responses
<a name="-greengrass-bulk-deployments-bulkdeploymentid-status-get-responses"></a>

**200**
Success. The response body contains the status of the bulk deployment.
 [ GetBulkDeploymentStatusResponse](definitions-getbulkdeploymentstatusresponse.md)

```
{
"BulkDeploymentStatus": "Initializing|Running|Completed|Stopping|Stopped|Failed",
"BulkDeploymentMetrics": {
  "RecordsProcessed": 0,
  "InvalidInputRecords": 0,
  "RetryAttempts": 0
},
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
},
"CreatedAt": "string",
"ErrorMessage": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GetBulkDeploymentStatusResponse
Information about the status of a bulk deployment at the time of the request.
type: object
BulkDeploymentStatus
The current status of the bulk deployment.
type: string
enum: ["Initializing", "Running", "Completed", "Stopping", "Stopped", "Failed"]
BulkDeploymentMetrics
Relevant metrics on input records processed during bulk deployment.
type: object
RecordsProcessed
The total number of group records from the input file that have been processed or attempted so far.
type: integer
InvalidInputRecords
The total number of records that returned a non-retryable error. For example, this can occur if a group record from the input file uses an invalid format or specifies a nonexistent group version, or if the execution role doesn't grant permission to deploy a group or group version.
type: integer
RetryAttempts
The total number of deployment attempts that returned a retryable error. For example, a retry is triggered if the attempt to deploy a group returns a throttling error. `StartBulkDeployment` retries a group deployment up to five times.
type: integer
tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string
CreatedAt
The time, in ISO format, when the deployment was created.
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

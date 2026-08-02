---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-bulkdeploymentresults.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# BulkDeploymentResults
<a name="definitions-bulkdeploymentresults"></a>

```
[
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
]
```

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
The current status of the group deployment: `Building`, `InProgress`, `Success`, or `Failure`.
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

---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-getdeploymentstatusresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# GetDeploymentStatusResponse
<a name="definitions-getdeploymentstatusresponse"></a>

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

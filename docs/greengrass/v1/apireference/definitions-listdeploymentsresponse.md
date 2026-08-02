---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-listdeploymentsresponse.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ListDeploymentsResponse
<a name="definitions-listdeploymentsresponse"></a>

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

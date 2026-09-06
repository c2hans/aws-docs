---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createdeploymentrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateDeploymentRequestBody
<a name="parameters-createdeploymentrequestbody"></a>

```
{
"DeploymentType": "NewDeployment|Redeployment|ResetDeployment|ForceResetDeployment",
"DeploymentId": "string",
"GroupVersionId": "string"
}
```

CreateDeploymentRequestBody
in: body
required: true
schema: [CreateDeploymentRequest](definitions-createdeploymentrequest.md)

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

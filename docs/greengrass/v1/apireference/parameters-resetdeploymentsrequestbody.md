---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-resetdeploymentsrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# ResetDeploymentsRequestBody
<a name="parameters-resetdeploymentsrequestbody"></a>

```
{
"Force": true
}
```

ResetDeploymentsRequestBody
Information required to reset deployments.
in: body
required: true
schema: [ResetDeploymentsRequest](definitions-resetdeploymentsrequest.md)

ResetDeploymentsRequest
Information about a group reset request.
type: object

Force
If true, performs a best-effort only core reset.
type: boolean

---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-associateserviceroletoaccountrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# AssociateServiceRoleToAccountRequestBody
<a name="parameters-associateserviceroletoaccountrequestbody"></a>

```
{
"RoleArn": "string"
}
```

AssociateServiceRoleToAccountRequestBody
in: body
required: true
schema: [AssociateServiceRoleToAccountRequest](definitions-associateserviceroletoaccountrequest.md)

AssociateServiceRoleToAccountRequest
type: object
required: ["RoleArn"]

RoleArn
The ARN of the service role to associate with your account.
type: string

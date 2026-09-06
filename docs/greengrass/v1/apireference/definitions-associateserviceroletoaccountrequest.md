---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-associateserviceroletoaccountrequest.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# AssociateServiceRoleToAccountRequest
<a name="definitions-associateserviceroletoaccountrequest"></a>

```
{
"RoleArn": "string"
}
```

AssociateServiceRoleToAccountRequest
type: object
required: ["RoleArn"]

RoleArn
The ARN of the service role to associate with your account.
type: string

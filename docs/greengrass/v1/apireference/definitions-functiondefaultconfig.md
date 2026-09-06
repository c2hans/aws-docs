---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-functiondefaultconfig.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# FunctionDefaultConfig
<a name="definitions-functiondefaultconfig"></a>

```
{
"Execution": {
  "IsolationMode": "GreengrassContainer|NoContainer",
  "RunAs": {
    "Uid": 1001,
    "Gid": 1002
  }
}
}
```

FunctionDefaultConfig
The default configuration that applies to all Lambda functions in the group. Individual Lambda functions can override these settings.
type: object

Execution
Configuration information that specifies how a Lambda function runs.

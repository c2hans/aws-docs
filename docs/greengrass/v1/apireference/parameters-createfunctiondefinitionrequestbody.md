---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createfunctiondefinitionrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateFunctionDefinitionRequestBody
<a name="parameters-createfunctiondefinitionrequestbody"></a>

```
{
"Name": "string",
"InitialVersion": {
  "DefaultConfig": {
    "Execution": {
      "IsolationMode": "GreengrassContainer|NoContainer",
      "RunAs": {
        "Uid": 1001,
        "Gid": 1002
      }
    }
  },
  "Functions": [
    {
      "Id": "string",
      "FunctionArn": "string",
      "FunctionConfiguration": {
        "Pinned": true,
        "Executable": "string",
        "ExecArgs": "string",
        "MemorySize": 0,
        "Timeout": 0,
        "EncodingType": "binary|json",
        "Environment": {
          "Variables": {
            "additionalProperty0": "string",
            "additionalProperty1": "string",
            "additionalProperty2": "string"
          },
          "ResourceAccessPolicies": [
            {
              "ResourceId": "string",
              "Permission": "ro|rw"
            }
          ],
          "AccessSysfs": true,
          "Execution": {
            "IsolationMode": "GreengrassContainer|NoContainer",
            "RunAs": {
              "Uid": 1001,
              "Gid": 1002
            }
          }
        },
        "FunctionRuntimeOverride": "string"
      }
    }
  ]
},
"tags": {
  "additionalProperty0": "string",
  "additionalProperty1": "string",
  "additionalProperty2": "string"
}
}
```

CreateFunctionDefinitionRequestBody
in: body
required: true

properties
Name: The name of the function definition. Type: string
InitialVersion: Information about the initial version of the function definition. Type: FunctionDefinitionVersion
tags: The tags to attach to the new resource. Type: tags

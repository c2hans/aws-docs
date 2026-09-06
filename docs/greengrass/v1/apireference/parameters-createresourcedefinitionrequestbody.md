---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/parameters-createresourcedefinitionrequestbody.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateResourceDefinitionRequestBody
<a name="parameters-createresourcedefinitionrequestbody"></a>

```
{
"Name": "string",
"InitialVersion": {
  "Resources": [
    {
      "Id": "string",
      "Name": "string",
      "ResourceDataContainer": {
        "*-- NOTE:": "choose one of the following --*",
        "LocalDeviceResourceData": {
          "SourcePath": "string",
          "GroupOwnerSetting": {
            "AutoAddGroupOwner": true,
            "GroupOwner": "string"
          }
        },
        "LocalVolumeResourceData": {
          "SourcePath": "string",
          "DestinationPath": "string",
          "GroupOwnerSetting": {
            "AutoAddGroupOwner": true,
            "GroupOwner": "string"
          }
        },
        "SageMakerMachineLearningModelResourceData": {
          "SageMakerJobArn": "string",
          "DestinationPath": "string",
          "OwnerSetting": {
            "GroupOwner": "string",
            "GroupPermission": "ro|rw"
          }
        },
        "S3MachineLearningModelResourceData": {
          "S3Uri": "string",
          "DestinationPath": "string",
          "OwnerSetting": {
            "GroupOwner": "string",
            "GroupPermission": "ro|rw"
          }
        },
        "SecretsManagerSecretResourceData": {
          "ARN": "string",
          "AdditionalStagingLabelsToDownload": [
            "string"
          ]
        }
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

CreateResourceDefinitionRequestBody
in: body
required: true

properties
Name: The name of the resource definition. Type: string
InitialVersion: Information about the initial version of the resource definition. Type: ResourceDefinitionVersion
tags: The tags to attach to the new resource. Type: tags

---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# /greengrass/definition/resources/ResourceDefinitionId/versions/ResourceDefinitionVersionId
<a name="-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid"></a>

## GET
<a name="-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid-get"></a>

 `GET /greengrass/definition/resources/{{ResourceDefinitionId}}/versions/{{ResourceDefinitionVersionId}}`

Operation ID: [GetResourceDefinitionVersion](getresourcedefinitionversion-get.md)

Retrieves information about a resource definition version, including which resources are included in the version.

Produces: application/json

### Path Parameters
<a name="-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid-get-path"></a>

[**ResourceDefinitionId**](parameters-resourcedefinitionidparam.md)
The ID of the resource definition.
where used: path; required: true
type: string

[**ResourceDefinitionVersionId**](parameters-resourcedefinitionversionidparam.md)
The ID of the resource definition version. This value maps to the `Version` property of the corresponding `VersionInformation` object, which is returned by `ListResourceDefinitionVersions` requests. If the version is the last one that was associated with a resource definition, the value also maps to the `LatestVersion` property of the corresponding `DefinitionInformation` object.
where used: path; required: true
type: string

### CLI
<a name="-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid-get-cli"></a>

```
aws greengrass get-resource-definition-version \
  --resource-definition-id <value> \
  --resource-definition-version-id <value>  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

```
{
"ResourceDefinitionId": "string",
"ResourceDefinitionVersionId": "string"
}
```

### Responses
<a name="-greengrass-definition-resources-resourcedefinitionid-versions-resourcedefinitionversionid-get-responses"></a>

**200**
Success.
 [ GetResourceDefinitionVersionResponse](definitions-getresourcedefinitionversionresponse.md)

```
{
"Arn": "string",
"Id": "string",
"Version": "string",
"CreationTimestamp": "string",
"Definition": {
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
}
}
```
GetResourceDefinitionVersionResponse
Information about a resource definition version.
type: object
Arn
The ARN of the resource definition version.
type: string
Id
The ID of the resource definition version.
type: string
Version
The version of the resource definition version.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the resource definition version was created.
type: string
Definition
Information about a resource definition version.
type: object
Resources
A list of resources.
type: array
items: [Resource](definitions-resource.md)
Resource
Information about a resource.
type: object
required: ["Id", "Name", "ResourceDataContainer"]
Id
The resource ID, used to refer to a resource in the Lambda function configuration. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`. This must be unique within a Greengrass group.
type: string
Name
The descriptive resource name, which is displayed on the AWS IoT Greengrass console. Maximum length is 128 characters with the pattern `[a‑zA‑Z0‑9:_‑]+`. This must be unique within a Greengrass group.
type: string
ResourceDataContainer
A container for resource data. The container takes only one of the following supported resource data types: `LocalDeviceResourceData`, `LocalVolumeResourceData`, `SageMakerMachineLearningModelResourceData`, `S3MachineLearningModelResourceData`, `SecretsManagerSecretResourceData`.
type: object
NOTE: oneOf
LocalDeviceResourceData
Attributes that define a local device resource.
type: object
SourcePath
The local absolute path of the device resource. The source path for a device resource can refer only to a character device or block device under `/dev`.
type: string
GroupOwnerSetting
Group owner related settings for local resources.
type: object
AutoAddGroupOwner
If true, AWS IoT Greengrass adds the specified Linux OS group owner of the resource to the Lambda process privileges. The Lambda process then has the file access permissions of the added Linux group.
type: boolean
GroupOwner
The name of the Linux OS group whose privileges are added to the Lambda process. This field is optional.
type: string
LocalVolumeResourceData
Attributes that define a local volume resource.
type: object
SourcePath
The local absolute path of the volume resource on the host. The source path for a volume resource type cannot start with `/sys`.
type: string
DestinationPath
The absolute local path of the resource inside the Lambda environment.
type: string
GroupOwnerSetting
Group owner related settings for local resources.
type: object
AutoAddGroupOwner
If true, AWS IoT Greengrass adds the specified Linux OS group owner of the resource to the Lambda process privileges. The Lambda process then has the file access permissions of the added Linux group.
type: boolean
GroupOwner
The name of the Linux OS group whose privileges are added to the Lambda process. This field is optional.
type: string
SageMakerMachineLearningModelResourceData
Attributes that define an Amazon SageMaker machine learning resource.
type: object
SageMakerJobArn
The ARN of the Amazon SageMaker training job that represents the source model.
type: string
DestinationPath
The absolute local path of the resource inside the Lambda environment.
type: string
OwnerSetting
The owner setting for the downloaded machine learning resource.
type: object
required: ["GroupOwner", "GroupPermission"]
GroupOwner
The group owner of the resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
type: string
GroupPermission
The permissions that the group owner has to the resource. Valid values are `rw` (read-write) or `ro` (read-only).
type: string
enum: ["ro", "rw"]
S3MachineLearningModelResourceData
Attributes that define an Amazon S3 machine learning resource.
type: object
S3Uri
The URI of the source model in an S3 bucket. The model package must be in tar.gz or .zip format.
type: string
DestinationPath
The absolute local path of the resource inside the Lambda environment.
type: string
OwnerSetting
The owner setting for the downloaded machine learning resource.
type: object
required: ["GroupOwner", "GroupPermission"]
GroupOwner
The group owner of the resource. This is the group ID (GID) of an existing Linux OS group on the system. The group's permissions are added to the Lambda process.
type: string
GroupPermission
The permissions that the group owner has to the resource. Valid values are `rw` (read-write) or `ro` (read-only).
type: string
enum: ["ro", "rw"]
SecretsManagerSecretResourceData
Attributes that define a secret resource, which references a secret from AWS Secrets Manager. AWS IoT Greengrass stores a local, encrypted copy of the secret on the Greengrass core, where it can be securely accessed by connectors and Lambda functions.
type: object
ARN
The ARN of the Secrets Manager secret to make available on the core. The value of the secret's latest version (represented by the `AWSCURRENT` staging label) is included by default.
type: string
AdditionalStagingLabelsToDownload
Optional. The staging labels in addition to `AWSCURRENT` whose values you want to make available on the core.
type: array

**400**
Invalid request.
 [ GeneralError](definitions-generalerror.md)

```
{
"Message": "string",
"ErrorDetails": [
  {
    "DetailedErrorCode": "string",
    "DetailedErrorMessage": "string"
  }
]
}
```
GeneralError
General error information.
type: object
required: ["Message"]
Message
A message that contains information about the error.
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

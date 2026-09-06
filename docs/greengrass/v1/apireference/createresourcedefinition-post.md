---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/createresourcedefinition-post.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# CreateResourceDefinition
<a name="createresourcedefinition-post"></a>

Creates a resource definition that contains a list of resources to be used in a group. You can create an initial version of the definition by providing a list of resources now, or use `CreateResourceDefinitionVersion` later.

URI: `POST /greengrass/definition/resources`

Produces: application/json

## CLI:
<a name="createresourcedefinition-post-cli"></a>

```
aws greengrass create-resource-definition \
  [--name <value>] \
  [--initial-version <value>] \
  [--tags <value>] \
  [--amzn-client-token <value>]  \
  [--cli-input-json <value>] \
  [--generate-cli-skeleton]
```

cli-input-json format:

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
            "AutoAddGroupOwner": "boolean",
            "GroupOwner": "string"
          }
        },
        "LocalVolumeResourceData": {
          "SourcePath": "string",
          "DestinationPath": "string",
          "GroupOwnerSetting": {
            "AutoAddGroupOwner": "boolean",
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
},
"AmznClientToken": "string"
}
```

## Parameters:
<a name="createresourcedefinition-post-params"></a>

[**CreateResourceDefinitionRequestBody**](parameters-createresourcedefinitionrequestbody.md)

where used: body; required: true

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
schema:
Name
The name of the resource definition.
type: string
InitialVersion
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

tags
The resource tags.
type: object
additionalProperties: The key-value pair for the resource tag. Type: string

[**X-Amzn-Client-Token**](parameters-clienttoken.md)
A client token used to correlate requests and responses.
where used: header; required: false
type: string

## Responses:
<a name="createresourcedefinition-post-resp"></a>

**200** (CreateResourceDefinitionResponse)

 [ DefinitionInformation](definitions-definitioninformation.md)

```
{
"Name": "string",
"Id": "string",
"Arn": "string",
"LastUpdatedTimestamp": "string",
"CreationTimestamp": "string",
"LatestVersion": "string",
"LatestVersionArn": "string"
}
```
DefinitionInformation
Information about a definition.
type: object
Name
The name of the definition.
type: string
Id
The ID of the definition.
type: string
Arn
The ARN of the definition.
type: string
LastUpdatedTimestamp
The time, in milliseconds since the epoch, when the definition was last updated.
type: string
CreationTimestamp
The time, in milliseconds since the epoch, when the definition was created.
type: string
LatestVersion
The ID of the latest version associated with the definition.
type: string
LatestVersionArn
The ARN of the latest version associated with the definition.
type: string

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

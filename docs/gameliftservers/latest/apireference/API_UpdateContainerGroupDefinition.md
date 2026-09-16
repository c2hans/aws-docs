---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateContainerGroupDefinition.html
---

# UpdateContainerGroupDefinition
<a name="API_UpdateContainerGroupDefinition"></a>

 **This API works with the following fleet types:** Container

Updates properties in an existing container group definition. This operation doesn't replace the definition. Instead, it creates a new version of the definition and saves it separately. You can access all versions that you choose to retain.

The only property you can't update is the container group type.

 **Request options:**
+ Update based on the latest version of the container group definition. Specify the container group definition name only, or use an ARN value without a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the latest version.
+ Update based on a specific version of the container group definition. Specify the container group definition name and a source version number, or use an ARN value with a version number. Provide updated values for the properties that you want to change only. All other values remain the same as the source version.
+ Change a game server container definition. Provide a complete set of container definitions, including the updated definition.
+ Add or change a support container definition. Provide a complete set of container definitions, including the updated definition.
+ Remove a support container definition. Provide a complete set of container definitions, excluding the definition to remove. If the container group has only one support container definition, provide an empty set.

 **Results:**

If successful, this operation returns the complete properties of the new container group definition version.

If the container group definition version is used in an active fleets, the update automatically initiates a new fleet deployment of the new version. You can track a fleet's deployments using [ListFleetDeployments](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListFleetDeployments.html).

## Request Syntax
<a name="API_UpdateContainerGroupDefinition_RequestSyntax"></a>

```
{
   "GameServerContainerDefinition": {
      "ContainerName": "{{string}}",
      "DependsOn": [
         {
            "Condition": "{{string}}",
            "ContainerName": "{{string}}"
         }
      ],
      "EnvironmentOverride": [
         {
            "Name": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ImageUri": "{{string}}",
      "LinuxCapabilities": {
         "Include": [ "{{string}}" ]
      },
      "MountPoints": [
         {
            "AccessLevel": "{{string}}",
            "ContainerPath": "{{string}}",
            "InstancePath": "{{string}}"
         }
      ],
      "PortConfiguration": {
         "ContainerPortRanges": [
            {
               "FromPort": {{number}},
               "Protocol": "{{string}}",
               "ToPort": {{number}}
            }
         ]
      },
      "ServerSdkVersion": "{{string}}"
   },
   "Name": "{{string}}",
   "OperatingSystem": "{{string}}",
   "SourceVersionNumber": {{number}},
   "SupportContainerDefinitions": [
      {
         "ContainerName": "{{string}}",
         "DependsOn": [
            {
               "Condition": "{{string}}",
               "ContainerName": "{{string}}"
            }
         ],
         "EnvironmentOverride": [
            {
               "Name": "{{string}}",
               "Value": "{{string}}"
            }
         ],
         "Essential": {{boolean}},
         "HealthCheck": {
            "Command": [ "{{string}}" ],
            "Interval": {{number}},
            "Retries": {{number}},
            "StartPeriod": {{number}},
            "Timeout": {{number}}
         },
         "ImageUri": "{{string}}",
         "LinuxCapabilities": {
            "Include": [ "{{string}}" ]
         },
         "MemoryHardLimitMebibytes": {{number}},
         "MountPoints": [
            {
               "AccessLevel": "{{string}}",
               "ContainerPath": "{{string}}",
               "InstancePath": "{{string}}"
            }
         ],
         "PortConfiguration": {
            "ContainerPortRanges": [
               {
                  "FromPort": {{number}},
                  "Protocol": "{{string}}",
                  "ToPort": {{number}}
               }
            ]
         },
         "Vcpu": {{number}}
      }
   ],
   "TotalMemoryLimitMebibytes": {{number}},
   "TotalVcpuLimit": {{number}},
   "VersionDescription": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateContainerGroupDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-Name"></a>
A descriptive identifier for the container group definition. The name value must be unique in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: Yes

 ** [GameServerContainerDefinition](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-GameServerContainerDefinition"></a>
An updated definition for the game server container in this group. Define a game server container only when the container group type is `GAME_SERVER`. You can pass in your container definitions as a JSON file.
Type: [GameServerContainerDefinitionInput](API_GameServerContainerDefinitionInput.md) object
Required: No

 ** [OperatingSystem](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-OperatingSystem"></a>
The platform that all containers in the group use. Containers in a group must run on the same operating system.
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `AMAZON_LINUX_2023`
Required: No

 ** [SourceVersionNumber](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-SourceVersionNumber"></a>
The container group definition version to update. The new version starts with values from the source version, and then updates values included in this request.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [SupportContainerDefinitions](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-SupportContainerDefinitions"></a>
One or more definitions for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.
Type: Array of [SupportContainerDefinitionInput](API_SupportContainerDefinitionInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [TotalMemoryLimitMebibytes](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-TotalMemoryLimitMebibytes"></a>
The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024000.
Required: No

 ** [TotalVcpuLimit](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-TotalVcpuLimit"></a>
The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share this memory. If you specify vCPU limits for individual containers, the total value must be equal to or greater than the sum of the CPU limits for all containers in the group.
Type: Double
Valid Range: Minimum value of 0.125. Maximum value of 10.
Required: No

 ** [VersionDescription](#API_UpdateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-request-VersionDescription"></a>
A description for this update to the container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_UpdateContainerGroupDefinition_ResponseSyntax"></a>

```
{
   "ContainerGroupDefinition": {
      "ContainerGroupDefinitionArn": "string",
      "ContainerGroupType": "string",
      "CreationTime": number,
      "GameServerContainerDefinition": {
         "ContainerName": "string",
         "DependsOn": [
            {
               "Condition": "string",
               "ContainerName": "string"
            }
         ],
         "EnvironmentOverride": [
            {
               "Name": "string",
               "Value": "string"
            }
         ],
         "ImageUri": "string",
         "LinuxCapabilities": {
            "Include": [ "string" ]
         },
         "MountPoints": [
            {
               "AccessLevel": "string",
               "ContainerPath": "string",
               "InstancePath": "string"
            }
         ],
         "PortConfiguration": {
            "ContainerPortRanges": [
               {
                  "FromPort": number,
                  "Protocol": "string",
                  "ToPort": number
               }
            ]
         },
         "ResolvedImageDigest": "string",
         "ServerSdkVersion": "string"
      },
      "Name": "string",
      "OperatingSystem": "string",
      "Status": "string",
      "StatusReason": "string",
      "SupportContainerDefinitions": [
         {
            "ContainerName": "string",
            "DependsOn": [
               {
                  "Condition": "string",
                  "ContainerName": "string"
               }
            ],
            "EnvironmentOverride": [
               {
                  "Name": "string",
                  "Value": "string"
               }
            ],
            "Essential": boolean,
            "HealthCheck": {
               "Command": [ "string" ],
               "Interval": number,
               "Retries": number,
               "StartPeriod": number,
               "Timeout": number
            },
            "ImageUri": "string",
            "LinuxCapabilities": {
               "Include": [ "string" ]
            },
            "MemoryHardLimitMebibytes": number,
            "MountPoints": [
               {
                  "AccessLevel": "string",
                  "ContainerPath": "string",
                  "InstancePath": "string"
               }
            ],
            "PortConfiguration": {
               "ContainerPortRanges": [
                  {
                     "FromPort": number,
                     "Protocol": "string",
                     "ToPort": number
                  }
               ]
            },
            "ResolvedImageDigest": "string",
            "Vcpu": number
         }
      ],
      "TotalMemoryLimitMebibytes": number,
      "TotalVcpuLimit": number,
      "VersionDescription": "string",
      "VersionNumber": number
   }
}
```

## Response Elements
<a name="API_UpdateContainerGroupDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerGroupDefinition](#API_UpdateContainerGroupDefinition_ResponseSyntax) **   <a name="gameliftservers-UpdateContainerGroupDefinition-response-ContainerGroupDefinition"></a>
The properties of the updated container group definition version.
Type: [ContainerGroupDefinition](API_ContainerGroupDefinition.md) object

## Errors
<a name="API_UpdateContainerGroupDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** NotFoundException **
The requested resource was not found. The resource was either not created yet or deleted.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_UpdateContainerGroupDefinition_Examples"></a>

### Update a game server container group definition for a new support container
<a name="API_UpdateContainerGroupDefinition_Example_1"></a>

This example adds a new support container definition to a game server container group that previously had one game server container defined. The request has these characteristics:
+ A source version isn't provided, and the container group Name parameter is an ARN without a version number. As a result, this update will use the latest version as the source.
+ The request changes the total memory limit for the container group.
+ The new support container definition supplies the minimum required parameters.

As shown, an update request includes only the properties that you want to change or add.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateContainerGroupDefinition_Example_1_Request"></a>

```
{
  "Name": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup",
  "TotalMemoryLimitMebibytes": 2048,
  "SupportContainerDefinitions": [
    {
      "ContainerName": "MyAdventureGameDependencies",
      "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameDependenciesContainerImage"
    }
  ],
  "VersionDescription": "New support container for game server dependencies and groups total memory limit increased to 2048"
}
```

#### Sample Response
<a name="API_UpdateContainerGroupDefinition_Example_1_Response"></a>

```
{
  "ContainerGroupDefinition": {
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:4",
    "ContainerGroupType": "GAME_SERVER",
    "CreationTime": 1496365885.44,
    "GameServerContainerDefinition": [
      {
        "ContainerName": "MyAdventureGameServer",
        "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage",
        "PortConfiguration": {
          "ContainerPortRanges": [
            {
              "FromPort": 35000,
              "Protocol": "TCP",
              "ToPort": 40000
            }
          ]
        },
        "LinuxCapabilities": {
          "Include": ["NET_BIND_SERVICE", "SYS_PTRACE"]
        },
        "ResolvedImageDigest": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "ServerSdkVersion": "5.2.0"
      }
    ],
    "Name": "MyAdventureGameContainerGroup",
    "OperatingSystem": "AMAZON_LINUX_2023",
    "Status": "COPYING",
    "SupportContainerDefinitions": [
      {
      "ContainerName": "MyAdventureGameDependencies",
      "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameDependenciesContainerImage"
      "ResolvedImageDigest": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789fedcba",
      }
    ],
    "TotalMemoryLimitMebibytes": 2048,
    "TotalVcpuLimit": 1,
    "VersionDescription": "New support container for game server dependencies and groups total memory limit increased to 2048",
    "VersionNumber": 4
  }
}
```

## See Also
<a name="API_UpdateContainerGroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateContainerGroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateContainerGroupDefinition)

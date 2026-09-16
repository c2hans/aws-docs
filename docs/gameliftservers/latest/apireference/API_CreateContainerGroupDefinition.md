---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_CreateContainerGroupDefinition.html
---

# CreateContainerGroupDefinition
<a name="API_CreateContainerGroupDefinition"></a>

 **This API works with the following fleet types:** Container

Creates a `ContainerGroupDefinition` that describes a set of containers for hosting your game server with Amazon GameLift Servers managed containers hosting. An Amazon GameLift Servers container group is similar to a container task or pod. Use container group definitions when you create a container fleet with [CreateContainerFleet](https://docs.aws.amazon.com/gamelift/latest/apireference/API_CreateContainerFleet.html).

A container group definition determines how Amazon GameLift Servers deploys your containers to each instance in a container fleet. You can maintain multiple versions of a container group definition.

There are two types of container groups:
+ A **game server container group** has the containers that run your game server application and supporting software. A game server container group can have these container types:
  + Game server container. This container runs your game server. You can define one game server container in a game server container group.
  + Support container. This container runs software in parallel with your game server. You can define up to 8 support containers in a game server group.

  When building a game server container group definition, you can choose to bundle your game server executable and all dependent software into a single game server container. Alternatively, you can separate the software into one game server container and one or more support containers.

  On a container fleet instance, a game server container group can be deployed multiple times (depending on the compute resources of the instance). This means that all containers in the container group are replicated together.
+ A **per-instance container group** has containers for processes that aren't replicated on a container fleet instance. This might include background services, logging, test processes, or processes that need to persist independently of the game server container group. When building a per-instance container group, you can define up to 10 support containers.

**Note**
This operation requires AWS Identity and Access Management (IAM) permissions to access container images in Amazon ECR repositories. See [ IAM permissions for Amazon GameLift Servers](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-iam-policy-examples.html) for help setting the appropriate permissions.

 **Request options**

Use this operation to make the following types of requests. You can specify values for the minimum required parameters and customize optional values later.
+ Create a game server container group definition. Provide the following required parameter values:
  +  `Name`
  +  `ContainerGroupType` (`GAME_SERVER`)
  +  `OperatingSystem`
  +  `TotalMemoryLimitMebibytes`
  +  `TotalVcpuLimit`
  + At least one `GameServerContainerDefinition`
    +  `ContainerName`
    +  `ImageUrl`
    +  `PortConfiguration`
    +  `ServerSdkVersion`
+ Create a per-instance container group definition. Provide the following required parameter values:
  +  `Name`
  +  `ContainerGroupType` (`PER_INSTANCE`)
  +  `OperatingSystem`
  +  `TotalMemoryLimitMebibytes`
  +  `TotalVcpuLimit`
  + At least one `SupportContainerDefinition`
    +  `ContainerName`
    +  `ImageUrl`

 **Results**

If successful, this request creates a `ContainerGroupDefinition` resource and assigns a unique ARN value. You can update most properties of a container group definition by calling [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html), and optionally save the update as a new version.

## Request Syntax
<a name="API_CreateContainerGroupDefinition_RequestSyntax"></a>

```
{
   "ContainerGroupType": "{{string}}",
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
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TotalMemoryLimitMebibytes": {{number}},
   "TotalVcpuLimit": {{number}},
   "VersionDescription": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateContainerGroupDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-Name"></a>
A descriptive identifier for the container group definition. The name value must be unique in an AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: Yes

 ** [OperatingSystem](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-OperatingSystem"></a>
The platform that all containers in the group use. Containers in a group must run on the same operating system.
Default value: `AMAZON_LINUX_2023`
Amazon Linux 2 (AL2) will reach end of support on 6/30/2026. See more details in the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/). For game servers that are hosted on AL2 and use server SDK version 4.x for Amazon GameLift Servers, first update the game server build to server SDK 5.x, and then deploy to AL2023 instances. See [ Migrate to server SDK version 5.](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk5-migration.html)
Type: String
Valid Values: `AMAZON_LINUX_2023`
Required: Yes

 ** [TotalMemoryLimitMebibytes](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-TotalMemoryLimitMebibytes"></a>
The maximum amount of memory (in MiB) to allocate to the container group. All containers in the group share this memory. If you specify memory limits for an individual container, the total value must be greater than any individual container's memory limit.
Default value: 1024
Type: Integer
Valid Range: Minimum value of 4. Maximum value of 1024000.
Required: Yes

 ** [TotalVcpuLimit](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-TotalVcpuLimit"></a>
The maximum amount of vCPU units to allocate to the container group (1 vCPU is equal to 1024 CPU units). All containers in the group share this memory. If you specify vCPU limits for individual containers, the total value must be equal to or greater than the sum of the CPU limits for all containers in the group.
Default value: 1
Type: Double
Valid Range: Minimum value of 0.125. Maximum value of 10.
Required: Yes

 ** [ContainerGroupType](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-ContainerGroupType"></a>
The type of container group being defined. Container group type determines how Amazon GameLift Servers deploys the container group on each fleet instance.
Default value: `GAME_SERVER`
Type: String
Valid Values: `GAME_SERVER | PER_INSTANCE`
Required: No

 ** [GameServerContainerDefinition](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-GameServerContainerDefinition"></a>
The definition for the game server container in this group. Define a game server container only when the container group type is `GAME_SERVER`. Game server containers specify a container image with your game server build. You can pass in your container definitions as a JSON file.
Type: [GameServerContainerDefinitionInput](API_GameServerContainerDefinitionInput.md) object
Required: No

 ** [SupportContainerDefinitions](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-SupportContainerDefinitions"></a>
One or more definition for support containers in this group. You can define a support container in any type of container group. You can pass in your container definitions as a JSON file.
Type: Array of [SupportContainerDefinitionInput](API_SupportContainerDefinitionInput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [Tags](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-Tags"></a>
A list of labels to assign to the container group definition resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [VersionDescription](#API_CreateContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-request-VersionDescription"></a>
A description for the initial version of this container group definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_CreateContainerGroupDefinition_ResponseSyntax"></a>

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
<a name="API_CreateContainerGroupDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerGroupDefinition](#API_CreateContainerGroupDefinition_ResponseSyntax) **   <a name="gameliftservers-CreateContainerGroupDefinition-response-ContainerGroupDefinition"></a>
The properties of the new container group definition resource. You can use this resource to create a container fleet.
Type: [ContainerGroupDefinition](API_ContainerGroupDefinition.md) object

## Errors
<a name="API_CreateContainerGroupDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** LimitExceededException **
The requested operation would cause the resource to exceed the allowed service limit. Resolve the issue before retrying.
HTTP Status Code: 400

 ** TaggingFailedException **
The requested tagging operation did not succeed. This may be due to invalid tag format or the maximum tag limit may have been exceeded. Resolve the issue before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_CreateContainerGroupDefinition_Examples"></a>

### Create a simple game server container group definition
<a name="API_CreateContainerGroupDefinition_Example_1"></a>

This example creates a game server container group definition with a game server container definition. The request includes the minimal parameter settings and uses the default values for all other parameters. The container definition has these characteristics:
+ It defines a container port range, which is required for containers that run game server processes.
+ The image URI points to an ECR private repo.
+ It doesn't need a health check configuration. Amazon GameLift Servers handles the health checks for a game server container.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateContainerGroupDefinition_Example_1_Request"></a>

```
{
  "Name": "MyAdventureGameContainerGroup",
  "ContainerGroupType": "GAME_SERVER",
  "GameServerContainerDefinition": [
    {
      "ContainerName": "MyAdventureGameServer",
      "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage",
      "ServerSdkVersion": 5.2.0,
      "PortConfiguration": {
        "ContainerPortRanges": [
          {
            "FromPort": 35000,
            "Protocol": "UDP",
            "ToPort": 40000
          }
        ]
      }
    }
  ]
}
```

#### Sample Response
<a name="API_CreateContainerGroupDefinition_Example_1_Response"></a>

```
{
  "ContainerGroupDefinition": {
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:1",
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
        "ResolvedImageDigest": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "ServerSdkVersion": "5.2.0"
      }
    ],
    "Name": "MyAdventureGameContainerGroup",
    "OperatingSystem": "AMAZON_LINUX_2023",
    "Status": "COPYING",
    "TotalMemoryLimitMebibytes": 1024,
    "TotalVcpuLimit": 1,
    "VersionNumber": "1"
  }
}
```

### Create a game server container with support containers
<a name="API_CreateContainerGroupDefinition_Example_2"></a>

This example creates a game server container group definition with a game server container definition and one support container The request includes the minimal parameter settings and uses the default values for all other parameters.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_CreateContainerGroupDefinition_Example_2_Request"></a>

```
{
  "Name": "MyAdventureGameContainerGroup",
  "ContainerGroupType": "GAME_SERVER",
  "GameServerContainerDefinition": [
    {
      "ContainerName": "MyAdventureGameServer",
      "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage",
      "ServerSdkVersion": 5.2.0,
      "PortConfiguration": {
        "ContainerPortRanges": [
          {
            "FromPort": 35000,
            "Protocol": "UDP",
            "ToPort": 40000
          }
        ]
      }
    }
  ],
  "SupportContainerDefinitions": [
    {
      "ContainerName": "MyAdventureGameDependencies",
      "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage"
    }
  ]
}
```

#### Sample Response
<a name="API_CreateContainerGroupDefinition_Example_2_Response"></a>

```
{
  "ContainerGroupDefinition": {
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:1",
    "ContainerGroupType": "GAME_SERVER",
    "CreationTime": 1496365885.44,
    "GameServerContainerDefinition": [
      {
        "ContainerName": "MyAdventureGameContainer",
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
        "ResolvedImageDigest": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "ServerSdkVersion": "5.2.0"
      }
    ],
    "Name": "MyAdventureGameContainerGroup",
    "OperatingSystem": "AMAZON_LINUX_2023",
    "Status": "READY",
    "SupportContainerDefinitions": [
      {
        "ContainerName": "MyAdventureGameDependencies",
        "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage"
      }
    ],
    "TotalMemoryLimitMebibytes": 1024,
    "TotalVcpuLimit": 1,
    "VersionNumber": "1"
  }
}
```

## See Also
<a name="API_CreateContainerGroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/CreateContainerGroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/CreateContainerGroupDefinition)

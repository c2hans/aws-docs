---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerGroupDefinition.html
---

# DescribeContainerGroupDefinition
<a name="API_DescribeContainerGroupDefinition"></a>

 **This API works with the following fleet types:** Container

Retrieves the properties of a container group definition, including all container definitions in the group.

 **Request options:**
+ Retrieve the latest version of a container group definition. Specify the container group definition name only, or use an ARN value without a version number.
+ Retrieve a particular version. Specify the container group definition name and a version number, or use an ARN value that includes the version number.

 **Results:**

If successful, this operation returns the complete properties of a container group definition version.

 **Learn more**
+  [Manage a container group definition](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html)

## Request Syntax
<a name="API_DescribeContainerGroupDefinition_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "VersionNumber": {{number}}
}
```

## Request Parameters
<a name="API_DescribeContainerGroupDefinition_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_DescribeContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupDefinition-request-Name"></a>
The unique identifier for the container group definition to retrieve properties for. You can use either the `Name` or `ARN` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: Yes

 ** [VersionNumber](#API_DescribeContainerGroupDefinition_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupDefinition-request-VersionNumber"></a>
The specific version to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## Response Syntax
<a name="API_DescribeContainerGroupDefinition_ResponseSyntax"></a>

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
<a name="API_DescribeContainerGroupDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerGroupDefinition](#API_DescribeContainerGroupDefinition_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupDefinition-response-ContainerGroupDefinition"></a>
The properties of the requested container group definition resource.
Type: [ContainerGroupDefinition](API_ContainerGroupDefinition.md) object

## Errors
<a name="API_DescribeContainerGroupDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
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
<a name="API_DescribeContainerGroupDefinition_Examples"></a>

### Retrieve a container group definition version
<a name="API_DescribeContainerGroupDefinition_Example_1"></a>

This example retrieves the 3rd version of a container group definition. It assumes we're working in the same AWS Region as the container group we want to retrieve. To retrieve a container group definition in a different region, we could make the request using the definition's ARN value or we could specify the other region.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeContainerGroupDefinition_Example_1_Request"></a>

```
{
  "Name": "MyAdventureGameContainerGroup",
  "Version": 3
}
```

#### Sample Response
<a name="API_DescribeContainerGroupDefinition_Example_1_Response"></a>

```
{
  "ContainerGroupDefinition": {
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:3",
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
        "LinuxCapabilities": {
          "Include": ["NET_BIND_SERVICE", "SYS_PTRACE"]
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
        "ImageUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/MyAdventureGameContainerImage",
        "LinuxCapabilities": {
          "Include": ["NET_ADMIN"]
        }
      }
    ],
    "TotalMemoryLimitMebibytes": 1024,
    "TotalVcpuLimit": 1,
    "VersionNumber": "3"
  }
}
```

## See Also
<a name="API_DescribeContainerGroupDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeContainerGroupDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeContainerGroupDefinition)

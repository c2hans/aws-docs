---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerGroupDefinitionVersions.html
---

# ListContainerGroupDefinitionVersions
<a name="API_ListContainerGroupDefinitionVersions"></a>

 **This API works with the following fleet types:** Container

Retrieves all versions of a container group definition. Use the pagination parameters to retrieve results in a set of sequential pages.

 **Request options:**
+ Get all versions of a specified container group definition. Specify the container group definition name or ARN value. (If the ARN value has a version number, it's ignored.)

 **Results:**

If successful, this operation returns the complete properties of a set of container group definition versions that match the request.

**Note**
This operation returns the list of container group definitions in descending version order (latest first).

 **Learn more**
+  [Manage a container group definition](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html)

## Request Syntax
<a name="API_ListContainerGroupDefinitionVersions_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Name": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListContainerGroupDefinitionVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Name](#API_ListContainerGroupDefinitionVersions_RequestSyntax) **   <a name="gameliftservers-ListContainerGroupDefinitionVersions-request-Name"></a>
The unique identifier for the container group definition to retrieve properties for. You can use either the `Name` or `ARN` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: Yes

 ** [Limit](#API_ListContainerGroupDefinitionVersions_RequestSyntax) **   <a name="gameliftservers-ListContainerGroupDefinitionVersions-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListContainerGroupDefinitionVersions_RequestSyntax) **   <a name="gameliftservers-ListContainerGroupDefinitionVersions-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListContainerGroupDefinitionVersions_ResponseSyntax"></a>

```
{
   "ContainerGroupDefinitions": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContainerGroupDefinitionVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerGroupDefinitions](#API_ListContainerGroupDefinitionVersions_ResponseSyntax) **   <a name="gameliftservers-ListContainerGroupDefinitionVersions-response-ContainerGroupDefinitions"></a>
A result set of container group definitions that match the request.
Type: Array of [ContainerGroupDefinition](API_ContainerGroupDefinition.md) objects

 ** [NextToken](#API_ListContainerGroupDefinitionVersions_ResponseSyntax) **   <a name="gameliftservers-ListContainerGroupDefinitionVersions-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListContainerGroupDefinitionVersions_Errors"></a>

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
<a name="API_ListContainerGroupDefinitionVersions_Examples"></a>

### Retrieve versions of a container group definition
<a name="API_ListContainerGroupDefinitionVersions_Example_1"></a>

This example retrieves all versions of a container group definition. It uses the pagination parameters to retrieve two definitions at a time. The response includes a `NextToken`, which indicates that there are still more results to retrieve.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListContainerGroupDefinitionVersions_Example_1_Request"></a>

```
{
    "Name": "MyAdventureGameContainerGroup",
    "Limit": 2
}
```

#### Sample Response
<a name="API_ListContainerGroupDefinitionVersions_Example_1_Response"></a>

```
{
  "ContainerGroupDefinitions": [
    {
      "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:3",
      "ContainerGroupType": "GAME_SERVER",
      "CreationTime": 1496365885.44,
      "GameServerContainerDefinition": {
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
      "Name": "MyAdventureGameContainerGroup",
      "OperatingSystem": "AMAZON_LINUX_2023",
      "Status": "READY",
      "TotalMemoryLimitMebibytes": 1024,
      "TotalVcpuLimit": 1,
      "VersionNumber": "3"
    },
    {
      "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2",
      "ContainerGroupType": "GAME_SERVER",
      "CreationTime": 1496365892.11,
      "GameServerContainerDefinition": {
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
          "Include": ["NET_BIND_SERVICE"]
        },
        "ResolvedImageDigest": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "ServerSdkVersion": "5.2.0"
      }
      "Name": "MyAdventureGameContainerGroup",
      "OperatingSystem": "AMAZON_LINUX_2023",
      "Status": "COPYING",
      "TotalMemoryLimitMebibytes": 1024,
      "TotalVcpuLimit": 1,
      "VersionNumber": "2"
    },
  ],
  "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1"
}
```

## See Also
<a name="API_ListContainerGroupDefinitionVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListContainerGroupDefinitionVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

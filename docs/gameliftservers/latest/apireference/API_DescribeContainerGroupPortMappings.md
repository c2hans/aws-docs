---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerGroupPortMappings.html
---

# DescribeContainerGroupPortMappings
<a name="API_DescribeContainerGroupPortMappings"></a>

 **This API works with the following fleet types:** Container

Retrieves the port mappings for a container group running on a container fleet. Port mappings show how container ports are mapped to connection ports on the fleet instance. Use this operation to find the connection port for a specific container on a fleet instance.

 **Request options**
+ Get port mappings for a game server container group. Provide the fleet ID, set `ContainerGroupType` to `GAME_SERVER`, and specify the `ComputeName` for the game server container group.
+ Get port mappings for a per-instance container group. Provide the fleet ID, set `ContainerGroupType` to `PER_INSTANCE`, and specify the `InstanceId` for the instance.
+ Optionally filter results to a single container by providing a `ContainerName`.

 **Results**

This operation returns the fleet ID, fleet ARN, location, container group definition ARN, container group type, compute name (for game server container groups), instance ID, and a list of `ContainerGroupPortMapping` objects. Each object contains the container name, runtime ID, and a list of port mappings that show how container ports map to connection ports on the instance.

 **Learn more**

 [Connect to containers](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-remote-access.html)

 [Create a container group definition](https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-create-groups.html)

## Request Syntax
<a name="API_DescribeContainerGroupPortMappings_RequestSyntax"></a>

```
{
   "ComputeName": "{{string}}",
   "ContainerGroupType": "{{string}}",
   "ContainerName": "{{string}}",
   "FleetId": "{{string}}",
   "InstanceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContainerGroupPortMappings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ContainerGroupType](#API_DescribeContainerGroupPortMappings_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-request-ContainerGroupType"></a>
The type of container group to retrieve port mappings for.
+  `GAME_SERVER` -- Get port mappings for a game server container group.
+  `PER_INSTANCE` -- Get port mappings for a per-instance container group.
Type: String
Valid Values: `GAME_SERVER | PER_INSTANCE`
Required: Yes

 ** [FleetId](#API_DescribeContainerGroupPortMappings_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-request-FleetId"></a>
A unique identifier for the container fleet. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [ComputeName](#API_DescribeContainerGroupPortMappings_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-request-ComputeName"></a>
A unique identifier for the compute resource for which to retrieve port mappings. For a container fleet, a compute represents a game server container group running on a fleet instance. You can use either the compute name or ARN value.
When `ContainerGroupType` is `GAME_SERVER`, this parameter is required.
When `ContainerGroupType` is `PER_INSTANCE`, do not provide this parameter. If you provide a compute name with `PER_INSTANCE`, the request fails with an `InvalidRequestException`.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?$|^arn:.*:compute\/[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`
Required: No

 ** [ContainerName](#API_DescribeContainerGroupPortMappings_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-request-ContainerName"></a>
A container name to filter the results. When provided, the operation returns port mappings for the specified container only. If no container with the specified name exists in the container group, the request fails with a `NotFoundException`.
If not provided, the operation returns port mappings for all containers in the container group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

 ** [InstanceId](#API_DescribeContainerGroupPortMappings_RequestSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-request-InstanceId"></a>
A unique identifier for the fleet instance to retrieve port mappings for.
When `ContainerGroupType` is `PER_INSTANCE`, this parameter is required.
When `ContainerGroupType` is `GAME_SERVER`, this parameter is optional. If you provide an instance ID, it must match the instance that's running the specified compute. If the instance ID doesn't match, the request fails with an `InvalidRequestException`.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`
Required: No

## Response Syntax
<a name="API_DescribeContainerGroupPortMappings_ResponseSyntax"></a>

```
{
   "ComputeName": "string",
   "ContainerGroupDefinitionArn": "string",
   "ContainerGroupPortMappings": [
      {
         "ContainerName": "string",
         "ContainerPortMappings": [
            {
               "ConnectionPort": number,
               "ContainerPort": number,
               "Protocol": "string"
            }
         ],
         "ContainerRuntimeId": "string"
      }
   ],
   "ContainerGroupType": "string",
   "FleetArn": "string",
   "FleetId": "string",
   "InstanceId": "string",
   "Location": "string"
}
```

## Response Elements
<a name="API_DescribeContainerGroupPortMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ComputeName](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-ComputeName"></a>
A unique identifier for the compute resource running the game server container group. Returned when `ContainerGroupType` is `GAME_SERVER`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9\-]+(\/[a-zA-Z0-9\-]+)?`

 ** [ContainerGroupDefinitionArn](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-ContainerGroupDefinitionArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to the container group definition. The ARN value also identifies the specific container group definition version in use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`

 ** [ContainerGroupPortMappings](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-ContainerGroupPortMappings"></a>
A list of `ContainerGroupPortMapping` objects that describe the port mappings for each container in the container group.
Type: Array of [ContainerGroupPortMapping](API_ContainerGroupPortMapping.md) objects

 ** [ContainerGroupType](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-ContainerGroupType"></a>
The type of container group that was specified in the request. Valid values are `GAME_SERVER` or `PER_INSTANCE`.
Type: String
Valid Values: `GAME_SERVER | PER_INSTANCE`

 ** [FleetArn](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift fleet ARN, the resource ID matches the `FleetId` value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-FleetId"></a>
A unique identifier for the container fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

 ** [InstanceId](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-InstanceId"></a>
A unique identifier for the fleet instance. For `GAME_SERVER` requests, this is the instance running the specified compute. For `PER_INSTANCE` requests, this is the instance specified in the request.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`

 ** [Location](#API_DescribeContainerGroupPortMappings_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerGroupPortMappings-response-Location"></a>
The location of the fleet instance, expressed as an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`

## Errors
<a name="API_DescribeContainerGroupPortMappings_Errors"></a>

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
<a name="API_DescribeContainerGroupPortMappings_Examples"></a>

### Get port mappings for a game server container group
<a name="API_DescribeContainerGroupPortMappings_Example_1"></a>

This example retrieves port mappings for a game server container group running on a specific compute in a container fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeContainerGroupPortMappings_Example_1_Request"></a>

```
{
    "FleetId": "containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "ContainerGroupType": "GAME_SERVER",
    "ComputeName": "62c5ff7f7a9a445d84877074c80aeafc"
}
```

#### Sample Response
<a name="API_DescribeContainerGroupPortMappings_Example_1_Response"></a>

```
{
    "FleetId": "containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:containerfleet/containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Location": "us-west-2",
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyGameServerContainerGroup:1",
    "ContainerGroupType": "GAME_SERVER",
    "ComputeName": "62c5ff7f7a9a445d84877074c80aeafc",
    "InstanceId": "i-1234567890abcdef0",
    "ContainerGroupPortMappings": [
        {
            "ContainerName": "MyGameServer",
            "ContainerRuntimeId": "a1b2c3d4e5f6",
            "ContainerPortMappings": [
                {
                    "ContainerPort": 7777,
                    "ConnectionPort": 49200,
                    "Protocol": "UDP"
                },
                {
                    "ContainerPort": 8080,
                    "ConnectionPort": 49201,
                    "Protocol": "TCP"
                }
            ]
        },
        {
            "ContainerName": "MySidecar",
            "ContainerRuntimeId": "f6e5d4c3b2a1",
            "ContainerPortMappings": [
                {
                    "ContainerPort": 9090,
                    "ConnectionPort": 49202,
                    "Protocol": "TCP"
                }
            ]
        }
    ]
}
```

### Get port mappings for a per-instance container group
<a name="API_DescribeContainerGroupPortMappings_Example_2"></a>

This example retrieves port mappings for a per-instance container group (such as daemon or logging containers) running on a specific instance in a container fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeContainerGroupPortMappings_Example_2_Request"></a>

```
{
    "FleetId": "containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "ContainerGroupType": "PER_INSTANCE",
    "InstanceId": "i-1234567890abcdef0"
}
```

#### Sample Response
<a name="API_DescribeContainerGroupPortMappings_Example_2_Response"></a>

```
{
    "FleetId": "containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:containerfleet/containerfleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Location": "us-west-2",
    "ContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyDaemonContainerGroup:1",
    "ContainerGroupType": "PER_INSTANCE",
    "InstanceId": "i-1234567890abcdef0",
    "ContainerGroupPortMappings": [
        {
            "ContainerName": "MyLoggingAgent",
            "ContainerRuntimeId": "b2c3d4e5f6a1",
            "ContainerPortMappings": [
                {
                    "ContainerPort": 8125,
                    "ConnectionPort": 49300,
                    "Protocol": "UDP"
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_DescribeContainerGroupPortMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeContainerGroupPortMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeContainerGroupPortMappings)

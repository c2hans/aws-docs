---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateContainerFleet.html
---

# UpdateContainerFleet
<a name="API_UpdateContainerFleet"></a>

 **This API works with the following fleet types:** Container

Updates the properties of a managed container fleet. Depending on the properties being updated, this operation might initiate a fleet deployment. You can track deployments for a fleet using [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetDeployment.html).

**Note**
A managed fleet's runtime environment, which depends on the fleet's Amazon Machine Image {AMI} version, can't be updated. You must create a new fleet. As a best practice, we recommend replacing your managed fleets every 30 days to maintain a secure and up-to-date runtime environment for your hosted game servers. For guidance, see [ Security best practices for Amazon GameLift Servers](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/security-best-practices.html).

 **Request options**

As with CreateContainerFleet, many fleet properties use common defaults or are calculated based on the fleet's container group definitions.
+ Update fleet properties that result in a fleet deployment. Include only those properties that you want to change. Specify deployment configuration settings.
+ Update fleet properties that don't result in a fleet deployment. Include only those properties that you want to change.

Changes to the following properties initiate a fleet deployment:
+  `GameServerContainerGroupDefinition`
+  `PerInstanceContainerGroupDefinition`
+  `GameServerContainerGroupsPerInstance`
+  `InstanceInboundPermissions`
+  `InstanceConnectionPortRange`
+  `LogConfiguration`

 **Results**

If successful, this operation updates the container fleet resource, and might initiate a new deployment of fleet resources using the deployment configuration provided. A deployment replaces existing fleet instances with new instances that are deployed with the updated fleet properties. The fleet is placed in `UPDATING` status until the deployment is complete, then return to `ACTIVE`.

You can have only one update deployment active at a time for a fleet. If a second update request initiates a deployment while another deployment is in progress, the first deployment is cancelled.

## Request Syntax
<a name="API_UpdateContainerFleet_RequestSyntax"></a>

```
{
   "DeploymentConfiguration": {
      "ImpairmentStrategy": "{{string}}",
      "MinimumHealthyPercentage": {{number}},
      "ProtectionStrategy": "{{string}}"
   },
   "Description": "{{string}}",
   "FleetId": "{{string}}",
   "GameServerContainerGroupDefinitionName": "{{string}}",
   "GameServerContainerGroupsPerInstance": {{number}},
   "GameSessionCreationLimitPolicy": {
      "NewGameSessionsPerCreator": {{number}},
      "PolicyPeriodInMinutes": {{number}}
   },
   "InstanceConnectionPortRange": {
      "FromPort": {{number}},
      "ToPort": {{number}}
   },
   "InstanceInboundPermissionAuthorizations": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ],
   "InstanceInboundPermissionRevocations": [
      {
         "FromPort": {{number}},
         "IpRange": "{{string}}",
         "Protocol": "{{string}}",
         "ToPort": {{number}}
      }
   ],
   "LogConfiguration": {
      "LogDestination": "{{string}}",
      "LogGroupArn": "{{string}}",
      "S3BucketName": "{{string}}"
   },
   "MetricGroups": [ "{{string}}" ],
   "NewGameSessionProtectionPolicy": "{{string}}",
   "PerInstanceContainerGroupDefinitionName": "{{string}}",
   "RemoveAttributes": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateContainerFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-FleetId"></a>
A unique identifier for the container fleet to update. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [DeploymentConfiguration](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-DeploymentConfiguration"></a>
Instructions for how to deploy updates to a container fleet, if the fleet update initiates a deployment. The deployment configuration lets you determine how to replace fleet instances and what actions to take if the deployment fails.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** [Description](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-Description"></a>
A meaningful description of the container fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [GameServerContainerGroupDefinitionName](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-GameServerContainerGroupDefinitionName"></a>
The name or ARN value of a new game server container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value. You can't remove a fleet's game server container group definition, you can only update or replace it with another definition.
Update a container group definition by calling [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html). This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource with an incremented version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [GameServerContainerGroupsPerInstance](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-GameServerContainerGroupsPerInstance"></a>
The number of times to replicate the game server container group on each fleet instance. By default, Amazon GameLift Servers calculates the maximum number of game server container groups that can fit on each instance. You can remove this property value to use the calculated value, or set it manually. If you set this number manually, Amazon GameLift Servers uses your value as long as it's less than the calculated maximum.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 5000.
Required: No

 ** [GameSessionCreationLimitPolicy](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-GameSessionCreationLimitPolicy"></a>
A policy that limits the number of game sessions that each individual player can create on instances in this fleet. The limit applies for a specified span of time.
Type: [GameSessionCreationLimitPolicy](API_GameSessionCreationLimitPolicy.md) object
Required: No

 ** [InstanceConnectionPortRange](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-InstanceConnectionPortRange"></a>
A revised set of port numbers to open on each fleet instance. By default, Amazon GameLift Servers calculates an optimal port range based on your fleet configuration. If you previously set this parameter manually, you can't reset this to use the calculated settings.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
Type: [ConnectionPortRange](API_ConnectionPortRange.md) object
Required: No

 ** [InstanceInboundPermissionAuthorizations](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-InstanceInboundPermissionAuthorizations"></a>
A set of ports to add to the container fleet's inbound permissions.
The port range must not overlap with the Amazon GameLift Servers reserved port range `4092-4191`. This range is reserved for internal Amazon GameLift Servers services.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [InstanceInboundPermissionRevocations](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-InstanceInboundPermissionRevocations"></a>
A set of ports to remove from the container fleet's inbound permissions.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.
Required: No

 ** [LogConfiguration](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-LogConfiguration"></a>
The method for collecting container logs for the fleet.
Type: [LogConfiguration](API_LogConfiguration.md) object
Required: No

 ** [MetricGroups](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-MetricGroups"></a>
The name of an AWS CloudWatch metric group to add this fleet to.
Type: Array of strings
Array Members: Maximum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [NewGameSessionProtectionPolicy](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-NewGameSessionProtectionPolicy"></a>
The game session protection policy to apply to all new game sessions that are started in this fleet. Game sessions that already exist are not affected.
Type: String
Valid Values: `NoProtection | FullProtection`
Required: No

 ** [PerInstanceContainerGroupDefinitionName](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-PerInstanceContainerGroupDefinitionName"></a>
The name or ARN value of a new per-instance container group definition to deploy on the fleet. If you're updating the fleet to a specific version of a container group definition, use the ARN value and include the version number. If you're updating the fleet to the latest version of a container group definition, you can use the name value.
Update a container group definition by calling [UpdateContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateContainerGroupDefinition.html). This operation creates a [ContainerGroupDefinition](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ContainerGroupDefinition.html) resource with an incremented version.
To remove a fleet's per-instance container group definition, leave this parameter empty and use the parameter `RemoveAttributes`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [RemoveAttributes](#API_UpdateContainerFleet_RequestSyntax) **   <a name="gameliftservers-UpdateContainerFleet-request-RemoveAttributes"></a>
If set, this update removes a fleet's per-instance container group definition. You can't remove a fleet's game server container group definition.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `PER_INSTANCE_CONTAINER_GROUP_DEFINITION`
Required: No

## Response Syntax
<a name="API_UpdateContainerFleet_ResponseSyntax"></a>

```
{
   "ContainerFleet": {
      "BillingType": "string",
      "CreationTime": number,
      "DeploymentDetails": {
         "LatestDeploymentId": "string"
      },
      "Description": "string",
      "FleetArn": "string",
      "FleetId": "string",
      "FleetRoleArn": "string",
      "GameServerContainerGroupDefinitionArn": "string",
      "GameServerContainerGroupDefinitionName": "string",
      "GameServerContainerGroupsPerInstance": number,
      "GameSessionCreationLimitPolicy": {
         "NewGameSessionsPerCreator": number,
         "PolicyPeriodInMinutes": number
      },
      "InstanceConnectionPortRange": {
         "FromPort": number,
         "ToPort": number
      },
      "InstanceInboundPermissions": [
         {
            "FromPort": number,
            "IpRange": "string",
            "Protocol": "string",
            "ToPort": number
         }
      ],
      "InstanceType": "string",
      "LocationAttributes": [
         {
            "Location": "string",
            "PlayerGatewayStatus": "string",
            "Status": "string"
         }
      ],
      "LogConfiguration": {
         "LogDestination": "string",
         "LogGroupArn": "string",
         "S3BucketName": "string"
      },
      "MaximumGameServerContainerGroupsPerInstance": number,
      "MetricGroups": [ "string" ],
      "NewGameSessionProtectionPolicy": "string",
      "PerInstanceContainerGroupDefinitionArn": "string",
      "PerInstanceContainerGroupDefinitionName": "string",
      "PlayerGatewayMode": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_UpdateContainerFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerFleet](#API_UpdateContainerFleet_ResponseSyntax) **   <a name="gameliftservers-UpdateContainerFleet-response-ContainerFleet"></a>
A collection of container fleet objects for all fleets that match the request criteria.
Type: [ContainerFleet](API_ContainerFleet.md) object

## Errors
<a name="API_UpdateContainerFleet_Errors"></a>

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

 ** NotReadyException **
 The operation failed because Amazon GameLift Servers has not yet finished validating this compute. We recommend attempting 8 to 10 retries over 3 to 5 minutes with [exponential backoffs and jitter](http://aws.amazon.com/blogs/https:/aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_UpdateContainerFleet_Examples"></a>

### Update a single-region container fleet with a new game server container group
<a name="API_UpdateContainerFleet_Example_1"></a>

This example updates the fleet with a new version of the fleet's game server container group. No other fleet properties are changed. The update initiates a fleet deployment.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateContainerFleet_Example_1_Request"></a>

```
{
  "DeploymentConfiguration": {
    "ImpairmentStrategy": "ROLLBACK",
    "MinimumHealthyPercentage": 75,
    "ProtectionStrategy": "WITH_PROTECTION"
  },
  "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "GameServerContainerGroupDefinitionName": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2"
}
```

#### Sample Response
<a name="API_UpdateContainerFleet_Example_1_Response"></a>

```
{
  "ContainerFleet": {
    "BillingType": ON_DEMAND,
    "CreationTime": 1736365885.22,
    "DeploymentDetails": {
      "LatestDeploymentId": "deployment-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
    },
    "FleetArn": "arn:aws:gamelift:us-west-2:111122223333:containerfleet/containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetRoleArn": "arn:aws:iam::MyAccount:role/MyRole",
    "GameServerContainerGroupDefinitionArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2",
    "GameServerContainerGroupDefinitionName": "MyAdventureGameContainerGroup",
    "GameServerContainerGroupsPerInstance": number,
    "InstanceConnectionPortRange": {
      "FromPort": 4192,
      "ToPort": 4242
    },
    "InstanceInboundPermissions": [
      {
        "FromPort": 4192,
        "IpRange": "string",
        "Protocol": "UDP",
        "ToPort": 4242,
      }
    ],
    "InstanceType": "c5.large",
    "LogConfiguration": {
      "LogGroupArn": "arn:aws:logs:us-west-2:111222333444:log-group:customerLogs",
      "LogDestination": "CLOUDWATCH"
    },
    "MaximumGameServerContainerGroupsPerInstance": 10,
    "NewGameSessionProtectionPolicy": "NoProtection",
    "Status": "UPDATING"
  }
}
```

## See Also
<a name="API_UpdateContainerFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateContainerFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateContainerFleet)

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeGameServerGroup.html
---

# DescribeGameServerGroup
<a name="API_DescribeGameServerGroup"></a>

 **This API works with the following fleet types:** EC2 (FleetIQ)

Retrieves information on a game server group. This operation returns only properties related to Amazon GameLift Servers FleetIQ. To view or update properties for the corresponding Auto Scaling group, such as launch template, auto scaling policies, and maximum/minimum group size, access the Auto Scaling group directly.

To get attributes for a game server group, provide a group name or ARN value. If successful, a `GameServerGroup` object is returned.

 **Learn more**

 [Amazon GameLift Servers FleetIQ Guide](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html)

## Request Syntax
<a name="API_DescribeGameServerGroup_RequestSyntax"></a>

```
{
   "GameServerGroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGameServerGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GameServerGroupName](#API_DescribeGameServerGroup_RequestSyntax) **   <a name="gameliftservers-DescribeGameServerGroup-request-GameServerGroupName"></a>
A unique identifier for the game server group. Use either the name or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-\.]+|^arn:.*:gameservergroup\/[a-zA-Z0-9-\.]+`
Required: Yes

## Response Syntax
<a name="API_DescribeGameServerGroup_ResponseSyntax"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "string",
      "BalancingStrategy": "string",
      "CreationTime": number,
      "GameServerGroupArn": "string",
      "GameServerGroupName": "string",
      "GameServerProtectionPolicy": "string",
      "InstanceDefinitions": [
         {
            "InstanceType": "string",
            "WeightedCapacity": "string"
         }
      ],
      "LastUpdatedTime": number,
      "RoleArn": "string",
      "Status": "string",
      "StatusReason": "string",
      "SuspendedActions": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeGameServerGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GameServerGroup](#API_DescribeGameServerGroup_ResponseSyntax) **   <a name="gameliftservers-DescribeGameServerGroup-response-GameServerGroup"></a>
An object with the property settings for the requested game server group resource.
Type: [GameServerGroup](API_GameServerGroup.md) object

## Errors
<a name="API_DescribeGameServerGroup_Errors"></a>

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

## Examples
<a name="API_DescribeGameServerGroup_Examples"></a>

### Retrieve a game server group
<a name="API_DescribeGameServerGroup_Example_1"></a>

This example retrieves information about a game server group by providing the group name.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeGameServerGroup_Example_1_Request"></a>

```
{
   "GameServerGroupName": "MegaFrogServers_NA"
}

CLI command:

aws gamelift describe-game-server-group \
    --game-server-group-name MegaFrogServers_NA
```

#### Sample Response
<a name="API_DescribeGameServerGroup_Example_1_Response"></a>

```
{
   "GameServerGroup": {
      "AutoScalingGroupArn": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:1111aaaa-22bb-33cc-44dd-5555eeee66ff:autoScalingGroupName/MegaFrogServers_NA",
      "BalancingStrategy": "SPOT_PREFERRED",
      "CreationTime": 1496365885.44,
      "GameServerGroupArn": "arn:aws:gamelift:us-west-2::GameServerGroup/MegaFrogServers_NA",
      "GameServerGroupName": " MegaFrogServers_NA",
      "GameServerProtectionPolicy": "NO_PROTECTION",
      "InstanceDefinitions": [
         {
            "InstanceType": "c5.2xlarge",
            "WeightedCapacity": "1"
         },
         {
            "InstanceType": "c5.4xlarge",
            "WeightedCapacity": "2"
         }
      ],
      "LastUpdatedTime": 1496365885.44,
      "RoleArn": "arn:aws:iam:123456789012::role/GameLiftGsgRole",
      "Status": "ACTIVE",
      "StatusReason": "",
      "SuspendedActions": []
}
```

## See Also
<a name="API_DescribeGameServerGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeGameServerGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeGameServerGroup)

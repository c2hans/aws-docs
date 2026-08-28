---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeContainerFleet.html
---

# DescribeContainerFleet
<a name="API_DescribeContainerFleet"></a>

 **This API works with the following fleet types:** Container

Retrieves the properties for a container fleet. When requesting attributes for multiple fleets, use the pagination parameters to retrieve results as a set of sequential pages.

 **Request options**
+ Get container fleet properties for a single fleet. Provide either the fleet ID or ARN value.

 **Results**

If successful, a `ContainerFleet` object is returned. This object includes the fleet properties, including information about the most recent deployment.

**Note**
Some API operations limit the number of fleet IDs that allowed in one request. If a request exceeds this limit, the request fails and the error message contains the maximum allowed number.

## Request Syntax
<a name="API_DescribeContainerFleet_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeContainerFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeContainerFleet_RequestSyntax) **   <a name="gameliftservers-DescribeContainerFleet-request-FleetId"></a>
A unique identifier for the container fleet to retrieve. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

## Response Syntax
<a name="API_DescribeContainerFleet_ResponseSyntax"></a>

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
<a name="API_DescribeContainerFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerFleet](#API_DescribeContainerFleet_ResponseSyntax) **   <a name="gameliftservers-DescribeContainerFleet-response-ContainerFleet"></a>
The properties for the requested container fleet, including current status.
Type: [ContainerFleet](API_ContainerFleet.md) object

## Errors
<a name="API_DescribeContainerFleet_Errors"></a>

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
<a name="API_DescribeContainerFleet_Examples"></a>

### Request attributes for a container fleet
<a name="API_DescribeContainerFleet_Example_1"></a>

This example retrieves attributes for an managed container fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeContainerFleet_Example_1_Request"></a>

```
{
    "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

#### Sample Response
<a name="API_DescribeContainerFleet_Example_1_Response"></a>

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
      "Status": "PENDING"
   }
}
```

## See Also
<a name="API_DescribeContainerFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeContainerFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeContainerFleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

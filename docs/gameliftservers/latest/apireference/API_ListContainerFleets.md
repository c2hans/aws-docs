---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListContainerFleets.html
---

# ListContainerFleets
<a name="API_ListContainerFleets"></a>

 **This API works with the following fleet types:** Container

Retrieves a collection of container fleet resources in an AWS Region. For fleets that have multiple locations, this operation retrieves fleets based on their home Region only.

 **Request options**
+ Get a list of all fleets. Call this operation without specifying a container group definition.
+ Get a list of fleets filtered by container group definition. Provide the container group definition name or ARN value.
+ To get a list of all Amazon GameLift Servers Realtime fleets with a specific configuration script, provide the script ID.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, this operation returns a collection of container fleets that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.

**Note**
Fleet IDs are returned in no particular order.

## Request Syntax
<a name="API_ListContainerFleets_RequestSyntax"></a>

```
{
   "ContainerGroupDefinitionName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListContainerFleets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ContainerGroupDefinitionName](#API_ListContainerFleets_RequestSyntax) **   <a name="gameliftservers-ListContainerFleets-request-ContainerGroupDefinitionName"></a>
The container group definition to filter the list on. Use this parameter to retrieve only those fleets that use the specified container group definition. You can specify the container group definition's name to get fleets with the latest versions. Alternatively, provide an ARN value to get fleets with a specific version number.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z0-9\-]+$|^arn:.*:containergroupdefinition\/[a-zA-Z0-9\-]+(:[0-9]+)?$`
Required: No

 ** [Limit](#API_ListContainerFleets_RequestSyntax) **   <a name="gameliftservers-ListContainerFleets-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListContainerFleets_RequestSyntax) **   <a name="gameliftservers-ListContainerFleets-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListContainerFleets_ResponseSyntax"></a>

```
{
   "ContainerFleets": [
      {
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
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListContainerFleets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ContainerFleets](#API_ListContainerFleets_ResponseSyntax) **   <a name="gameliftservers-ListContainerFleets-response-ContainerFleets"></a>
A collection of container fleet objects for all fleets that match the request criteria.
Type: Array of [ContainerFleet](API_ContainerFleet.md) objects
Array Members: Minimum number of 1 item.

 ** [NextToken](#API_ListContainerFleets_ResponseSyntax) **   <a name="gameliftservers-ListContainerFleets-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListContainerFleets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidRequestException **
One or more parameter values in the request are invalid. Correct the invalid parameter values before retrying.
HTTP Status Code: 400

 ** UnauthorizedException **
The client failed authentication. Clients should not retry such requests.
HTTP Status Code: 400

 ** UnsupportedRegionException **
The requested operation is not supported in the Region specified.
HTTP Status Code: 400

## Examples
<a name="API_ListContainerFleets_Examples"></a>

### List container fleets with a container group definition
<a name="API_ListContainerFleets_Example_1"></a>

This example retrieves the properties of all fleets with a specified container group definition. Because the request uses the definition name, it returns fleets that are deployed with the latest version of the container group definition. The request uses the pagination parameters to retrieve one fleet at a time. The example response includes a `NextToken`, which indicates that there are still more results to retrieve.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListContainerFleets_Example_1_Request"></a>

```
{
    "ContainerGroupDefinitionName": "MyAdventureGameContainerGroup",
    "Limit": 1,
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE1"
}
```

#### Sample Response
<a name="API_ListContainerFleets_Example_1_Response"></a>

```
{
  "ContainerFleets": [
    {
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
  ],
  "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

## See Also
<a name="API_ListContainerFleets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListContainerFleets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListContainerFleets)

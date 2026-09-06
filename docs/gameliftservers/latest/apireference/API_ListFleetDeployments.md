---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ListFleetDeployments.html
---

# ListFleetDeployments
<a name="API_ListFleetDeployments"></a>

 **This API works with the following fleet types:** Container

Retrieves a collection of container fleet deployments in an AWS Region. Use the pagination parameters to retrieve results as a set of sequential pages.

 **Request options**
+ Get a list of all deployments. Call this operation without specifying a fleet ID.
+ Get a list of all deployments for a fleet. Specify the container fleet ID or ARN value.

 **Results**

If successful, this operation returns a list of deployments that match the request parameters. A NextToken value is also returned if there are more result pages to retrieve.

**Note**
Deployments are returned starting with the latest.

## Request Syntax
<a name="API_ListFleetDeployments_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListFleetDeployments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_ListFleetDeployments_RequestSyntax) **   <a name="gameliftservers-ListFleetDeployments-request-FleetId"></a>
A unique identifier for the container fleet. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** [Limit](#API_ListFleetDeployments_RequestSyntax) **   <a name="gameliftservers-ListFleetDeployments-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListFleetDeployments_RequestSyntax) **   <a name="gameliftservers-ListFleetDeployments-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListFleetDeployments_ResponseSyntax"></a>

```
{
   "FleetDeployments": [
      {
         "CreationTime": number,
         "DeploymentConfiguration": {
            "ImpairmentStrategy": "string",
            "MinimumHealthyPercentage": number,
            "ProtectionStrategy": "string"
         },
         "DeploymentId": "string",
         "DeploymentStatus": "string",
         "FleetId": "string",
         "GameServerBinaryArn": "string",
         "PerInstanceBinaryArn": "string",
         "RollbackGameServerBinaryArn": "string",
         "RollbackPerInstanceBinaryArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListFleetDeployments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetDeployments](#API_ListFleetDeployments_ResponseSyntax) **   <a name="gameliftservers-ListFleetDeployments-response-FleetDeployments"></a>
The requested deployment information.
Type: Array of [FleetDeployment](API_FleetDeployment.md) objects

 ** [NextToken](#API_ListFleetDeployments_ResponseSyntax) **   <a name="gameliftservers-ListFleetDeployments-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListFleetDeployments_Errors"></a>

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
<a name="API_ListFleetDeployments_Examples"></a>

### List deployments for a container fleet
<a name="API_ListFleetDeployments_Example_1"></a>

This example retrieves the properties of all deployments for a specified container fleets The request uses the pagination parameters to retrieve one fleet at a time. The example response includes a `NextToken`, which indicates that there are still more results to retrieve.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_ListFleetDeployments_Example_1_Request"></a>

```
{
  "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "Limit": 1
}
```

#### Sample Response
<a name="API_ListFleetDeployments_Example_1_Response"></a>

```
{
  "FleetDeployments": [
    {
      "CreationTime": 1736365885.22,
      "DeploymentConfiguration": {
         "ImpairmentStrategy": "ROLLBACK",
         "MinimumHealthyPercentage": 30,
         "ProtectionStrategy": "WITH_PROTECTION"
      },
      "DeploymentId": "deployment-3333aaaa-44bb-55cc-66dd-7777eeee88ff",
      "DeploymentStatus": "COMPLETE",
      "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
      "GameServerBinaryArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:2",
      "RollbackGameServerBinaryArn": "arn:aws:gamelift:us-west-2:111122223333:containergroupdefinition/MyAdventureGameContainerGroup:1",
    }
  ],
  "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

## See Also
<a name="API_ListFleetDeployments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/ListFleetDeployments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ListFleetDeployments)

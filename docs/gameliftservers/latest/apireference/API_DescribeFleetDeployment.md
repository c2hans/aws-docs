---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetDeployment.html
---

# DescribeFleetDeployment
<a name="API_DescribeFleetDeployment"></a>

 **This API works with the following fleet types:** Container

Retrieves information about a managed container fleet deployment.

 **Request options**
+ Get information about the latest deployment for a specific fleet. Provide the fleet ID or ARN.
+  Get information about a specific deployment. Provide the fleet ID or ARN and the deployment ID.

 **Results**

If successful, a `FleetDeployment` object is returned.

## Request Syntax
<a name="API_DescribeFleetDeployment_RequestSyntax"></a>

```
{
   "DeploymentId": "{{string}}",
   "FleetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetDeployment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeFleetDeployment_RequestSyntax) **   <a name="gameliftservers-DescribeFleetDeployment-request-FleetId"></a>
A unique identifier for the container fleet. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [DeploymentId](#API_DescribeFleetDeployment_RequestSyntax) **   <a name="gameliftservers-DescribeFleetDeployment-request-DeploymentId"></a>
A unique identifier for the deployment to return information for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[a-zA-Z0-9\-]+$`
Required: No

## Response Syntax
<a name="API_DescribeFleetDeployment_ResponseSyntax"></a>

```
{
   "FleetDeployment": {
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
   },
   "LocationalDeployments": {
      "string" : {
         "DeploymentStatus": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeFleetDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetDeployment](#API_DescribeFleetDeployment_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetDeployment-response-FleetDeployment"></a>
The requested deployment information.
Type: [FleetDeployment](API_FleetDeployment.md) object

 ** [LocationalDeployments](#API_DescribeFleetDeployment_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetDeployment-response-LocationalDeployments"></a>
If the deployment is for a multi-location fleet, the requests returns the deployment status in each fleet location.
Type: String to [LocationalDeployment](API_LocationalDeployment.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[a-zA-Z0-9\-]+$`

## Errors
<a name="API_DescribeFleetDeployment_Errors"></a>

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
<a name="API_DescribeFleetDeployment_Examples"></a>

### Retrieve information on a fleet deployment
<a name="API_DescribeFleetDeployment_Example_1"></a>

This example gets information on a specific deployment for a container fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetDeployment_Example_1_Request"></a>

```
{
  "FleetId": "containerfleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
  "DeploymentId": "deployment-3333aaaa-44bb-55cc-66dd-7777eeee88ff"
}
```

#### Sample Response
<a name="API_DescribeFleetDeployment_Example_1_Response"></a>

```
{
   "FleetDeployment": {
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
}
```

## See Also
<a name="API_DescribeFleetDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetDeployment)

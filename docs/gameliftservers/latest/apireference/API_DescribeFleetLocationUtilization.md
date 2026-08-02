---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationUtilization.html
---

# DescribeFleetLocationUtilization
<a name="API_DescribeFleetLocationUtilization"></a>

 **This API works with the following fleet types:** EC2, Anywhere, Container

Retrieves current usage data for a fleet location. Utilization data provides a snapshot of current game hosting activity at the requested location. Use this operation to retrieve utilization information for a fleet's remote location or home Region (you can also retrieve home Region utilization by calling `DescribeFleetUtilization`).

To retrieve utilization data, identify a fleet and location.

If successful, a `FleetUtilization` object is returned for the requested fleet location.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting

 [GameLift metrics for fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)

## Request Syntax
<a name="API_DescribeFleetLocationUtilization_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetLocationUtilization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeFleetLocationUtilization_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationUtilization-request-FleetId"></a>
A unique identifier for the fleet to request location utilization for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Location](#API_DescribeFleetLocationUtilization_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationUtilization-request-Location"></a>
The fleet location to retrieve utilization information for. Specify a location in the form of an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeFleetLocationUtilization_ResponseSyntax"></a>

```
{
   "FleetUtilization": {
      "ActiveGameSessionCount": number,
      "ActiveServerProcessCount": number,
      "CurrentPlayerSessionCount": number,
      "FleetArn": "string",
      "FleetId": "string",
      "Location": "string",
      "MaximumPlayerSessionCount": number
   }
}
```

## Response Elements
<a name="API_DescribeFleetLocationUtilization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetUtilization](#API_DescribeFleetLocationUtilization_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationUtilization-response-FleetUtilization"></a>
Utilization information for the requested fleet location. Utilization objects are returned only for fleets and locations that currently exist.
Type: [FleetUtilization](API_FleetUtilization.md) object

## Errors
<a name="API_DescribeFleetLocationUtilization_Errors"></a>

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
<a name="API_DescribeFleetLocationUtilization_Examples"></a>

### Request utilization for a fleet location
<a name="API_DescribeFleetLocationUtilization_Example_1"></a>

This example retrieves usage data for the remote fleet location `sa-east-1`. The fleet's home Region is `us-west-2`.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetLocationUtilization_Example_1_Request"></a>

```
{
    "FleetId": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Location": "sa-east-1"
}
```

#### Sample Response
<a name="API_DescribeFleetLocationUtilization_Example_1_Response"></a>

```
{
    "FleetUtilization": {
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "ActiveServerProcessCount": 100,
        "ActiveGameSessionCount": 62,
        "CurrentPlayerSessionCount": 329,
        "MaximumPlayerSessionCount": 1000,
        "Location": "sa-east-1"
        }
}
```

## See Also
<a name="API_DescribeFleetLocationUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetLocationUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetLocationUtilization)

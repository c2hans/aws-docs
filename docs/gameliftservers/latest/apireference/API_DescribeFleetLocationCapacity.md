---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetLocationCapacity.html
---

# DescribeFleetLocationCapacity
<a name="API_DescribeFleetLocationCapacity"></a>

 **This API works with the following fleet types:** EC2, Container

Retrieves the resource capacity settings for a fleet location. The data returned includes the current capacity (number of EC2 instances) and some scaling settings for the requested fleet location. For a managed container fleet, this operation also returns counts for game server container groups.

Use this operation to retrieve capacity information for a fleet's remote location or home Region (you can also retrieve home Region capacity by calling `DescribeFleetCapacity`).

To retrieve capacity data, identify a fleet and location.

If successful, a `FleetCapacity` object is returned for the requested fleet location.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

 [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting

 [GameLift metrics for fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html#gamelift-metrics-fleet)

## Request Syntax
<a name="API_DescribeFleetLocationCapacity_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetLocationCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeFleetLocationCapacity_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationCapacity-request-FleetId"></a>
A unique identifier for the fleet to request location capacity for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Location](#API_DescribeFleetLocationCapacity_RequestSyntax) **   <a name="gameliftservers-DescribeFleetLocationCapacity-request-Location"></a>
The fleet location to retrieve capacity information for. Specify a location in the form of an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeFleetLocationCapacity_ResponseSyntax"></a>

```
{
   "FleetCapacity": {
      "FleetArn": "string",
      "FleetId": "string",
      "GameServerContainerGroupCounts": {
         "ACTIVE": number,
         "IDLE": number,
         "PENDING": number,
         "TERMINATING": number
      },
      "InstanceCounts": {
         "ACTIVE": number,
         "DESIRED": number,
         "IDLE": number,
         "MAXIMUM": number,
         "MINIMUM": number,
         "PENDING": number,
         "TERMINATING": number
      },
      "InstanceType": "string",
      "Location": "string",
      "ManagedCapacityConfiguration": {
         "ScaleInAfterInactivityMinutes": number,
         "ZeroCapacityStrategy": "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeFleetLocationCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetCapacity](#API_DescribeFleetLocationCapacity_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetLocationCapacity-response-FleetCapacity"></a>
Resource capacity information for the requested fleet location. Capacity objects are returned only for fleets and locations that currently exist. Changes in desired instance value can take up to 1 minute to be reflected.
Type: [FleetCapacity](API_FleetCapacity.md) object

## Errors
<a name="API_DescribeFleetLocationCapacity_Errors"></a>

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
<a name="API_DescribeFleetLocationCapacity_Examples"></a>

### Request capacity information for a fleet location
<a name="API_DescribeFleetLocationCapacity_Example_1"></a>

This example retrieves fleet capacity information for a remote fleet location. The returned `FleetCapacity` object describes the capacity at the specified location only. To get a fleet's current total capacity, first call `DescribeFleetLocationAttributes` to get a list of the fleet's remote locations, and then call DescribeFleetLocationCapacity for each remote location plus the home Region, and sum the results for active instances.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetLocationCapacity_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Location": "sa-east-1"
}
```

#### Sample Response
<a name="API_DescribeFleetLocationCapacity_Example_1_Response"></a>

```
{
    "FleetCapacity": {
        "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
        "InstanceCounts": {
            "DESIRED": 10,
            "MINIMUM": 1,
            "MAXIMUM": 20,
            "PENDING": 0,
            "ACTIVE": 10,
            "IDLE": 3,
            "TERMINATING": 0
        },
        "InstanceType": "c5.large",
        "Location": "sa-east-1"
        }
    ]
}
```

## See Also
<a name="API_DescribeFleetLocationCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetLocationCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetLocationCapacity)

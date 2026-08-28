---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_UpdateFleetCapacity.html
---

# UpdateFleetCapacity
<a name="API_UpdateFleetCapacity"></a>

 **This API works with the following fleet types:** EC2, Container

Updates capacity settings for a managed EC2 fleet or managed container fleet. For these fleets, you adjust capacity by changing the number of instances in the fleet. Fleet capacity determines the number of game sessions and players that the fleet can host based on its configuration. For fleets with multiple locations, use this operation to manage capacity settings in each location individually.
+ Minimum/maximum size: Set hard limits on the number of Amazon EC2 instances allowed. If Amazon GameLift Servers receives a request--either through manual update or automatic scaling--it won't change the capacity to a value outside of this range.
+ Desired capacity: As an alternative to automatic scaling, manually set the number of Amazon EC2 instances to be maintained. Before changing a fleet's desired capacity, check the maximum capacity of the fleet's Amazon EC2 instance type by calling [DescribeEC2InstanceLimits](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeEC2InstanceLimits.html).

To update capacity for a fleet's home Region, or if the fleet has no remote locations, omit the `Location` parameter. The fleet must be in `ACTIVE` status.

To update capacity for a fleet's remote location, set the `Location` parameter to the location to update. The location must be in `ACTIVE` status.

If successful, Amazon GameLift Servers updates the capacity settings and returns the identifiers for the updated fleet and/or location. If a requested change to desired capacity exceeds the instance type's limit, the `LimitExceeded` exception occurs.

Updates often prompt an immediate change in fleet capacity, such as when current capacity is different than the new desired capacity or outside the new limits. In this scenario, Amazon GameLift Servers automatically initiates steps to add or remove instances in the fleet location. You can track a fleet's current capacity by calling [DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html) or [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html).

 Use ManagedCapacityConfiguration with the "SCALE\_TO\_AND\_FROM\_ZERO" ZeroCapacityStrategy to enable Amazon GameLift Servers to fully manage the MinSize value, switching between 0 and 1 based on game session activity. This is ideal for eliminating compute costs during periods of no game activity. It is particularly beneficial during development when you're away from your desk, iterating on builds for extended periods, in production environments serving low-traffic locations, or for games with long, predictable downtime windows. By automatically managing capacity between 0 and 1 instances, you avoid paying for idle instances while maintaining the ability to serve game sessions when demand arrives. Note that while scale-out is triggered immediately upon receiving a game session request, actual game session availability depends on your server process startup time, so this approach works best with multi-location Fleets where cold-start latency is tolerable. With a "MANUAL" ZeroCapacityStrategy Amazon GameLift Servers will not modify Fleet MinSize values automatically and will not scale out from zero instances in response to game sessions. This is configurable per-location.

 **Learn more**

 [Scaling fleet capacity](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html)

## Request Syntax
<a name="API_UpdateFleetCapacity_RequestSyntax"></a>

```
{
   "DesiredInstances": {{number}},
   "FleetId": "{{string}}",
   "Location": "{{string}}",
   "ManagedCapacityConfiguration": {
      "ScaleInAfterInactivityMinutes": {{number}},
      "ZeroCapacityStrategy": "{{string}}"
   },
   "MaxSize": {{number}},
   "MinSize": {{number}}
}
```

## Request Parameters
<a name="API_UpdateFleetCapacity_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-FleetId"></a>
A unique identifier for the fleet to update capacity settings for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [DesiredInstances](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-DesiredInstances"></a>
The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [Location](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-Location"></a>
The name of a remote location to update fleet capacity settings for, in the form of an AWS Region code such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [ManagedCapacityConfiguration](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-ManagedCapacityConfiguration"></a>
Configuration for Amazon GameLift Servers-managed capacity scaling options.
Type: [ManagedCapacityConfiguration](API_ManagedCapacityConfiguration.md) object
Required: No

 ** [MaxSize](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-MaxSize"></a>
The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** [MinSize](#API_UpdateFleetCapacity_RequestSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-request-MinSize"></a>
The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0. This parameter cannot be set when using a ManagedCapacityConfiguration where ZeroCapacityStrategy has a value of SCALE\_TO\_AND\_FROM\_ZERO.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## Response Syntax
<a name="API_UpdateFleetCapacity_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string",
   "Location": "string",
   "ManagedCapacityConfiguration": {
      "ScaleInAfterInactivityMinutes": number,
      "ZeroCapacityStrategy": "string"
   }
}
```

## Response Elements
<a name="API_UpdateFleetCapacity_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_UpdateFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_UpdateFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-response-FleetId"></a>
A unique identifier for the fleet that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

 ** [Location](#API_UpdateFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-response-Location"></a>
The remote location being updated, expressed as an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`

 ** [ManagedCapacityConfiguration](#API_UpdateFleetCapacity_ResponseSyntax) **   <a name="gameliftservers-UpdateFleetCapacity-response-ManagedCapacityConfiguration"></a>
Configuration for Amazon GameLift Servers-managed capacity scaling options.
Type: [ManagedCapacityConfiguration](API_ManagedCapacityConfiguration.md) object

## Errors
<a name="API_UpdateFleetCapacity_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.

HTTP Status Code: 400

 ** InternalServiceException **
The service encountered an unrecoverable internal failure while processing the request. Clients can retry such requests immediately or after a waiting period.
HTTP Status Code: 500

 ** InvalidFleetStatusException **
The requested operation would cause a conflict with the current state of a resource associated with the request and/or the fleet. Resolve the conflict before retrying.
HTTP Status Code: 400

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
<a name="API_UpdateFleetCapacity_Examples"></a>

### Increase fleet capacity
<a name="API_UpdateFleetCapacity_Example_1"></a>

This example requests an increase in fleet capacity and raises the maximum allowed instances to accommodate the request. Because no location is specified, the update is applied to the fleet's home Region (where the fleet was created), which is `us-west-2`. Note that a fleet's home Region is always identified in the fleet ARN.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateFleetCapacity_Example_1_Request"></a>

```
{
   "FleetId": "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
   "DesiredInstances": 10,
   "MaxSize": 10
}
```

#### Sample Response
<a name="API_UpdateFleetCapacity_Example_1_Response"></a>

```
{
    "FleetArn":"arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Location": "us-west-2",
    "ManagedCapacityConfiguration": {
        "ZeroCapacityStrategy": "MANUAL"
    }
}
```

### Update capacity settings for a fleet's remote location
<a name="API_UpdateFleetCapacity_Example_2"></a>

This example adjusts the minimum/maximum allowed instances for one remote location in a multi-location fleet. For fleets that use auto-scaling, allowed instance settings define the scaling range for a fleet location. In this example, the updates are being applied to the remote location `sa-east-1`.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateFleetCapacity_Example_2_Request"></a>

```
{
    "FleetId": "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Location": "sa-east-1",
    "MinSize": 10,
    "MaxSize": 100
}
```

#### Sample Response
<a name="API_UpdateFleetCapacity_Example_2_Response"></a>

```
{
    "FleetArn":"arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Location": "sa-east-1",
    "ManagedCapacityConfiguration": {
        "ZeroCapacityStrategy": "MANUAL"
    }
}
```

### Configure ManagedCapacityConfiguration to Scale to/from Zero
<a name="API_UpdateFleetCapacity_Example_3"></a>

This example configures ManagedCapacityConfiguration such that fleet capacity will automatically scale in to zero following a period (60 minutes in this example) where no game sessions are placed on the fleet and will scale out from zero in response to game session activity.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_UpdateFleetCapacity_Example_3_Request"></a>

```
{
    "FleetId": "arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "ManagedCapacityConfiguration": {
        "ScaleInAfterInactivityMinutes": 60,
        "ZeroCapacityStrategy": "SCALE_TO_AND_FROM_ZERO"
    }
}
```

#### Sample Response
<a name="API_UpdateFleetCapacity_Example_3_Response"></a>

```
{
    "FleetArn":"arn:aws:gamelift:us-west-2::fleet/fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "FleetId": "fleet-1111aaaa-22bb-33cc-44dd-5555eeee66ff",
    "Location": "us-west-2",
    "ManagedCapacityConfiguration": {
        "ScaleInAfterInactivityMinutes": 60,
        "ZeroCapacityStrategy": "SCALE_TO_AND_FROM_ZERO"
    }
}
```

## See Also
<a name="API_UpdateFleetCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/UpdateFleetCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/UpdateFleetCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

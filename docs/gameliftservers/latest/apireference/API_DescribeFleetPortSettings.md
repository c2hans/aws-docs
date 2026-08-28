---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeFleetPortSettings.html
---

# DescribeFleetPortSettings
<a name="API_DescribeFleetPortSettings"></a>

 **This API works with the following fleet types:** EC2

Retrieves a fleet's inbound connection permissions. Connection permissions specify IP addresses and port settings that incoming traffic can use to access server processes in the fleet. Game server processes that are running in the fleet must use a port that falls within this range.

Use this operation in the following ways:
+ To retrieve the port settings for a fleet, identify the fleet's unique identifier.
+ To check the status of recent updates to a fleet remote location, specify the fleet ID and a location. Port setting updates can take time to propagate across all locations.

If successful, a set of `IpPermission` objects is returned for the requested fleet ID. When specifying a location, this operation returns a pending status. If the requested fleet has been deleted, the result set is empty.

 **Learn more**

 [Setting up Amazon GameLift Servers fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

## Request Syntax
<a name="API_DescribeFleetPortSettings_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Location": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFleetPortSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeFleetPortSettings_RequestSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-request-FleetId"></a>
A unique identifier for the fleet to retrieve port settings for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Location](#API_DescribeFleetPortSettings_RequestSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-request-Location"></a>
A remote location to check for status of port setting updates. Use the AWS Region code format, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

## Response Syntax
<a name="API_DescribeFleetPortSettings_ResponseSyntax"></a>

```
{
   "FleetArn": "string",
   "FleetId": "string",
   "InboundPermissions": [
      {
         "FromPort": number,
         "IpRange": "string",
         "Protocol": "string",
         "ToPort": number
      }
   ],
   "Location": "string",
   "UpdateStatus": "string"
}
```

## Response Elements
<a name="API_DescribeFleetPortSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FleetArn](#API_DescribeFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-response-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`

 ** [FleetId](#API_DescribeFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-response-FleetId"></a>
A unique identifier for the fleet that was requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`

 ** [InboundPermissions](#API_DescribeFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-response-InboundPermissions"></a>
The port settings for the requested fleet ID.
Type: Array of [IpPermission](API_IpPermission.md) objects
Array Members: Maximum number of 50 items.

 ** [Location](#API_DescribeFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-response-Location"></a>
The requested fleet location, expressed as an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`

 ** [UpdateStatus](#API_DescribeFleetPortSettings_ResponseSyntax) **   <a name="gameliftservers-DescribeFleetPortSettings-response-UpdateStatus"></a>
The current status of updates to the fleet's port settings in the requested fleet location. A status of `PENDING_UPDATE` indicates that an update was requested for the fleet but has not yet been completed for the location.
Type: String
Valid Values: `PENDING_UPDATE`

## Errors
<a name="API_DescribeFleetPortSettings_Errors"></a>

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
<a name="API_DescribeFleetPortSettings_Examples"></a>

### Request inbound connection permissions for a fleet
<a name="API_DescribeFleetPortSettings_Example_1"></a>

This example retrieves connection settings for a specified fleet.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetPortSettings_Example_1_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
}
```

#### Sample Response
<a name="API_DescribeFleetPortSettings_Example_1_Response"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetArn": "arn:aws:gamelift:us-east-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "InboundPermissions": [
        {
            "FromPort": 33400,
            "ToPort": 33500,
            "IpRange": "0.0.0.0/0",
            "Protocol": "UDP"
        },
        {
            "FromPort": 1900,
            "ToPort": 2000,
            "IpRange": "0.0.0.0/0",
            "Protocol": "TCP"
        }
    ]
}
```

### Check port setting updates in a remote location
<a name="API_DescribeFleetPortSettings_Example_2"></a>

This example retrieves the current status of recent port setting updates for a specified remote location.

HTTP requests are authenticated using an [AWS Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) signature in the `Authorization` header field.

#### Sample Request
<a name="API_DescribeFleetPortSettings_Example_2_Request"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Location": "us-west-2"
}
```

#### Sample Response
<a name="API_DescribeFleetPortSettings_Example_2_Response"></a>

```
{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "FleetArn": "arn:aws:gamelift:us-east-2::fleet/fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "InboundPermissions": [
        {
            "FromPort": 33400,
            "ToPort": 33500,
            "IpRange": "0.0.0.0/0",
            "Protocol": "UDP"
        },
        {
            "FromPort": 1900,
            "ToPort": 2000,
            "IpRange": "0.0.0.0/0",
            "Protocol": "TCP"
        }
    ],
    "Location": "us-west-2",
    "Status": "PENDING_UPDATE"
}
```

## See Also
<a name="API_DescribeFleetPortSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeFleetPortSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeFleetPortSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

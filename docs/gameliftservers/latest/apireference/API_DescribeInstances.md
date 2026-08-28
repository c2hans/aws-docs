---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeInstances.html
---

# DescribeInstances
<a name="API_DescribeInstances"></a>

 **This API works with the following fleet types:**EC2, Container

Retrieves information about the EC2 instances in an Amazon GameLift Servers managed fleet, including instance ID, connection data, and status. You can use this operation with a multi-location fleet to get location-specific instance information. As an alternative, use the operations [https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListCompute) and [https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeCompute) to retrieve information for compute resources, including EC2 and Anywhere fleets.

You can call this operation in the following ways:
+ To get information on all instances in a fleet's home Region, specify the fleet ID.
+ To get information on all instances in a fleet's remote location, specify the fleet ID and location name.
+ To get information on a specific instance in a fleet, specify the fleet ID and instance ID.

Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, this operation returns `Instance` objects for each requested instance, listed in no particular order. If you call this operation for an Anywhere fleet, you receive an InvalidRequestException.

 **Learn more**

 [Remotely connect to fleet instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html)

 [Debug fleet issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html)

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Request Syntax
<a name="API_DescribeInstances_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "InstanceId": "{{string}}",
   "Limit": {{number}},
   "Location": "{{string}}",
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstances_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeInstances_RequestSyntax) **   <a name="gameliftservers-DescribeInstances-request-FleetId"></a>
A unique identifier for the fleet to retrieve instance information for. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [InstanceId](#API_DescribeInstances_RequestSyntax) **   <a name="gameliftservers-DescribeInstances-request-InstanceId"></a>
A unique identifier for an instance to retrieve. Specify an instance ID or leave blank to retrieve all instances in the fleet.
Type: String
Pattern: `[a-zA-Z0-9\.-]+`
Required: No

 ** [Limit](#API_DescribeInstances_RequestSyntax) **   <a name="gameliftservers-DescribeInstances-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Location](#API_DescribeInstances_RequestSyntax) **   <a name="gameliftservers-DescribeInstances-request-Location"></a>
The name of a location to retrieve instance information for, in the form of an AWS Region code such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_DescribeInstances_RequestSyntax) **   <a name="gameliftservers-DescribeInstances-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_DescribeInstances_ResponseSyntax"></a>

```
{
   "Instances": [
      {
         "CreationTime": number,
         "DnsName": "string",
         "FleetArn": "string",
         "FleetId": "string",
         "InstanceId": "string",
         "IpAddress": "string",
         "Location": "string",
         "OperatingSystem": "string",
         "Status": "string",
         "Type": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Instances](#API_DescribeInstances_ResponseSyntax) **   <a name="gameliftservers-DescribeInstances-response-Instances"></a>
A collection of objects containing properties for each instance returned.
Type: Array of [Instance](API_Instance.md) objects

 ** [NextToken](#API_DescribeInstances_ResponseSyntax) **   <a name="gameliftservers-DescribeInstances-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_DescribeInstances_Errors"></a>

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
<a name="API_DescribeInstances_Examples"></a>

### Get instance data on a fleet's home Region
<a name="API_DescribeInstances_Example_1"></a>

This example requests information on instances in a fleet's home Region. If the specified fleet also has instances deployed to remote locations, they aren't included in the response.

#### Sample Request
<a name="API_DescribeInstances_Example_1_Request"></a>

```
{
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Limit": "1"
}
```

#### Sample Response
<a name="API_DescribeInstances_Example_1_Response"></a>

```
{
    "Instances": [
        {
            "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "InstanceId": "i-11111111a222b333c,
            "IpAddress": "192.0.2.0",
            "DnsName": "ec2-192-0-2-0.us-west-2.compute.amazonaws.com",
            "OperatingSystem": "WIN_2012",
            "Type": "c4.large",
            "Status": "Active",
            "CreationTime": 1515032347.867,
            "Location": "us-west-2
        }
    ]
}
```

### Get instance data on a fleet's remote location
<a name="API_DescribeInstances_Example_2"></a>

This example requests information on fleet instances deployed to a remote location in the AWS Region `sa-east-1`. This example retrieves information on fleet instances in the `sa-east-1` only.

#### Sample Request
<a name="API_DescribeInstances_Example_2_Request"></a>

```
{
    "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
    "Location": "sa-east-1",
    "Limit": "2"
}
```

#### Sample Response
<a name="API_DescribeInstances_Example_2_Response"></a>

```
{
    "Instances": [
        {
            "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "FleetArn": "arn:aws:gamelift:us-west-2::fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "InstanceId": "i-11111111a222b333c,
            "IpAddress": "192.0.2.0",
            "DnsName": "ec2-192-0-2-0.us-west-2.compute.amazonaws.com",
            "OperatingSystem": "WIN_2012",
            "Type": "c4.large",
            "Status": "Active",
            "CreationTime": 1515032347.867,
            "Location": "sa-east-1"
        },
        {
            "FleetId": "fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "FleetArn": "arn:aws:gamelift:us-east-2::fleet/fleet-9999ffff-88ee-77dd-66cc-5555bbbb44aa",
            "InstanceId": "i-12312311a222b444d,
            "IpAddress": "192.0.2.0",
            "DnsName": "ec2-192-0-2-0.us-west-2.compute.amazonaws.com",
            "OperatingSystem": "WIN_2012",
            "Type": "c4.large",
            "Status": "Active",
            "CreationTime": 1515032999.867,
            "Location": "sa-east-1"
        }
    ]
}
```

## See Also
<a name="API_DescribeInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeInstances)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

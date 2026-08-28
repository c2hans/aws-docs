---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DescribeScalingPolicies.html
---

# DescribeScalingPolicies
<a name="API_DescribeScalingPolicies"></a>

 **This API works with the following fleet types:** EC2, Container

Retrieves all scaling policies applied to a fleet.

To get a fleet's scaling policies, specify the fleet ID. You can filter this request by policy status, such as to retrieve only active scaling policies. Use the pagination parameters to retrieve results as a set of sequential pages. If successful, set of `ScalingPolicy` objects is returned for the fleet.

A fleet may have all of its scaling policies suspended. This operation does not affect the status of the scaling policies, which remains ACTIVE.

## Request Syntax
<a name="API_DescribeScalingPolicies_RequestSyntax"></a>

```
{
   "FleetId": "{{string}}",
   "Limit": {{number}},
   "Location": "{{string}}",
   "NextToken": "{{string}}",
   "StatusFilter": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeScalingPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [FleetId](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-request-FleetId"></a>
A unique identifier for the fleet for which to retrieve scaling policies. You can use either the fleet ID or ARN value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+$|^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: Yes

 ** [Limit](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-request-Limit"></a>
The maximum number of results to return. Use this parameter with `NextToken` to get results as a set of sequential pages.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [Location](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-request-Location"></a>
 The fleet location. If you don't specify this value, the response contains the scaling policies of every location in the fleet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** [NextToken](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-request-NextToken"></a>
A token that indicates the start of the next sequential page of results. Use the token that is returned with a previous call to this operation. To start at the beginning of the result set, do not specify a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [StatusFilter](#API_DescribeScalingPolicies_RequestSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-request-StatusFilter"></a>
Scaling policy status to filter results on. A scaling policy is only in force when in an `ACTIVE` status.
+  **ACTIVE** -- The scaling policy is currently in force.
+  **UPDATEREQUESTED** -- A request to update the scaling policy has been received.
+  **UPDATING** -- A change is being made to the scaling policy.
+  **DELETEREQUESTED** -- A request to delete the scaling policy has been received.
+  **DELETING** -- The scaling policy is being deleted.
+  **DELETED** -- The scaling policy has been deleted.
+  **ERROR** -- An error occurred in creating the policy. It should be removed and recreated.
Type: String
Valid Values: `ACTIVE | UPDATE_REQUESTED | UPDATING | DELETE_REQUESTED | DELETING | DELETED | ERROR`
Required: No

## Response Syntax
<a name="API_DescribeScalingPolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScalingPolicies": [
      {
         "ComparisonOperator": "string",
         "EvaluationPeriods": number,
         "FleetArn": "string",
         "FleetId": "string",
         "Location": "string",
         "MetricName": "string",
         "Name": "string",
         "PolicyType": "string",
         "ScalingAdjustment": number,
         "ScalingAdjustmentType": "string",
         "Status": "string",
         "TargetConfiguration": {
            "TargetValue": number
         },
         "Threshold": number,
         "UpdateStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeScalingPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeScalingPolicies_ResponseSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-response-NextToken"></a>
A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ScalingPolicies](#API_DescribeScalingPolicies_ResponseSyntax) **   <a name="gameliftservers-DescribeScalingPolicies-response-ScalingPolicies"></a>
A collection of objects containing the scaling policies matching the request.
Type: Array of [ScalingPolicy](API_ScalingPolicy.md) objects

## Errors
<a name="API_DescribeScalingPolicies_Errors"></a>

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
<a name="API_DescribeScalingPolicies_Examples"></a>

### View active scaling policies
<a name="API_DescribeScalingPolicies_Example_1"></a>

In this example, we want to get a list of active scaling policies for a specific fleet. We can do this by retrieving the list of all policies for the fleet filtered by status. The sample request illustrates the use of pagination parameters, `Limit` and `NextToken`, to retrieve multiple results in sequential sets.

#### Sample Request
<a name="API_DescribeScalingPolicies_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: gamelift.us-west-2.amazonaws.com;
Accept-Encoding: identity
Content-Length: 336
User-Agent: aws-cli/1.11.36 Python/2.7.9 Windows/7 botocore/1.4.93
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256  Credential=AKIAIOSFODNN7EXAMPLE/20170406/us-west-2/gamelift/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
X-Amz-Date: 20170406T004805Z
X-Amz-Target: GameLift.DescribeScalingPolicies

{
    "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
    "Limit": "2",
    "StatusFilter": "ACTIVE"
    }
}

CLI syntax:

$aws gamelift describe-scaling-policies
--fleet-id "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa"
--limit "2"
--status-filter "ACTIVE"
```

#### Sample Response
<a name="API_DescribeScalingPolicies_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: b34f8665-EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 600
Date: Thu, 06 Apr 2017 00:48:07 GMT

{
    "ScalingPolicies": [
        {
            "Status": "ACTIVE",
            "Name": "My_Target_Policy_1",
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "PolicyType": "TargetBased",
            "MetricName": "PercentAvailableGameSessions",
            "TargetConfiguration": {"TargetValue": 15"}
        },
        {
            "Status": "ACTIVE",
            "EvaluationPeriods": "1",
            "Name": "My_Rule_Policy_1",
            "ComparisonOperator": "GreaterThanThreshold",
            "FleetId": "fleet-2222bbbb-33cc-44dd-55ee-6666ffff77aa",
            "PolicyType": "RuleBased",
            "Threshold": "1.0",
            "ScalingAdjustment": "10",
            "MetricName": "QueueDepth",
            "ScalingAdjustmentType": "PercentChangeInCapacity"
        }
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjJEXAMPLE="
}
```

## See Also
<a name="API_DescribeScalingPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gamelift-2015-10-01/DescribeScalingPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DescribeScalingPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

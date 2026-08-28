---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatchStates.html
---

# DescribeInstancePatchStates
<a name="API_DescribeInstancePatchStates"></a>

Retrieves the high-level patch state of one or more managed nodes.

## Request Syntax
<a name="API_DescribeInstancePatchStates_RequestSyntax"></a>

```
{
   "InstanceIds": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstancePatchStates_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceIds](#API_DescribeInstancePatchStates_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStates-request-InstanceIds"></a>
The ID of the managed node for which patch state information should be retrieved.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [MaxResults](#API_DescribeInstancePatchStates_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStates-request-MaxResults"></a>
The maximum number of managed nodes to return (per page).
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeInstancePatchStates_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStates-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeInstancePatchStates_ResponseSyntax"></a>

```
{
   "InstancePatchStates": [
      {
         "AvailableSecurityUpdateCount": number,
         "BaselineId": "string",
         "CriticalNonCompliantCount": number,
         "FailedCount": number,
         "InstalledCount": number,
         "InstalledOtherCount": number,
         "InstalledPendingRebootCount": number,
         "InstalledRejectedCount": number,
         "InstallOverrideList": "string",
         "InstanceId": "string",
         "LastNoRebootInstallOperationTime": number,
         "MissingCount": number,
         "NotApplicableCount": number,
         "Operation": "string",
         "OperationEndTime": number,
         "OperationStartTime": number,
         "OtherNonCompliantCount": number,
         "OwnerInformation": "string",
         "PatchGroup": "string",
         "RebootOption": "string",
         "SecurityNonCompliantCount": number,
         "SnapshotId": "string",
         "UnreportedNotApplicableCount": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeInstancePatchStates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstancePatchStates](#API_DescribeInstancePatchStates_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatchStates-response-InstancePatchStates"></a>
The high-level patch state for the requested managed nodes.
Type: Array of [InstancePatchState](API_InstancePatchState.md) objects

 ** [NextToken](#API_DescribeInstancePatchStates_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatchStates-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeInstancePatchStates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstancePatchStates_Examples"></a>

### Example
<a name="API_DescribeInstancePatchStates_Example_1"></a>

This example illustrates one usage of DescribeInstancePatchStates.

#### Sample Request
<a name="API_DescribeInstancePatchStates_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 40
X-Amz-Target: AmazonSSM.DescribeInstancePatchStates
X-Amz-Date: 20240308T202310Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "InstanceIds": [
        "i-02573cafcfEXAMPLE"
    ]
}
```

#### Sample Response
<a name="API_DescribeInstancePatchStates_Example_1_Response"></a>

```
{
    "InstancePatchStates": [
        {
            "InstanceId": "i-02573cafcfEXAMPLE",
            "PatchGroup": "mypatchgroup",
            "BaselineId": "pb-0c10e65780EXAMPLE",
            "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE",
            "CriticalNonCompliantCount": 2,
            "SecurityNonCompliantCount": 2,
            "OtherNonCompliantCount": 1,
            "InstalledCount": 123,
            "InstalledOtherCount": 334,
            "InstalledPendingRebootCount": 0,
            "InstalledRejectedCount": 0,
            "MissingCount": 1,
            "FailedCount": 2,
            "UnreportedNotApplicableCount": 11,
            "NotApplicableCount": 2063,
            "OperationStartTime": "2024-05-03T11:00:56-07:00",
            "OperationEndTime": "2024-05-03T11:01:09-07:00",
            "Operation": "Scan",
            "LastNoRebootInstallOperationTime": "2024-04-14T12:17:41-07:00",
            "RebootOption": "RebootIfNeeded"
        }
    ]
}
```

## See Also
<a name="API_DescribeInstancePatchStates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstancePatchStates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstancePatchStates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

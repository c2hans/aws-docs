---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatchStatesForPatchGroup.html
---

# DescribeInstancePatchStatesForPatchGroup
<a name="API_DescribeInstancePatchStatesForPatchGroup"></a>

Retrieves the high-level patch state for the managed nodes in the specified patch group.

## Request Syntax
<a name="API_DescribeInstancePatchStatesForPatchGroup_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Type": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PatchGroup": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInstancePatchStatesForPatchGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeInstancePatchStatesForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-request-Filters"></a>
Each entry in the array is a structure containing:
+ Key (string between 1 and 200 characters)
+ Values (array containing a single string)
+ Type (string "Equal", "NotEqual", "LessThan", "GreaterThan")
Type: Array of [InstancePatchStateFilter](API_InstancePatchStateFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

 ** [MaxResults](#API_DescribeInstancePatchStatesForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-request-MaxResults"></a>
The maximum number of patches to return (per page).
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeInstancePatchStatesForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [PatchGroup](#API_DescribeInstancePatchStatesForPatchGroup_RequestSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-request-PatchGroup"></a>
The name of the patch group for which the patch state information should be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_DescribeInstancePatchStatesForPatchGroup_ResponseSyntax"></a>

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
<a name="API_DescribeInstancePatchStatesForPatchGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstancePatchStates](#API_DescribeInstancePatchStatesForPatchGroup_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-response-InstancePatchStates"></a>
The high-level patch state for the requested managed nodes.
Type: Array of [InstancePatchState](API_InstancePatchState.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.

 ** [NextToken](#API_DescribeInstancePatchStatesForPatchGroup_ResponseSyntax) **   <a name="systemsmanager-DescribeInstancePatchStatesForPatchGroup-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeInstancePatchStatesForPatchGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilter **
The filter name isn't valid. Verify that you entered the correct name and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeInstancePatchStatesForPatchGroup_Examples"></a>

### Example
<a name="API_DescribeInstancePatchStatesForPatchGroup_Example_1"></a>

This example illustrates one usage of DescribeInstancePatchStatesForPatchGroup.

#### Sample Request
<a name="API_DescribeInstancePatchStatesForPatchGroup_Example_1_Request"></a>

```
POST / HTTP/1.1
  Host: ssm.us-east-2.amazonaws.com
  Accept-Encoding: identity
  Content-Length: 33
  X-Amz-Target: AmazonSSM.DescribeInstancePatchStatesForPatchGroup
  X-Amz-Date: 20240308T204541Z
  User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
  Content-Type: application/x-amz-json-1.1
  Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240308/us-east-2/ssm/aws4_request,
  SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

  {
    "PatchGroup": "mypatchgroup"
}
```

#### Sample Response
<a name="API_DescribeInstancePatchStatesForPatchGroup_Example_1_Response"></a>

```
{
    "InstancePatchStates": [
        {
            "InstanceId": "i-02573cafcfEXAMPLE",
            "PatchGroup": "mypatchgroup",
            "BaselineId": "pb-0c10e65780EXAMPLE",
            "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE",
            "OwnerInformation": "",
            "InstalledCount": 32,
            "InstalledOtherCount": 1,
            "InstalledPendingRebootCount": 0,
            "InstalledRejectedCount": 0,
            "MissingCount": 2,
            "FailedCount": 0,
            "UnreportedNotApplicableCount": 2671,
            "NotApplicableCount": 400,
            "OperationStartTime": "2024-08-04T11:03:50.590000-07:00",
            "OperationEndTime": "2024-08-04T11:04:21.555000-07:00",
            "Operation": "Scan",
            "RebootOption": "NoReboot",
            "CriticalNonCompliantCount": 0,
            "SecurityNonCompliantCount": 1,
            "OtherNonCompliantCount": 0
        },
        {

            "InstanceId": "i-0471e04240EXAMPLE",
            "PatchGroup": "mypatchgroup",
            "BaselineId": "pb-09ca3fb51fEXAMPLE",
            "SnapshotId": "05d8ffb0-1bbe-4812-ba2d-d9b7bEXAMPLE",
            "OwnerInformation": "",
            "InstalledCount": 45,
            "InstalledOtherCount": 3,
            "InstalledPendingRebootCount": 1,
            "InstalledRejectedCount": 0,
            "MissingCount": 2,
            "FailedCount": 1,
            "UnreportedNotApplicableCount": 3154,
            "NotApplicableCount": 321,
            "OperationStartTime": "2024-08-04T11:04:30.290000-07:00",
            "OperationEndTime": "2024-08-04T11:04:49.255000-07:00",
            "Operation": "Scan",
            "RebootOption": "NoReboot",
            "CriticalNonCompliantCount": 0,
            "SecurityNonCompliantCount": 2,
            "OtherNonCompliantCount": 1
        }
        // There may be more content here
    ]
}
```

## See Also
<a name="API_DescribeInstancePatchStatesForPatchGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeInstancePatchStatesForPatchGroup)

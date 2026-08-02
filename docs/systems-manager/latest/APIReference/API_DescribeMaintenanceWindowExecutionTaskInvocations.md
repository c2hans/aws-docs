---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutionTaskInvocations.html
---

# DescribeMaintenanceWindowExecutionTaskInvocations
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations"></a>

Retrieves the individual task executions (one per target) for a particular task run as part of a maintenance window execution.

## Request Syntax
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "TaskId": "{{string}}",
   "WindowExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-request-Filters"></a>
Optional filters used to scope down the returned task invocations. The supported filter key is `STATUS` with the corresponding values `PENDING`, `IN_PROGRESS`, `SUCCESS`, `FAILED`, `TIMED_OUT`, `CANCELLING`, and `CANCELLED`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [TaskId](#API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-request-TaskId"></a>
The ID of the specific task in the maintenance window task that should be retrieved.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

 ** [WindowExecutionId](#API_DescribeMaintenanceWindowExecutionTaskInvocations_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-request-WindowExecutionId"></a>
The ID of the maintenance window execution the task is part of.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WindowExecutionTaskInvocationIdentities": [
      {
         "EndTime": number,
         "ExecutionId": "string",
         "InvocationId": "string",
         "OwnerInformation": "string",
         "Parameters": "string",
         "StartTime": number,
         "Status": "string",
         "StatusDetails": "string",
         "TaskExecutionId": "string",
         "TaskType": "string",
         "WindowExecutionId": "string",
         "WindowTargetId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowExecutionTaskInvocations_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [WindowExecutionTaskInvocationIdentities](#API_DescribeMaintenanceWindowExecutionTaskInvocations_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTaskInvocations-response-WindowExecutionTaskInvocationIdentities"></a>
Information about the task invocation results per invocation.
Type: Array of [MaintenanceWindowExecutionTaskInvocationIdentity](API_MaintenanceWindowExecutionTaskInvocationIdentity.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowExecutionTaskInvocations.

#### Sample Request
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowExecutionTaskInvocations
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240224T233800Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240224/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 111

{
    "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef4EXAMPLE",
    "TaskId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_Example_1_Response"></a>

```
{
    "WindowExecutionTaskInvocationIdentities": [
        {
            "WindowExecutionId": "b40a588d-32a7-4ea7-9a6b-b4ef4EXAMPLE",
            "TaskExecutionId": "0c9ac961-dafd-4a94-b6c7-1bef3EXAMPLE",
            "InvocationId": "0e466033-290b-4d74-9ae0-f33e3EXAMPLE",
            "ExecutionId": "1203cf98-5a79-4ec3-97e9-12e0bEXAMPLE",
            "TaskType": "RUN_COMMAND",
            "Parameters": "{\"comment\":\"\",\"documentName\":\"AWS-ApplyPatchBaseline\",\"instanceIds\":[\"i-00ec29b21eEXAMPLE\",\"i-09911ddd90EXAMPLE\"],\"maxConcurrency\":\"1\",\"maxErrors\":\"1\",\"parameters\":{\"SnapshotId\":[\"\"],\"Operation\":[\"Install\"]},\"timeoutSeconds\":600}",
            "Status": "SUCCESS",
            "StatusDetails": "Success",
            "StartTime": "2024-08-04T11:35:35.170000-07:00",
            "EndTime": "2024-08-04T11:42:11.330000-07:00"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowExecutionTaskInvocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTaskInvocations)

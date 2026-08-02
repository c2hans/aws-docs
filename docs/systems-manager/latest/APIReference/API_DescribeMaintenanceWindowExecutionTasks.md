---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutionTasks.html
---

# DescribeMaintenanceWindowExecutionTasks
<a name="API_DescribeMaintenanceWindowExecutionTasks"></a>

For a given maintenance window execution, lists the tasks that were run.

## Request Syntax
<a name="API_DescribeMaintenanceWindowExecutionTasks_RequestSyntax"></a>

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
   "WindowExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowExecutionTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowExecutionTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-request-Filters"></a>
Optional filters used to scope down the returned tasks. The supported filter key is `STATUS` with the corresponding values `PENDING`, `IN_PROGRESS`, `SUCCESS`, `FAILED`, `TIMED_OUT`, `CANCELLING`, and `CANCELLED`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowExecutionTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowExecutionTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [WindowExecutionId](#API_DescribeMaintenanceWindowExecutionTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-request-WindowExecutionId"></a>
The ID of the maintenance window execution whose task executions should be retrieved.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowExecutionTasks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WindowExecutionTaskIdentities": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "EndTime": number,
         "StartTime": number,
         "Status": "string",
         "StatusDetails": "string",
         "TaskArn": "string",
         "TaskExecutionId": "string",
         "TaskType": "string",
         "TriggeredAlarms": [
            {
               "Name": "string",
               "State": "string"
            }
         ],
         "WindowExecutionId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowExecutionTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowExecutionTasks_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [WindowExecutionTaskIdentities](#API_DescribeMaintenanceWindowExecutionTasks_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutionTasks-response-WindowExecutionTaskIdentities"></a>
Information about the task executions.
Type: Array of [MaintenanceWindowExecutionTaskIdentity](API_MaintenanceWindowExecutionTaskIdentity.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowExecutionTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowExecutionTasks_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowExecutionTasks_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowExecutionTasks.

#### Sample Request
<a name="API_DescribeMaintenanceWindowExecutionTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowExecutionTasks
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240224T234903Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240224/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 61

{
    "WindowExecutionId": "a06e9f91-3b9c-4c3e-8bd4-246ccEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowExecutionTasks_Example_1_Response"></a>

```
{
    "WindowExecutionTaskIdentities": [
        {
            "WindowExecutionId": "a06e9f91-3b9c-4c3e-8bd4-246ccEXAMPLE",
            "TaskExecutionId": "f407ba63-998f-4b89-8467-279fcEXAMPLE",
            "Status": "SUCCESS",
            "StartTime": "2024-08-04T11:35:35.145000-07:00",
            "EndTime": "2024-08-04T11:38:09.062000-07:00",
            "TaskArn": "AWS-RunPatchBaseline",
            "TaskType": "RUN_COMMAND"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowExecutionTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutionTasks)

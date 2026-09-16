---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowTasks.html
---

# DescribeMaintenanceWindowTasks
<a name="API_DescribeMaintenanceWindowTasks"></a>

Lists the tasks in a maintenance window.

**Note**
For maintenance window tasks without a specified target, you can't supply values for `--max-errors` and `--max-concurrency`. Instead, the system inserts a placeholder value of `1`, which may be reported in the response to this command. These values don't affect the running of your task and can be ignored.

## Request Syntax
<a name="API_DescribeMaintenanceWindowTasks_RequestSyntax"></a>

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
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowTasks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-request-Filters"></a>
Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are `WindowTaskId`, `TaskArn`, `Priority`, and `TaskType`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [WindowId](#API_DescribeMaintenanceWindowTasks_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-request-WindowId"></a>
The ID of the maintenance window whose tasks should be retrieved.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowTasks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tasks": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "CutoffBehavior": "string",
         "Description": "string",
         "LoggingInfo": {
            "S3BucketName": "string",
            "S3KeyPrefix": "string",
            "S3Region": "string"
         },
         "MaxConcurrency": "string",
         "MaxErrors": "string",
         "Name": "string",
         "Priority": number,
         "ServiceRoleArn": "string",
         "Targets": [
            {
               "Key": "string",
               "Values": [ "string" ]
            }
         ],
         "TaskArn": "string",
         "TaskParameters": {
            "string" : {
               "Values": [ "string" ]
            }
         },
         "Type": "string",
         "WindowId": "string",
         "WindowTaskId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowTasks_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [Tasks](#API_DescribeMaintenanceWindowTasks_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowTasks-response-Tasks"></a>
Information about the tasks in the maintenance window.
Type: Array of [MaintenanceWindowTask](API_MaintenanceWindowTask.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowTasks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowTasks_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowTasks_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowTasks.

#### Sample Request
<a name="API_DescribeMaintenanceWindowTasks_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowTasks
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240225T004311Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240225/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 36

{
    "WindowId": "mw-0ecb1226dd7bEXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowTasks_Example_1_Response"></a>

```
{
    "Tasks": [
        {
            "WindowId": "mw-0ecb1226ddEXAMPLE",
            "WindowTaskId": "018b31c3-2d77-4b9e-bd48-c91edEXAMPLE",
            "TaskArn": "AWS-RestartEC2Instance",
            "TaskParameters": {},
            "Type": "AUTOMATION",
            "Description": "Restarting EC2 Instance for maintenance",
            "MaxConcurrency": "1",
            "MaxErrors": "1",
            "Name": "My-Automation-Example-Task",
            "Priority": 0,
            "ServiceRoleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ]
        },
        {
            "WindowId": "mw-0ecb1226ddEXAMPLE",
            "WindowTaskId": "1943dee0-0a17-4978-9bf4-3cc2fEXAMPLE",
            "TaskArn": "AWS-DisableS3BucketPublicReadWrite",
            "TaskParameters": {},
            "Type": "AUTOMATION",
            "Description": "Automation task to disable read/write access on public S3 buckets",
            "MaxConcurrency": "10",
            "MaxErrors": "5",
            "Name": "My-Disable-S3-Public-Read-Write-Access-Automation-Task",
            "Priority": 0,
            "ServiceRoleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM",
            "Targets": [
                {
                    "Key": "WindowTargetIds",
                    "Values": [
                        "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE"
                    ]
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowTasks)

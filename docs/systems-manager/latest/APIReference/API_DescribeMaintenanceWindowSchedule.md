---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowSchedule.html
---

# DescribeMaintenanceWindowSchedule
<a name="API_DescribeMaintenanceWindowSchedule"></a>

Retrieves information about upcoming executions of a maintenance window.

## Request Syntax
<a name="API_DescribeMaintenanceWindowSchedule_RequestSyntax"></a>

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
   "ResourceType": "{{string}}",
   "Targets": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "WindowId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindowSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-Filters"></a>
Filters used to limit the range of results. For example, you can limit maintenance window executions to only those scheduled before or after a certain date and time.
Type: Array of [PatchOrchestratorFilter](API_PatchOrchestratorFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [ResourceType](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-ResourceType"></a>
The type of resource you want to retrieve information about. For example, `INSTANCE`.
Type: String
Valid Values: `INSTANCE | RESOURCE_GROUP`
Required: No

 ** [Targets](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-Targets"></a>
The managed node ID or key-value pair to retrieve information about.
Type: Array of [Target](API_Target.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [WindowId](#API_DescribeMaintenanceWindowSchedule_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-request-WindowId"></a>
The ID of the maintenance window to retrieve information about.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: No

## Response Syntax
<a name="API_DescribeMaintenanceWindowSchedule_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ScheduledWindowExecutions": [
      {
         "ExecutionTime": "string",
         "Name": "string",
         "WindowId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowSchedule_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-response-NextToken"></a>
The token for the next set of items to return. (You use this token in the next call.)
Type: String

 ** [ScheduledWindowExecutions](#API_DescribeMaintenanceWindowSchedule_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowSchedule-response-ScheduledWindowExecutions"></a>
Information about maintenance window executions scheduled for the specified time range.
Type: Array of [ScheduledWindowExecution](API_ScheduledWindowExecution.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DoesNotExistException **
Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.
For information about resource quotas in AWS Systems Manager, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowSchedule_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowSchedule_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowSchedule.

#### Sample Request
<a name="API_DescribeMaintenanceWindowSchedule_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowSchedule
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
X-Amz-Date: 20240224T235938Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240224/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 36

{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowSchedule_Example_1_Response"></a>

```
{
    "NextToken": "EXAMPLE/39c3b3042cd2aEXAMPLEAKIAIOSFODNN7EXAMPLE==",
    "ScheduledWindowExecutions": [
        {
            "ExecutionTime": "2024-02-25T00:00:15.099Z",
            "Name": "MyMaintenanceWindow",
            "WindowId": "mw-0c50858d01EXAMPLE"
        },
        {
            "ExecutionTime": "2024-02-26T00:00:15.099Z",
            "Name": "MyMaintenanceWindow",
            "WindowId": "mw-0c50858d01EXAMPLE"
        },
        {
            "ExecutionTime": "2024-02-27T00:00:15.099Z",
            "Name": "MyMaintenanceWindow",
            "WindowId": "mw-0c50858d01EXAMPLE"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowSchedule)

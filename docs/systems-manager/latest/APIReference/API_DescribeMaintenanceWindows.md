---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindows.html
---

# DescribeMaintenanceWindows
<a name="API_DescribeMaintenanceWindows"></a>

Retrieves the maintenance windows in an AWS account.

## Request Syntax
<a name="API_DescribeMaintenanceWindows_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceWindows_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindows_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindows-request-Filters"></a>
Optional filters used to narrow down the scope of the returned maintenance windows. Supported filter keys are `Name` and `Enabled`. For example, `Name=MyMaintenanceWindow` and `Enabled=True`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindows_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindows-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindows_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindows-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeMaintenanceWindows_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WindowIdentities": [
      {
         "Cutoff": number,
         "Description": "string",
         "Duration": number,
         "Enabled": boolean,
         "EndDate": "string",
         "Name": "string",
         "NextExecutionTime": "string",
         "Schedule": "string",
         "ScheduleOffset": number,
         "ScheduleTimezone": "string",
         "StartDate": "string",
         "WindowId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindows_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindows_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindows-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [WindowIdentities](#API_DescribeMaintenanceWindows_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindows-response-WindowIdentities"></a>
Information about the maintenance windows.
Type: Array of [MaintenanceWindowIdentity](API_MaintenanceWindowIdentity.md) objects

## Errors
<a name="API_DescribeMaintenanceWindows_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindows_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindows_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindows.

#### Sample Request
<a name="API_DescribeMaintenanceWindows_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 2
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindows
X-Amz-Date: 20240312T202609Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "Filters": [
        {
            "Values": [
                "true"
            ],
            "Key": "Enabled"
        }
    ]
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindows_Example_1_Response"></a>

```
{
    "WindowIdentities": [
        {
            "WindowId": "mw-0c5ed765acEXAMPLE",
            "Name": "Windows-Testing-Maintenance-Window",
            "Description": "Standard maintenance windows for Test Servers",
            "Enabled": true,
            "Duration": 6,
            "Cutoff": 2,
            "Schedule": "rate(2 weeks)",
            "NextExecutionTime": "2024-02-24T23:52:15.099Z"
        },
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "Name": "Windows-Staging-Maintenance-Window",
            "Description": "Standard maintenance windows for Staging Servers",
            "Enabled": true,
            "Duration": 10,
            "Cutoff": 4,
            "Schedule": "cron(0 0 6 ? * MON *)",
            "NextExecutionTime": "2024-03-02T06:00:00.099Z"
        },
        {
            "WindowId": "mw-07f80c1841EXAMPLE",
            "Cutoff": 4,
            "Name": "Windows-Production-Maintenance-Window",
            "Description": "Standard maintenance windows for Production Servers",
            "Enabled": true,
            "Duration": 10,
            "Schedule": "cron(0 0 6 ? * WED *)",
            "NextExecutionTime": "2024-03-05T06:00:00.099Z"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindows_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindows)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindows)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

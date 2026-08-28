---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeMaintenanceWindowExecutions.html
---

# DescribeMaintenanceWindowExecutions
<a name="API_DescribeMaintenanceWindowExecutions"></a>

Lists the executions of a maintenance window. This includes information about when the maintenance window was scheduled to be active, and information about tasks registered and run with the maintenance window.

## Request Syntax
<a name="API_DescribeMaintenanceWindowExecutions_RequestSyntax"></a>

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
<a name="API_DescribeMaintenanceWindowExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeMaintenanceWindowExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-request-Filters"></a>
Each entry in the array is a structure containing:
+ Key. A string between 1 and 128 characters. Supported keys include `ExecutedBefore` and `ExecutedAfter`.
+ Values. An array of strings, each between 1 and 256 characters. Supported values are date/time strings in a valid ISO 8601 date/time format, such as `2024-11-04T05:00:00Z`.
Type: Array of [MaintenanceWindowFilter](API_MaintenanceWindowFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [MaxResults](#API_DescribeMaintenanceWindowExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeMaintenanceWindowExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [WindowId](#API_DescribeMaintenanceWindowExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-request-WindowId"></a>
The ID of the maintenance window whose executions should be retrieved.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `^mw-[0-9a-f]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceWindowExecutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "WindowExecutions": [
      {
         "EndTime": number,
         "StartTime": number,
         "Status": "string",
         "StatusDetails": "string",
         "WindowExecutionId": "string",
         "WindowId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeMaintenanceWindowExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeMaintenanceWindowExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [WindowExecutions](#API_DescribeMaintenanceWindowExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeMaintenanceWindowExecutions-response-WindowExecutions"></a>
Information about the maintenance window executions.
Type: Array of [MaintenanceWindowExecution](API_MaintenanceWindowExecution.md) objects

## Errors
<a name="API_DescribeMaintenanceWindowExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_DescribeMaintenanceWindowExecutions_Examples"></a>

### Example
<a name="API_DescribeMaintenanceWindowExecutions_Example_1"></a>

This example illustrates one usage of DescribeMaintenanceWindowExecutions.

#### Sample Request
<a name="API_DescribeMaintenanceWindowExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 36
X-Amz-Target: AmazonSSM.DescribeMaintenanceWindowExecutions
X-Amz-Date: 20240312T204551Z
User-Agent: aws-cli/1.11.180 Python/2.7.9 Windows/8 botocore/1.7.38
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240312/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE

{
    "WindowId": "mw-0c50858d01EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceWindowExecutions_Example_1_Response"></a>

```
{
    "NextToken": "AAEABbrXFUcgJpmXZxxu+AD17F+5bzlsAyqrig1EXAMPLE...pYY",
    "WindowExecutions": [
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "WindowExecutionId": "6027b513-64fe-4cf0-be7d-1191aEXAMPLE",
            "Status": "IN_PROGRESS",
            "StartTime": "2024-08-04T11:00:00.000000-07:00"
        },
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "WindowExecutionId": "ff75b750-4834-4377-8f61-b3cadEXAMPLE",
            "Status": "SUCCESS",
            "StartTime": "2024-08-03T11:00:00.000000-07:00",
            "EndTime": "2024-08-03T11:37:21.450000-07:00"
        },
        {
            "WindowId": "mw-0c50858d01EXAMPLE",
            "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE",
            "Status": "FAILED",
            "StatusDetails": "One or more tasks in the orchestration failed.",
            "StartTime": "2024-08-02T11:00:00.000000-07:00",
            "EndTime": "2024-08-02T11:22:36.190000-07:00"
        }
    ]
}
```

## See Also
<a name="API_DescribeMaintenanceWindowExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeMaintenanceWindowExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationExecutions.html
---

# DescribeAutomationExecutions
<a name="API_DescribeAutomationExecutions"></a>

Provides details about all active and terminated Automation executions.

## Request Syntax
<a name="API_DescribeAutomationExecutions_RequestSyntax"></a>

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
<a name="API_DescribeAutomationExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeAutomationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationExecutions-request-Filters"></a>
Filters used to limit the scope of executions that are requested.
Type: Array of [AutomationExecutionFilter](API_AutomationExecutionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [MaxResults](#API_DescribeAutomationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationExecutions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeAutomationExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationExecutions-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

## Response Syntax
<a name="API_DescribeAutomationExecutions_ResponseSyntax"></a>

```
{
   "AutomationExecutionMetadataList": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "AssociationId": "string",
         "AutomationExecutionId": "string",
         "AutomationExecutionStatus": "string",
         "AutomationSubtype": "string",
         "AutomationType": "string",
         "ChangeRequestName": "string",
         "CurrentAction": "string",
         "CurrentStepName": "string",
         "DocumentName": "string",
         "DocumentVersion": "string",
         "ExecutedBy": "string",
         "ExecutionEndTime": number,
         "ExecutionStartTime": number,
         "FailureMessage": "string",
         "LogFile": "string",
         "MaxConcurrency": "string",
         "MaxErrors": "string",
         "Mode": "string",
         "OpsItemId": "string",
         "Outputs": {
            "string" : [ "string" ]
         },
         "ParentAutomationExecutionId": "string",
         "ResolvedTargets": {
            "ParameterValues": [ "string" ],
            "Truncated": boolean
         },
         "Runbooks": [
            {
               "DocumentName": "string",
               "DocumentVersion": "string",
               "MaxConcurrency": "string",
               "MaxErrors": "string",
               "Parameters": {
                  "string" : [ "string" ]
               },
               "TargetLocations": [
                  {
                     "Accounts": [ "string" ],
                     "ExcludeAccounts": [ "string" ],
                     "ExecutionRoleName": "string",
                     "IncludeChildOrganizationUnits": boolean,
                     "Regions": [ "string" ],
                     "TargetLocationAlarmConfiguration": {
                        "Alarms": [
                           {
                              "Name": "string"
                           }
                        ],
                        "IgnorePollAlarmFailure": boolean
                     },
                     "TargetLocationMaxConcurrency": "string",
                     "TargetLocationMaxErrors": "string",
                     "Targets": [
                        {
                           "Key": "string",
                           "Values": [ "string" ]
                        }
                     ],
                     "TargetsMaxConcurrency": "string",
                     "TargetsMaxErrors": "string"
                  }
               ],
               "TargetMaps": [
                  {
                     "string" : [ "string" ]
                  }
               ],
               "TargetParameterName": "string",
               "Targets": [
                  {
                     "Key": "string",
                     "Values": [ "string" ]
                  }
               ]
            }
         ],
         "ScheduledTime": number,
         "Target": "string",
         "TargetLocationsURL": "string",
         "TargetMaps": [
            {
               "string" : [ "string" ]
            }
         ],
         "TargetParameterName": "string",
         "Targets": [
            {
               "Key": "string",
               "Values": [ "string" ]
            }
         ],
         "TriggeredAlarms": [
            {
               "Name": "string",
               "State": "string"
            }
         ],
         "WarningMessage": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeAutomationExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomationExecutionMetadataList](#API_DescribeAutomationExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAutomationExecutions-response-AutomationExecutionMetadataList"></a>
The list of details about each automation execution which has occurred which matches the filter specification, if any.
Type: Array of [AutomationExecutionMetadata](API_AutomationExecutionMetadata.md) objects

 ** [NextToken](#API_DescribeAutomationExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAutomationExecutions-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

## Errors
<a name="API_DescribeAutomationExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidFilterKey **
The specified key isn't valid.
HTTP Status Code: 400

 ** InvalidFilterValue **
The filter value isn't valid. Verify the value and try again.
HTTP Status Code: 400

 ** InvalidNextToken **
The specified token isn't valid.
HTTP Status Code: 400

## Examples
<a name="API_DescribeAutomationExecutions_Examples"></a>

### Example
<a name="API_DescribeAutomationExecutions_Example_1"></a>

This example illustrates one usage of DescribeAutomationExecutions.

#### Sample Request
<a name="API_DescribeAutomationExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeAutomationExecutions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T173011Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 2
```

#### Sample Response
<a name="API_DescribeAutomationExecutions_Example_1_Response"></a>

```
{
    "AutomationExecutionMetadataList": [
        {
            "AutomationExecutionId": "8a5f5be8-5d93-437a-adbb-394f7EXAMPLE",
            "AutomationExecutionStatus": "Success",
            "AutomationType": "Local",
            "DocumentName": "Example",
            "DocumentVersion": "1",
            "ExecutedBy": "arn:aws:sts::111122223333:assumed-role/Example",
            "ExecutionEndTime": 1585062669.053,
            "ExecutionStartTime": 1585061570.827,
            "LogFile": "",
            "Mode": "Auto",
            "Outputs": {},
            "ResolvedTargets": {
                "ParameterValues": [],
                "Truncated": false
            },
            "Targets": []
        }
    ]
}
```

## See Also
<a name="API_DescribeAutomationExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAutomationExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAutomationExecutions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

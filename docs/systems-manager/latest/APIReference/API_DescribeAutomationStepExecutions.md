---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeAutomationStepExecutions.html
---

# DescribeAutomationStepExecutions
<a name="API_DescribeAutomationStepExecutions"></a>

Information about all active and terminated step executions in an Automation workflow.

## Request Syntax
<a name="API_DescribeAutomationStepExecutions_RequestSyntax"></a>

```
{
   "AutomationExecutionId": "{{string}}",
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ReverseOrder": {{boolean}}
}
```

## Request Parameters
<a name="API_DescribeAutomationStepExecutions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutomationExecutionId](#API_DescribeAutomationStepExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-request-AutomationExecutionId"></a>
The Automation execution ID for which you want step execution descriptions.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

 ** [Filters](#API_DescribeAutomationStepExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-request-Filters"></a>
One or more filters to limit the number of step executions returned by the request.
Type: Array of [StepExecutionFilter](API_StepExecutionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Required: No

 ** [MaxResults](#API_DescribeAutomationStepExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-request-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [NextToken](#API_DescribeAutomationStepExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-request-NextToken"></a>
The token for the next set of items to return. (You received this token from a previous call.)
Type: String
Required: No

 ** [ReverseOrder](#API_DescribeAutomationStepExecutions_RequestSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-request-ReverseOrder"></a>
Indicates whether to list step executions in reverse order by start time. The default value is 'false'.
Type: Boolean
Required: No

## Response Syntax
<a name="API_DescribeAutomationStepExecutions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "StepExecutions": [
      {
         "Action": "string",
         "ExecutionEndTime": number,
         "ExecutionStartTime": number,
         "FailureDetails": {
            "Details": {
               "string" : [ "string" ]
            },
            "FailureStage": "string",
            "FailureType": "string"
         },
         "FailureMessage": "string",
         "Inputs": {
            "string" : "string"
         },
         "IsCritical": boolean,
         "IsEnd": boolean,
         "MaxAttempts": number,
         "NextStep": "string",
         "OnFailure": "string",
         "Outputs": {
            "string" : [ "string" ]
         },
         "OverriddenParameters": {
            "string" : [ "string" ]
         },
         "ParentStepDetails": {
            "Action": "string",
            "Iteration": number,
            "IteratorValue": "string",
            "StepExecutionId": "string",
            "StepName": "string"
         },
         "Response": "string",
         "ResponseCode": "string",
         "StepExecutionId": "string",
         "StepName": "string",
         "StepStatus": "string",
         "TargetLocation": {
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
         },
         "Targets": [
            {
               "Key": "string",
               "Values": [ "string" ]
            }
         ],
         "TimeoutSeconds": number,
         "TriggeredAlarms": [
            {
               "Name": "string",
               "State": "string"
            }
         ],
         "ValidNextSteps": [ "string" ],
         "WarningMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAutomationStepExecutions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeAutomationStepExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-response-NextToken"></a>
The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.
Type: String

 ** [StepExecutions](#API_DescribeAutomationStepExecutions_ResponseSyntax) **   <a name="systemsmanager-DescribeAutomationStepExecutions-response-StepExecutions"></a>
A list of details about the current state of all steps that make up an execution.
Type: Array of [StepExecution](API_StepExecution.md) objects

## Errors
<a name="API_DescribeAutomationStepExecutions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AutomationExecutionNotFoundException **
There is no automation execution information for the requested automation execution ID.
HTTP Status Code: 400

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
<a name="API_DescribeAutomationStepExecutions_Examples"></a>

### Example
<a name="API_DescribeAutomationStepExecutions_Example_1"></a>

This example illustrates one usage of DescribeAutomationStepExecutions.

#### Sample Request
<a name="API_DescribeAutomationStepExecutions_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.DescribeAutomationStepExecutions
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T180909Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 65

{
    "AutomationExecutionId": "8a5f5be8-5d93-437a-adbb-394f7EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeAutomationStepExecutions_Example_1_Response"></a>

```
{
    "StepExecutions": [
        {
            "Action": "aws:createImage",
            "ExecutionEndTime": 1585062668.968,
            "ExecutionStartTime": 1585061571.144,
            "Inputs": {
                "ImageDescription": "\"AMI for i-02573cafcfEXAMPLE created on 2020-03-24_14.52.51\"",
                "ImageName": "\"i-02573cafcfEXAMPLE-2020-03-24_14.52.51\"",
                "InstanceId": "\"i-02573cafcfEXAMPLE\"",
                "NoReboot": "false"
            },
            "OnFailure": "Abort",
            "Outputs": {
                "ImageId": [
                    "ami-0f4706cb37EXAMPLE"
                ],
                "ImageState": [
                    "available"
                ],
                "OutputPayload": [
                    "{\"ImageId\":\"ami-0f4706cb37EXAMPLE\",\"ImageState\":\"available\"}"
                ]
            },
            "OverriddenParameters": {},
            "StepExecutionId": "eff80946-356d-4128-97b2-6a0f5EXAMPLE",
            "StepName": "createImage",
            "StepStatus": "Success"
        }
    ]
}
```

## See Also
<a name="API_DescribeAutomationStepExecutions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/DescribeAutomationStepExecutions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DescribeAutomationStepExecutions)

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetAutomationExecution.html
---

# GetAutomationExecution
<a name="API_GetAutomationExecution"></a>

Get detailed information about a particular Automation execution.

## Request Syntax
<a name="API_GetAutomationExecution_RequestSyntax"></a>

```
{
   "AutomationExecutionId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAutomationExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AutomationExecutionId](#API_GetAutomationExecution_RequestSyntax) **   <a name="systemsmanager-GetAutomationExecution-request-AutomationExecutionId"></a>
The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation runbook is initiated.
Type: String
Length Constraints: Fixed length of 36.
Required: Yes

## Response Syntax
<a name="API_GetAutomationExecution_ResponseSyntax"></a>

```
{
   "AutomationExecution": {
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
      "ChangeRequestName": "string",
      "CurrentAction": "string",
      "CurrentStepName": "string",
      "DocumentName": "string",
      "DocumentVersion": "string",
      "ExecutedBy": "string",
      "ExecutionEndTime": number,
      "ExecutionStartTime": number,
      "FailureMessage": "string",
      "MaxConcurrency": "string",
      "MaxErrors": "string",
      "Mode": "string",
      "OpsItemId": "string",
      "Outputs": {
         "string" : [ "string" ]
      },
      "Parameters": {
         "string" : [ "string" ]
      },
      "ParentAutomationExecutionId": "string",
      "ProgressCounters": {
         "CancelledSteps": number,
         "FailedSteps": number,
         "SuccessSteps": number,
         "TimedOutSteps": number,
         "TotalSteps": number
      },
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
      ],
      "StepExecutionsTruncated": boolean,
      "Target": "string",
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
      "Variables": {
         "string" : [ "string" ]
      },
      "WarningMessage": "string"
   }
}
```

## Response Elements
<a name="API_GetAutomationExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomationExecution](#API_GetAutomationExecution_ResponseSyntax) **   <a name="systemsmanager-GetAutomationExecution-response-AutomationExecution"></a>
Detailed information about the current state of an automation execution.
Type: [AutomationExecution](API_AutomationExecution.md) object

## Errors
<a name="API_GetAutomationExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AutomationExecutionNotFoundException **
There is no automation execution information for the requested automation execution ID.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

## Examples
<a name="API_GetAutomationExecution_Examples"></a>

### Example
<a name="API_GetAutomationExecution_Example_1"></a>

This example illustrates one usage of GetAutomationExecution.

#### Sample Request
<a name="API_GetAutomationExecution_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.GetAutomationExecution
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T185532Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 65

{
    "AutomationExecutionId": "8a5f5be8-5d93-437a-adbb-394f7EXAMPLE"
}
```

#### Sample Response
<a name="API_GetAutomationExecution_Example_1_Response"></a>

```
{
    "AutomationExecution": {
        "AutomationExecutionId": "8a5f5be8-5d93-437a-adbb-394f7EXAMPLE",
        "AutomationExecutionStatus": "Success",
        "DocumentName": "CreateImage",
        "DocumentVersion": "1",
        "ExecutedBy": "arn:aws:sts::111122223333:assumed-role/Example",
        "ExecutionEndTime": 1585062669.053,
        "ExecutionStartTime": 1585061570.827,
        "Mode": "Auto",
        "Outputs": {},
        "Parameters": {
            "InstanceId": [
                "i-02573cafcfEXAMPLE"
            ]
        },
        "ResolvedTargets": {
            "ParameterValues": [],
            "Truncated": false
        },
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
        ],
        "StepExecutionsTruncated": false,
        "Targets": []
    }
}
```

## See Also
<a name="API_GetAutomationExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/GetAutomationExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/GetAutomationExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociationBatch.html
---

# CreateAssociationBatch
<a name="API_CreateAssociationBatch"></a>

Associates the specified AWS Systems Manager document (SSM document) with the specified managed nodes or targets.

When you associate a document with one or more managed nodes using IDs or tags, AWS Systems Manager Agent (SSM Agent) running on the managed node processes the document and configures the node as specified.

If you associate a document with a managed node that already has an associated document, the system returns the AssociationAlreadyExists exception.

## Request Syntax
<a name="API_CreateAssociationBatch_RequestSyntax"></a>

```
{
   "AssociationDispatchAssumeRole": "{{string}}",
   "Entries": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "{{string}}"
               }
            ],
            "IgnorePollAlarmFailure": {{boolean}}
         },
         "ApplyOnlyAtCronInterval": {{boolean}},
         "AssociationName": "{{string}}",
         "AutomationTargetParameterName": "{{string}}",
         "CalendarNames": [ "{{string}}" ],
         "ComplianceSeverity": "{{string}}",
         "DocumentVersion": "{{string}}",
         "Duration": {{number}},
         "InstanceId": "{{string}}",
         "MaxConcurrency": "{{string}}",
         "MaxErrors": "{{string}}",
         "Name": "{{string}}",
         "OutputLocation": {
            "S3Location": {
               "OutputS3BucketName": "{{string}}",
               "OutputS3KeyPrefix": "{{string}}",
               "OutputS3Region": "{{string}}"
            }
         },
         "Parameters": {
            "{{string}}" : [ "{{string}}" ]
         },
         "ScheduleExpression": "{{string}}",
         "ScheduleOffset": {{number}},
         "SyncCompliance": "{{string}}",
         "TargetLocations": [
            {
               "Accounts": [ "{{string}}" ],
               "ExcludeAccounts": [ "{{string}}" ],
               "ExecutionRoleName": "{{string}}",
               "IncludeChildOrganizationUnits": {{boolean}},
               "Regions": [ "{{string}}" ],
               "TargetLocationAlarmConfiguration": {
                  "Alarms": [
                     {
                        "Name": "{{string}}"
                     }
                  ],
                  "IgnorePollAlarmFailure": {{boolean}}
               },
               "TargetLocationMaxConcurrency": "{{string}}",
               "TargetLocationMaxErrors": "{{string}}",
               "Targets": [
                  {
                     "Key": "{{string}}",
                     "Values": [ "{{string}}" ]
                  }
               ],
               "TargetsMaxConcurrency": "{{string}}",
               "TargetsMaxErrors": "{{string}}"
            }
         ],
         "TargetMaps": [
            {
               "{{string}}" : [ "{{string}}" ]
            }
         ],
         "Targets": [
            {
               "Key": "{{string}}",
               "Values": [ "{{string}}" ]
            }
         ]
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAssociationBatch_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationDispatchAssumeRole](#API_CreateAssociationBatch_RequestSyntax) **   <a name="systemsmanager-CreateAssociationBatch-request-AssociationDispatchAssumeRole"></a>
A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, [ service-linked role for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html) will be used by default.
It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.
Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
Required: No

 ** [Entries](#API_CreateAssociationBatch_RequestSyntax) **   <a name="systemsmanager-CreateAssociationBatch-request-Entries"></a>
One or more associations.
Type: Array of [CreateAssociationBatchRequestEntry](API_CreateAssociationBatchRequestEntry.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Syntax
<a name="API_CreateAssociationBatch_ResponseSyntax"></a>

```
{
   "Failed": [
      {
         "Entry": {
            "AlarmConfiguration": {
               "Alarms": [
                  {
                     "Name": "string"
                  }
               ],
               "IgnorePollAlarmFailure": boolean
            },
            "ApplyOnlyAtCronInterval": boolean,
            "AssociationName": "string",
            "AutomationTargetParameterName": "string",
            "CalendarNames": [ "string" ],
            "ComplianceSeverity": "string",
            "DocumentVersion": "string",
            "Duration": number,
            "InstanceId": "string",
            "MaxConcurrency": "string",
            "MaxErrors": "string",
            "Name": "string",
            "OutputLocation": {
               "S3Location": {
                  "OutputS3BucketName": "string",
                  "OutputS3KeyPrefix": "string",
                  "OutputS3Region": "string"
               }
            },
            "Parameters": {
               "string" : [ "string" ]
            },
            "ScheduleExpression": "string",
            "ScheduleOffset": number,
            "SyncCompliance": "string",
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
            "Targets": [
               {
                  "Key": "string",
                  "Values": [ "string" ]
               }
            ]
         },
         "Fault": "string",
         "Message": "string"
      }
   ],
   "Successful": [
      {
         "AlarmConfiguration": {
            "Alarms": [
               {
                  "Name": "string"
               }
            ],
            "IgnorePollAlarmFailure": boolean
         },
         "ApplyOnlyAtCronInterval": boolean,
         "AssociationDispatchAssumeRole": "string",
         "AssociationId": "string",
         "AssociationName": "string",
         "AssociationVersion": "string",
         "AutomationTargetParameterName": "string",
         "CalendarNames": [ "string" ],
         "ComplianceSeverity": "string",
         "Date": number,
         "DocumentVersion": "string",
         "Duration": number,
         "InstanceId": "string",
         "LastExecutionDate": number,
         "LastSuccessfulExecutionDate": number,
         "LastUpdateAssociationDate": number,
         "MaxConcurrency": "string",
         "MaxErrors": "string",
         "Name": "string",
         "OutputLocation": {
            "S3Location": {
               "OutputS3BucketName": "string",
               "OutputS3KeyPrefix": "string",
               "OutputS3Region": "string"
            }
         },
         "Overview": {
            "AssociationStatusAggregatedCount": {
               "string" : number
            },
            "DetailedStatus": "string",
            "Status": "string"
         },
         "Parameters": {
            "string" : [ "string" ]
         },
         "ScheduleExpression": "string",
         "ScheduleOffset": number,
         "Status": {
            "AdditionalInfo": "string",
            "Date": number,
            "Message": "string",
            "Name": "string"
         },
         "SyncCompliance": "string",
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
         ]
      }
   ]
}
```

## Response Elements
<a name="API_CreateAssociationBatch_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Failed](#API_CreateAssociationBatch_ResponseSyntax) **   <a name="systemsmanager-CreateAssociationBatch-response-Failed"></a>
Information about the associations that failed.
Type: Array of [FailedCreateAssociation](API_FailedCreateAssociation.md) objects

 ** [Successful](#API_CreateAssociationBatch_ResponseSyntax) **   <a name="systemsmanager-CreateAssociationBatch-response-Successful"></a>
Information about the associations that succeeded.
Type: Array of [AssociationDescription](API_AssociationDescription.md) objects

## Errors
<a name="API_CreateAssociationBatch_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationLimitExceeded **
You can have at most 2,000 active associations.
HTTP Status Code: 400

 ** DuplicateInstanceId **
You can't specify a managed node ID in more than one association.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidDocumentVersion **
The document version isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** InvalidOutputLocation **
The output location isn't valid or doesn't exist.
HTTP Status Code: 400

 ** InvalidParameters **
You must specify values for all required parameters in the AWS Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.
HTTP Status Code: 400

 ** InvalidSchedule **
The schedule is invalid. Verify your cron or rate expression and try again.
HTTP Status Code: 400

 ** InvalidTarget **
The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.
HTTP Status Code: 400

 ** InvalidTargetMaps **
TargetMap parameter isn't valid.
HTTP Status Code: 400

 ** UnsupportedPlatformType **
The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.
HTTP Status Code: 400

## Examples
<a name="API_CreateAssociationBatch_Examples"></a>

### Example
<a name="API_CreateAssociationBatch_Example_1"></a>

This example illustrates one usage of CreateAssociationBatch.

#### Sample Request
<a name="API_CreateAssociationBatch_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.CreateAssociationBatch
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240324T142446Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240324/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 151

{
    "Entries": [
        {
            "InstanceId": "i-0471e04240EXAMPLE",
            "Name": "AWS-UpdateSSMAgent"
        },
        {
            "InstanceId": "i-07782c72faEXAMPLE",
            "Name": "AWS-UpdateSSMAgent"
        }
    ]
}
```

#### Sample Response
<a name="API_CreateAssociationBatch_Example_1_Response"></a>

```
{
    "Failed": [],
    "Successful": [
        {
            "ApplyOnlyAtCronInterval": false,
            "AssociationId": "33858bec-0c55-4547-a054-eb5fcEXAMPLE",
            "AssociationVersion": "1",
            "Date": 1585059887.692,
            "DocumentVersion": "$DEFAULT",
            "InstanceId": "i-0471e04240EXAMPLE",
            "LastUpdateAssociationDate": 1585059887.692,
            "Name": "AWS-UpdateSSMAgent",
            "Overview": {
                "DetailedStatus": "Creating",
                "Status": "Pending"
            },
            "Status": {
                "Date": 1585059887.692,
                "Message": "Associated with AWS-UpdateSSMAgent",
                "Name": "Associated"
            },
            "Targets": [
                {
                    "Key": "InstanceIds",
                    "Values": [
                        "i-0471e04240EXAMPLE"
                    ]
                }
            ]
        },
        {
            "ApplyOnlyAtCronInterval": false,
            "AssociationId": "e0e0a062-3dcb-4b3e-bb2b-d01b4EXAMPLE",
            "AssociationVersion": "1",
            "Date": 1585059887.726,
            "DocumentVersion": "$DEFAULT",
            "InstanceId": "i-07782c72faEXAMPLE",
            "LastUpdateAssociationDate": 1585059887.726,
            "Name": "AWS-UpdateSSMAgent",
            "Overview": {
                "DetailedStatus": "Creating",
                "Status": "Pending"
            },
            "Status": {
                "Date": 1585059887.726,
                "Message": "Associated with AWS-UpdateSSMAgent",
                "Name": "Associated"
            },
            "Targets": [
                {
                    "Key": "InstanceIds",
                    "Values": [
                        "i-07782c72faEXAMPLE"
                    ]
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_CreateAssociationBatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/CreateAssociationBatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CreateAssociationBatch)

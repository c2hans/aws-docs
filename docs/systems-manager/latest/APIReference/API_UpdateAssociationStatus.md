---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociationStatus.html
---

# UpdateAssociationStatus
<a name="API_UpdateAssociationStatus"></a>

Updates the status of the AWS Systems Manager document (SSM document) associated with the specified managed node.

 `UpdateAssociationStatus` is primarily used by the AWS Systems Manager Agent (SSM Agent) to report status updates about your associations and is only used for associations created with the `InstanceId` legacy parameter.

## Request Syntax
<a name="API_UpdateAssociationStatus_RequestSyntax"></a>

```
{
   "AssociationStatus": {
      "AdditionalInfo": "{{string}}",
      "Date": {{number}},
      "Message": "{{string}}",
      "Name": "{{string}}"
   },
   "InstanceId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAssociationStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociationStatus](#API_UpdateAssociationStatus_RequestSyntax) **   <a name="systemsmanager-UpdateAssociationStatus-request-AssociationStatus"></a>
The association status.
Type: [AssociationStatus](API_AssociationStatus.md) object
Required: Yes

 ** [InstanceId](#API_UpdateAssociationStatus_RequestSyntax) **   <a name="systemsmanager-UpdateAssociationStatus-request-InstanceId"></a>
The managed node ID.
Type: String
Pattern: `(^i-(\w{8}|\w{17})$)|(^mi-\w{17}$)`
Required: Yes

 ** [Name](#API_UpdateAssociationStatus_RequestSyntax) **   <a name="systemsmanager-UpdateAssociationStatus-request-Name"></a>
The name of the SSM document.
Type: String
Pattern: `^[a-zA-Z0-9_\-.:/]{3,128}$`
Required: Yes

## Response Syntax
<a name="API_UpdateAssociationStatus_ResponseSyntax"></a>

```
{
   "AssociationDescription": {
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
}
```

## Response Elements
<a name="API_UpdateAssociationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociationDescription](#API_UpdateAssociationStatus_ResponseSyntax) **   <a name="systemsmanager-UpdateAssociationStatus-response-AssociationDescription"></a>
Information about the association.
Type: [AssociationDescription](API_AssociationDescription.md) object

## Errors
<a name="API_UpdateAssociationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssociationDoesNotExist **
The specified association doesn't exist.
HTTP Status Code: 400

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidDocument **
The specified SSM document doesn't exist.
 ** Message **
The SSM document doesn't exist or the document isn't available to the user. This exception can be issued by various API operations.
HTTP Status Code: 400

 ** InvalidInstanceId **
The following problems can cause this exception:
+ You don't have permission to access the managed node.
+  AWS Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.
+ SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.
+ The managed node isn't in a valid state. Valid states are: `Running`, `Pending`, `Stopped`, and `Stopping`. Invalid states are: `Shutting-down` and `Terminated`.
HTTP Status Code: 400

 ** StatusUnchanged **
The updated status is the same as the current status.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAssociationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateAssociationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateAssociationStatus)

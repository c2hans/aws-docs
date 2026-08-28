---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateRestoreTestingPlan.html
---

# UpdateRestoreTestingPlan
<a name="API_UpdateRestoreTestingPlan"></a>

This request will send changes to your specified restore testing plan. `RestoreTestingPlanName` cannot be updated after it is created.

 `RecoveryPointSelection` can contain:
+  `Algorithm`
+  `ExcludeVaults`
+  `IncludeVaults`
+  `RecoveryPointTypes`
+  `SelectionWindowDays`

## Request Syntax
<a name="API_UpdateRestoreTestingPlan_RequestSyntax"></a>

```
PUT /restore-testing/plans/{{RestoreTestingPlanName}} HTTP/1.1
Content-type: application/json

{
   "RestoreTestingPlan": {
      "RecoveryPointSelection": {
         "Algorithm": "{{string}}",
         "ExcludeVaults": [ "{{string}}" ],
         "IncludeVaults": [ "{{string}}" ],
         "RecoveryPointTypes": [ "{{string}}" ],
         "SelectionWindowDays": {{number}}
      },
      "ScheduleExpression": "{{string}}",
      "ScheduleExpressionTimezone": "{{string}}",
      "StartWindowHours": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_UpdateRestoreTestingPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [RestoreTestingPlanName](#API_UpdateRestoreTestingPlan_RequestSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-request-uri-RestoreTestingPlanName"></a>
The name of the restore testing plan name.
Required: Yes

## Request Body
<a name="API_UpdateRestoreTestingPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [RestoreTestingPlan](#API_UpdateRestoreTestingPlan_RequestSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-request-RestoreTestingPlan"></a>
Specifies the body of a restore testing plan.
Type: [RestoreTestingPlanForUpdate](API_RestoreTestingPlanForUpdate.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateRestoreTestingPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "RestoreTestingPlanArn": "string",
   "RestoreTestingPlanName": "string",
   "UpdateTime": number
}
```

## Response Elements
<a name="API_UpdateRestoreTestingPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_UpdateRestoreTestingPlan_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-response-CreationTime"></a>
The time the resource testing plan was created.
Type: Timestamp

 ** [RestoreTestingPlanArn](#API_UpdateRestoreTestingPlan_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-response-RestoreTestingPlanArn"></a>
Unique ARN (Amazon Resource Name) of the restore testing plan.
Type: String

 ** [RestoreTestingPlanName](#API_UpdateRestoreTestingPlan_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-response-RestoreTestingPlanName"></a>
The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.
Type: String

 ** [UpdateTime](#API_UpdateRestoreTestingPlan_ResponseSyntax) **   <a name="Backup-UpdateRestoreTestingPlan-response-UpdateTime"></a>
The time the update completed for the restore testing plan.
Type: Timestamp

## Errors
<a name="API_UpdateRestoreTestingPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
 AWS Backup can't perform the action that you requested until it finishes performing a previous action. Try again later.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_UpdateRestoreTestingPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateRestoreTestingPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateRestoreTestingPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

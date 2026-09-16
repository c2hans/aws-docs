---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_UpdateReportPlan.html
---

# UpdateReportPlan
<a name="API_UpdateReportPlan"></a>

Updates the specified report plan.

## Request Syntax
<a name="API_UpdateReportPlan_RequestSyntax"></a>

```
PUT /audit/report-plans/{{reportPlanName}} HTTP/1.1
Content-type: application/json

{
   "IdempotencyToken": "{{string}}",
   "ReportDeliveryChannel": {
      "Formats": [ "{{string}}" ],
      "S3BucketName": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "ReportPlanDescription": "{{string}}",
   "ReportSetting": {
      "Accounts": [ "{{string}}" ],
      "FrameworkArns": [ "{{string}}" ],
      "NumberOfFrameworks": {{number}},
      "OrganizationUnits": [ "{{string}}" ],
      "Regions": [ "{{string}}" ],
      "ReportTemplate": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateReportPlan_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reportPlanName](#API_UpdateReportPlan_RequestSyntax) **   <a name="Backup-UpdateReportPlan-request-uri-ReportPlanName"></a>
The unique name of the report plan. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_UpdateReportPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdempotencyToken](#API_UpdateReportPlan_RequestSyntax) **   <a name="Backup-UpdateReportPlan-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `UpdateReportPlanInput`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

 ** [ReportDeliveryChannel](#API_UpdateReportPlan_RequestSyntax) **   <a name="Backup-UpdateReportPlan-request-ReportDeliveryChannel"></a>
The information about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
Type: [ReportDeliveryChannel](API_ReportDeliveryChannel.md) object
Required: No

 ** [ReportPlanDescription](#API_UpdateReportPlan_RequestSyntax) **   <a name="Backup-UpdateReportPlan-request-ReportPlanDescription"></a>
An optional description of the report plan with a maximum 1,024 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [ReportSetting](#API_UpdateReportPlan_RequestSyntax) **   <a name="Backup-UpdateReportPlan-request-ReportSetting"></a>
The report template for the report. Reports are built using a report template. The report templates are:
 `RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`
If the report template is `RESOURCE_COMPLIANCE_REPORT` or `CONTROL_COMPLIANCE_REPORT`, this API resource also describes the report coverage by AWS Regions and frameworks.
Type: [ReportSetting](API_ReportSetting.md) object
Required: No

## Response Syntax
<a name="API_UpdateReportPlan_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": number,
   "ReportPlanArn": "string",
   "ReportPlanName": "string"
}
```

## Response Elements
<a name="API_UpdateReportPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_UpdateReportPlan_ResponseSyntax) **   <a name="Backup-UpdateReportPlan-response-CreationTime"></a>
The date and time that a report plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ReportPlanArn](#API_UpdateReportPlan_ResponseSyntax) **   <a name="Backup-UpdateReportPlan-response-ReportPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String

 ** [ReportPlanName](#API_UpdateReportPlan_ResponseSyntax) **   <a name="Backup-UpdateReportPlan-response-ReportPlanName"></a>
The unique name of the report plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

## Errors
<a name="API_UpdateReportPlan_Errors"></a>

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
<a name="API_UpdateReportPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/UpdateReportPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/UpdateReportPlan)

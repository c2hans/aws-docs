---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CreateReportPlan.html
---

# CreateReportPlan
<a name="API_CreateReportPlan"></a>

Creates a report plan. A report plan is a document that contains information about the contents of the report and where AWS Backup will deliver it.

If you call `CreateReportPlan` with a plan that already exists, you receive an `AlreadyExistsException` exception.

## Request Syntax
<a name="API_CreateReportPlan_RequestSyntax"></a>

```
POST /audit/report-plans HTTP/1.1
Content-type: application/json

{
   "IdempotencyToken": "{{string}}",
   "ReportDeliveryChannel": {
      "Formats": [ "{{string}}" ],
      "S3BucketName": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   },
   "ReportPlanDescription": "{{string}}",
   "ReportPlanName": "{{string}}",
   "ReportPlanTags": {
      "{{string}}" : "{{string}}"
   },
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
<a name="API_CreateReportPlan_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReportPlan_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdempotencyToken](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `CreateReportPlanInput`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

 ** [ReportDeliveryChannel](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-ReportDeliveryChannel"></a>
A structure that contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
Type: [ReportDeliveryChannel](API_ReportDeliveryChannel.md) object
Required: Yes

 ** [ReportPlanDescription](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-ReportPlanDescription"></a>
An optional description of the report plan with a maximum of 1,024 characters.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** [ReportPlanName](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-ReportPlanName"></a>
The unique name of the report plan. The name must be between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (\_).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

 ** [ReportPlanTags](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-ReportPlanTags"></a>
The tags to assign to the report plan.
Type: String to string map
Required: No

 ** [ReportSetting](#API_CreateReportPlan_RequestSyntax) **   <a name="Backup-CreateReportPlan-request-ReportSetting"></a>
Identifies the report template for the report. Reports are built using a report template. The report templates are:
 `RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT `
If the report template is `RESOURCE_COMPLIANCE_REPORT` or `CONTROL_COMPLIANCE_REPORT`, this API resource also describes the report coverage by AWS Regions and frameworks.
Type: [ReportSetting](API_ReportSetting.md) object
Required: Yes

## Response Syntax
<a name="API_CreateReportPlan_ResponseSyntax"></a>

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
<a name="API_CreateReportPlan_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_CreateReportPlan_ResponseSyntax) **   <a name="Backup-CreateReportPlan-response-CreationTime"></a>
The date and time a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp

 ** [ReportPlanArn](#API_CreateReportPlan_ResponseSyntax) **   <a name="Backup-CreateReportPlan-response-ReportPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.
Type: String

 ** [ReportPlanName](#API_CreateReportPlan_ResponseSyntax) **   <a name="Backup-CreateReportPlan-response-ReportPlanName"></a>
The unique name of the report plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

## Errors
<a name="API_CreateReportPlan_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The required resource already exists.
 ** Arn **

 ** Context **

 ** CreatorRequestId **

 ** Type **

HTTP Status Code: 400

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** LimitExceededException **
A limit in the request has been exceeded; for example, a maximum number of items allowed in a request.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_CreateReportPlan_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/CreateReportPlan)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CreateReportPlan)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

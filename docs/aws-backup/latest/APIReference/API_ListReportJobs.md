---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListReportJobs.html
---

# ListReportJobs
<a name="API_ListReportJobs"></a>

Returns details about your report jobs.

## Request Syntax
<a name="API_ListReportJobs_RequestSyntax"></a>

```
GET /audit/report-jobs?CreationAfter={{ByCreationAfter}}&CreationBefore={{ByCreationBefore}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&ReportPlanName={{ByReportPlanName}}&Status={{ByStatus}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ByCreationAfter](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-ByCreationAfter"></a>
Returns only report jobs that were created after the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.

 ** [ByCreationBefore](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-ByCreationBefore"></a>
Returns only report jobs that were created before the date and time specified in Unix format and Coordinated Universal Time (UTC). For example, the value 1516925490 represents Friday, January 26, 2018 12:11:30 AM.

 ** [ByReportPlanName](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-ByReportPlanName"></a>
Returns only report jobs with the specified report plan name.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

 ** [ByStatus](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-ByStatus"></a>
Returns only report jobs that are in the specified status. The statuses are:
 `CREATED | RUNNING | COMPLETED | FAILED | COMPLETED_WITH_ISSUES`
 Please note that only scanning jobs finish with state completed with issues. For backup jobs this is a console interpretation of a job that finishes in completed state and has a status message.

 ** [MaxResults](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-MaxResults"></a>
The number of desired results from 1 to 1000. Optional. If unspecified, the query will return 1 MB of data.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListReportJobs_RequestSyntax) **   <a name="Backup-ListReportJobs-request-uri-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.

## Request Body
<a name="API_ListReportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ReportJobs": [
      {
         "CompletionTime": number,
         "CreationTime": number,
         "ReportDestination": {
            "S3BucketName": "string",
            "S3Keys": [ "string" ]
         },
         "ReportJobId": "string",
         "ReportPlanArn": "string",
         "ReportTemplate": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListReportJobs_ResponseSyntax) **   <a name="Backup-ListReportJobs-response-NextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String

 ** [ReportJobs](#API_ListReportJobs_ResponseSyntax) **   <a name="Backup-ListReportJobs-response-ReportJobs"></a>
Details about your report jobs in JSON format.
Type: Array of [ReportJob](API_ReportJob.md) objects

## Errors
<a name="API_ListReportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
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
<a name="API_ListReportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/ListReportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ListReportJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

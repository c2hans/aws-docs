---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_GetAssessmentReport.html
---

# GetAssessmentReport
<a name="API_GetAssessmentReport"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for (Amazon Inspector Classic). After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

Produces an assessment report that includes detailed and comprehensive results of a specified assessment run.

## Request Syntax
<a name="API_GetAssessmentReport_RequestSyntax"></a>

```
{
   "assessmentRunArn": "{{string}}",
   "reportFileFormat": "{{string}}",
   "reportType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAssessmentReport_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [assessmentRunArn](#API_GetAssessmentReport_RequestSyntax) **   <a name="Inspector-GetAssessmentReport-request-assessmentRunArn"></a>
The ARN that specifies the assessment run for which you want to generate a report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [reportFileFormat](#API_GetAssessmentReport_RequestSyntax) **   <a name="Inspector-GetAssessmentReport-request-reportFileFormat"></a>
Specifies the file format (html or pdf) of the assessment report that you want to generate.
Type: String
Valid Values: `HTML | PDF`
Required: Yes

 ** [reportType](#API_GetAssessmentReport_RequestSyntax) **   <a name="Inspector-GetAssessmentReport-request-reportType"></a>
Specifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see [Assessment Reports](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html).
Type: String
Valid Values: `FINDING | FULL`
Required: Yes

## Response Syntax
<a name="API_GetAssessmentReport_ResponseSyntax"></a>

```
{
   "status": "string",
   "url": "string"
}
```

## Response Elements
<a name="API_GetAssessmentReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [status](#API_GetAssessmentReport_ResponseSyntax) **   <a name="Inspector-GetAssessmentReport-response-status"></a>
Specifies the status of the request to generate an assessment report.
Type: String
Valid Values: `WORK_IN_PROGRESS | FAILED | COMPLETED`

 ** [url](#API_GetAssessmentReport_ResponseSyntax) **   <a name="Inspector-GetAssessmentReport-response-url"></a>
Specifies the URL where you can find the generated assessment report. This parameter is only returned if the report is successfully generated.
Type: String
Length Constraints: Maximum length of 2048.

## Errors
<a name="API_GetAssessmentReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AssessmentRunInProgressException **
You cannot perform a specified action if an assessment run is currently in progress.
 ** assessmentRunArns **
The ARNs of the assessment runs that are currently in progress.
 ** assessmentRunArnsTruncated **
Boolean value that indicates whether the ARN list of the assessment runs is truncated.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** InternalException **
Internal server error.
 ** canRetry **
You can immediately retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 500

 ** InvalidInputException **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** NoSuchEntityException **
The request was rejected because it referenced an entity that does not exist. The error code describes the entity.
 ** canRetry **
You can immediately retry your request.
 ** errorCode **
Code that indicates the type of error that is generated.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** ServiceTemporarilyUnavailableException **
The serice is temporary unavailable.
 ** canRetry **
You can wait and then retry your request.
 ** message **
Details of the exception error.
HTTP Status Code: 400

 ** UnsupportedFeatureException **
Used by the [GetAssessmentReport](#API_GetAssessmentReport) API. The request was rejected because you tried to generate a report for an assessment run that existed before reporting was supported in Amazon Inspector. You can only generate reports for assessment runs that took place or will take place after generating reports in Amazon Inspector Classic became available.
HTTP Status Code: 400

## See Also
<a name="API_GetAssessmentReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector-2016-02-16/GetAssessmentReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/GetAssessmentReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Inspector Classic. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

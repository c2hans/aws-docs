---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetDeclarativePoliciesReportSummary.html
---

# GetDeclarativePoliciesReportSummary
<a name="API_GetDeclarativePoliciesReportSummary"></a>

Retrieves a summary of the account status report.

To view the full report, download it from the Amazon S3 bucket where it was saved. Reports are accessible only when they have the `complete` status. Reports with other statuses (`running`, `cancelled`, or `error`) are not available in the S3 bucket. For more information about downloading objects from an S3 bucket, see [Downloading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the *Amazon Simple Storage Service User Guide*.

For more information, see [Generating the account status report for declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_status-report.html) in the * AWS Organizations User Guide*.

## Request Parameters
<a name="API_GetDeclarativePoliciesReportSummary_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ReportId**
The ID of the report.
Type: String
Required: Yes

## Response Elements
<a name="API_GetDeclarativePoliciesReportSummary_ResponseElements"></a>

The following elements are returned by the service.

 **attributeSummarySet**
The attributes described in the report.
Type: Array of [AttributeSummary](API_AttributeSummary.md) objects

 **endTime**
The time when the report generation ended.
Type: Timestamp

 **numberOfAccounts**
The total number of accounts associated with the specified `targetId`.
Type: Integer

 **numberOfFailedAccounts**
The number of accounts where attributes could not be retrieved in any Region.
Type: Integer

 **reportId**
The ID of the report.
Type: String

 **requestId**
The ID of the request.
Type: String

 **s3Bucket**
The name of the Amazon S3 bucket where the report is located.
Type: String

 **s3Prefix**
The prefix for your S3 object.
Type: String

 **startTime**
The time when the report generation started.
Type: Timestamp

 **targetId**
The root ID, organizational unit ID, or account ID.
Format:
+ For root: `r-ab12`
+ For OU: `ou-ab12-cdef1234`
+ For account: `123456789012`
Type: String

## Errors
<a name="API_GetDeclarativePoliciesReportSummary_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetDeclarativePoliciesReportSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetDeclarativePoliciesReportSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

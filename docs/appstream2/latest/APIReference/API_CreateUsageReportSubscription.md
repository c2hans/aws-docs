---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateUsageReportSubscription.html
---

# CreateUsageReportSubscription
<a name="API_CreateUsageReportSubscription"></a>

Creates a usage report subscription. Usage reports are generated daily.

## Response Syntax
<a name="API_CreateUsageReportSubscription_ResponseSyntax"></a>

```
{
   "S3BucketName": "string",
   "Schedule": "string"
}
```

## Response Elements
<a name="API_CreateUsageReportSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [S3BucketName](#API_CreateUsageReportSubscription_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateUsageReportSubscription-response-S3BucketName"></a>
The Amazon S3 bucket where generated reports are stored.
If you enabled on-instance session scripts and Amazon S3 logging for your session script configuration, WorkSpaces Applications created an S3 bucket to store the script output. The bucket is unique to your account and Region. When you enable usage reporting in this case, WorkSpaces Applications uses the same bucket to store your usage reports. If you haven't already enabled on-instance session scripts, when you enable usage reports, WorkSpaces Applications creates a new S3 bucket.
Type: String
Length Constraints: Minimum length of 1.

 ** [Schedule](#API_CreateUsageReportSubscription_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateUsageReportSubscription-response-Schedule"></a>
The schedule for generating usage reports.
Type: String
Valid Values: `DAILY`

## Errors
<a name="API_CreateUsageReportSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateUsageReportSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateUsageReportSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateUsageReportSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_JobLogs.html
---

# JobLogs
<a name="API_JobLogs"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Contains job logs. Whenever a Snow device is used to import data into or export data out of Amazon S3, you'll have the option of downloading a PDF job report. Job logs are returned as a part of the response syntax of the `DescribeJob` action in the `JobMetadata` data type. The job logs can be accessed for up to 60 minutes after this request has been made. To access any of the job logs after 60 minutes have passed, you'll have to make another call to the `DescribeJob` action.

For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snow device for your job part is being delivered to you.

The job report provides you insight into the state of your Amazon S3 data transfer. The report includes details about your job or job part for your records.

For deeper visibility into the status of your transferred objects, you can look at the two associated logs: a success log and a failure log. The logs are saved in comma-separated value (CSV) format, and the name of each log includes the ID of the job or job part that the log describes.

## Contents
<a name="API_JobLogs_Contents"></a>

 ** JobCompletionReportURI **   <a name="Snowball-Type-JobLogs-JobCompletionReportURI"></a>
A link to an Amazon S3 presigned URL where the job completion report is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** JobFailureLogURI **   <a name="Snowball-Type-JobLogs-JobFailureLogURI"></a>
A link to an Amazon S3 presigned URL where the job failure log is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** JobSuccessLogURI **   <a name="Snowball-Type-JobLogs-JobSuccessLogURI"></a>
A link to an Amazon S3 presigned URL where the job success log is located.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_JobLogs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/JobLogs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/JobLogs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/JobLogs)

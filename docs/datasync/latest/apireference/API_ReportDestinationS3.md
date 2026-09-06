---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ReportDestinationS3.html
---

# ReportDestinationS3
<a name="API_ReportDestinationS3"></a>

Specifies the Amazon S3 bucket where DataSync uploads your [task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).

## Contents
<a name="API_ReportDestinationS3_Contents"></a>

 ** BucketAccessRoleArn **   <a name="DataSync-Type-ReportDestinationS3-BucketAccessRoleArn"></a>
Specifies the Amazon Resource Name (ARN) of the IAM policy that allows DataSync to upload a task report to your S3 bucket. For more information, see [Allowing DataSync to upload a task report to an Amazon S3 bucket](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
Required: Yes

 ** S3BucketArn **   <a name="DataSync-Type-ReportDestinationS3-S3BucketArn"></a>
Specifies the ARN of the S3 bucket where DataSync uploads your report.
Type: String
Length Constraints: Maximum length of 268.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]{12}:accesspoint[/:][a-zA-Z0-9\-.]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:][a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:::[a-zA-Z0-9.\-_]{1,255}$`
Required: Yes

 ** Subdirectory **   <a name="DataSync-Type-ReportDestinationS3-Subdirectory"></a>
Specifies a bucket prefix for your report.
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
Required: No

## See Also
<a name="API_ReportDestinationS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ReportDestinationS3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ReportDestinationS3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ReportDestinationS3)

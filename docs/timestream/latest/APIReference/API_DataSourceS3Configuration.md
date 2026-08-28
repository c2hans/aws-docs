---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_DataSourceS3Configuration.html
---

# DataSourceS3Configuration
<a name="API_DataSourceS3Configuration"></a>

## Contents
<a name="API_DataSourceS3Configuration_Contents"></a>

 ** BucketName **   <a name="timestream-Type-DataSourceS3Configuration-BucketName"></a>
The bucket name of the customer S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: Yes

 ** ObjectKeyPrefix **   <a name="timestream-Type-DataSourceS3Configuration-ObjectKeyPrefix"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`
Required: No

## See Also
<a name="API_DataSourceS3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/DataSourceS3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/DataSourceS3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/DataSourceS3Configuration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

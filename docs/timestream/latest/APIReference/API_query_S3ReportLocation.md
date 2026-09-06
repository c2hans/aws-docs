---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_S3ReportLocation.html
---

# S3ReportLocation
<a name="API_query_S3ReportLocation"></a>

 S3 report location for the scheduled query run.

## Contents
<a name="API_query_S3ReportLocation_Contents"></a>

 ** BucketName **   <a name="timestream-Type-query_S3ReportLocation-BucketName"></a>
 S3 bucket name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
Required: No

 ** ObjectKey **   <a name="timestream-Type-query_S3ReportLocation-ObjectKey"></a>
S3 key.
Type: String
Required: No

## See Also
<a name="API_query_S3ReportLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/S3ReportLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/S3ReportLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/S3ReportLocation)

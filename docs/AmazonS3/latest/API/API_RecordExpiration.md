---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_RecordExpiration.html
---

# RecordExpiration
<a name="API_RecordExpiration"></a>

 The journal table record expiration settings for a journal table in an S3 Metadata configuration.

## Contents
<a name="API_RecordExpiration_Contents"></a>

 ** Expiration **   <a name="AmazonS3-Type-RecordExpiration-Expiration"></a>
 Specifies whether journal table record expiration is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

 ** Days **   <a name="AmazonS3-Type-RecordExpiration-Days"></a>
 If you enable journal table record expiration, you can set the number of days to retain your journal table records. Journal table records must be retained for a minimum of 7 days. To set this value, specify any whole number from `7` to `2147483647`. For example, to retain your journal table records for one year, set this value to `365`.
Type: Integer
Required: No

## See Also
<a name="API_RecordExpiration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RecordExpiration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RecordExpiration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RecordExpiration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

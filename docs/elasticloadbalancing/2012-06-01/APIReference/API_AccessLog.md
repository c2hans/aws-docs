---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_AccessLog.html
---

# AccessLog
<a name="API_AccessLog"></a>

Information about the `AccessLog` attribute.

## Contents
<a name="API_AccessLog_Contents"></a>

 ** Enabled **
Specifies whether access logs are enabled for the load balancer.
Type: Boolean
Required: Yes

 ** EmitInterval **
The interval for publishing the access logs. You can specify an interval of either 5 minutes or 60 minutes.
Default: 60 minutes
Type: Integer
Required: No

 ** S3BucketName **
The name of the Amazon S3 bucket where the access logs are stored.
Type: String
Required: No

 ** S3BucketPrefix **
The logical hierarchy you created for your Amazon S3 bucket, for example `my-bucket-prefix/prod`. If the prefix is not provided, the log is placed at the root level of the bucket.
Type: String
Required: No

## See Also
<a name="API_AccessLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/AccessLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/AccessLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/AccessLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

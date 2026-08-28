---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElbLoadBalancerAccessLog.html
---

# AwsElbLoadBalancerAccessLog
<a name="API_AwsElbLoadBalancerAccessLog"></a>

Contains information about the access log configuration for the load balancer.

## Contents
<a name="API_AwsElbLoadBalancerAccessLog_Contents"></a>

 ** EmitInterval **   <a name="securityhub-Type-AwsElbLoadBalancerAccessLog-EmitInterval"></a>
The interval in minutes for publishing the access logs.
You can publish access logs either every 5 minutes or every 60 minutes.
Type: Integer
Required: No

 ** Enabled **   <a name="securityhub-Type-AwsElbLoadBalancerAccessLog-Enabled"></a>
Indicates whether access logs are enabled for the load balancer.
Type: Boolean
Required: No

 ** S3BucketName **   <a name="securityhub-Type-AwsElbLoadBalancerAccessLog-S3BucketName"></a>
The name of the S3 bucket where the access logs are stored.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3BucketPrefix **   <a name="securityhub-Type-AwsElbLoadBalancerAccessLog-S3BucketPrefix"></a>
The logical hierarchy that was created for the S3 bucket.
If a prefix is not provided, the log is placed at the root level of the bucket.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElbLoadBalancerAccessLog_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElbLoadBalancerAccessLog)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElbLoadBalancerAccessLog)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElbLoadBalancerAccessLog)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

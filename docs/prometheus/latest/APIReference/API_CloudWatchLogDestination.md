---
source_url: https://docs.aws.amazon.com/prometheus/latest/APIReference/API_CloudWatchLogDestination.html
---

# CloudWatchLogDestination
<a name="API_CloudWatchLogDestination"></a>

Configuration details for logging to CloudWatch Logs.

## Contents
<a name="API_CloudWatchLogDestination_Contents"></a>

 ** logGroupArn **   <a name="prometheus-Type-CloudWatchLogDestination-logGroupArn"></a>
The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.
Type: String
Pattern: `arn:aws[a-z0-9-]*:logs:[a-z0-9-]+:[0-9]{12}:log-group:[A-Za-z0-9\.\-\_\#/]{1,512}\:\*`
Required: Yes

## See Also
<a name="API_CloudWatchLogDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amp-2020-08-01/CloudWatchLogDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amp-2020-08-01/CloudWatchLogDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amp-2020-08-01/CloudWatchLogDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

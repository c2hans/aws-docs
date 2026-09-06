---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CloudWatchLogsLogGroupArnConfigDetails.html
---

# CloudWatchLogsLogGroupArnConfigDetails
<a name="API_CloudWatchLogsLogGroupArnConfigDetails"></a>

 The Amazon Resource Name (ARN) and other details of the Amazon CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

## Contents
<a name="API_CloudWatchLogsLogGroupArnConfigDetails_Contents"></a>

 ** CloudWatchLogsLogGroupArn **   <a name="securityhub-Type-CloudWatchLogsLogGroupArnConfigDetails-CloudWatchLogsLogGroupArn"></a>
 The ARN of the CloudWatch Logs log group that Route 53 is publishing logs to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** HostedZoneId **   <a name="securityhub-Type-CloudWatchLogsLogGroupArnConfigDetails-HostedZoneId"></a>
 The ID of the hosted zone that CloudWatch Logs is logging queries for.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-CloudWatchLogsLogGroupArnConfigDetails-Id"></a>
 The ID for a DNS query logging configuration.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_CloudWatchLogsLogGroupArnConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CloudWatchLogsLogGroupArnConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CloudWatchLogsLogGroupArnConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CloudWatchLogsLogGroupArnConfigDetails)

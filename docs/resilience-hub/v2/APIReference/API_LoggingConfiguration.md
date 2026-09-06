---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_LoggingConfiguration.html
---

# LoggingConfiguration
<a name="API_LoggingConfiguration"></a>

Configuration for test execution logging destinations.

## Contents
<a name="API_LoggingConfiguration_Contents"></a>

 ** cloudWatchLogGroupArn **   <a name="ngresiliencehub-Type-LoggingConfiguration-cloudWatchLogGroupArn"></a>
The ARN of the CloudWatch Logs log group for log delivery.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** logSchemaVersion **   <a name="ngresiliencehub-Type-LoggingConfiguration-logSchemaVersion"></a>
The version of the log schema.
Type: String
Required: No

 ** s3BucketName **   <a name="ngresiliencehub-Type-LoggingConfiguration-s3BucketName"></a>
The name of the S3 bucket for log delivery.
Type: String
Required: No

## See Also
<a name="API_LoggingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/LoggingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/LoggingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/LoggingConfiguration)

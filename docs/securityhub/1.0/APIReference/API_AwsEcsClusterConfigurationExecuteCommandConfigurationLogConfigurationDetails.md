---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails.html
---

# AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails"></a>

The log configuration for the results of the run command actions.

## Contents
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails_Contents"></a>

 ** CloudWatchEncryptionEnabled **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails-CloudWatchEncryptionEnabled"></a>
Whether to enable encryption on the CloudWatch logs.
Type: Boolean
Required: No

 ** CloudWatchLogGroupName **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails-CloudWatchLogGroupName"></a>
The name of the CloudWatch log group to send the logs to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3BucketName **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails-S3BucketName"></a>
The name of the S3 bucket to send logs to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** S3EncryptionEnabled **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails-S3EncryptionEnabled"></a>
Whether to encrypt the logs that are sent to the S3 bucket.
Type: Boolean
Required: No

 ** S3KeyPrefix **   <a name="securityhub-Type-AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails-S3KeyPrefix"></a>
Identifies the folder in the S3 bucket to send the logs to.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails)

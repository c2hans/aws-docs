---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterLoggingStatus.html
---

# AwsRedshiftClusterLoggingStatus
<a name="API_AwsRedshiftClusterLoggingStatus"></a>

Provides information about the logging status of the cluster.

## Contents
<a name="API_AwsRedshiftClusterLoggingStatus_Contents"></a>

 ** BucketName **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-BucketName"></a>
The name of the S3 bucket where the log files are stored.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastFailureMessage **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-LastFailureMessage"></a>
The message indicating that the logs failed to be delivered.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastFailureTime **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-LastFailureTime"></a>
The last time when logs failed to be delivered.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastSuccessfulDeliveryTime **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-LastSuccessfulDeliveryTime"></a>
The last time that logs were delivered successfully.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoggingEnabled **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-LoggingEnabled"></a>
Indicates whether logging is enabled.
Type: Boolean
Required: No

 ** S3KeyPrefix **   <a name="securityhub-Type-AwsRedshiftClusterLoggingStatus-S3KeyPrefix"></a>
Provides the prefix applied to the log file names.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterLoggingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterLoggingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterLoggingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterLoggingStatus)

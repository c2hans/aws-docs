---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ObjectLockRetentionEventHoldDuration.html
---

# S3ObjectLockRetentionEventHoldDuration
<a name="API_control_S3ObjectLockRetentionEventHoldDuration"></a>

Contains the duration configuration for an event hold, specified in either days or years.

## Contents
<a name="API_control_S3ObjectLockRetentionEventHoldDuration_Contents"></a>

 ** Days **   <a name="AmazonS3-Type-control_S3ObjectLockRetentionEventHoldDuration-Days"></a>
The number of days for the event hold duration. The minimum value is 1 and the maximum value is 36,500.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 36500.
Required: No

 ** Years **   <a name="AmazonS3-Type-control_S3ObjectLockRetentionEventHoldDuration-Years"></a>
The number of years for the event hold duration. The minimum value is 1 and the maximum value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_control_S3ObjectLockRetentionEventHoldDuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ObjectLockRetentionEventHoldDuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ObjectLockRetentionEventHoldDuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ObjectLockRetentionEventHoldDuration)

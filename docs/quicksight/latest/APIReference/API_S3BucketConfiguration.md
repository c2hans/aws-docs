---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_S3BucketConfiguration.html
---

# S3BucketConfiguration
<a name="API_S3BucketConfiguration"></a>

An optional structure that contains the Amazon S3 bucket configuration that the generated snapshots are stored in. If you don't provide this information, generated snapshots are stored in the default Amazon Quick Sight bucket.

## Contents
<a name="API_S3BucketConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BucketName **   <a name="QS-Type-S3BucketConfiguration-BucketName"></a>
The name of an existing Amazon S3 bucket where the generated snapshot artifacts are sent.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** BucketPrefix **   <a name="QS-Type-S3BucketConfiguration-BucketPrefix"></a>
The prefix of the Amazon S3 bucket that the generated snapshots are stored in.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** BucketRegion **   <a name="QS-Type-S3BucketConfiguration-BucketRegion"></a>
The region that the Amazon S3 bucket is located in. The bucket must be located in the same region that the `StartDashboardSnapshotJob` API call is made.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_S3BucketConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/S3BucketConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/S3BucketConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/S3BucketConfiguration)

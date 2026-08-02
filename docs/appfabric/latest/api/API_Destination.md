---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_Destination.html
---

# Destination
<a name="API_Destination"></a>

Contains information about an audit log destination.

## Contents
<a name="API_Destination_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** firehoseStream **   <a name="appfabric-Type-Destination-firehoseStream"></a>
Contains information about an Amazon Data Firehose delivery stream.
Type: [FirehoseStream](API_FirehoseStream.md) object
Required: No

 ** s3Bucket **   <a name="appfabric-Type-Destination-s3Bucket"></a>
Contains information about an Amazon S3 bucket.
Type: [S3Bucket](API_S3Bucket.md) object
Required: No

## See Also
<a name="API_Destination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/Destination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/Destination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/Destination)

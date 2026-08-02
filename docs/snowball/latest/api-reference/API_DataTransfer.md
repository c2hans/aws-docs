---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DataTransfer.html
---

# DataTransfer
<a name="API_DataTransfer"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

Defines the real-time status of a Snow device's data transfer while the device is at AWS. This data is only available while a job has a `JobState` value of `InProgress`, for both import and export jobs.

## Contents
<a name="API_DataTransfer_Contents"></a>

 ** BytesTransferred **   <a name="Snowball-Type-DataTransfer-BytesTransferred"></a>
The number of bytes transferred between a Snow device and Amazon S3.
Type: Long
Required: No

 ** ObjectsTransferred **   <a name="Snowball-Type-DataTransfer-ObjectsTransferred"></a>
The number of objects transferred between a Snow device and Amazon S3.
Type: Long
Required: No

 ** TotalBytes **   <a name="Snowball-Type-DataTransfer-TotalBytes"></a>
The total bytes of data for a transfer between a Snow device and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
Type: Long
Required: No

 ** TotalObjects **   <a name="Snowball-Type-DataTransfer-TotalObjects"></a>
The total number of objects for a transfer between a Snow device and Amazon S3. This value is set to 0 (zero) until all the keys that will be transferred have been listed.
Type: Long
Required: No

## See Also
<a name="API_DataTransfer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DataTransfer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DataTransfer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DataTransfer)

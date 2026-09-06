---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_MagneticStoreWriteProperties.html
---

# MagneticStoreWriteProperties
<a name="API_MagneticStoreWriteProperties"></a>

The set of properties on a table for configuring magnetic store writes.

## Contents
<a name="API_MagneticStoreWriteProperties_Contents"></a>

 ** EnableMagneticStoreWrites **   <a name="timestream-Type-MagneticStoreWriteProperties-EnableMagneticStoreWrites"></a>
A flag to enable magnetic store writes.
Type: Boolean
Required: Yes

 ** MagneticStoreRejectedDataLocation **   <a name="timestream-Type-MagneticStoreWriteProperties-MagneticStoreRejectedDataLocation"></a>
The location to write error reports for records rejected asynchronously during magnetic store writes.
Type: [MagneticStoreRejectedDataLocation](API_MagneticStoreRejectedDataLocation.md) object
Required: No

## See Also
<a name="API_MagneticStoreWriteProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/MagneticStoreWriteProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/MagneticStoreWriteProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/MagneticStoreWriteProperties)

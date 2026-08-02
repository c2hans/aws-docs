---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectVersion.html
---

# ObjectVersion
<a name="API_ObjectVersion"></a>

The version of an object.

## Contents
<a name="API_ObjectVersion_Contents"></a>

 ** ChecksumAlgorithm **   <a name="AmazonS3-Type-ObjectVersion-ChecksumAlgorithm"></a>
The algorithm that was used to create a checksum of the object.
Type: Array of strings
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`
Required: No

 ** ChecksumType **   <a name="AmazonS3-Type-ObjectVersion-ChecksumType"></a>
The checksum type that is used to calculate the object’s checksum value. For more information, see [Checking object integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html) in the *Amazon S3 User Guide*.
Type: String
Valid Values: `COMPOSITE | FULL_OBJECT`
Required: No

 ** ETag **   <a name="AmazonS3-Type-ObjectVersion-ETag"></a>
The entity tag is an MD5 hash of that version of the object.
Type: String
Required: No

 ** IsLatest **   <a name="AmazonS3-Type-ObjectVersion-IsLatest"></a>
Specifies whether the object is (true) or is not (false) the latest version of an object.
Type: Boolean
Required: No

 ** Key **   <a name="AmazonS3-Type-ObjectVersion-Key"></a>
The object key.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** LastModified **   <a name="AmazonS3-Type-ObjectVersion-LastModified"></a>
Date and time when the object was last modified.
Type: Timestamp
Required: No

 ** Owner **   <a name="AmazonS3-Type-ObjectVersion-Owner"></a>
Specifies the owner of the object.
Type: [Owner](API_Owner.md) data type
Required: No

 ** RestoreStatus **   <a name="AmazonS3-Type-ObjectVersion-RestoreStatus"></a>
Specifies the restoration status of an object. Objects in certain storage classes must be restored before they can be retrieved. For more information about these storage classes and how to work with archived objects, see [ Working with archived objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html) in the *Amazon S3 User Guide*.
Type: [RestoreStatus](API_RestoreStatus.md) data type
Required: No

 ** Size **   <a name="AmazonS3-Type-ObjectVersion-Size"></a>
Size in bytes of the object.
Type: Long
Required: No

 ** StorageClass **   <a name="AmazonS3-Type-ObjectVersion-StorageClass"></a>
The class of storage used to store the object.
Type: String
Valid Values: `STANDARD`
Required: No

 ** VersionId **   <a name="AmazonS3-Type-ObjectVersion-VersionId"></a>
Version ID of an object.
Type: String
Required: No

## See Also
<a name="API_ObjectVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectVersion)

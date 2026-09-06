---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_SequenceStoreDetail.html
---

# SequenceStoreDetail
<a name="API_SequenceStoreDetail"></a>

Details about a sequence store.

## Contents
<a name="API_SequenceStoreDetail_Contents"></a>

 ** arn **   <a name="omics-Type-SequenceStoreDetail-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: Yes

 ** creationTime **   <a name="omics-Type-SequenceStoreDetail-creationTime"></a>
When the store was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="omics-Type-SequenceStoreDetail-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** description **   <a name="omics-Type-SequenceStoreDetail-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** eTagAlgorithmFamily **   <a name="omics-Type-SequenceStoreDetail-eTagAlgorithmFamily"></a>
The algorithm family of the ETag.
Type: String
Valid Values: `MD5up | SHA256up | SHA512up`
Required: No

 ** fallbackLocation **   <a name="omics-Type-SequenceStoreDetail-fallbackLocation"></a>
 An S3 location that is used to store files that have failed a direct upload.
Type: String
Pattern: `$|^s3://([a-z0-9][a-z0-9-.]{1,61}[a-z0-9])/?((.{1,1024})/)?`
Required: No

 ** name **   <a name="omics-Type-SequenceStoreDetail-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** sseConfig **   <a name="omics-Type-SequenceStoreDetail-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object
Required: No

 ** status **   <a name="omics-Type-SequenceStoreDetail-status"></a>
Status of the sequence store.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: No

 ** statusMessage **   <a name="omics-Type-SequenceStoreDetail-statusMessage"></a>
The status message of the sequence store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** updateTime **   <a name="omics-Type-SequenceStoreDetail-updateTime"></a>
The last-updated time of the Sequence Store.
Type: Timestamp
Required: No

## See Also
<a name="API_SequenceStoreDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/SequenceStoreDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/SequenceStoreDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/SequenceStoreDetail)

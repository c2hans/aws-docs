---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreItem.html
---

# AnnotationStoreItem
<a name="API_AnnotationStoreItem"></a>

An annotation store.

## Contents
<a name="API_AnnotationStoreItem_Contents"></a>

 ** creationTime **   <a name="omics-Type-AnnotationStoreItem-creationTime"></a>
The store's creation time.
Type: Timestamp
Required: Yes

 ** description **   <a name="omics-Type-AnnotationStoreItem-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** id **   <a name="omics-Type-AnnotationStoreItem-id"></a>
The store's ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="omics-Type-AnnotationStoreItem-name"></a>
The store's name.
Type: String
Required: Yes

 ** reference **   <a name="omics-Type-AnnotationStoreItem-reference"></a>
The store's genome reference.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sseConfig **   <a name="omics-Type-AnnotationStoreItem-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object
Required: Yes

 ** status **   <a name="omics-Type-AnnotationStoreItem-status"></a>
The store's status.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`
Required: Yes

 ** statusMessage **   <a name="omics-Type-AnnotationStoreItem-statusMessage"></a>
The store's status message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** storeArn **   <a name="omics-Type-AnnotationStoreItem-storeArn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`
Required: Yes

 ** storeFormat **   <a name="omics-Type-AnnotationStoreItem-storeFormat"></a>
The store's file format.
Type: String
Valid Values: `GFF | TSV | VCF`
Required: Yes

 ** storeSizeBytes **   <a name="omics-Type-AnnotationStoreItem-storeSizeBytes"></a>
The store's size in bytes.
Type: Long
Required: Yes

 ** updateTime **   <a name="omics-Type-AnnotationStoreItem-updateTime"></a>
When the store was updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_AnnotationStoreItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/AnnotationStoreItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/AnnotationStoreItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/AnnotationStoreItem)

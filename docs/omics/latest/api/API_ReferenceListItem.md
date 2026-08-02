---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReferenceListItem.html
---

# ReferenceListItem
<a name="API_ReferenceListItem"></a>

A genome reference.

## Contents
<a name="API_ReferenceListItem_Contents"></a>

 ** arn **   <a name="omics-Type-ReferenceListItem-arn"></a>
The reference's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`
Required: Yes

 ** creationTime **   <a name="omics-Type-ReferenceListItem-creationTime"></a>
When the reference was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="omics-Type-ReferenceListItem-id"></a>
The reference's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** md5 **   <a name="omics-Type-ReferenceListItem-md5"></a>
The reference's MD5 checksum.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{N}]+`
Required: Yes

 ** referenceStoreId **   <a name="omics-Type-ReferenceListItem-referenceStoreId"></a>
The reference's store ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** updateTime **   <a name="omics-Type-ReferenceListItem-updateTime"></a>
When the reference was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="omics-Type-ReferenceListItem-description"></a>
The reference's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** name **   <a name="omics-Type-ReferenceListItem-name"></a>
The reference's name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

 ** status **   <a name="omics-Type-ReferenceListItem-status"></a>
The reference's status.
Type: String
Valid Values: `ACTIVE | DELETING | DELETED`
Required: No

## See Also
<a name="API_ReferenceListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReferenceListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReferenceListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReferenceListItem)

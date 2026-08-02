---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_S3ItemFilter.html
---

# S3ItemFilter
<a name="API_BKS_S3ItemFilter"></a>

This contains arrays of objects, which may include ObjectKeys, Sizes, CreationTimes, VersionIds, and/or Etags.

## Contents
<a name="API_BKS_S3ItemFilter_Contents"></a>

 ** CreationTimes **   <a name="Backup-Type-BKS_S3ItemFilter-CreationTimes"></a>
You can include 1 to 10 values.
If one value is included, the results will return only items that match the value.
If more than one value is included, the results will return all items that match any of the values.
Type: Array of [TimeCondition](API_BKS_TimeCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ETags **   <a name="Backup-Type-BKS_S3ItemFilter-ETags"></a>
You can include 1 to 10 values.
If one value is included, the results will return only items that match the value.
If more than one value is included, the results will return all items that match any of the values.
Type: Array of [StringCondition](API_BKS_StringCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** ObjectKeys **   <a name="Backup-Type-BKS_S3ItemFilter-ObjectKeys"></a>
You can include 1 to 10 values.
If one value is included, the results will return only items that match the value.
If more than one value is included, the results will return all items that match any of the values.
Type: Array of [StringCondition](API_BKS_StringCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Sizes **   <a name="Backup-Type-BKS_S3ItemFilter-Sizes"></a>
You can include 1 to 10 values.
If one value is included, the results will return only items that match the value.
If more than one value is included, the results will return all items that match any of the values.
Type: Array of [LongCondition](API_BKS_LongCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** VersionIds **   <a name="Backup-Type-BKS_S3ItemFilter-VersionIds"></a>
You can include 1 to 10 values.
If one value is included, the results will return only items that match the value.
If more than one value is included, the results will return all items that match any of the values.
Type: Array of [StringCondition](API_BKS_StringCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_BKS_S3ItemFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/S3ItemFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/S3ItemFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/S3ItemFilter)

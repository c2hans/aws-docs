---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ItemFilters.html
---

# ItemFilters
<a name="API_BKS_ItemFilters"></a>

Item Filters represent all input item properties specified when the search was created.

Contains either EBSItemFilters or S3ItemFilters

## Contents
<a name="API_BKS_ItemFilters_Contents"></a>

 ** EBSItemFilters **   <a name="Backup-Type-BKS_ItemFilters-EBSItemFilters"></a>
This array can contain CreationTimes, FilePaths, LastModificationTimes, or Sizes objects.
Type: Array of [EBSItemFilter](API_BKS_EBSItemFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** S3ItemFilters **   <a name="Backup-Type-BKS_ItemFilters-S3ItemFilters"></a>
This array can contain CreationTimes, ETags, ObjectKeys, Sizes, or VersionIds objects.
Type: Array of [S3ItemFilter](API_BKS_S3ItemFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_BKS_ItemFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ItemFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ItemFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ItemFilters)

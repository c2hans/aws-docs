---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_EBSItemFilter.html
---

# EBSItemFilter
<a name="API_BKS_EBSItemFilter"></a>

This contains arrays of objects, which may include CreationTimes time condition objects, FilePaths string objects, LastModificationTimes time condition objects,

## Contents
<a name="API_BKS_EBSItemFilter_Contents"></a>

 ** CreationTimes **   <a name="Backup-Type-BKS_EBSItemFilter-CreationTimes"></a>
You can include 1 to 10 values.
If one is included, the results will return only items that match.
If more than one is included, the results will return all items that match any of the included values.
Type: Array of [TimeCondition](API_BKS_TimeCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** FilePaths **   <a name="Backup-Type-BKS_EBSItemFilter-FilePaths"></a>
You can include 1 to 10 values.
If one file path is included, the results will return only items that match the file path.
If more than one file path is included, the results will return all items that match any of the file paths.
Type: Array of [StringCondition](API_BKS_StringCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** LastModificationTimes **   <a name="Backup-Type-BKS_EBSItemFilter-LastModificationTimes"></a>
You can include 1 to 10 values.
If one is included, the results will return only items that match.
If more than one is included, the results will return all items that match any of the included values.
Type: Array of [TimeCondition](API_BKS_TimeCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** Sizes **   <a name="Backup-Type-BKS_EBSItemFilter-Sizes"></a>
You can include 1 to 10 values.
If one is included, the results will return only items that match.
If more than one is included, the results will return all items that match any of the included values.
Type: Array of [LongCondition](API_BKS_LongCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_BKS_EBSItemFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/EBSItemFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/EBSItemFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/EBSItemFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

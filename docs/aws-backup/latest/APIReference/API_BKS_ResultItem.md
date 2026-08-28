---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_ResultItem.html
---

# ResultItem
<a name="API_BKS_ResultItem"></a>

This is an object representing the item returned in the results of a search for a specific resource type.

## Contents
<a name="API_BKS_ResultItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EBSResultItem **   <a name="Backup-Type-BKS_ResultItem-EBSResultItem"></a>
These are items returned in the search results of an Amazon EBS search.
Type: [EBSResultItem](API_BKS_EBSResultItem.md) object
Required: No

 ** S3ResultItem **   <a name="Backup-Type-BKS_ResultItem-S3ResultItem"></a>
These are items returned in the search results of an Amazon S3 search.
Type: [S3ResultItem](API_BKS_S3ResultItem.md) object
Required: No

## See Also
<a name="API_BKS_ResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/ResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/ResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/ResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

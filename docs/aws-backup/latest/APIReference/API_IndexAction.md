---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_IndexAction.html
---

# IndexAction
<a name="API_IndexAction"></a>

This is an optional array within a BackupRule.

IndexAction consists of one ResourceTypes.

## Contents
<a name="API_IndexAction_Contents"></a>

 ** ResourceTypes **   <a name="Backup-Type-IndexAction-ResourceTypes"></a>
0 or 1 index action will be accepted for each BackupRule.
Valid values:
+  `EBS` for Amazon Elastic Block Store
+  `S3` for Amazon Simple Storage Service (Amazon S3)
Type: Array of strings
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

## See Also
<a name="API_IndexAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/IndexAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/IndexAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/IndexAction)

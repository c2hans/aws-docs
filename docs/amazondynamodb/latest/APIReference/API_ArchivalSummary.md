---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ArchivalSummary.html
---

# ArchivalSummary
<a name="API_ArchivalSummary"></a>

Contains details of a table archival operation.

## Contents
<a name="API_ArchivalSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ArchivalBackupArn **   <a name="DDB-Type-ArchivalSummary-ArchivalBackupArn"></a>
The Amazon Resource Name (ARN) of the backup the table was archived to, when applicable in the archival reason. If you wish to restore this backup to the same table name, you will need to delete the original table.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** ArchivalDateTime **   <a name="DDB-Type-ArchivalSummary-ArchivalDateTime"></a>
The date and time when table archival was initiated by DynamoDB, in UNIX epoch time format.
Type: Timestamp
Required: No

 ** ArchivalReason **   <a name="DDB-Type-ArchivalSummary-ArchivalReason"></a>
The reason DynamoDB archived the table. Currently, the only possible value is:
+  `INACCESSIBLE_ENCRYPTION_CREDENTIALS` - The table was archived due to the table's AWS KMS key being inaccessible for more than seven days. An On-Demand backup was created at the archival time.
Type: String
Required: No

## See Also
<a name="API_ArchivalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ArchivalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ArchivalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ArchivalSummary)

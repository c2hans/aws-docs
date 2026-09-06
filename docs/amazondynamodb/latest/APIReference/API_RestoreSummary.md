---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_RestoreSummary.html
---

# RestoreSummary
<a name="API_RestoreSummary"></a>

Contains details for the restore.

## Contents
<a name="API_RestoreSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RestoreDateTime **   <a name="DDB-Type-RestoreSummary-RestoreDateTime"></a>
Point in time or source backup time.
Type: Timestamp
Required: Yes

 ** RestoreInProgress **   <a name="DDB-Type-RestoreSummary-RestoreInProgress"></a>
Indicates if a restore is in progress or not.
Type: Boolean
Required: Yes

 ** SourceBackupArn **   <a name="DDB-Type-RestoreSummary-SourceBackupArn"></a>
The Amazon Resource Name (ARN) of the backup from which the table was restored.
Type: String
Length Constraints: Minimum length of 37. Maximum length of 1024.
Required: No

 ** SourceTableArn **   <a name="DDB-Type-RestoreSummary-SourceTableArn"></a>
The ARN of the source table of the backup that is being restored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_RestoreSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/RestoreSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/RestoreSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/RestoreSummary)

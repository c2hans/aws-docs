---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_TableSummary.html
---

# TableSummary
<a name="API_TableSummary"></a>

Returns the name of the specified table, the keyspace it is stored in, and the unique identifier in the format of an Amazon Resource Name (ARN).

## Contents
<a name="API_TableSummary_Contents"></a>

 ** keyspaceName **   <a name="keyspaces-Type-TableSummary-keyspaceName"></a>
The name of the keyspace that the table is stored in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** resourceArn **   <a name="keyspaces-Type-TableSummary-resourceArn"></a>
The unique identifier of the table in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`
Required: Yes

 ** tableName **   <a name="keyspaces-Type-TableSummary-tableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## See Also
<a name="API_TableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/TableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/TableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/TableSummary)

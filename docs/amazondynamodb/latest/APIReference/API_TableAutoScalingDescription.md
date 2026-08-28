---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_TableAutoScalingDescription.html
---

# TableAutoScalingDescription
<a name="API_TableAutoScalingDescription"></a>

Represents the auto scaling configuration for a global table.

## Contents
<a name="API_TableAutoScalingDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Replicas **   <a name="DDB-Type-TableAutoScalingDescription-Replicas"></a>
Represents replicas of the global table.
Type: Array of [ReplicaAutoScalingDescription](API_ReplicaAutoScalingDescription.md) objects
Required: No

 ** TableName **   <a name="DDB-Type-TableAutoScalingDescription-TableName"></a>
The name of the table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** TableStatus **   <a name="DDB-Type-TableAutoScalingDescription-TableStatus"></a>
The current state of the table:
+  `CREATING` - The table is being created.
+  `UPDATING` - The table is being updated.
+  `DELETING` - The table is being deleted.
+  `ACTIVE` - The table is ready for use.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | INACCESSIBLE_ENCRYPTION_CREDENTIALS | ARCHIVING | ARCHIVED | REPLICATION_NOT_AUTHORIZED`
Required: No

## See Also
<a name="API_TableAutoScalingDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/TableAutoScalingDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/TableAutoScalingDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/TableAutoScalingDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

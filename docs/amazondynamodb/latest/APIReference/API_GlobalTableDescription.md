---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GlobalTableDescription.html
---

# GlobalTableDescription
<a name="API_GlobalTableDescription"></a>

Contains details about the global table.

## Contents
<a name="API_GlobalTableDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationDateTime **   <a name="DDB-Type-GlobalTableDescription-CreationDateTime"></a>
The creation time of the global table.
Type: Timestamp
Required: No

 ** GlobalTableArn **   <a name="DDB-Type-GlobalTableDescription-GlobalTableArn"></a>
The unique identifier of the global table.
Type: String
Required: No

 ** GlobalTableName **   <a name="DDB-Type-GlobalTableDescription-GlobalTableName"></a>
The global table name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** GlobalTableStatus **   <a name="DDB-Type-GlobalTableDescription-GlobalTableStatus"></a>
The current state of the global table:
+  `CREATING` - The global table is being created.
+  `UPDATING` - The global table is being updated.
+  `DELETING` - The global table is being deleted.
+  `ACTIVE` - The global table is ready for use.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | UPDATING`
Required: No

 ** ReplicationGroup **   <a name="DDB-Type-GlobalTableDescription-ReplicationGroup"></a>
The Regions where the global table has replicas.
Type: Array of [ReplicaDescription](API_ReplicaDescription.md) objects
Required: No

## See Also
<a name="API_GlobalTableDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/GlobalTableDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/GlobalTableDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/GlobalTableDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

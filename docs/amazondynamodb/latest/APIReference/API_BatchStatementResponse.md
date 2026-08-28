---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchStatementResponse.html
---

# BatchStatementResponse
<a name="API_BatchStatementResponse"></a>

 A PartiQL batch statement response..

## Contents
<a name="API_BatchStatementResponse_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Error **   <a name="DDB-Type-BatchStatementResponse-Error"></a>
 The error associated with a failed PartiQL batch statement.
Type: [BatchStatementError](API_BatchStatementError.md) object
Required: No

 ** Item **   <a name="DDB-Type-BatchStatementResponse-Item"></a>
 A DynamoDB item associated with a BatchStatementResponse
Type: String to [AttributeValue](API_AttributeValue.md) object map
Key Length Constraints: Maximum length of 65535.
Required: No

 ** TableName **   <a name="DDB-Type-BatchStatementResponse-TableName"></a>
 The table name associated with a failed PartiQL batch statement.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

## See Also
<a name="API_BatchStatementResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BatchStatementResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BatchStatementResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BatchStatementResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

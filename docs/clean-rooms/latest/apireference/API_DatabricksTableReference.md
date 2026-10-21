---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DatabricksTableReference.html
---

# DatabricksTableReference
<a name="API_DatabricksTableReference"></a>

 A reference to a table within Databricks.

## Contents
<a name="API_DatabricksTableReference_Contents"></a>

 ** connectionType **   <a name="API-Type-DatabricksTableReference-connectionType"></a>
Type of the connector to be used for connecting to Databricks. Supported connector: Delta Sharing
Type: [DatabricksConnectionType](API_DatabricksConnectionType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** schemaName **   <a name="API-Type-DatabricksTableReference-schemaName"></a>
Name of the Schema within Databricks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+`
Required: Yes

 ** tableName **   <a name="API-Type-DatabricksTableReference-tableName"></a>
Name of the Table within Databricks.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+`
Required: Yes

 ** workspaceUrl **   <a name="API-Type-DatabricksTableReference-workspaceUrl"></a>
URL for the Databricks Workspace.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 256.
Pattern: `https://[a-zA-Z0-9.-]+\.cloud\.databricks\.com/?`
Required: Yes

## See Also
<a name="API_DatabricksTableReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DatabricksTableReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DatabricksTableReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DatabricksTableReference)

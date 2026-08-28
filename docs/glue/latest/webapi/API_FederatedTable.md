---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FederatedTable.html
---

# FederatedTable
<a name="API_FederatedTable"></a>

A table that points to an entity outside the AWS Glue Data Catalog.

## Contents
<a name="API_FederatedTable_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-FederatedTable-ConnectionName"></a>
The name of the connection to the external metastore.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ConnectionType **   <a name="Glue-Type-FederatedTable-ConnectionType"></a>
The type of connection used to access the federated table, specifying the protocol or method for connecting to the external data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DatabaseIdentifier **   <a name="Glue-Type-FederatedTable-DatabaseIdentifier"></a>
A unique identifier for the federated database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Identifier **   <a name="Glue-Type-FederatedTable-Identifier"></a>
A unique identifier for the federated table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_FederatedTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FederatedTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FederatedTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FederatedTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

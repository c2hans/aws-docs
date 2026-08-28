---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergInput.html
---

# IcebergInput
<a name="API_IcebergInput"></a>

A structure that defines an Apache Iceberg metadata table to create in the catalog.

## Contents
<a name="API_IcebergInput_Contents"></a>

 ** MetadataOperation **   <a name="Glue-Type-IcebergInput-MetadataOperation"></a>
A required metadata operation. Can only be set to `CREATE`.
Type: String
Valid Values: `CREATE`
Required: Yes

 ** CreateIcebergTableInput **   <a name="Glue-Type-IcebergInput-CreateIcebergTableInput"></a>
The configuration parameters required to create a new Iceberg table in the AWS Glue Data Catalog, including table properties and metadata specifications.
Type: [CreateIcebergTableInput](API_CreateIcebergTableInput.md) object
Required: No

 ** Version **   <a name="Glue-Type-IcebergInput-Version"></a>
The table version for the Iceberg table. Defaults to 2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_IcebergInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

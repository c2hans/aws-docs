---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_DataIntegrationFlowTransformation.html
---

# DataIntegrationFlowTransformation
<a name="API_DataIntegrationFlowTransformation"></a>

The DataIntegrationFlow transformation parameters.

## Contents
<a name="API_DataIntegrationFlowTransformation_Contents"></a>

 ** transformationType **   <a name="supplychain-Type-DataIntegrationFlowTransformation-transformationType"></a>
The DataIntegrationFlow transformation type.
Type: String
Valid Values: `SQL | NONE`
Required: Yes

 ** sqlTransformation **   <a name="supplychain-Type-DataIntegrationFlowTransformation-sqlTransformation"></a>
The SQL DataIntegrationFlow transformation configuration.
Type: [DataIntegrationFlowSQLTransformationConfiguration](API_DataIntegrationFlowSQLTransformationConfiguration.md) object
Required: No

## See Also
<a name="API_DataIntegrationFlowTransformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/DataIntegrationFlowTransformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/DataIntegrationFlowTransformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/DataIntegrationFlowTransformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

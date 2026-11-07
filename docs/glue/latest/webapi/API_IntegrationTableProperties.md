---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationTableProperties.html
---

# IntegrationTableProperties
<a name="API_IntegrationTableProperties"></a>

The properties of a single integration table, including the resource ARN, the table name, and the source or target table configuration.

## Contents
<a name="API_IntegrationTableProperties_Contents"></a>

 ** ResourceArn **   <a name="Glue-Type-IntegrationTableProperties-ResourceArn"></a>
The connection ARN of the source, or the database ARN of the target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** TableName **   <a name="Glue-Type-IntegrationTableProperties-TableName"></a>
The name of the source table to be replicated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** SourceTableConfig **   <a name="Glue-Type-IntegrationTableProperties-SourceTableConfig"></a>
A structure for the source table configuration.
Type: [SourceTableConfig](API_SourceTableConfig.md) object
Required: No

 ** TargetTableConfig **   <a name="Glue-Type-IntegrationTableProperties-TargetTableConfig"></a>
A structure for the target table configuration.
Type: [TargetTableConfig](API_TargetTableConfig.md) object
Required: No

## See Also
<a name="API_IntegrationTableProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationTableProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationTableProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationTableProperties)

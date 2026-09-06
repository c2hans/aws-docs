---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceConfigurationInput.html
---

# DataSourceConfigurationInput
<a name="API_DataSourceConfigurationInput"></a>

The configuration of the data source.

## Contents
<a name="API_DataSourceConfigurationInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glueRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationInput-glueRunConfiguration"></a>
The configuration of the AWS Glue data source.
Type: [GlueRunConfigurationInput](API_GlueRunConfigurationInput.md) object
Required: No

 ** redshiftRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationInput-redshiftRunConfiguration"></a>
The configuration of the Amazon Redshift data source.
Type: [RedshiftRunConfigurationInput](API_RedshiftRunConfigurationInput.md) object
Required: No

 ** sageMakerRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationInput-sageMakerRunConfiguration"></a>
The Amazon SageMaker run configuration.
Type: [SageMakerRunConfigurationInput](API_SageMakerRunConfigurationInput.md) object
Required: No

## See Also
<a name="API_DataSourceConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceConfigurationInput)

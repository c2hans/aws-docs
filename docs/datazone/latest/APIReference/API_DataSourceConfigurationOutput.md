---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataSourceConfigurationOutput.html
---

# DataSourceConfigurationOutput
<a name="API_DataSourceConfigurationOutput"></a>

The configuration of the data source.

## Contents
<a name="API_DataSourceConfigurationOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glueRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationOutput-glueRunConfiguration"></a>
The configuration of the AWS Glue data source.
Type: [GlueRunConfigurationOutput](API_GlueRunConfigurationOutput.md) object
Required: No

 ** redshiftRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationOutput-redshiftRunConfiguration"></a>
The configuration of the Amazon Redshift data source.
Type: [RedshiftRunConfigurationOutput](API_RedshiftRunConfigurationOutput.md) object
Required: No

 ** sageMakerRunConfiguration **   <a name="datazone-Type-DataSourceConfigurationOutput-sageMakerRunConfiguration"></a>
The Amazon SageMaker run configuration.
Type: [SageMakerRunConfigurationOutput](API_SageMakerRunConfigurationOutput.md) object
Required: No

## See Also
<a name="API_DataSourceConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataSourceConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataSourceConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataSourceConfigurationOutput)

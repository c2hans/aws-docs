---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlueRunConfigurationOutput.html
---

# GlueRunConfigurationOutput
<a name="API_GlueRunConfigurationOutput"></a>

The configuration details of the AWS Glue data source.

## Contents
<a name="API_GlueRunConfigurationOutput_Contents"></a>

 ** relationalFilterConfigurations **   <a name="datazone-Type-GlueRunConfigurationOutput-relationalFilterConfigurations"></a>
The relational filter configurations included in the configuration details of the AWS Glue data source.
Type: Array of [RelationalFilterConfiguration](API_RelationalFilterConfiguration.md) objects
Required: Yes

 ** accountId **   <a name="datazone-Type-GlueRunConfigurationOutput-accountId"></a>
The AWS account ID included in the configuration details of the AWS Glue data source.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** autoImportDataQualityResult **   <a name="datazone-Type-GlueRunConfigurationOutput-autoImportDataQualityResult"></a>
Specifies whether to automatically import data quality metrics as part of the data source run.
Type: Boolean
Required: No

 ** catalogName **   <a name="datazone-Type-GlueRunConfigurationOutput-catalogName"></a>
The catalog name in the AWS Glue run configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** dataAccessRole **   <a name="datazone-Type-GlueRunConfigurationOutput-dataAccessRole"></a>
The data access role included in the configuration details of the AWS Glue data source.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}`
Required: No

 ** region **   <a name="datazone-Type-GlueRunConfigurationOutput-region"></a>
The AWS region included in the configuration details of the AWS Glue data source.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `.*[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9].*`
Required: No

## See Also
<a name="API_GlueRunConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlueRunConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlueRunConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlueRunConfigurationOutput)

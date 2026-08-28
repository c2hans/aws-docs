---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GlueRunConfigurationInput.html
---

# GlueRunConfigurationInput
<a name="API_GlueRunConfigurationInput"></a>

The configuration details of the AWS Glue data source.

## Contents
<a name="API_GlueRunConfigurationInput_Contents"></a>

 ** relationalFilterConfigurations **   <a name="datazone-Type-GlueRunConfigurationInput-relationalFilterConfigurations"></a>
The relational filter configurations included in the configuration details of the AWS Glue data source.
Type: Array of [RelationalFilterConfiguration](API_RelationalFilterConfiguration.md) objects
Required: Yes

 ** autoImportDataQualityResult **   <a name="datazone-Type-GlueRunConfigurationInput-autoImportDataQualityResult"></a>
Specifies whether to automatically import data quality metrics as part of the data source run.
Type: Boolean
Required: No

 ** catalogName **   <a name="datazone-Type-GlueRunConfigurationInput-catalogName"></a>
The catalog name in the AWS Glue run configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** dataAccessRole **   <a name="datazone-Type-GlueRunConfigurationInput-dataAccessRole"></a>
The data access role included in the configuration details of the AWS Glue data source.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}`
Required: No

## See Also
<a name="API_GlueRunConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GlueRunConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GlueRunConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GlueRunConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

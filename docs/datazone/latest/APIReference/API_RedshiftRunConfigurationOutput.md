---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftRunConfigurationOutput.html
---

# RedshiftRunConfigurationOutput
<a name="API_RedshiftRunConfigurationOutput"></a>

The configuration details of the Amazon Redshift data source.

## Contents
<a name="API_RedshiftRunConfigurationOutput_Contents"></a>

 ** redshiftStorage **   <a name="datazone-Type-RedshiftRunConfigurationOutput-redshiftStorage"></a>
The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.
Type: [RedshiftStorage](API_RedshiftStorage.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** relationalFilterConfigurations **   <a name="datazone-Type-RedshiftRunConfigurationOutput-relationalFilterConfigurations"></a>
The relational filger configurations included in the configuration details of the Amazon Redshift data source.
Type: Array of [RelationalFilterConfiguration](API_RelationalFilterConfiguration.md) objects
Required: Yes

 ** accountId **   <a name="datazone-Type-RedshiftRunConfigurationOutput-accountId"></a>
The ID of the AWS account included in the configuration details of the Amazon Redshift data source.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** dataAccessRole **   <a name="datazone-Type-RedshiftRunConfigurationOutput-dataAccessRole"></a>
The data access role included in the configuration details of the Amazon Redshift data source.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}`
Required: No

 ** redshiftCredentialConfiguration **   <a name="datazone-Type-RedshiftRunConfigurationOutput-redshiftCredentialConfiguration"></a>
The details of the credentials required to access an Amazon Redshift cluster.
Type: [RedshiftCredentialConfiguration](API_RedshiftCredentialConfiguration.md) object
Required: No

 ** region **   <a name="datazone-Type-RedshiftRunConfigurationOutput-region"></a>
The AWS region included in the configuration details of the Amazon Redshift data source.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `.*[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9].*`
Required: No

## See Also
<a name="API_RedshiftRunConfigurationOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftRunConfigurationOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftRunConfigurationOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftRunConfigurationOutput)

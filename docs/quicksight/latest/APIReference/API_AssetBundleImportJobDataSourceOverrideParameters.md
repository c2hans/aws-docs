---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobDataSourceOverrideParameters.html
---

# AssetBundleImportJobDataSourceOverrideParameters
<a name="API_AssetBundleImportJobDataSourceOverrideParameters"></a>

The override parameters for a single data source that is being imported.

## Contents
<a name="API_AssetBundleImportJobDataSourceOverrideParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSourceId **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-DataSourceId"></a>
The ID of the data source to apply overrides to.
Type: String
Required: Yes

 ** Credentials **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-Credentials"></a>
An optional structure that provides the credentials to be used to create the imported data source.
Type: [AssetBundleImportJobDataSourceCredentials](API_AssetBundleImportJobDataSourceCredentials.md) object
Required: No

 ** DataSourceParameters **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-DataSourceParameters"></a>
The parameters that Quick Sight uses to connect to your underlying data source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.
Type: [DataSourceParameters](API_DataSourceParameters.md) object
Required: No

 ** Name **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-Name"></a>
A new name for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** SslProperties **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-SslProperties"></a>
Secure Socket Layer (SSL) properties that apply when Quick Sight connects to your underlying data source.
Type: [SslProperties](API_SslProperties.md) object
Required: No

 ** VpcConnectionProperties **   <a name="QS-Type-AssetBundleImportJobDataSourceOverrideParameters-VpcConnectionProperties"></a>
VPC connection properties.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

## See Also
<a name="API_AssetBundleImportJobDataSourceOverrideParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobDataSourceOverrideParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobDataSourceOverrideParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobDataSourceOverrideParameters)

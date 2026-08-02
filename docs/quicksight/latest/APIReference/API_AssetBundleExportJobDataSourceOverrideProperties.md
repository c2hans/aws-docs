---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleExportJobDataSourceOverrideProperties.html
---

# AssetBundleExportJobDataSourceOverrideProperties
<a name="API_AssetBundleExportJobDataSourceOverrideProperties"></a>

Controls how a specific `DataSource` resource is parameterized in the returned CloudFormation template.

## Contents
<a name="API_AssetBundleExportJobDataSourceOverrideProperties_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-AssetBundleExportJobDataSourceOverrideProperties-Arn"></a>
The ARN of the specific `DataSource` resource whose override properties are configured in this structure.
Type: String
Required: Yes

 ** Properties **   <a name="QS-Type-AssetBundleExportJobDataSourceOverrideProperties-Properties"></a>
A list of `DataSource` resource properties to generate variables for in the returned CloudFormation template.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `Name | DisableSsl | SecretArn | Username | Password | Domain | WorkGroup | Host | Port | Database | DataSetName | Catalog | InstanceId | ClusterId | ManifestFileLocation | Warehouse | RoleArn | ProductType`
Required: Yes

## See Also
<a name="API_AssetBundleExportJobDataSourceOverrideProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleExportJobDataSourceOverrideProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleExportJobDataSourceOverrideProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleExportJobDataSourceOverrideProperties)

---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftPropertiesOutput.html
---

# RedshiftPropertiesOutput
<a name="API_RedshiftPropertiesOutput"></a>

The Amazon Redshift properties.

## Contents
<a name="API_RedshiftPropertiesOutput_Contents"></a>

 ** credentials **   <a name="datazone-Type-RedshiftPropertiesOutput-credentials"></a>
The Amazon Redshift credentials.
Type: [RedshiftCredentials](API_RedshiftCredentials.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** databaseName **   <a name="datazone-Type-RedshiftPropertiesOutput-databaseName"></a>
The Amazon Redshift database name.
Type: String
Required: No

 ** isProvisionedSecret **   <a name="datazone-Type-RedshiftPropertiesOutput-isProvisionedSecret"></a>
Specifies whether Amaon Redshift properties has a provisioned secret.
Type: Boolean
Required: No

 ** jdbcIamUrl **   <a name="datazone-Type-RedshiftPropertiesOutput-jdbcIamUrl"></a>
The jdbcIam URL of the Amazon Redshift properties.
Type: String
Required: No

 ** jdbcUrl **   <a name="datazone-Type-RedshiftPropertiesOutput-jdbcUrl"></a>
The jdbcURL of the Amazon Redshift properties.
Type: String
Required: No

 ** lineageSync **   <a name="datazone-Type-RedshiftPropertiesOutput-lineageSync"></a>
The lineage syn of the Amazon Redshift properties.
Type: [RedshiftLineageSyncConfigurationOutput](API_RedshiftLineageSyncConfigurationOutput.md) object
Required: No

 ** redshiftTempDir **   <a name="datazone-Type-RedshiftPropertiesOutput-redshiftTempDir"></a>
The redshiftTempDir of the Amazon Redshift properties.
Type: String
Required: No

 ** status **   <a name="datazone-Type-RedshiftPropertiesOutput-status"></a>
The status in the Amazon Redshift properties.
Type: String
Valid Values: `CREATING | CREATE_FAILED | DELETING | DELETE_FAILED | READY | UPDATING | UPDATE_FAILED | DELETED`
Required: No

 ** storage **   <a name="datazone-Type-RedshiftPropertiesOutput-storage"></a>
The storage in the Amazon Redshift properties.
Type: [RedshiftStorageProperties](API_RedshiftStorageProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_RedshiftPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftPropertiesOutput)

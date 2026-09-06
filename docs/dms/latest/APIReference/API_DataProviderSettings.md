---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DataProviderSettings.html
---

# DataProviderSettings
<a name="API_DataProviderSettings"></a>

Provides information that defines a data provider.

## Contents
<a name="API_DataProviderSettings_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DocDbSettings **   <a name="DMS-Type-DataProviderSettings-DocDbSettings"></a>
Provides information that defines a DocumentDB data provider.
Type: [DocDbDataProviderSettings](API_DocDbDataProviderSettings.md) object
Required: No

 ** IbmDb2LuwSettings **   <a name="DMS-Type-DataProviderSettings-IbmDb2LuwSettings"></a>
Provides information that defines an IBM DB2 LUW data provider.
Type: [IbmDb2LuwDataProviderSettings](API_IbmDb2LuwDataProviderSettings.md) object
Required: No

 ** IbmDb2zOsSettings **   <a name="DMS-Type-DataProviderSettings-IbmDb2zOsSettings"></a>
Provides information that defines an IBM DB2 for z/OS data provider.
Type: [IbmDb2zOsDataProviderSettings](API_IbmDb2zOsDataProviderSettings.md) object
Required: No

 ** MariaDbSettings **   <a name="DMS-Type-DataProviderSettings-MariaDbSettings"></a>
Provides information that defines a MariaDB data provider.
Type: [MariaDbDataProviderSettings](API_MariaDbDataProviderSettings.md) object
Required: No

 ** MicrosoftSqlServerSettings **   <a name="DMS-Type-DataProviderSettings-MicrosoftSqlServerSettings"></a>
Provides information that defines a Microsoft SQL Server data provider.
Type: [MicrosoftSqlServerDataProviderSettings](API_MicrosoftSqlServerDataProviderSettings.md) object
Required: No

 ** MongoDbSettings **   <a name="DMS-Type-DataProviderSettings-MongoDbSettings"></a>
Provides information that defines a MongoDB data provider.
Type: [MongoDbDataProviderSettings](API_MongoDbDataProviderSettings.md) object
Required: No

 ** MySqlSettings **   <a name="DMS-Type-DataProviderSettings-MySqlSettings"></a>
Provides information that defines a MySQL data provider.
Type: [MySqlDataProviderSettings](API_MySqlDataProviderSettings.md) object
Required: No

 ** OracleSettings **   <a name="DMS-Type-DataProviderSettings-OracleSettings"></a>
Provides information that defines an Oracle data provider.
Type: [OracleDataProviderSettings](API_OracleDataProviderSettings.md) object
Required: No

 ** PostgreSqlSettings **   <a name="DMS-Type-DataProviderSettings-PostgreSqlSettings"></a>
Provides information that defines a PostgreSQL data provider.
Type: [PostgreSqlDataProviderSettings](API_PostgreSqlDataProviderSettings.md) object
Required: No

 ** RedshiftSettings **   <a name="DMS-Type-DataProviderSettings-RedshiftSettings"></a>
Provides information that defines an Amazon Redshift data provider.
Type: [RedshiftDataProviderSettings](API_RedshiftDataProviderSettings.md) object
Required: No

 ** SybaseAseSettings **   <a name="DMS-Type-DataProviderSettings-SybaseAseSettings"></a>
Provides information that defines an SAP ASE data provider.
Type: [SybaseAseDataProviderSettings](API_SybaseAseDataProviderSettings.md) object
Required: No

## See Also
<a name="API_DataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DataProviderSettings)

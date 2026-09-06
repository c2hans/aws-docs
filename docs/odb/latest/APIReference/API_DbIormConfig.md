---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_DbIormConfig.html
---

# DbIormConfig
<a name="API_DbIormConfig"></a>

The IORM configuration settings for the database.

## Contents
<a name="API_DbIormConfig_Contents"></a>

 ** dbName **   <a name="odb-Type-DbIormConfig-dbName"></a>
The database name. For the default DbPlan, the dbName is `default`.
Type: String
Required: No

 ** flashCacheLimit **   <a name="odb-Type-DbIormConfig-flashCacheLimit"></a>
The flash cache limit for this database. This value is internally configured based on the share value assigned to the database.
Type: String
Required: No

 ** share **   <a name="odb-Type-DbIormConfig-share"></a>
The relative priority of this database.
Type: Integer
Required: No

## See Also
<a name="API_DbIormConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/DbIormConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/DbIormConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/DbIormConfig)

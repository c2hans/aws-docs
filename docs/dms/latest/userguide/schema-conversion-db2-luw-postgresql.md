---
source_url: https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-luw-postgresql.html
---

# IBM Db2 for LUW to Amazon RDS for PostgreSQL conversion settings
<a name="schema-conversion-db2-luw-postgresql"></a>

**Important**
You cannot use the AWS Management Console to create or configure migration projects for the IBM Db2 for LUW to Amazon RDS for PostgreSQL conversion path. To configure the target engine version, use the AWS CLI or the AWS Database Migration Service API.

The IBM Db2 for LUW to Amazon RDS for PostgreSQL conversion path has no pair-specific conversion settings other than the target engine version. The following section describes that setting.

DMS Schema Conversion also provides common settings that apply to every conversion path. Examples include the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

To configure the target engine version, use the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation or the AWS CLI. To find the current value, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first.

`DB2LUW_TO_POSTGRESQL_target_engine_version`
Specifies the PostgreSQL major version feature set that DMS Schema Conversion targets for conversion. The value `15` targets the features of PostgreSQL 15 and later versions. The value `14` targets the features of PostgreSQL 14. Your target database can run a later version than the value you choose. For example, you can specify `15` for a PostgreSQL 16 target. This setting is stored in the top-level `Conversion version` section, as shown in the following example.

```
{
  "Conversion version": {
    "DB2LUW_TO_POSTGRESQL_target_engine_version": "15"
  }
}
```
**Type:** String (`14` \| `15`)
**Default:** `15`

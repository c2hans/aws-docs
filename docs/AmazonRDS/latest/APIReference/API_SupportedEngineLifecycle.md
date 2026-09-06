---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SupportedEngineLifecycle.html
---

# SupportedEngineLifecycle
<a name="API_SupportedEngineLifecycle"></a>

This data type is used as a response element in the operation `DescribeDBMajorEngineVersions`.

You can use the information that this data type returns to plan for upgrades.

This data type only returns information for the open source engines Amazon RDS for MariaDB, Amazon RDS for MySQL, Amazon RDS for PostgreSQL, Aurora MySQL, and Aurora PostgreSQL.

## Contents
<a name="API_SupportedEngineLifecycle_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LifecycleSupportEndDate **
The end date for the type of support returned by `LifecycleSupportName`.
Type: Timestamp
Required: Yes

 ** LifecycleSupportName **
The type of lifecycle support that the engine version is in.
This parameter returns the following values:
+  `open-source-rds-standard-support` - Indicates RDS standard support or Aurora standard support.
+  `open-source-rds-extended-support` - Indicates Amazon RDS Extended Support.
For Amazon RDS for MySQL, Amazon RDS for PostgreSQL, Aurora MySQL, and Aurora PostgreSQL, this parameter returns both `open-source-rds-standard-support` and `open-source-rds-extended-support`.
For Amazon RDS for MariaDB, this parameter only returns the value `open-source-rds-standard-support`.
For information about Amazon RDS Extended Support, see [Amazon RDS Extended Support with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html) in the *Amazon RDS User Guide* and [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html) in the *Amazon Aurora User Guide*.
Type: String
Valid Values: `open-source-rds-standard-support | open-source-rds-extended-support`
Required: Yes

 ** LifecycleSupportStartDate **
The start date for the type of support returned by `LifecycleSupportName`.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SupportedEngineLifecycle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/SupportedEngineLifecycle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/SupportedEngineLifecycle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/SupportedEngineLifecycle)

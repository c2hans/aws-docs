---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceDescription.html
---

# DatabaseSourceDescription
<a name="API_DatabaseSourceDescription"></a>

 The top level object for database source description.

Amazon Data Firehose is in preview release and is subject to change.

## Contents
<a name="API_DatabaseSourceDescription_Contents"></a>

 ** Columns **   <a name="Firehose-Type-DatabaseSourceDescription-Columns"></a>
 The list of column patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseColumnList](API_DatabaseColumnList.md) object
Required: No

 ** Databases **   <a name="Firehose-Type-DatabaseSourceDescription-Databases"></a>
 The list of database patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseList](API_DatabaseList.md) object
Required: No

 ** DatabaseSourceAuthenticationConfiguration **   <a name="Firehose-Type-DatabaseSourceDescription-DatabaseSourceAuthenticationConfiguration"></a>
 The structure to configure the authentication methods for Firehose to connect to source database endpoint.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseSourceAuthenticationConfiguration](API_DatabaseSourceAuthenticationConfiguration.md) object
Required: No

 ** DatabaseSourceVPCConfiguration **   <a name="Firehose-Type-DatabaseSourceDescription-DatabaseSourceVPCConfiguration"></a>
 The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseSourceVPCConfiguration](API_DatabaseSourceVPCConfiguration.md) object
Required: No

 ** Endpoint **   <a name="Firehose-Type-DatabaseSourceDescription-Endpoint"></a>
 The endpoint of the database server.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(?!\s*$).+`
Required: No

 ** Port **   <a name="Firehose-Type-DatabaseSourceDescription-Port"></a>
The port of the database. This can be one of the following values.
+ 3306 for MySQL database type
+ 5432 for PostgreSQL database type
Amazon Data Firehose is in preview release and is subject to change.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** SnapshotInfo **   <a name="Firehose-Type-DatabaseSourceDescription-SnapshotInfo"></a>
 The structure that describes the snapshot information of a table in source database endpoint that Firehose reads.
Amazon Data Firehose is in preview release and is subject to change.
Type: Array of [DatabaseSnapshotInfo](API_DatabaseSnapshotInfo.md) objects
Required: No

 ** SnapshotWatermarkTable **   <a name="Firehose-Type-DatabaseSourceDescription-SnapshotWatermarkTable"></a>
 The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 129.
Pattern: `[\u0001-\uFFFF]*`
Required: No

 ** SSLMode **   <a name="Firehose-Type-DatabaseSourceDescription-SSLMode"></a>
 The mode to enable or disable SSL when Firehose connects to the database endpoint.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Valid Values: `Disabled | Enabled`
Required: No

 ** SurrogateKeys **   <a name="Firehose-Type-DatabaseSourceDescription-SurrogateKeys"></a>
 The optional list of table and column names used as unique key columns when taking snapshot if the tables don’t have primary keys configured.
Amazon Data Firehose is in preview release and is subject to change.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 194.
Pattern: `[\u0001-\uFFFF]*`
Required: No

 ** Tables **   <a name="Firehose-Type-DatabaseSourceDescription-Tables"></a>
 The list of table patterns in source database endpoint for Firehose to read from.
Amazon Data Firehose is in preview release and is subject to change.
Type: [DatabaseTableList](API_DatabaseTableList.md) object
Required: No

 ** Type **   <a name="Firehose-Type-DatabaseSourceDescription-Type"></a>
The type of database engine. This can be one of the following values.
+ MySQL
+ PostgreSQL
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Valid Values: `MySQL | PostgreSQL`
Required: No

## See Also
<a name="API_DatabaseSourceDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DatabaseSourceDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DatabaseSourceDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DatabaseSourceDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

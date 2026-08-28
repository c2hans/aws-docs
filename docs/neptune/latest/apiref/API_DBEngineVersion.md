---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBEngineVersion.html
---

# DBEngineVersion
<a name="API_DBEngineVersion"></a>

 This data type is used as a response element in the action [DescribeDBEngineVersions](API_DescribeDBEngineVersions.md).

## Contents
<a name="API_DBEngineVersion_Contents"></a>

 ** DBEngineDescription **
The description of the database engine.
Type: String
Required: No

 ** DBEngineVersionDescription **
The description of the database engine version.
Type: String
Required: No

 ** DBParameterGroupFamily **
The name of the DB parameter group family for the database engine.
Type: String
Required: No

 ** DefaultCharacterSet **
 *(Not supported by Neptune)*
Type: [CharacterSet](API_CharacterSet.md) object
Required: No

 ** Engine **
The name of the database engine.
Type: String
Required: No

 ** EngineVersion **
The version number of the database engine.
Type: String
Required: No

 ** ExportableLogTypes.member.N **
The types of logs that the database engine has available for export to CloudWatch Logs.
Type: Array of strings
Required: No

 ** SupportedCharacterSets.CharacterSet.N **
 *(Not supported by Neptune)*
Type: Array of [CharacterSet](API_CharacterSet.md) objects
Required: No

 ** SupportedTimezones.Timezone.N **
A list of the time zones supported by this engine for the `Timezone` parameter of the `CreateDBInstance` action.
Type: Array of [Timezone](API_Timezone.md) objects
Required: No

 ** SupportsGlobalDatabases **
A value that indicates whether you can use Aurora global databases with a specific DB engine version.
Type: Boolean
Required: No

 ** SupportsLogExportsToCloudwatchLogs **
A value that indicates whether the engine version supports exporting the log types specified by ExportableLogTypes to CloudWatch Logs.
Type: Boolean
Required: No

 ** SupportsReadReplica **
Indicates whether the database engine version supports read replicas.
Type: Boolean
Required: No

 ** ValidUpgradeTarget.UpgradeTarget.N **
A list of engine versions that this database engine version can be upgraded to.
Type: Array of [UpgradeTarget](API_UpgradeTarget.md) objects
Required: No

## See Also
<a name="API_DBEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBEngineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBEngineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBEngineVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

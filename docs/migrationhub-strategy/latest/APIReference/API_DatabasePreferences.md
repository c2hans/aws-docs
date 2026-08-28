---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_DatabasePreferences.html
---

# DatabasePreferences
<a name="API_DatabasePreferences"></a>

 Preferences on managing your databases on AWS.

## Contents
<a name="API_DatabasePreferences_Contents"></a>

 ** databaseManagementPreference **   <a name="migrationhubstrategy-Type-DatabasePreferences-databaseManagementPreference"></a>
 Specifies whether you're interested in self-managed databases or databases managed by AWS.
Type: String
Valid Values: `AWS-managed | Self-manage | No preference`
Required: No

 ** databaseMigrationPreference **   <a name="migrationhubstrategy-Type-DatabasePreferences-databaseMigrationPreference"></a>
 Specifies your preferred migration path.
Type: [DatabaseMigrationPreference](API_DatabaseMigrationPreference.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_DatabasePreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/DatabasePreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/DatabasePreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/DatabasePreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

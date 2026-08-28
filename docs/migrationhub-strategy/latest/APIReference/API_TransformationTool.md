---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_TransformationTool.html
---

# TransformationTool
<a name="API_TransformationTool"></a>

 Information of the transformation tool that can be used to migrate and modernize the application.

## Contents
<a name="API_TransformationTool_Contents"></a>

 ** description **   <a name="migrationhubstrategy-Type-TransformationTool-description"></a>
 Description of the tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** name **   <a name="migrationhubstrategy-Type-TransformationTool-name"></a>
 Name of the tool.
Type: String
Valid Values: `App2Container | Porting Assistant For .NET | End of Support Migration | Windows Web Application Migration Assistant | Application Migration Service | Strategy Recommendation Support | In Place Operating System Upgrade | Schema Conversion Tool | Database Migration Service | Native SQL Server Backup/Restore`
Required: No

 ** tranformationToolInstallationLink **   <a name="migrationhubstrategy-Type-TransformationTool-tranformationToolInstallationLink"></a>
 URL for installing the tool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_TransformationTool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/TransformationTool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/TransformationTool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/TransformationTool)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

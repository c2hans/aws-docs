---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_SystemInfo.html
---

# SystemInfo
<a name="API_SystemInfo"></a>

 Information about the server that hosts application components.

## Contents
<a name="API_SystemInfo_Contents"></a>

 ** cpuArchitecture **   <a name="migrationhubstrategy-Type-SystemInfo-cpuArchitecture"></a>
 CPU architecture type for the server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** fileSystemType **   <a name="migrationhubstrategy-Type-SystemInfo-fileSystemType"></a>
 File system type for the server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** networkInfoList **   <a name="migrationhubstrategy-Type-SystemInfo-networkInfoList"></a>
 Networking information related to a server.
Type: Array of [NetworkInfo](API_NetworkInfo.md) objects
Required: No

 ** osInfo **   <a name="migrationhubstrategy-Type-SystemInfo-osInfo"></a>
 Operating system corresponding to a server.
Type: [OSInfo](API_OSInfo.md) object
Required: No

## See Also
<a name="API_SystemInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/SystemInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/SystemInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/SystemInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

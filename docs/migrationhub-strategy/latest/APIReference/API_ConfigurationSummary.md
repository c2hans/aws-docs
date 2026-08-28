---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ConfigurationSummary.html
---

# ConfigurationSummary
<a name="API_ConfigurationSummary"></a>

Summary of the collector configuration.

## Contents
<a name="API_ConfigurationSummary_Contents"></a>

 ** ipAddressBasedRemoteInfoList **   <a name="migrationhubstrategy-Type-ConfigurationSummary-ipAddressBasedRemoteInfoList"></a>
IP address based configurations.
Type: Array of [IPAddressBasedRemoteInfo](API_IPAddressBasedRemoteInfo.md) objects
Required: No

 ** pipelineInfoList **   <a name="migrationhubstrategy-Type-ConfigurationSummary-pipelineInfoList"></a>
The list of pipeline info configurations.
Type: Array of [PipelineInfo](API_PipelineInfo.md) objects
Required: No

 ** remoteSourceCodeAnalysisServerInfo **   <a name="migrationhubstrategy-Type-ConfigurationSummary-remoteSourceCodeAnalysisServerInfo"></a>
Info about the remote server source code configuration.
Type: [RemoteSourceCodeAnalysisServerInfo](API_RemoteSourceCodeAnalysisServerInfo.md) object
Required: No

 ** vcenterBasedRemoteInfoList **   <a name="migrationhubstrategy-Type-ConfigurationSummary-vcenterBasedRemoteInfoList"></a>
The list of vCenter configurations.
Type: Array of [VcenterBasedRemoteInfo](API_VcenterBasedRemoteInfo.md) objects
Required: No

 ** versionControlInfoList **   <a name="migrationhubstrategy-Type-ConfigurationSummary-versionControlInfoList"></a>
The list of the version control configurations.
Type: Array of [VersionControlInfo](API_VersionControlInfo.md) objects
Required: No

## See Also
<a name="API_ConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ConfigurationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

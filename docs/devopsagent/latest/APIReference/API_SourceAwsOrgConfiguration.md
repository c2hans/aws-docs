---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SourceAwsOrgConfiguration.html
---

# SourceAwsOrgConfiguration

Configuration for AWS Organization-wide source account integration. Use this configuration to monitor AWS resources across multiple accounts within an organization or within targeted organizational units.

## Contents
<a name="API_SourceAwsOrgConfiguration_Contents"></a>

 ** accountType **   <a name="devopsagent-Type-SourceAwsOrgConfiguration-accountType"></a>
The account type for this configuration. For AWS Organization-level configurations, this value is `source`.
Type: String
Valid Values: `source`
Required: Yes

 ** organizationalUnit **   <a name="devopsagent-Type-SourceAwsOrgConfiguration-organizationalUnit"></a>
The organizational units within the AWS Organization that are targeted for source monitoring.
Type: [SourceAwsOrgUnit](API_SourceAwsOrgUnit.md) object
Required: Yes

 ** deploymentState **   <a name="devopsagent-Type-SourceAwsOrgConfiguration-deploymentState"></a>
The current deployment state of the AWS Organization-wide source configuration.
Type: [OrgSourceDeploymentState](API_OrgSourceDeploymentState.md) object
Required: No

## See Also
<a name="API_SourceAwsOrgConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/SourceAwsOrgConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/SourceAwsOrgConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/SourceAwsOrgConfiguration)

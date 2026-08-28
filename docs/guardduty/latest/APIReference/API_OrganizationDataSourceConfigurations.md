---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_OrganizationDataSourceConfigurations.html
---

# OrganizationDataSourceConfigurations
<a name="API_OrganizationDataSourceConfigurations"></a>

An object that contains information on which data sources will be configured to be automatically enabled for new members within the organization.

## Contents
<a name="API_OrganizationDataSourceConfigurations_Contents"></a>

 ** kubernetes **   <a name="guardduty-Type-OrganizationDataSourceConfigurations-kubernetes"></a>
Describes the configuration of Kubernetes data sources for new members of the organization.
Type: [OrganizationKubernetesConfiguration](API_OrganizationKubernetesConfiguration.md) object
Required: No

 ** malwareProtection **   <a name="guardduty-Type-OrganizationDataSourceConfigurations-malwareProtection"></a>
Describes the configuration of Malware Protection for new members of the organization.
Type: [OrganizationMalwareProtectionConfiguration](API_OrganizationMalwareProtectionConfiguration.md) object
Required: No

 ** s3Logs **   <a name="guardduty-Type-OrganizationDataSourceConfigurations-s3Logs"></a>
Describes whether S3 data event logs are enabled for new members of the organization.
Type: [OrganizationS3LogsConfiguration](API_OrganizationS3LogsConfiguration.md) object
Required: No

## See Also
<a name="API_OrganizationDataSourceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/OrganizationDataSourceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/OrganizationDataSourceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/OrganizationDataSourceConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

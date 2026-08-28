---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ProviderConfiguration.html
---

# ProviderConfiguration
<a name="API_ProviderConfiguration"></a>

The initial configuration settings required to establish an integration between Security Hub and third-party provider.

## Contents
<a name="API_ProviderConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Azure **   <a name="securityhub-Type-ProviderConfiguration-Azure"></a>
The configuration settings required to establish a CSPM integration with Microsoft Azure.
Type: [AzureProviderConfiguration](API_AzureProviderConfiguration.md) object
Required: No

 ** JiraCloud **   <a name="securityhub-Type-ProviderConfiguration-JiraCloud"></a>
The configuration settings required to establish an integration with Jira Cloud.
Type: [JiraCloudProviderConfiguration](API_JiraCloudProviderConfiguration.md) object
Required: No

 ** ServiceNow **   <a name="securityhub-Type-ProviderConfiguration-ServiceNow"></a>
The configuration settings required to establish an integration with ServiceNow ITSM.
Type: [ServiceNowProviderConfiguration](API_ServiceNowProviderConfiguration.md) object
Required: No

## See Also
<a name="API_ProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ProviderConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

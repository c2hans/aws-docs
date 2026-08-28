---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AzureProviderConfiguration.html
---

# AzureProviderConfiguration
<a name="API_AzureProviderConfiguration"></a>

The configuration for connecting to an Azure environment.

## Contents
<a name="API_AzureProviderConfiguration_Contents"></a>

 ** AWSConfigConnectorArn **   <a name="securityhub-Type-AzureProviderConfiguration-AWSConfigConnectorArn"></a>
The ARN of the multi-cloud configuration connector used to establish the connection to Azure.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** AzureRegions **   <a name="securityhub-Type-AzureProviderConfiguration-AzureRegions"></a>
The list of Azure regions to monitor.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: Yes

 ** ScopeConfiguration **   <a name="securityhub-Type-AzureProviderConfiguration-ScopeConfiguration"></a>
The scope configuration that defines which Azure resources are monitored.
Type: [AzureScopeConfiguration](API_AzureScopeConfiguration.md) object
Required: Yes

## See Also
<a name="API_AzureProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AzureProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AzureProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AzureProviderConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

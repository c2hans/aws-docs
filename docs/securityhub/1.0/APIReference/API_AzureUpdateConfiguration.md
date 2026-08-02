---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AzureUpdateConfiguration.html
---

# AzureUpdateConfiguration
<a name="API_AzureUpdateConfiguration"></a>

The configuration for updating an Azure connector's scope and regions.

## Contents
<a name="API_AzureUpdateConfiguration_Contents"></a>

 ** AzureRegions **   <a name="securityhub-Type-AzureUpdateConfiguration-AzureRegions"></a>
The updated list of Azure regions to monitor.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: Yes

 ** ScopeConfiguration **   <a name="securityhub-Type-AzureUpdateConfiguration-ScopeConfiguration"></a>
The updated scope configuration.
Type: [AzureScopeConfiguration](API_AzureScopeConfiguration.md) object
Required: Yes

## See Also
<a name="API_AzureUpdateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AzureUpdateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AzureUpdateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AzureUpdateConfiguration)

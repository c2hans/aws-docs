---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AzureDetail.html
---

# AzureDetail
<a name="API_AzureDetail"></a>

The detailed Azure configuration for a connector.

## Contents
<a name="API_AzureDetail_Contents"></a>

 ** AWSConfigConnectorArn **   <a name="securityhub-Type-AzureDetail-AWSConfigConnectorArn"></a>
The ARN of the multi-cloud configuration connector used to establish the connection to Azure.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** AzureRegions **   <a name="securityhub-Type-AzureDetail-AzureRegions"></a>
The list of Azure regions being monitored.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: Yes

 ** ScopeConfiguration **   <a name="securityhub-Type-AzureDetail-ScopeConfiguration"></a>
The scope configuration that defines which Azure resources are monitored.
Type: [AzureScopeConfiguration](API_AzureScopeConfiguration.md) object
Required: Yes

## See Also
<a name="API_AzureDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AzureDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AzureDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AzureDetail)

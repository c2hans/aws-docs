---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ProviderDetail.html
---

# ProviderDetail
<a name="API_ProviderDetail"></a>

The third-party provider detail for a service configuration.

## Contents
<a name="API_ProviderDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Azure **   <a name="securityhub-Type-ProviderDetail-Azure"></a>
Details about a Microsoft Azure CSPM integration.
Type: [AzureDetail](API_AzureDetail.md) object
Required: No

 ** JiraCloud **   <a name="securityhub-Type-ProviderDetail-JiraCloud"></a>
Details about a Jira Cloud integration.
Type: [JiraCloudDetail](API_JiraCloudDetail.md) object
Required: No

 ** ServiceNow **   <a name="securityhub-Type-ProviderDetail-ServiceNow"></a>
Details about a ServiceNow ITSM integration.
Type: [ServiceNowDetail](API_ServiceNowDetail.md) object
Required: No

## See Also
<a name="API_ProviderDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ProviderDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ProviderDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ProviderDetail)

---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CloudConnectorFilter.html
---

# CloudConnectorFilter
<a name="API_CloudConnectorFilter"></a>

A filter for listing cloud connectors.

## Contents
<a name="API_CloudConnectorFilter_Contents"></a>

 ** FilterKey **   <a name="systemsmanager-Type-CloudConnectorFilter-FilterKey"></a>
The name of the filter key.
Type: String
Valid Values: `SubscriptionId | TenantId`
Required: No

 ** FilterValues **   <a name="systemsmanager-Type-CloudConnectorFilter-FilterValues"></a>
The filter values. Valid values for each filter key are as follows:
SubscriptionId
The Azure subscription ID to filter by. To return only tenant-level connectors, specify `NONE`.
TenantId
The Azure tenant ID to filter by. Filters the results to connectors that target the specified tenant.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CloudConnectorFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/CloudConnectorFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/CloudConnectorFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/CloudConnectorFilter)

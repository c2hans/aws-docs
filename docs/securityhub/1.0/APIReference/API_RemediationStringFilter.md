---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RemediationStringFilter.html
---

# RemediationStringFilter
<a name="API_RemediationStringFilter"></a>

A string filter for filtering remediation targets.

## Contents
<a name="API_RemediationStringFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-RemediationStringFilter-FieldName"></a>
The name of the filter field. Valid values are `Resource.Type`, `Priority`, `Status`, `Resource.Id`, `Resource.ResourceOwnerAccountId`, and `Resource.CloudProvider`.
Type: String
Valid Values: `Resource.Type | Priority | Status | Resource.Id | Resource.ResourceOwnerAccountId | Resource.CloudProvider`
Required: Yes

 ** Filter **   <a name="securityhub-Type-RemediationStringFilter-Filter"></a>
The string filter definition.
Type: [RemediationStringFilterCondition](API_RemediationStringFilterCondition.md) object
Required: Yes

## See Also
<a name="API_RemediationStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RemediationStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RemediationStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RemediationStringFilter)

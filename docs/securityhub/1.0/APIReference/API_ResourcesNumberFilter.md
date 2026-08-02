---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesNumberFilter.html
---

# ResourcesNumberFilter
<a name="API_ResourcesNumberFilter"></a>

Enables filtering of AWS resources based on numerical values.

## Contents
<a name="API_ResourcesNumberFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-ResourcesNumberFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `FindingsSummary.TotalFindings | FindingsSummary.Severities.Other | FindingsSummary.Severities.Fatal | FindingsSummary.Severities.Critical | FindingsSummary.Severities.High | FindingsSummary.Severities.Medium | FindingsSummary.Severities.Low | FindingsSummary.Severities.Informational | FindingsSummary.Severities.Unknown | ResourceInfo.AIDetails.SelfHostedAIModelResourceCount | ResourceInfo.AIDetails.SelfHostedAIAgentResourceCount | ResourceInfo.AIDetails.SelfHostedAIModelServingResourceCount | ResourceInfo.AIDetails.SelfHostedAIExternalEndpointResourceCount | ResourceInfo.AIDetails.SelfHostedAIDevelopmentResourceCount | ResourceInfo.AIDetails.SelfHostedAIAgentFrameworkResourceCount | ResourceInfo.AIDetails.SelfHostedAIAgentToolsAndIdentityResourceCount | ResourceInfo.AIDetails.SelfHostedTotalAIResourceCount`
Required: No

 ** Filter **   <a name="securityhub-Type-ResourcesNumberFilter-Filter"></a>
A number filter for querying findings.
Type: [NumberFilter](API_NumberFilter.md) object
Required: No

## See Also
<a name="API_ResourcesNumberFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesNumberFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesNumberFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesNumberFilter)

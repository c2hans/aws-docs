---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_OrganizationAggregationSource.html
---

# OrganizationAggregationSource
<a name="API_OrganizationAggregationSource"></a>

This object contains regions to set up the aggregator and an IAM role to retrieve organization details.

## Contents
<a name="API_OrganizationAggregationSource_Contents"></a>

 ** RoleArn **   <a name="config-Type-OrganizationAggregationSource-RoleArn"></a>
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.
Type: String
Required: Yes

 ** AllAwsRegions **   <a name="config-Type-OrganizationAggregationSource-AllAwsRegions"></a>
If true, aggregate existing AWS Config regions and future regions.
Type: Boolean
Required: No

 ** AwsRegions **   <a name="config-Type-OrganizationAggregationSource-AwsRegions"></a>
The source regions being aggregated.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_OrganizationAggregationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/OrganizationAggregationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/OrganizationAggregationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/OrganizationAggregationSource)

---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_FrameworkFilters.html
---

# FrameworkFilters
<a name="API_FrameworkFilters"></a>

Framework-specific filters used to scope `ListAssessments` results. Set exactly one member, corresponding to the framework you want to filter by.

## Contents
<a name="API_FrameworkFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AMISecurityFilters **   <a name="AWSMarketplaceService-Type-FrameworkFilters-AMISecurityFilters"></a>
Filters that apply to assessments performed against the AMI Security framework.
Type: [AMISecurityFilters](API_AMISecurityFilters.md) object
Required: No

 ** ContainerSecurityFilters **   <a name="AWSMarketplaceService-Type-FrameworkFilters-ContainerSecurityFilters"></a>
Filters that apply to assessments performed against the Container Security framework.
Type: [ContainerSecurityFilters](API_ContainerSecurityFilters.md) object
Required: No

## See Also
<a name="API_FrameworkFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/FrameworkFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/FrameworkFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/FrameworkFilters)

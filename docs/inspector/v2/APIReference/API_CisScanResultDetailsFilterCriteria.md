---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CisScanResultDetailsFilterCriteria.html
---

# CisScanResultDetailsFilterCriteria
<a name="API_CisScanResultDetailsFilterCriteria"></a>

The CIS scan result details filter criteria.

## Contents
<a name="API_CisScanResultDetailsFilterCriteria_Contents"></a>

 ** checkIdFilters **   <a name="inspector2-Type-CisScanResultDetailsFilterCriteria-checkIdFilters"></a>
The criteria's check ID filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** findingArnFilters **   <a name="inspector2-Type-CisScanResultDetailsFilterCriteria-findingArnFilters"></a>
The criteria's finding ARN filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** findingStatusFilters **   <a name="inspector2-Type-CisScanResultDetailsFilterCriteria-findingStatusFilters"></a>
The criteria's finding status filters.
Type: Array of [CisFindingStatusFilter](API_CisFindingStatusFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** securityLevelFilters **   <a name="inspector2-Type-CisScanResultDetailsFilterCriteria-securityLevelFilters"></a>
 The criteria's security level filters. . Security level refers to the Benchmark levels that CIS assigns to a profile.
Type: Array of [CisSecurityLevelFilter](API_CisSecurityLevelFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** titleFilters **   <a name="inspector2-Type-CisScanResultDetailsFilterCriteria-titleFilters"></a>
The criteria's title filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CisScanResultDetailsFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CisScanResultDetailsFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CisScanResultDetailsFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CisScanResultDetailsFilterCriteria)

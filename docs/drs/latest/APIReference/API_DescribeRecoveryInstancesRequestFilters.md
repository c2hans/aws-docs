---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoveryInstancesRequestFilters.html
---

# DescribeRecoveryInstancesRequestFilters
<a name="API_DescribeRecoveryInstancesRequestFilters"></a>

A set of filters by which to return Recovery Instances.

## Contents
<a name="API_DescribeRecoveryInstancesRequestFilters_Contents"></a>

 ** recoveryInstanceIDs **   <a name="drs-Type-DescribeRecoveryInstancesRequestFilters-recoveryInstanceIDs"></a>
An array of Recovery Instance IDs that should be returned. An empty array means all Recovery Instances.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** sourceServerIDs **   <a name="drs-Type-DescribeRecoveryInstancesRequestFilters-sourceServerIDs"></a>
An array of Source Server IDs for which associated Recovery Instances should be returned.
Type: Array of strings
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_DescribeRecoveryInstancesRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeRecoveryInstancesRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeRecoveryInstancesRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeRecoveryInstancesRequestFilters)

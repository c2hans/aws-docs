---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DescribeJobsRequestFilters.html
---

# DescribeJobsRequestFilters
<a name="API_DescribeJobsRequestFilters"></a>

Request to describe Job log filters.

## Contents
<a name="API_DescribeJobsRequestFilters_Contents"></a>

 ** fromDate **   <a name="mgn-Type-DescribeJobsRequestFilters-fromDate"></a>
Request to describe Job log filters by date.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** jobIDs **   <a name="mgn-Type-DescribeJobsRequestFilters-jobIDs"></a>
Request to describe Job log filters by job ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Fixed length of 24.
Pattern: `mgnjob-[0-9a-zA-Z]{17}`
Required: No

 ** toDate **   <a name="mgn-Type-DescribeJobsRequestFilters-toDate"></a>
Request to describe job log items by last date.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_DescribeJobsRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DescribeJobsRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DescribeJobsRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DescribeJobsRequestFilters)

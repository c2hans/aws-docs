---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoverySnapshotsRequestFilters.html
---

# DescribeRecoverySnapshotsRequestFilters
<a name="API_DescribeRecoverySnapshotsRequestFilters"></a>

A set of filters by which to return Recovery Snapshots.

## Contents
<a name="API_DescribeRecoverySnapshotsRequestFilters_Contents"></a>

 ** fromDateTime **   <a name="drs-Type-DescribeRecoverySnapshotsRequestFilters-fromDateTime"></a>
The start date in a date range query.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** toDateTime **   <a name="drs-Type-DescribeRecoverySnapshotsRequestFilters-toDateTime"></a>
The end date in a date range query.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

## See Also
<a name="API_DescribeRecoverySnapshotsRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DescribeRecoverySnapshotsRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DescribeRecoverySnapshotsRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DescribeRecoverySnapshotsRequestFilters)

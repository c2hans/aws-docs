---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_SolutionSort.html
---

# SolutionSort
<a name="API_SolutionSort"></a>

Configures the solutions' response sorting that enables partners to order solutions based on specified attributes.

## Contents
<a name="API_SolutionSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSPartnerCentral-Type-SolutionSort-SortBy"></a>
Specifies the attribute to sort by, such as `Name`, `CreatedDate`, or `Status`.
Type: String
Valid Values: `Identifier | Name | Status | Category | CreatedDate`
Required: Yes

 ** SortOrder **   <a name="AWSPartnerCentral-Type-SolutionSort-SortOrder"></a>
Specifies the sorting order, either `Ascending` or `Descending`. The default is `Descending`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: Yes

## See Also
<a name="API_SolutionSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/SolutionSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/SolutionSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/SolutionSort)

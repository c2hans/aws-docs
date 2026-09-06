---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchJobsFilter.html
---

# SearchJobsFilter
<a name="API_SearchJobsFilter"></a>

A filter used to search for Amazon Braket hybrid jobs. You can combine multiple filters in a single request, except that `jobArn` cannot be combined with any other filter.

## Contents
<a name="API_SearchJobsFilter_Contents"></a>

 ** name **   <a name="braket-Type-SearchJobsFilter-name"></a>
The name of the hybrid job parameter to filter based on. Supported filter names:
 `jobArn` — Filter by the job ARN. Supports the `EQUAL` operator only. Cannot be combined with other filters.
 `jobName` — Filter by the job name. Supports the `EQUAL` operator for exact match, or the `CONTAINS` operator for substring match. For example, use `CONTAINS` with a value of `my-experiment` to find all jobs whose name includes "my-experiment".
 `deviceArn` — Filter by the target device. Supports the `EQUAL` operator only. The value can be a device ARN (for example, `arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1`) or a local simulator identifier (for example, `local:braket/default`).
 `createdAt` — Filter by the job creation time. Supports the `EQUAL`, `GT`, `GTE`, `LT`, `LTE`, and `BETWEEN` operators. Values must be in RFC 3339 date-time format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** operator **   <a name="braket-Type-SearchJobsFilter-operator"></a>
An operator to use for the filter. The supported operators depend on the filter name. See the `name` parameter for details.
Type: String
Valid Values: `LT | LTE | EQUAL | GT | GTE | BETWEEN | CONTAINS`
Required: Yes

 ** values **   <a name="braket-Type-SearchJobsFilter-values"></a>
The values used to filter hybrid jobs based on the filter name and operator. Each filter accepts an array of values. Most filters accept a single value, except `createdAt` with the `BETWEEN` operator, which requires exactly two values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SearchJobsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchJobsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchJobsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchJobsFilter)

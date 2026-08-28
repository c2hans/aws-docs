---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A search filter in Amazon DataZone.

## Contents
<a name="API_Filter_Contents"></a>

 ** attribute **   <a name="datazone-Type-Filter-attribute"></a>
A search filter attribute in Amazon DataZone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** intValue **   <a name="datazone-Type-Filter-intValue"></a>
A search filter integer value in Amazon DataZone.
Type: Long
Required: No

 ** operator **   <a name="datazone-Type-Filter-operator"></a>
Specifies the search filter operator.
Type: String
Valid Values: `EQ | LE | LT | GE | GT | TEXT_SEARCH`
Required: No

 ** value **   <a name="datazone-Type-Filter-value"></a>
A search filter string value in Amazon DataZone.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

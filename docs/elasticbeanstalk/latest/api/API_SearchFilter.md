---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_SearchFilter.html
---

# SearchFilter
<a name="API_SearchFilter"></a>

Describes criteria to restrict a list of results.

For operators that apply a single value to the attribute, the filter is evaluated as follows: `Attribute Operator Values[1]`

Some operators, e.g. `in`, can apply multiple values. In this case, the filter is evaluated as a logical union (OR) of applications of the operator to the attribute with each one of the values: `(Attribute Operator Values[1]) OR (Attribute Operator Values[2]) OR ...`

The valid values for attributes of `SearchFilter` depend on the API action. For valid values, see the reference page for the API action you're calling that takes a `SearchFilter` parameter.

## Contents
<a name="API_SearchFilter_Contents"></a>

 ** Attribute **
The result attribute to which the filter values are applied. Valid values vary by API action.
Type: String
Required: No

 ** Operator **
The operator to apply to the `Attribute` with each of the `Values`. Valid values vary by `Attribute`.
Type: String
Required: No

 ** Values.member.N **
The list of values applied to the `Attribute` and `Operator` attributes. Number of values and valid values vary by `Attribute`.
Type: Array of strings
Required: No

## See Also
<a name="API_SearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/SearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/SearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/SearchFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

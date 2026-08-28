---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Contains information on a recommendation filter, including its ARN, status, and filter expression.

## Contents
<a name="API_Filter_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-Filter-creationDateTime"></a>
The time at which the filter was created.
Type: Timestamp
Required: No

 ** datasetGroupArn **   <a name="personalize-Type-Filter-datasetGroupArn"></a>
The ARN of the dataset group to which the filter belongs.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`
Required: No

 ** failureReason **   <a name="personalize-Type-Filter-failureReason"></a>
If the filter failed, the reason for its failure.
Type: String
Required: No

 ** filterArn **   <a name="personalize-Type-Filter-filterArn"></a>
The ARN of the filter.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`
Required: No

 ** filterExpression **   <a name="personalize-Type-Filter-filterExpression"></a>
Specifies the type of item interactions to filter out of recommendation results. The filter expression must follow specific format rules. For information about filter expression structure and syntax, see [Filter expressions](https://docs.aws.amazon.com/personalize/latest/dg/filter-expressions.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-Filter-lastUpdatedDateTime"></a>
The time at which the filter was last updated.
Type: Timestamp
Required: No

 ** name **   <a name="personalize-Type-Filter-name"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
Required: No

 ** status **   <a name="personalize-Type-Filter-status"></a>
The status of the filter.
Type: String
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

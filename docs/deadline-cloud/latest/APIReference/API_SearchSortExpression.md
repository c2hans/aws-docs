---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchSortExpression.html
---

# SearchSortExpression
<a name="API_SearchSortExpression"></a>

The resources to search.

## Contents
<a name="API_SearchSortExpression_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** fieldSort **   <a name="deadlinecloud-Type-SearchSortExpression-fieldSort"></a>
Options for sorting by a field.
Type: [FieldSortExpression](API_FieldSortExpression.md) object
Required: No

 ** parameterSort **   <a name="deadlinecloud-Type-SearchSortExpression-parameterSort"></a>
Options for sorting by a parameter.
Type: [ParameterSortExpression](API_ParameterSortExpression.md) object
Required: No

 ** userJobsFirst **   <a name="deadlinecloud-Type-SearchSortExpression-userJobsFirst"></a>
Options for sorting a particular user's jobs first.
Type: [UserJobsFirst](API_UserJobsFirst.md) object
Required: No

## See Also
<a name="API_SearchSortExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/SearchSortExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/SearchSortExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/SearchSortExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

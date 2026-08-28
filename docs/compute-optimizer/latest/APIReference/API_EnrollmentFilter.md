---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EnrollmentFilter.html
---

# EnrollmentFilter
<a name="API_EnrollmentFilter"></a>

Describes a filter that returns a more specific list of account enrollment statuses. Use this filter with the [GetEnrollmentStatusesForOrganization](API_GetEnrollmentStatusesForOrganization.md) action.

## Contents
<a name="API_EnrollmentFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-EnrollmentFilter-name"></a>
The name of the filter.
Specify `Status` to return accounts with a specific enrollment status (for example, `Active`).
Type: String
Valid Values: `Status`
Required: No

 ** values **   <a name="computeoptimizer-Type-EnrollmentFilter-values"></a>
The value of the filter.
The valid values are `Active`, `Inactive`, `Pending`, and `Failed`.
Type: Array of strings
Required: No

## See Also
<a name="API_EnrollmentFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EnrollmentFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EnrollmentFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EnrollmentFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

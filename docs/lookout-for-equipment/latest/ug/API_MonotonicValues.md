---
source_url: https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/API_MonotonicValues.html
---

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/).

# MonotonicValues
<a name="API_MonotonicValues"></a>

 Entity that comprises information on monotonic values in the data.

## Contents
<a name="API_MonotonicValues_Contents"></a>

 ** Status **   <a name="LookoutForEquipment-Type-MonotonicValues-Status"></a>
 Indicates whether there is a potential data issue related to having monotonic values.
Type: String
Valid Values: `POTENTIAL_ISSUE_DETECTED | NO_ISSUE_DETECTED`
Required: Yes

 ** Monotonicity **   <a name="LookoutForEquipment-Type-MonotonicValues-Monotonicity"></a>
 Indicates the monotonicity of values. Can be INCREASING, DECREASING, or STATIC.
Type: String
Valid Values: `DECREASING | INCREASING | STATIC`
Required: No

## See Also
<a name="API_MonotonicValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/MonotonicValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/MonotonicValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/MonotonicValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lookout for Equipment. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lookout-for-equipment` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

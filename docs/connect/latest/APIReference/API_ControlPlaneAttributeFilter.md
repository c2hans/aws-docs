---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ControlPlaneAttributeFilter.html
---

# ControlPlaneAttributeFilter
<a name="API_ControlPlaneAttributeFilter"></a>

An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` or `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.

## Contents
<a name="API_ControlPlaneAttributeFilter_Contents"></a>

 ** AndCondition **   <a name="connect-Type-ControlPlaneAttributeFilter-AndCondition"></a>
A list of conditions which would be applied together with an `AND` condition.
Type: [CommonAttributeAndCondition](API_CommonAttributeAndCondition.md) object
Required: No

 ** OrConditions **   <a name="connect-Type-ControlPlaneAttributeFilter-OrConditions"></a>
A list of conditions which would be applied together with an `OR` condition.
Type: Array of [CommonAttributeAndCondition](API_CommonAttributeAndCondition.md) objects
Required: No

 ** TagCondition **   <a name="connect-Type-ControlPlaneAttributeFilter-TagCondition"></a>
A leaf node condition which can be used to specify a tag condition, for example, `HAVE BPO = 123`.
Type: [TagCondition](API_TagCondition.md) object
Required: No

## See Also
<a name="API_ControlPlaneAttributeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ControlPlaneAttributeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ControlPlaneAttributeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ControlPlaneAttributeFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

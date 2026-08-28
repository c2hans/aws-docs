---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_Selector.html
---

# Selector
<a name="API_Selector"></a>

A comparison that is used to determine whether a query should return this object.

## Contents
<a name="API_Selector_Contents"></a>

 ** fieldName **   <a name="DP-Type-Selector-fieldName"></a>
The name of the field that the operator will be applied to. The field name is the "key" portion of the field definition in the pipeline definition syntax that is used by the AWS Data Pipeline API. If the field is not set on the object, the condition fails.
Type: String
Required: No

 ** operator **   <a name="DP-Type-Selector-operator"></a>
Contains a logical operation for comparing the value of a field with a specified value.
Type: [Operator](API_Operator.md) object
Required: No

## See Also
<a name="API_Selector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/Selector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/Selector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/Selector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

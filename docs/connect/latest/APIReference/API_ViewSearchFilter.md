---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ViewSearchFilter.html
---

# ViewSearchFilter
<a name="API_ViewSearchFilter"></a>

Defines filters to apply when searching for views, such as tag-based filters.

## Contents
<a name="API_ViewSearchFilter_Contents"></a>

 ** AttributeFilter **   <a name="connect-Type-ViewSearchFilter-AttributeFilter"></a>
An object that can be used to specify Tag conditions inside the `SearchFilter`. This accepts an `OR` or `AND` (List of List) input where:
+ The top level list specifies conditions that need to be applied with `OR` operator.
+ The inner list specifies conditions that need to be applied with `AND` operator.
Type: [ControlPlaneAttributeFilter](API_ControlPlaneAttributeFilter.md) object
Required: No

## See Also
<a name="API_ViewSearchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ViewSearchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ViewSearchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ViewSearchFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

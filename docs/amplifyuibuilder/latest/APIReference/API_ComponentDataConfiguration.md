---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentDataConfiguration.html
---

# ComponentDataConfiguration
<a name="API_ComponentDataConfiguration"></a>

Describes the configuration for binding a component's properties to data.

## Contents
<a name="API_ComponentDataConfiguration_Contents"></a>

 ** model **   <a name="amplifyuibuilder-Type-ComponentDataConfiguration-model"></a>
The name of the data model to use to bind data to a component.
Type: String
Required: Yes

 ** identifiers **   <a name="amplifyuibuilder-Type-ComponentDataConfiguration-identifiers"></a>
A list of IDs to use to bind data to a component. Use this property to bind specifically chosen data, rather than data retrieved from a query.
Type: Array of strings
Required: No

 ** predicate **   <a name="amplifyuibuilder-Type-ComponentDataConfiguration-predicate"></a>
Represents the conditional logic to use when binding data to a component. Use this property to retrieve only a subset of the data in a collection.
Type: [Predicate](API_Predicate.md) object
Required: No

 ** sort **   <a name="amplifyuibuilder-Type-ComponentDataConfiguration-sort"></a>
Describes how to sort the component's properties.
Type: Array of [SortProperty](API_SortProperty.md) objects
Required: No

## See Also
<a name="API_ComponentDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentDataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentDataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentDataConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentProperty.html
---

# ComponentProperty
<a name="API_ComponentProperty"></a>

Describes the configuration for all of a component's properties. Use `ComponentProperty` to specify the values to render or bind by default.

## Contents
<a name="API_ComponentProperty_Contents"></a>

 ** bindingProperties **   <a name="amplifyuibuilder-Type-ComponentProperty-bindingProperties"></a>
The information to bind the component property to data at runtime.
Type: [ComponentPropertyBindingProperties](API_ComponentPropertyBindingProperties.md) object
Required: No

 ** bindings **   <a name="amplifyuibuilder-Type-ComponentProperty-bindings"></a>
The information to bind the component property to form data.
Type: String to [FormBindingElement](API_FormBindingElement.md) object map
Required: No

 ** collectionBindingProperties **   <a name="amplifyuibuilder-Type-ComponentProperty-collectionBindingProperties"></a>
The information to bind the component property to data at runtime. Use this for collection components.
Type: [ComponentPropertyBindingProperties](API_ComponentPropertyBindingProperties.md) object
Required: No

 ** componentName **   <a name="amplifyuibuilder-Type-ComponentProperty-componentName"></a>
The name of the component that is affected by an event.
Type: String
Required: No

 ** concat **   <a name="amplifyuibuilder-Type-ComponentProperty-concat"></a>
A list of component properties to concatenate to create the value to assign to this component property.
Type: Array of [ComponentProperty](#API_ComponentProperty) objects
Required: No

 ** condition **   <a name="amplifyuibuilder-Type-ComponentProperty-condition"></a>
The conditional expression to use to assign a value to the component property.
Type: [ComponentConditionProperty](API_ComponentConditionProperty.md) object
Required: No

 ** configured **   <a name="amplifyuibuilder-Type-ComponentProperty-configured"></a>
Specifies whether the user configured the property in Amplify Studio after importing it.
Type: Boolean
Required: No

 ** defaultValue **   <a name="amplifyuibuilder-Type-ComponentProperty-defaultValue"></a>
The default value to assign to the component property.
Type: String
Required: No

 ** event **   <a name="amplifyuibuilder-Type-ComponentProperty-event"></a>
An event that occurs in your app. Use this for workflow data binding.
Type: String
Required: No

 ** importedValue **   <a name="amplifyuibuilder-Type-ComponentProperty-importedValue"></a>
The default value assigned to the property when the component is imported into an app.
Type: String
Required: No

 ** model **   <a name="amplifyuibuilder-Type-ComponentProperty-model"></a>
The data model to use to assign a value to the component property.
Type: String
Required: No

 ** property **   <a name="amplifyuibuilder-Type-ComponentProperty-property"></a>
The name of the component's property that is affected by an event.
Type: String
Required: No

 ** type **   <a name="amplifyuibuilder-Type-ComponentProperty-type"></a>
The component type.
Type: String
Required: No

 ** userAttribute **   <a name="amplifyuibuilder-Type-ComponentProperty-userAttribute"></a>
An authenticated user attribute to use to assign a value to the component property.
Type: String
Required: No

 ** value **   <a name="amplifyuibuilder-Type-ComponentProperty-value"></a>
The value to assign to the component property.
Type: String
Required: No

## See Also
<a name="API_ComponentProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

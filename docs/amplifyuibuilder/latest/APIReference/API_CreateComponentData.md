---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CreateComponentData.html
---

# CreateComponentData
<a name="API_CreateComponentData"></a>

Represents all of the information that is required to create a component.

## Contents
<a name="API_CreateComponentData_Contents"></a>

 ** bindingProperties **   <a name="amplifyuibuilder-Type-CreateComponentData-bindingProperties"></a>
The data binding information for the component's properties.
Type: String to [ComponentBindingPropertiesValue](API_ComponentBindingPropertiesValue.md) object map
Required: Yes

 ** componentType **   <a name="amplifyuibuilder-Type-CreateComponentData-componentType"></a>
The component type. This can be an Amplify custom UI component or another custom component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-CreateComponentData-name"></a>
The name of the component
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** overrides **   <a name="amplifyuibuilder-Type-CreateComponentData-overrides"></a>
Describes the component properties that can be overriden to customize an instance of the component.
Type: String to string to string map map
Required: Yes

 ** properties **   <a name="amplifyuibuilder-Type-CreateComponentData-properties"></a>
Describes the component's properties.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: Yes

 ** variants **   <a name="amplifyuibuilder-Type-CreateComponentData-variants"></a>
A list of the unique variants of this component.
Type: Array of [ComponentVariant](API_ComponentVariant.md) objects
Required: Yes

 ** children **   <a name="amplifyuibuilder-Type-CreateComponentData-children"></a>
A list of child components that are instances of the main component.
Type: Array of [ComponentChild](API_ComponentChild.md) objects
Required: No

 ** collectionProperties **   <a name="amplifyuibuilder-Type-CreateComponentData-collectionProperties"></a>
The data binding configuration for customizing a component's properties. Use this for a collection component.
Type: String to [ComponentDataConfiguration](API_ComponentDataConfiguration.md) object map
Required: No

 ** events **   <a name="amplifyuibuilder-Type-CreateComponentData-events"></a>
The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map
Required: No

 ** schemaVersion **   <a name="amplifyuibuilder-Type-CreateComponentData-schemaVersion"></a>
The schema version of the component when it was imported.
Type: String
Required: No

 ** sourceId **   <a name="amplifyuibuilder-Type-CreateComponentData-sourceId"></a>
The unique ID of the component in its original source system, such as Figma.
Type: String
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-CreateComponentData-tags"></a>
One or more key-value pairs to use when tagging the component data.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CreateComponentData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CreateComponentData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CreateComponentData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CreateComponentData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Component.html
---

# Component
<a name="API_Component"></a>

Contains the configuration settings for a user interface (UI) element for an Amplify app. A component is configured as a primary, stand-alone UI element. Use `ComponentChild` to configure an instance of a `Component`. A `ComponentChild` instance inherits the configuration of the main `Component`.

## Contents
<a name="API_Component_Contents"></a>

 ** appId **   <a name="amplifyuibuilder-Type-Component-appId"></a>
The unique ID of the Amplify app associated with the component.
Type: String
Required: Yes

 ** bindingProperties **   <a name="amplifyuibuilder-Type-Component-bindingProperties"></a>
The information to connect a component's properties to data at runtime. You can't specify `tags` as a valid property for `bindingProperties`.

Type: String to [ComponentBindingPropertiesValue](API_ComponentBindingPropertiesValue.md) object map
Required: Yes

 ** componentType **   <a name="amplifyuibuilder-Type-Component-componentType"></a>
The type of the component. This can be an Amplify custom UI component or another custom component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** createdAt **   <a name="amplifyuibuilder-Type-Component-createdAt"></a>
The time that the component was created.
Type: Timestamp
Required: Yes

 ** environmentName **   <a name="amplifyuibuilder-Type-Component-environmentName"></a>
The name of the backend environment that is a part of the Amplify app.
Type: String
Required: Yes

 ** id **   <a name="amplifyuibuilder-Type-Component-id"></a>
The unique ID of the component.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-Component-name"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** overrides **   <a name="amplifyuibuilder-Type-Component-overrides"></a>
Describes the component's properties that can be overriden in a customized instance of the component. You can't specify `tags` as a valid property for `overrides`.
Type: String to string to string map map
Required: Yes

 ** properties **   <a name="amplifyuibuilder-Type-Component-properties"></a>
Describes the component's properties. You can't specify `tags` as a valid property for `properties`.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: Yes

 ** variants **   <a name="amplifyuibuilder-Type-Component-variants"></a>
A list of the component's variants. A variant is a unique style configuration of a main component.
Type: Array of [ComponentVariant](API_ComponentVariant.md) objects
Required: Yes

 ** children **   <a name="amplifyuibuilder-Type-Component-children"></a>
A list of the component's `ComponentChild` instances.
Type: Array of [ComponentChild](API_ComponentChild.md) objects
Required: No

 ** collectionProperties **   <a name="amplifyuibuilder-Type-Component-collectionProperties"></a>
The data binding configuration for the component's properties. Use this for a collection component. You can't specify `tags` as a valid property for `collectionProperties`.
Type: String to [ComponentDataConfiguration](API_ComponentDataConfiguration.md) object map
Required: No

 ** events **   <a name="amplifyuibuilder-Type-Component-events"></a>
Describes the events that can be raised on the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map
Required: No

 ** modifiedAt **   <a name="amplifyuibuilder-Type-Component-modifiedAt"></a>
The time that the component was modified.
Type: Timestamp
Required: No

 ** schemaVersion **   <a name="amplifyuibuilder-Type-Component-schemaVersion"></a>
The schema version of the component when it was imported.
Type: String
Required: No

 ** sourceId **   <a name="amplifyuibuilder-Type-Component-sourceId"></a>
The unique ID of the component in its original source system, such as Figma.
Type: String
Required: No

 ** tags **   <a name="amplifyuibuilder-Type-Component-tags"></a>
One or more key-value pairs to use when tagging the component.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Component_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/Component)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/Component)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/Component)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

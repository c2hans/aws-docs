---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_UpdateComponentData.html
---

# UpdateComponentData
<a name="API_UpdateComponentData"></a>

Updates and saves all of the information about a component, based on component ID.

## Contents
<a name="API_UpdateComponentData_Contents"></a>

 ** bindingProperties **   <a name="amplifyuibuilder-Type-UpdateComponentData-bindingProperties"></a>
The data binding information for the component's properties.
Type: String to [ComponentBindingPropertiesValue](API_ComponentBindingPropertiesValue.md) object map
Required: No

 ** children **   <a name="amplifyuibuilder-Type-UpdateComponentData-children"></a>
The components that are instances of the main component.
Type: Array of [ComponentChild](API_ComponentChild.md) objects
Required: No

 ** collectionProperties **   <a name="amplifyuibuilder-Type-UpdateComponentData-collectionProperties"></a>
The configuration for binding a component's properties to a data model. Use this for a collection component.
Type: String to [ComponentDataConfiguration](API_ComponentDataConfiguration.md) object map
Required: No

 ** componentType **   <a name="amplifyuibuilder-Type-UpdateComponentData-componentType"></a>
The type of the component. This can be an Amplify custom UI component or another custom component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** events **   <a name="amplifyuibuilder-Type-UpdateComponentData-events"></a>
The event configuration for the component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map
Required: No

 ** id **   <a name="amplifyuibuilder-Type-UpdateComponentData-id"></a>
The unique ID of the component to update.
Type: String
Required: No

 ** name **   <a name="amplifyuibuilder-Type-UpdateComponentData-name"></a>
The name of the component to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** overrides **   <a name="amplifyuibuilder-Type-UpdateComponentData-overrides"></a>
Describes the properties that can be overriden to customize the component.
Type: String to string to string map map
Required: No

 ** properties **   <a name="amplifyuibuilder-Type-UpdateComponentData-properties"></a>
Describes the component's properties.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: No

 ** schemaVersion **   <a name="amplifyuibuilder-Type-UpdateComponentData-schemaVersion"></a>
The schema version of the component when it was imported.
Type: String
Required: No

 ** sourceId **   <a name="amplifyuibuilder-Type-UpdateComponentData-sourceId"></a>
The unique ID of the component in its original source system, such as Figma.
Type: String
Required: No

 ** variants **   <a name="amplifyuibuilder-Type-UpdateComponentData-variants"></a>
A list of the unique variants of the main component being updated.
Type: Array of [ComponentVariant](API_ComponentVariant.md) objects
Required: No

## See Also
<a name="API_UpdateComponentData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/UpdateComponentData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/UpdateComponentData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/UpdateComponentData)

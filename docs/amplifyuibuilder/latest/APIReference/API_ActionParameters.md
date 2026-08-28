---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ActionParameters.html
---

# ActionParameters
<a name="API_ActionParameters"></a>

Represents the event action configuration for an element of a `Component` or `ComponentChild`. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components. `ActionParameters` defines the action that is performed when an event occurs on the component.

## Contents
<a name="API_ActionParameters_Contents"></a>

 ** anchor **   <a name="amplifyuibuilder-Type-ActionParameters-anchor"></a>
The HTML anchor link to the location to open. Specify this value for a navigation action.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** fields **   <a name="amplifyuibuilder-Type-ActionParameters-fields"></a>
A dictionary of key-value pairs mapping Amplify Studio properties to fields in a data model. Use when the action performs an operation on an Amplify DataStore model.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: No

 ** global **   <a name="amplifyuibuilder-Type-ActionParameters-global"></a>
Specifies whether the user should be signed out globally. Specify this value for an auth sign out action.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** id **   <a name="amplifyuibuilder-Type-ActionParameters-id"></a>
The unique ID of the component that the `ActionParameters` apply to.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** model **   <a name="amplifyuibuilder-Type-ActionParameters-model"></a>
The name of the data model. Use when the action performs an operation on an Amplify DataStore model.
Type: String
Required: No

 ** state **   <a name="amplifyuibuilder-Type-ActionParameters-state"></a>
A key-value pair that specifies the state property name and its initial value.
Type: [MutationActionSetStateParameter](API_MutationActionSetStateParameter.md) object
Required: No

 ** target **   <a name="amplifyuibuilder-Type-ActionParameters-target"></a>
The element within the same component to modify when the action occurs.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** type **   <a name="amplifyuibuilder-Type-ActionParameters-type"></a>
The type of navigation action. Valid values are `url` and `anchor`. This value is required for a navigation action.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

 ** url **   <a name="amplifyuibuilder-Type-ActionParameters-url"></a>
The URL to the location to open. Specify this value for a navigation action.
Type: [ComponentProperty](API_ComponentProperty.md) object
Required: No

## See Also
<a name="API_ActionParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ActionParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ActionParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ActionParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

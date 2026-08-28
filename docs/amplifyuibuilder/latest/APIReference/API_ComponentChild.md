---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentChild.html
---

# ComponentChild
<a name="API_ComponentChild"></a>

A nested UI configuration within a parent `Component`.

## Contents
<a name="API_ComponentChild_Contents"></a>

 ** componentType **   <a name="amplifyuibuilder-Type-ComponentChild-componentType"></a>
The type of the child component.
Type: String
Required: Yes

 ** name **   <a name="amplifyuibuilder-Type-ComponentChild-name"></a>
The name of the child component.
Type: String
Required: Yes

 ** properties **   <a name="amplifyuibuilder-Type-ComponentChild-properties"></a>
Describes the properties of the child component. You can't specify `tags` as a valid property for `properties`.
Type: String to [ComponentProperty](API_ComponentProperty.md) object map
Required: Yes

 ** children **   <a name="amplifyuibuilder-Type-ComponentChild-children"></a>
The list of `ComponentChild` instances for this component.
Type: Array of [ComponentChild](#API_ComponentChild) objects
Required: No

 ** events **   <a name="amplifyuibuilder-Type-ComponentChild-events"></a>
Describes the events that can be raised on the child component. Use for the workflow feature in Amplify Studio that allows you to bind events and actions to components.
Type: String to [ComponentEvent](API_ComponentEvent.md) object map
Required: No

 ** sourceId **   <a name="amplifyuibuilder-Type-ComponentChild-sourceId"></a>
The unique ID of the child component in its original source system, such as Figma.
Type: String
Required: No

## See Also
<a name="API_ComponentChild_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentChild)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentChild)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentChild)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmplifyUIBuilder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amplifyuibuilder` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_ComponentEvent.html
---

# ComponentEvent
<a name="API_ComponentEvent"></a>

Describes the configuration of an event. You can bind an event and a corresponding action to a `Component` or a `ComponentChild`. A button click is an example of an event.

## Contents
<a name="API_ComponentEvent_Contents"></a>

 ** action **   <a name="amplifyuibuilder-Type-ComponentEvent-action"></a>
The action to perform when a specific event is raised.
Type: String
Required: No

 ** bindingEvent **   <a name="amplifyuibuilder-Type-ComponentEvent-bindingEvent"></a>
Binds an event to an action on a component. When you specify a `bindingEvent`, the event is called when the action is performed.
Type: String
Required: No

 ** parameters **   <a name="amplifyuibuilder-Type-ComponentEvent-parameters"></a>
Describes information about the action.
Type: [ActionParameters](API_ActionParameters.md) object
Required: No

## See Also
<a name="API_ComponentEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/ComponentEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/ComponentEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/ComponentEvent)

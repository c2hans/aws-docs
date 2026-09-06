---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedSessionAction.html
---

# AssignedSessionAction
<a name="API_AssignedSessionAction"></a>

The action for a session defined by the session action ID.

## Contents
<a name="API_AssignedSessionAction_Contents"></a>

 ** definition **   <a name="deadlinecloud-Type-AssignedSessionAction-definition"></a>
The definition of the assigned session action.
Type: [AssignedSessionActionDefinition](API_AssignedSessionActionDefinition.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sessionActionId **   <a name="deadlinecloud-Type-AssignedSessionAction-sessionActionId"></a>
The session action ID for the assigned session.
Type: String
Pattern: `sessionaction-[0-9a-f]{32}-(0|([1-9][0-9]{0,9}))`
Required: Yes

## See Also
<a name="API_AssignedSessionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedSessionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedSessionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedSessionAction)

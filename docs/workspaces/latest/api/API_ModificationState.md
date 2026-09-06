---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ModificationState.html
---

# ModificationState
<a name="API_ModificationState"></a>

Describes a WorkSpace modification.

## Contents
<a name="API_ModificationState_Contents"></a>

 ** Resource **   <a name="WorkSpaces-Type-ModificationState-Resource"></a>
The WorkSpace property being modified.
Type: String
Valid Values: `ROOT_VOLUME | USER_VOLUME | COMPUTE_TYPE | PROTOCOL | NESTED_VIRTUALIZATION`
Required: No

 ** State **   <a name="WorkSpaces-Type-ModificationState-State"></a>
The modification state.
Type: String
Valid Values: `UPDATE_INITIATED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: No

## See Also
<a name="API_ModificationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ModificationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ModificationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ModificationState)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_Change.html
---

# Change
<a name="API_Change"></a>

Represents a single change within a collaboration change request, containing the change identifier and specification.

## Contents
<a name="API_Change_Contents"></a>

 ** specification **   <a name="API-Type-Change-specification"></a>
The specification details for this change.
Type: [ChangeSpecification](API_ChangeSpecification.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** specificationType **   <a name="API-Type-Change-specificationType"></a>
The type of specification for this change.
Type: String
Valid Values: `MEMBER | COLLABORATION`
Required: Yes

 ** types **   <a name="API-Type-Change-types"></a>
The list of change types that were applied.
Type: Array of strings
Array Members: Minimum number of 1 item.
Valid Values: `ADD_MEMBER | GRANT_RECEIVE_RESULTS_ABILITY | REVOKE_RECEIVE_RESULTS_ABILITY | EDIT_AUTO_APPROVED_CHANGE_TYPES | ADD_PAYER_CANDIDATE | REMOVE_PAYER_CANDIDATE | GRANT_CAN_RECEIVE_MODEL_OUTPUT | GRANT_CAN_RECEIVE_INFERENCE_OUTPUT | REVOKE_CAN_RECEIVE_MODEL_OUTPUT | REVOKE_CAN_RECEIVE_INFERENCE_OUTPUT`
Required: Yes

## See Also
<a name="API_Change_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/Change)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/Change)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/Change)

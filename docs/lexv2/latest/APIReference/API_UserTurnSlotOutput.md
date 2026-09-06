---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UserTurnSlotOutput.html
---

# UserTurnSlotOutput
<a name="API_UserTurnSlotOutput"></a>

Contains information about a slot output by the test set execution.

## Contents
<a name="API_UserTurnSlotOutput_Contents"></a>

 ** subSlots **   <a name="lexv2-Type-UserTurnSlotOutput-subSlots"></a>
A list of items mapping the name of the subslots to information about those subslots.
Type: String to [UserTurnSlotOutput](#API_UserTurnSlotOutput) object map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: No

 ** value **   <a name="lexv2-Type-UserTurnSlotOutput-value"></a>
The value output by the slot recognition.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** values **   <a name="lexv2-Type-UserTurnSlotOutput-values"></a>
Values that are output by the slot recognition.
Type: Array of [UserTurnSlotOutput](#API_UserTurnSlotOutput) objects
Required: No

## See Also
<a name="API_UserTurnSlotOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UserTurnSlotOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UserTurnSlotOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UserTurnSlotOutput)

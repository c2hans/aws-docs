---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UserTurnInputSpecification.html
---

# UserTurnInputSpecification
<a name="API_UserTurnInputSpecification"></a>

Contains information about the user messages in the turn in the input.

## Contents
<a name="API_UserTurnInputSpecification_Contents"></a>

 ** utteranceInput **   <a name="lexv2-Type-UserTurnInputSpecification-utteranceInput"></a>
The utterance input in the user turn.
Type: [UtteranceInputSpecification](API_UtteranceInputSpecification.md) object
Required: Yes

 ** requestAttributes **   <a name="lexv2-Type-UserTurnInputSpecification-requestAttributes"></a>
Request attributes of the user turn.
Type: String to string map
Key Length Constraints: Minimum length of 1.
Required: No

 ** sessionState **   <a name="lexv2-Type-UserTurnInputSpecification-sessionState"></a>
Contains information about the session state in the input.
Type: [InputSessionStateSpecification](API_InputSessionStateSpecification.md) object
Required: No

## See Also
<a name="API_UserTurnInputSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UserTurnInputSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UserTurnInputSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UserTurnInputSpecification)

---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_TestSetTurnRecord.html
---

# TestSetTurnRecord
<a name="API_TestSetTurnRecord"></a>

Contains information about a turn in a test set.

## Contents
<a name="API_TestSetTurnRecord_Contents"></a>

 ** recordNumber **   <a name="lexv2-Type-TestSetTurnRecord-recordNumber"></a>
The record number associated with the turn.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 200000.
Required: Yes

 ** turnSpecification **   <a name="lexv2-Type-TestSetTurnRecord-turnSpecification"></a>
Contains information about the agent or user turn depending upon type of turn.
Type: [TurnSpecification](API_TurnSpecification.md) object
Required: Yes

 ** conversationId **   <a name="lexv2-Type-TestSetTurnRecord-conversationId"></a>
The unique identifier for the conversation associated with the turn.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^([0-9a-zA-Z][_-]?)+$`
Required: No

 ** turnNumber **   <a name="lexv2-Type-TestSetTurnRecord-turnNumber"></a>
The number of turns that has elapsed up to that turn.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 30.
Required: No

## See Also
<a name="API_TestSetTurnRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/TestSetTurnRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/TestSetTurnRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/TestSetTurnRecord)

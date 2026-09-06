---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_DayOfMonth.html
---

# DayOfMonth
<a name="API_agent_DayOfMonth"></a>

The day of the month on which a monthly sync runs. Specify exactly one of `dayNumber` or `lastDayOfMonth`.

## Contents
<a name="API_agent_DayOfMonth_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dayNumber **   <a name="bedrock-Type-agent_DayOfMonth-dayNumber"></a>
A specific day of the month, from 1 to 28. Values are capped at 28, so a monthly sync runs in every month, including February.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 28.
Required: No

 ** lastDayOfMonth **   <a name="bedrock-Type-agent_DayOfMonth-lastDayOfMonth"></a>
Set this option to run the monthly sync on the last calendar day of each month.
Type: [LastDayOfMonth](API_agent_LastDayOfMonth.md) object
Required: No

## See Also
<a name="API_agent_DayOfMonth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DayOfMonth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DayOfMonth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DayOfMonth)

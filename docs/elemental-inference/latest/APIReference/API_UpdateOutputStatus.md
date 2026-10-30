---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateOutputStatus.html
---

# UpdateOutputStatus
<a name="API_UpdateOutputStatus"></a>

Enables or disables an output at the action's scheduled time. This is a type of ScheduleActionOperation.

## Contents
<a name="API_UpdateOutputStatus_Contents"></a>

 ** outputName **   <a name="elementalinference-Type-UpdateOutputStatus-outputName"></a>
The name of the output that you want to enable or disable. The output must exist in the feed when you create the action.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** status **   <a name="elementalinference-Type-UpdateOutputStatus-status"></a>
Specifies whether the output is enabled or disabled after the action runs.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_UpdateOutputStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/UpdateOutputStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/UpdateOutputStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/UpdateOutputStatus)

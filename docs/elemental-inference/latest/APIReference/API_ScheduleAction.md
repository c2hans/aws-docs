---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ScheduleAction.html
---

# ScheduleAction
<a name="API_ScheduleAction"></a>

Describes one schedule action on a feed, including the changes it makes and whether it has run yet. Elemental Inference returns this structure in the ListScheduleActions operation.

## Contents
<a name="API_ScheduleAction_Contents"></a>

 ** actionName **   <a name="elementalinference-Type-ScheduleAction-actionName"></a>
The name of the schedule action. The name is unique within the feed.
Type: String
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])?`
Required: Yes

 ** operations **   <a name="elementalinference-Type-ScheduleAction-operations"></a>
The configuration changes that the action makes to the feed.
Type: Array of [ScheduleActionOperation](API_ScheduleActionOperation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** startConfiguration **   <a name="elementalinference-Type-ScheduleAction-startConfiguration"></a>
Specifies when the action runs.
Type: [ScheduleActionStartConfiguration](API_ScheduleActionStartConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="elementalinference-Type-ScheduleAction-status"></a>
The status of the action. Valid values are the following:
PENDING
The action is waiting for its scheduled time.
COMPLETED
Elemental Inference applied all the action's operations to the feed.
FAILED
Elemental Inference couldn't apply the action.
Type: String
Valid Values: `PENDING | COMPLETED | FAILED`
Required: Yes

 ** error **   <a name="elementalinference-Type-ScheduleAction-error"></a>
A description of why the action failed. Elemental Inference returns this property only when the status is FAILED.
Type: [ScheduleActionError](API_ScheduleActionError.md) object
Required: No

## See Also
<a name="API_ScheduleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ScheduleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ScheduleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ScheduleAction)

---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Activity.html
---

# Activity
<a name="API_Activity"></a>

Contains information about an activity, such as an API call, that was observed for a signal.

## Contents
<a name="API_Activity_Contents"></a>

 ** type **   <a name="guardduty-Type-Activity-type"></a>
The type of the observed activity.
Type: String
Valid Values: `API_CALL`
Required: Yes

 ** api **   <a name="guardduty-Type-Activity-api"></a>
Contains information about the API call that was observed, when the activity type is `API_CALL`.
Type: [ApiCall](API_ApiCall.md) object
Required: No

## See Also
<a name="API_Activity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Activity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Activity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Activity)

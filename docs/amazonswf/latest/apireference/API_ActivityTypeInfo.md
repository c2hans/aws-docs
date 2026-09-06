---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTypeInfo.html
---

# ActivityTypeInfo
<a name="API_ActivityTypeInfo"></a>

Detailed information about an activity type.

## Contents
<a name="API_ActivityTypeInfo_Contents"></a>

 ** activityType **   <a name="SWF-Type-ActivityTypeInfo-activityType"></a>
The [ActivityType](API_ActivityType.md) type structure representing the activity type.
Type: [ActivityType](API_ActivityType.md) object
Required: Yes

 ** creationDate **   <a name="SWF-Type-ActivityTypeInfo-creationDate"></a>
The date and time this activity type was created through [RegisterActivityType](API_RegisterActivityType.md).
Type: Timestamp
Required: Yes

 ** status **   <a name="SWF-Type-ActivityTypeInfo-status"></a>
The current status of the activity type.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** deprecationDate **   <a name="SWF-Type-ActivityTypeInfo-deprecationDate"></a>
If DEPRECATED, the date and time [DeprecateActivityType](API_DeprecateActivityType.md) was called.
Type: Timestamp
Required: No

 ** description **   <a name="SWF-Type-ActivityTypeInfo-description"></a>
The description of the activity type provided in [RegisterActivityType](API_RegisterActivityType.md).
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_ActivityTypeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/ActivityTypeInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/ActivityTypeInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/ActivityTypeInfo)

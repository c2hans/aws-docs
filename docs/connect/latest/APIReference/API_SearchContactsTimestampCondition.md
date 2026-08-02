---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactsTimestampCondition.html
---

# SearchContactsTimestampCondition
<a name="API_SearchContactsTimestampCondition"></a>

The timestamp condition indicating which contact timestamp should be used and how it should be filtered. It is not an actual timestamp value.

## Contents
<a name="API_SearchContactsTimestampCondition_Contents"></a>

 ** ConditionType **   <a name="connect-Type-SearchContactsTimestampCondition-ConditionType"></a>
Condition of the timestamp on the contact.
Type: String
Valid Values: `NOT_EXISTS`
Required: Yes

 ** Type **   <a name="connect-Type-SearchContactsTimestampCondition-Type"></a>
Type of the timestamps to use for the filter.
Type: String
Valid Values: `INITIATION_TIMESTAMP | SCHEDULED_TIMESTAMP | CONNECTED_TO_AGENT_TIMESTAMP | DISCONNECT_TIMESTAMP | ENQUEUE_TIMESTAMP`
Required: Yes

## See Also
<a name="API_SearchContactsTimestampCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContactsTimestampCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContactsTimestampCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContactsTimestampCondition)

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_EventTriggerSummaryItem.html
---

# EventTriggerSummaryItem
<a name="API_connect-customer-profiles_EventTriggerSummaryItem"></a>

The summary of the event trigger.

## Contents
<a name="API_connect-customer-profiles_EventTriggerSummaryItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-CreatedAt"></a>
The timestamp of when the event trigger was created.
Type: Timestamp
Required: No

 ** Description **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-Description"></a>
The description of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** EventTriggerName **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-EventTriggerName"></a>
The unique name of the event trigger.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-LastUpdatedAt"></a>
The timestamp of when the event trigger was most recently updated.
Type: Timestamp
Required: No

 ** ObjectTypeName **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-ObjectTypeName"></a>
The unique name of the object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_EventTriggerSummaryItem-Tags"></a>
An array of key-value pairs to apply to this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_connect-customer-profiles_EventTriggerSummaryItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/EventTriggerSummaryItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/EventTriggerSummaryItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/EventTriggerSummaryItem)

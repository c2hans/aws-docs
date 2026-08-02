---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_Event.html
---

# Event
<a name="API_Event"></a>

 This data type is used as a response element in the [DescribeEvents](API_DescribeEvents.md) action.

## Contents
<a name="API_Event_Contents"></a>

 ** Date **
Specifies the date and time of the event.
Type: Timestamp
Required: No

 ** EventCategories.EventCategory.N **
Specifies the category for the event.
Type: Array of strings
Required: No

 ** Message **
Provides the text of this event.
Type: String
Required: No

 ** SourceArn **
The Amazon Resource Name (ARN) for the event.
Type: String
Required: No

 ** SourceIdentifier **
Provides the identifier for the source of the event.
Type: String
Required: No

 ** SourceType **
Specifies the source type for this event.
Type: String
Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/Event)

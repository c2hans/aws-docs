---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventDetailsErrorItem.html
---

# EventDetailsErrorItem
<a name="API_EventDetailsErrorItem"></a>

Error information returned when a [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation can't find a specified event.

## Contents
<a name="API_EventDetailsErrorItem_Contents"></a>

 ** errorMessage **   <a name="AWSHealth-Type-EventDetailsErrorItem-errorMessage"></a>
A message that describes the error.
Type: String
Required: No

 ** errorName **   <a name="AWSHealth-Type-EventDetailsErrorItem-errorName"></a>
The name of the error.
Type: String
Required: No

 ** eventArn **   <a name="AWSHealth-Type-EventDetailsErrorItem-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

## See Also
<a name="API_EventDetailsErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventDetailsErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventDetailsErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventDetailsErrorItem)

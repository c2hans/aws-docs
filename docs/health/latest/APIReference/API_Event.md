---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html
---

# Event
<a name="API_Event"></a>

Summary information about an AWS Health event.

 AWS Health events can be public or account-specific:
+  *Public events* might be service events that are not specific to an AWS account. For example, if there is an issue with an AWS Region, AWS Health provides information about the event, even if you don't use services or resources in that Region.
+  *Account-specific* events are specific to either your AWS account or an account in your organization. For example, if there's an issue with Amazon Elastic Compute Cloud in a Region that you use, AWS Health provides information about the event and the affected resources in the account.

You can determine if an event is public or account-specific by using the `eventScopeCode` parameter. For more information, see [eventScopeCode](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode).

## Contents
<a name="API_Event_Contents"></a>

 ** actionability **   <a name="AWSHealth-Type-Event-actionability"></a>
The actionability classification of the event. Possible values are `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED` and `INFORMATIONAL`. Events with `ACTION_REQUIRED` actionability require customer action to resolve or mitigate the event. Events with `ACTION_MAY_BE_REQUIRED` actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with `INFORMATIONAL` actionability are provided for awareness and do not require immediate action.
Type: String
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** arn **   <a name="AWSHealth-Type-Event-arn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** availabilityZone **   <a name="AWSHealth-Type-Event-availabilityZone"></a>
The AWS Availability Zone of the event. For example, us-east-1a.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 18.
Pattern: `[a-z]{2,4}\-[0-9a-z\-]{4,16}`
Required: No

 ** endTime **   <a name="AWSHealth-Type-Event-endTime"></a>
The date and time that the event ended.
Type: Timestamp
Required: No

 ** eventScopeCode **   <a name="AWSHealth-Type-Event-eventScopeCode"></a>
This parameter specifies if the AWS Health event is a public AWS service event or an account-specific event.
+ If the `eventScopeCode` value is `PUBLIC`, then the `affectedAccounts` value is always empty.
+ If the `eventScopeCode` value is `ACCOUNT_SPECIFIC`, then the `affectedAccounts` value lists the affected AWS accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have AWS accounts that use that service, those account IDs appear in the response.
+ If the `eventScopeCode` value is `NONE`, then the `eventArn` that you specified in the request is invalid or doesn't exist.
Type: String
Valid Values: `PUBLIC | ACCOUNT_SPECIFIC | NONE`
Required: No

 ** eventTypeCategory **   <a name="AWSHealth-Type-Event-eventTypeCategory"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** eventTypeCode **   <a name="AWSHealth-Type-Event-eventTypeCode"></a>
The unique identifier for the event type. The format is `AWS_SERVICE_DESCRIPTION `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9\_\-]{3,100}`
Required: No

 ** lastUpdatedTime **   <a name="AWSHealth-Type-Event-lastUpdatedTime"></a>
The most recent date and time that the event was updated.
Type: Timestamp
Required: No

 ** personas **   <a name="AWSHealth-Type-Event-personas"></a>
A list of persona classifications that indicate the target audience for the event. Possible values are `OPERATIONS`, `SECURITY`, and `BILLING`. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** region **   <a name="AWSHealth-Type-Event-region"></a>
The AWS Region name of the event.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[^:/]{2,25}`
Required: No

 ** service **   <a name="AWSHealth-Type-Event-service"></a>
The AWS service that is affected by the event. For example, `EC2`, `RDS`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

 ** startTime **   <a name="AWSHealth-Type-Event-startTime"></a>
The date and time that the event began.
Type: Timestamp
Required: No

 ** statusCode **   <a name="AWSHealth-Type-Event-statusCode"></a>
The most recent status of the event. Possible values are `open`, `closed`, and `upcoming`.
Type: String
Valid Values: `open | closed | upcoming`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/Event)

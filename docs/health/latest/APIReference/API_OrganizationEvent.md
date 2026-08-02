---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEvent.html
---

# OrganizationEvent
<a name="API_OrganizationEvent"></a>

Summary information about an event, returned by the [DescribeEventsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html) operation.

## Contents
<a name="API_OrganizationEvent_Contents"></a>

 ** actionability **   <a name="AWSHealth-Type-OrganizationEvent-actionability"></a>
The actionability classification of the event. Possible values are `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED` and `INFORMATIONAL`. Events with `ACTION_REQUIRED` actionability require customer action to resolve or mitigate the event. Events with `ACTION_MAY_BE_REQUIRED` actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with `INFORMATIONAL` actionability are provided for awareness and do not require immediate action.
Type: String
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** arn **   <a name="AWSHealth-Type-OrganizationEvent-arn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** endTime **   <a name="AWSHealth-Type-OrganizationEvent-endTime"></a>
The date and time that the event ended.
Type: Timestamp
Required: No

 ** eventScopeCode **   <a name="AWSHealth-Type-OrganizationEvent-eventScopeCode"></a>
This parameter specifies if the AWS Health event is a public AWS service event or an account-specific event.
+ If the `eventScopeCode` value is `PUBLIC`, then the `affectedAccounts` value is always empty.
+ If the `eventScopeCode` value is `ACCOUNT_SPECIFIC`, then the `affectedAccounts` value lists the affected AWS accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have AWS accounts that use that service, those account IDs appear in the response.
+ If the `eventScopeCode` value is `NONE`, then the `eventArn` that you specified in the request is invalid or doesn't exist.
Type: String
Valid Values: `PUBLIC | ACCOUNT_SPECIFIC | NONE`
Required: No

 ** eventTypeCategory **   <a name="AWSHealth-Type-OrganizationEvent-eventTypeCategory"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** eventTypeCode **   <a name="AWSHealth-Type-OrganizationEvent-eventTypeCode"></a>
The unique identifier for the event type. The format is `AWS_SERVICE_DESCRIPTION`. For example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9\_\-]{3,100}`
Required: No

 ** lastUpdatedTime **   <a name="AWSHealth-Type-OrganizationEvent-lastUpdatedTime"></a>
The most recent date and time that the event was updated.
Type: Timestamp
Required: No

 ** personas **   <a name="AWSHealth-Type-OrganizationEvent-personas"></a>
A list of persona classifications that indicate the target audience for the event. Possible values are `OPERATIONS`, `SECURITY`, and `BILLING`. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** region **   <a name="AWSHealth-Type-OrganizationEvent-region"></a>
The AWS Region name of the event.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `[^:/]{2,25}`
Required: No

 ** service **   <a name="AWSHealth-Type-OrganizationEvent-service"></a>
The AWS service that is affected by the event, such as EC2 and RDS.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

 ** startTime **   <a name="AWSHealth-Type-OrganizationEvent-startTime"></a>
The date and time that the event began.
Type: Timestamp
Required: No

 ** statusCode **   <a name="AWSHealth-Type-OrganizationEvent-statusCode"></a>
The most recent status of the event. Possible values are `open`, `closed`, and `upcoming`.
Type: String
Valid Values: `open | closed | upcoming`
Required: No

## See Also
<a name="API_OrganizationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationEvent)

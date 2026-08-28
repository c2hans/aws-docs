---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html
---

# EventType
<a name="API_EventType"></a>

Contains the metadata about a type of event that is reported by AWS Health. The `EventType` shows the category, service, and the event type code of the event. For example, an `issue` might be the category, `EC2` the service, and `AWS_EC2_SYSTEM_MAINTENANCE_EVENT` the event type code.

You can use the [DescribeEventTypes](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html) API operation to return this information about an event.

You can also use the Amazon CloudWatch Events console to create a rule so that you can get notified or take action when AWS Health delivers a specific event to your AWS account. For more information, see [Monitor for AWS Health events with Amazon CloudWatch Events](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the * AWS Health User Guide*.

## Contents
<a name="API_EventType_Contents"></a>

 ** actionability **   <a name="AWSHealth-Type-EventType-actionability"></a>
The actionability classification of the event. Possible values are `ACTION_REQUIRED`, `ACTION_MAY_BE_REQUIRED` and `INFORMATIONAL`. Events with `ACTION_REQUIRED` actionability require customer action to resolve or mitigate the event. Events with `ACTION_MAY_BE_REQUIRED` actionability indicates that the current status is unknown or conditional and inspection is needed to determine if action is required. Events with `INFORMATIONAL` actionability are provided for awareness and do not require immediate action.
Type: String
Valid Values: `ACTION_REQUIRED | ACTION_MAY_BE_REQUIRED | INFORMATIONAL`
Required: No

 ** category **   <a name="AWSHealth-Type-EventType-category"></a>
A list of event type category codes. Possible values are `issue`, `accountNotification`, or `scheduledChange`. Currently, the `investigation` value isn't supported at this time.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Valid Values: `issue | accountNotification | scheduledChange | investigation`
Required: No

 ** code **   <a name="AWSHealth-Type-EventType-code"></a>
The unique identifier for the event type. The format is `AWS_SERVICE_DESCRIPTION `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[a-zA-Z0-9\_\-]{3,100}`
Required: No

 ** personas **   <a name="AWSHealth-Type-EventType-personas"></a>
A list of persona classifications that indicate the target audience for the event. Possible values are `OPERATIONS`, `SECURITY`, and `BILLING`. Events can be associated with multiple personas to indicate relevance to different teams or roles within an organization.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `OPERATIONS | SECURITY | BILLING`
Required: No

 ** service **   <a name="AWSHealth-Type-EventType-service"></a>
The AWS service that is affected by the event. For example, `EC2`, `RDS`.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 30.
Pattern: `[^:/]{2,30}`
Required: No

## See Also
<a name="API_EventType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/EventType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/EventType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/EventType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

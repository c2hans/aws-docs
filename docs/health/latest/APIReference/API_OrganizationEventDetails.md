---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventDetails.html
---

# OrganizationEventDetails
<a name="API_OrganizationEventDetails"></a>

Detailed information about an event. A combination of an [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) object, an [EventDescription](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html) object, and additional metadata about the event. Returned by the [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation.

## Contents
<a name="API_OrganizationEventDetails_Contents"></a>

 ** awsAccountId **   <a name="AWSHealth-Type-OrganizationEventDetails-awsAccountId"></a>
The 12-digit AWS account numbers that contains the affected entities.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** event **   <a name="AWSHealth-Type-OrganizationEventDetails-event"></a>
Summary information about an AWS Health event.
 AWS Health events can be public or account-specific:
+  *Public events* might be service events that are not specific to an AWS account. For example, if there is an issue with an AWS Region, AWS Health provides information about the event, even if you don't use services or resources in that Region.
+  *Account-specific* events are specific to either your AWS account or an account in your organization. For example, if there's an issue with Amazon Elastic Compute Cloud in a Region that you use, AWS Health provides information about the event and the affected resources in the account.
You can determine if an event is public or account-specific by using the `eventScopeCode` parameter. For more information, see [eventScopeCode](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode).
Type: [Event](API_Event.md) object
Required: No

 ** eventDescription **   <a name="AWSHealth-Type-OrganizationEventDetails-eventDescription"></a>
The detailed description of the event. Included in the information returned by the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation.
Type: [EventDescription](API_EventDescription.md) object
Required: No

 ** eventMetadata **   <a name="AWSHealth-Type-OrganizationEventDetails-eventMetadata"></a>
Additional metadata about the event.
Type: String to string map
Key Length Constraints: Maximum length of 32766.
Value Length Constraints: Maximum length of 32766.
Required: No

## See Also
<a name="API_OrganizationEventDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationEventDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationEventDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationEventDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

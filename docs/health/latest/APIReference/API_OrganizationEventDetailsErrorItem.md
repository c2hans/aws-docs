---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEventDetailsErrorItem.html
---

# OrganizationEventDetailsErrorItem
<a name="API_OrganizationEventDetailsErrorItem"></a>

Error information returned when a [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation can't find a specified event.

## Contents
<a name="API_OrganizationEventDetailsErrorItem_Contents"></a>

 ** awsAccountId **   <a name="AWSHealth-Type-OrganizationEventDetailsErrorItem-awsAccountId"></a>
Error information returned when a [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation can't find a specified event.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** errorMessage **   <a name="AWSHealth-Type-OrganizationEventDetailsErrorItem-errorMessage"></a>
A message that describes the error.
If you call the `DescribeEventDetailsForOrganization` operation and receive one of the following errors, follow the recommendations in the message:
+ We couldn't find a public event that matches your request. To find an event that is account specific, you must enter an AWS account ID in the request.
+ We couldn't find an account specific event for the specified AWS account. To find an event that is public, you must enter a null value for the AWS account ID in the request.
+ Your AWS account doesn't include the AWS Support plan required to use the AWS Health API. You must have either a AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan.
Type: String
Required: No

 ** errorName **   <a name="AWSHealth-Type-OrganizationEventDetailsErrorItem-errorName"></a>
The name of the error.
Type: String
Required: No

 ** eventArn **   <a name="AWSHealth-Type-OrganizationEventDetailsErrorItem-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

## See Also
<a name="API_OrganizationEventDetailsErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationEventDetailsErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationEventDetailsErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationEventDetailsErrorItem)

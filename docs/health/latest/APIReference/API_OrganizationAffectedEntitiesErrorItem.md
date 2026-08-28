---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationAffectedEntitiesErrorItem.html
---

# OrganizationAffectedEntitiesErrorItem
<a name="API_OrganizationAffectedEntitiesErrorItem"></a>

Error information returned when a [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html) operation can't find or process a specific entity.

## Contents
<a name="API_OrganizationAffectedEntitiesErrorItem_Contents"></a>

 ** awsAccountId **   <a name="AWSHealth-Type-OrganizationAffectedEntitiesErrorItem-awsAccountId"></a>
The 12-digit AWS account numbers that contains the affected entities.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** errorMessage **   <a name="AWSHealth-Type-OrganizationAffectedEntitiesErrorItem-errorMessage"></a>
A message that describes the error. Follow the error message and retry your request.
For example, the `InvalidAccountInputError` error message appears if you call the `DescribeAffectedEntitiesForOrganization` operation and specify the `AccountSpecific` value for the `EventScopeCode` parameter, but don't specify an AWS account.
Type: String
Required: No

 ** errorName **   <a name="AWSHealth-Type-OrganizationAffectedEntitiesErrorItem-errorName"></a>
The name of the error.
Type: String
Required: No

 ** eventArn **   <a name="AWSHealth-Type-OrganizationAffectedEntitiesErrorItem-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

## See Also
<a name="API_OrganizationAffectedEntitiesErrorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationAffectedEntitiesErrorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationAffectedEntitiesErrorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationAffectedEntitiesErrorItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

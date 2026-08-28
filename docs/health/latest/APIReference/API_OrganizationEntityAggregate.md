---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_OrganizationEntityAggregate.html
---

# OrganizationEntityAggregate
<a name="API_OrganizationEntityAggregate"></a>

The aggregate results of entities affected by the specified event in your organization. The results are aggregated by the entity status codes for the specified set of accountsIDs.

## Contents
<a name="API_OrganizationEntityAggregate_Contents"></a>

 ** accounts **   <a name="AWSHealth-Type-OrganizationEntityAggregate-accounts"></a>
A list of entity aggregates for each of the specified accounts in your organization that are affected by a specific event. If there are no `awsAccountIds` provided in the request, this field will be empty in the response.
Type: Array of [AccountEntityAggregate](API_AccountEntityAggregate.md) objects
Required: No

 ** count **   <a name="AWSHealth-Type-OrganizationEntityAggregate-count"></a>
The number of entities for the organization that match the filter criteria for the specified events.
Type: Integer
Required: No

 ** eventArn **   <a name="AWSHealth-Type-OrganizationEntityAggregate-eventArn"></a>
A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** statuses **   <a name="AWSHealth-Type-OrganizationEntityAggregate-statuses"></a>
The number of affected entities aggregated by the entitiy status codes.
Type: String to integer map
Valid Keys: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

## See Also
<a name="API_OrganizationEntityAggregate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/OrganizationEntityAggregate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/OrganizationEntityAggregate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/OrganizationEntityAggregate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

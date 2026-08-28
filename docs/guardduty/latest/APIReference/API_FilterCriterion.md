---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_FilterCriterion.html
---

# FilterCriterion
<a name="API_FilterCriterion"></a>

Represents a condition that when matched will be added to the response of the operation. Irrespective of using any filter criteria, an administrator account can view the scan entries for all of its member accounts. However, each member account can view the scan entries only for their own account.

## Contents
<a name="API_FilterCriterion_Contents"></a>

 ** criterionKey **   <a name="guardduty-Type-FilterCriterion-criterionKey"></a>
An enum value representing possible scan properties to match with given scan entries.
Type: String
Valid Values: `EC2_INSTANCE_ARN | SCAN_ID | ACCOUNT_ID | GUARDDUTY_FINDING_ID | SCAN_START_TIME | SCAN_STATUS | SCAN_TYPE`
Required: No

 ** filterCondition **   <a name="guardduty-Type-FilterCriterion-filterCondition"></a>
Contains information about the condition.
Type: [FilterCondition](API_FilterCondition.md) object
Required: No

## See Also
<a name="API_FilterCriterion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/FilterCriterion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/FilterCriterion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/FilterCriterion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

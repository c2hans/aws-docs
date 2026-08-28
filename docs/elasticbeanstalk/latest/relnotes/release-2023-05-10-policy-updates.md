---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-05-10-policy-updates.html
---

# Release: Elastic Beanstalk managed policy updates on May 10, 2023
<a name="release-2023-05-10-policy-updates"></a>

AWS Elastic Beanstalk has released updates to a managed policy.

**Release date:** May 10, 2023

## Changes
<a name="release-2023-05-10-policy-updates.changes"></a>

AWS services maintains AWS managed policies, occasionally updating them to support new features or updated security standards. This release updates one Elastic Beanstalk managed policy: `AWSElasticBeanstalkService`. This policy was updated to allow Elastic Beanstalk to tag resources upon creation for Elastic Load Balancing, Auto Scaling groups (ASG), and Amazon ECS.

**Note**
This `AWSElasticBeanstalkService` policy has been superseded by `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`. Although this policy is no longer available for attachment to new IAM users, groups, or roles, it may still be attached to prior existing ones.

For the updated history of Elastic Beanstalk managed policies and service-linked roles, see [AWS managed policies for AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/security-iam-awsmanpol.html) in the *AWS Elastic Beanstalk Developer Guide*.

For more information about all AWS managed policies that includes policy contents and last update date, see [AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html) in the *AWS Managed Policy Reference Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/int-actions-prerequisites.html
---

# Prerequisites
<a name="int-actions-prerequisites"></a>

Before using actions in Amazon Quick, ensure you have the following:

## Subscription requirements
<a name="qbs-actions-prerequisites-qbs-actions-license-requirements"></a>

For information about subscription requirements for configuring and using action connectors, see [Set up integrations in the console](integration-console-setup-process.md).

## Service requirements
<a name="qbs-actions-prerequisites-qbs-actions-service-requirements"></a>

For third-party services (such as Jira or Salesforce), ensure that you have:
+ Appropriate permissions in the target services.
+ Authentication credentials for each service.

For AWS action connectors, you need admin access to the relevant services.

## AWS account requirements
<a name="qbs-actions-prerequisites-qbs-actions-aws-account-requirements"></a>
+ Active AWS account - A valid AWS account with billing enabled and in good standing.
+ Appropriate IAM permissions - IAM roles and policies that allow Amazon Quick to access the required AWS services.
+ Required service quotas - Sufficient service limits for the AWS services you plan to integrate with your actions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

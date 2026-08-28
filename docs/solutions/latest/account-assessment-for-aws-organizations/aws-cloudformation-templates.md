---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/aws-cloudformation-templates.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-templates"></a>

You can download the CloudFormation templates for this solution before deploying it.

## Hub stack
<a name="hub-stack"></a>

 [![Orange button with "View template" text for accessing a document or form template](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-hub.template) **account-assessment-for-aws-organizations-hub.template** - Use this template to launch the solution and all associated components in your hub account. The default configuration deploys the [AWS services in this solution](aws-services.md) and the solution web UI to view the findings, but you can customize the template to meet your specific needs.

## Spoke stack
<a name="spoke-stack"></a>

 [![Orange button with "View template" text for accessing a document or form template](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-spoke.template) **account-assessment-for-aws-organizations-spoke.template** - Use this template to launch the solution and all associated components in your spoke account. The default configuration deploys IAM roles.

## Org-Management stack
<a name="orgmanagement-stack"></a>

 [![Orange button with "View template" text for accessing a document or form template](http://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/images/view-template.png)](https://solutions-reference.s3.amazonaws.com/account-assessment-for-aws-organizations/latest/account-assessment-for-aws-organizations-org-management.template) **account-assessment-for-aws-organizations-org-management.template** - Use this template to create an IAM role in you AWS Organizations management account. The hub account requires the role to find account IDs, delegated admin accounts, and trusted access services in your AWS Organizations.

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

This AWS CloudFormation template deploys the Account Assessment for AWS Organizations solution in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Account Assessment for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

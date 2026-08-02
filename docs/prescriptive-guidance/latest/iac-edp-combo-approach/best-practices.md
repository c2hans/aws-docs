---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iac-edp-combo-approach/best-practices.html
---

# Best practices
<a name="best-practices"></a>

To use IaC and EDP together in a way that's compatible, secure, and mutually beneficial, we recommend that you follow these best practices:
+ **Avoid making API calls directly on a resource** – Use the CloudFormation [update-stack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/update-stack.html) API call as part of an EDP approach, and make sure that only CloudFormation makes changes to the EBS volume. To ensure a successful update operation, the volume size must be valid and must not be lower than the value of the resources currently provisioned. The volume size could be a parameter in the CloudFormation stack.
+ **Avoid using a single, monolithic template** – Break your template into modular templates (similar to microservices). Modular templates are easier to update, maintain, and troubleshoot.
+ **Use a feedback mechanism for EDP** – Design feedback mechanisms that are tailored to your organization's needs. In the previous hypothetical scenario, a feedback mechanism could be an auto-generated pull request to the version control system coupled with a solution to tag system events and metadata.
+ **Create notification systems** – Notification systems can help notify the team when a certain event takes place. For example, you can create an email-based notification by using Amazon SNS. Finally, it's a best practice to always ensure that stacks are in sync and that your DevOps system is designed with guardrails that can help you avoid resource drift. For more information, see [Set up AWS CloudFormation drift detection in a multi-Region, multi-account organization](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-aws-cloudformation-drift-detection-in-a-multi-region-multi-account-organization.html) in the AWS Prescriptive Guidance documentation.

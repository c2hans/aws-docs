---
source_url: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/auditing.html
---

# Auditing
<a name="auditing"></a>

 In a microservices architecture, it's crucial to have visibility into user actions across all services. AWS provides tools like AWS CloudTrail, which logs all API calls made in AWS, and AWS CloudWatch, which is used to capture application logs. This allows you to track changes and analyze behavior across your microservices. Amazon EventBridge can react to system changes quickly, notifying the right people or even automatically starting workflows to resolve issues.

![Diagram showing auditing and remediation across your microservices](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/auditing-and-remediation.png)

## Resource inventory and change management
<a name="resource-inventory-and-change-management"></a>

 In an agile development environment with rapidly evolving infrastructure configurations, automated auditing and control are vital. AWS Config Rules provide a managed approach to monitoring these changes across microservices. They enable the definition of specific security policies that automatically detect, track, and send alerts on policy violations.

 For instance, if an API Gateway configuration in a microservice is altered to accept inbound HTTP traffic instead of only HTTPS requests, a predefined AWS Config rule can detect this security violation. It logs the change for auditing and triggers an SNS notification, restoring the compliant state.

![Diagram showing how to detect security violations with AWS Config](http://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/images/detect-security-violations.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

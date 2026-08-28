---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-roles-user.html
---

# Elastic Beanstalk user policy
<a name="concepts-roles-user"></a>

Create IAM users for each user who uses Elastic Beanstalk to avoid using your root account or sharing credentials. As a security best practice, only grant these users permissions to access services and features that they need.

Elastic Beanstalk requires permissions not only for its own API actions, but also for several other AWS services. Elastic Beanstalk uses user permissions to launch resources in an environment. These resources include EC2 instances, an Elastic Load Balancing load balancer, and an Auto Scaling group. Elastic Beanstalk also uses user permissions to save logs and templates to Amazon Simple Storage Service (Amazon S3), send notifications to Amazon SNS, assign instance profiles, and publish metrics to CloudWatch. Elastic Beanstalk requires CloudFormation permissions to orchestrate resource deployments and updates. It also requires Amazon RDS permissions to create databases when needed, and Amazon SQS permissions to create queues for worker environments.

For more information about user policies, see [Managing Elastic Beanstalk user policies](AWSHowTo.iam.managed-policies.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

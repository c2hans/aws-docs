---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/conclusion.html
---

# Conclusion
<a name="conclusion"></a>

Transitioning from a single AWS account to multiple accounts can feel overwhelming at first without an adoption strategy. By implementing a multi-account strategy, you can address many challenges that companies face when using a single AWS account:
+ **Mistaking production data for development data** – You can grant different permissions and access by using AWS IAM Identity Center with separate permission sets production and non-production organizational units. Only highly privileged users should have access to the production database, and that access should be for limited periods of time and audited.
+ **Production deployment affecting other business operations** – You can separate stakeholders by using multiple accounts and multiple environments. For example, you could create a dedicated sales demo environment, within a non-production account, so that you can plan deployments and releases when demos aren't occurring.
+ **Slow production workload performance when testing development workloads** – Each AWS account has independent service quotas that govern each service. By using multiple accounts, you can limit the scope of one environment impacting another environment.
+ **Distinguishing production costs from development costs** – Consolidated billing for the organization rolls up all of the costs at the AWS account level so that the finance team can see how much production costs compared to non-production environments, such as development, testing, and demo environments. You can also use tags and tagging policies to separate costs within an account.
+ **Limiting access to sensitive data** – IAM Identity Center allows you to have separate access policies for a group of people associated to a specific account.
+ **Controlling costs** – By using service-control policies (SCPs) in a multi-account architecture, you can disallow access to specific AWS services that might incur high costs for your organization. SCPs can deny all access to specific services or can limit the usage of a service to a specific type, such as restricting the types of Amazon Elastic Compute Cloud (Amazon EC2) instances that can be created.

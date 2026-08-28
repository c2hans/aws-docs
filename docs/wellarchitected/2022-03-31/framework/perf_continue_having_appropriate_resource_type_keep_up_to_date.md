---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_continue_having_appropriate_resource_type_keep_up_to_date.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF06-BP01 Stay up-to-date on new resources and services
<a name="perf_continue_having_appropriate_resource_type_keep_up_to_date"></a>

Evaluate ways to improve performance as new services, design patterns, and product offerings become available. Determine which of these could improve performance or increase the efficiency of the workload through evaluation, internal discussion, or external analysis.

Define a process to evaluate updates, new features, and services relevant to your workload. For example, building a proof of concept that uses new technologies or consulting with an internal group. When trying new ideas or services, run performance tests to measure the impact that they have on the performance of the workload. Using infrastructure as code (IaC) and a DevOps culture to take advantage of the ability to test new ideas or technologies frequently with minimal cost or risk.

 **Desired outcome:** You have documented the inventory of components, your design pattern, and your workload characteristics. You use that documentation to create a list of subscriptions to notify your team on service updates, features, and new products. You have identified component stakeholders that will evaluate the new releases and provide a recommendation for business impact and priority.

 **Common anti-patterns:**
+  You only review new options and services when your workload is not meeting performance requirements.
+  You assume all new product offerings will not be useful to your workload.
+  You always choose to build as opposed to buy when improving your workload.

 **Benefits of establishing this best practice:** By considering new services or product offerings, you can improve the performance and efficiency of your workload, lower the cost of the infrastructure, and reduce the effort required to maintain your services.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Define a process to evaluate updates, new features, and services from AWS. For example, building proof-of-concepts that use new technologies. When trying new ideas or services, run performance tests to measure the impact on the efficiency or performance of the workload. Take advantage of the flexibilfity that you have in AWS to test new ideas or technologies frequently with minimal cost or risk.

## Implementation steps
<a name="implementation-steps"></a>

1.  Document your workload solutions. Use your configuration management database (CMDB) solution to document your inventory and categorize your services and dependencies. Use tools like [AWS Config](https://aws.amazon.com/config/) to get a list of all services in AWS being used by your workload.

1.  Use a [tagging strategy](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) to document owners for each workload component and category. For example, if you are currently using Amazon RDS as your database solution, have your database administrator (DBA) assigned and documented as the owner for evaluating and researching new services and updates.

1.  Identify news and update sources related to your workload components. In the Amazon RDS example previously mentioned, the category owner should subscribe to the [What’s New at AWS blog](https://aws.amazon.com/new/) for the products that match their workload component. You can subscribe to the RSS feed or manage your [email subscriptions](https://pages.awscloud.com/communication-preferences.html). Monitor upgrades to the Amazon RDS database you use, features introduced, instances released and new products like Amazon Aurora Serverless. Monitor industry blogs, products, and vendors that the component relies on.

1.  Document your process for evaluating updates and new services. Provide your category owners the time and space needed to research, test, experiment, and validate updates and new services. Refer back to the documented business requirements and KPIs to help prioritize which update will make a positive business impact.

 **Level of effort for the implementation plan:** To establish this best practice, you must be aware of your current workload components, identify category owners and identify sources for service updates. This is a low level of effort to start but is an ongoing process that could evolve and improve over time.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Blog](https://aws.amazon.com/blogs/)
+  [What's New with AWS](https://aws.amazon.com/new/?ref=wellarchitected)

 **Related videos:**
+  [AWS Events YouTube Channel](https://www.youtube.com/channel/UCdoadna9HFHsxXWhafhNvKw)
+  [AWS Online Tech Talks YouTube Channel](https://www.youtube.com/user/AWSwebinars)
+  [Amazon Web Services YouTube Channel](https://www.youtube.com/channel/UCd6MoB9NC6uYN2grvUNT-Zg)

 **Related examples:**
+  [AWS Github](https://github.com/aws)
+  [AWS Skill Builder](https://explore.skillbuilder.aws/learn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

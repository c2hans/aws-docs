---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_securely_operate_implement_services_features.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP08 Evaluate and implement new security services and features regularly
<a name="sec_securely_operate_implement_services_features"></a>

 Evaluate and implement security services and features from AWS and AWS Partners that allow you to evolve the security posture of your workload. The AWS Security Blog highlights new AWS services and features, implementation guides, and general security guidance. [What's New with AWS?](https://aws.amazon.com/new) is a great way to stay up to date with all new AWS features, services, and announcements.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Plan regular reviews: Create a calendar of review activities that includes compliance requirements, evaluation of new AWS security features and services, and staying up-to-date with industry news.
+  Discover AWS services and features: Discover the security features that are available for the services that you are using, and review new features as they are released.
  + [AWS security blog](https://aws.amazon.com/blogs/security/)
  + [AWS security bulletins ](https://aws.amazon.com/security/security-bulletins/)
  +  [AWS service documentation ](https://aws.amazon.com/documentation/)
+  Define AWS service on-boarding process: Define processes for onboarding of new AWS services. Include how you evaluate new AWS services for functionality, and the compliance requirements for your workload.
+  Test new services and features: Test new services and features as they are released in a non-production environment that closely replicates your production one.
+  Implement other defense mechanisms: Implement automated mechanisms to defend your workload, explore the options available.
  +  [Remediating non-compliant AWS resources by AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)

## Resources
<a name="resources"></a>

 **Related videos:**
+  [Security Best Practices the Well-Architected Way ](https://youtu.be/u6BCVkXkPnM)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

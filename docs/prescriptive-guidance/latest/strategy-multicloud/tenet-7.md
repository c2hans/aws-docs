---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/tenet-7.html
---

# Tenet 7. Have a single CCoE, but specialize within it
<a name="tenet-7"></a>

As [we advise many AWS customers](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/), you should build a Cloud Center of Excellence (CCoE) within your organization to provide leadership, standardization, and acceleration of your cloud journey. When it comes to multicloud environments, we find that the most successful companies take a balanced approach with their CCoE.

Instead of establishing separate CCoEs for each CSP, we recommend that you have a single, unified CCoE that oversees the organization's multicloud strategy. This helps ensure a coordinated, consistent approach instead of siloed efforts that can lead to divergence, reengineering, and waste. Make sure that the teams within your single CCoE have the necessary specialized skills, tools, and mechanisms for each CSP that your organization uses. This specialized knowledge allows the CCoE to govern, support, and accelerate the use of the different cloud platforms effectively.

For example, the CCoE should have AWS-specific experts who understand the AWS Cloud, services, and best practices in depth, as well as experts for other CSPs who can guide the organization's use of those cloud technologies. This specialized expertise within the single CCoE can help your organization benefit from the coordination and standardization of a centralized approach while ensuring that each cloud platform is being used optimally.

The single CCoE should serve as the central governing body that establishes standards, policies, and best practices for the organization's multicloud strategy. The actual implementation of cloud workloads and projects can be distributed to specialized teams or business units while the CCOE provides oversight, support, and coordination. This balanced approach helps ensure a cohesive multicloud strategy while providing the necessary degree of flexibility and autonomy within the organization.

The following diagram illustrates how a CCoE can provide a centralized approach and governance across multiple lines of business (LOBs), cloud engineering teams, and Cloud Business Office (CBO) teams.

![CCoE structure in a multicloud environment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-multicloud/images/guide-img/8816e8ab-0d53-4fd1-b9e5-e4a8b4620ced/images/bfe0628a-fe90-4908-9db0-cf44ac9e7f9a.png)

**Our guidance:**
+ Structure your CCoE to maintain strategic oversight while embedding specialized expertise for each cloud provider. Focus on recruiting deep expertise in individual cloud platforms instead of seeking rare multicloud specialists, and foster internal knowledge sharing to build organizational capabilities.
+ Empower your CCoE to establish enterprise-wide standards for cross-cutting concerns such as security and observability, while giving individual teams the autonomy to execute within these guidelines by using cloud-native tools and services.
+ Develop a comprehensive talent strategy that balances deep expertise in primary cloud platforms with broader architectural knowledge. Focus on building teams that combine strong, cloud-specific skills with enterprise architecture experience.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

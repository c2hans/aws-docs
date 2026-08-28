---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-multiple-aws-accounts.html
---

# Benefits of using multiple AWS accounts
<a name="benefits-of-using-multiple-aws-accounts"></a>

 As you adopt AWS, we recommend that you determine how your business, governance, security, and operational requirements can be met in AWS. Use of multiple AWS accounts plays an important role in how you meet those requirements.

 The use of multiple accounts enables you to realize the benefits in the following sections.

**Topics**
+ [Group workloads based on business purpose and ownership](#group-workloads-based-on-business-purpose-and-ownership)
+ [Apply distinct security controls by environment](#apply-distinct-security-controls-by-environment)
+ [Constrain access to sensitive data](#constrain-access-to-sensitive-data)
+ [Promote innovation and agility](#promote-innovation-and-agility)
+ [Limit scope of impact from adverse events](#limit-scope-of-impact-from-adverse-events)
+ [Support multiple IT operating models](#support-multiple-it-operating-models)
+ [Manage costs](#manage-costs)
+ [Distribute AWS Service Quotas and API request rate limits](#distribute-aws-service-quotas-and-api-request-rate-limits)

## Group workloads based on business purpose and ownership
<a name="group-workloads-based-on-business-purpose-and-ownership"></a>

 You can group workloads with a common business purpose in distinct accounts. As a result, you can align the ownership and decision making with those accounts and avoid dependencies and conflicts with how workloads in other accounts are secured and managed.

 Different business units or product teams might have different processes or security boundary requirements. Depending on your overall business model, you might choose to isolate distinct business units or subsidiaries in different accounts or Organizational Units. Isolation of business units can help them operate with greater decentralized control, but still provides the ability for you to provide overarching controls. This approach might also ease divestment of those units over time.

 *Controls* are governance rules for security, operations, and compliance that you can define and apply to align with your overall requirements.

 If you acquire a business that is already operating in AWS, you can move the associated accounts intact into your existing organization. This movement of accounts can be an initial step toward integrating acquired services into your standard account structure.

## Apply distinct security controls by environment
<a name="apply-distinct-security-controls-by-environment"></a>

 Workloads often have distinct security postures that require separate controls and mechanisms to support them. For example, it's common to apply different security and operational controls for the non-production and production environments of a given workload. By using separate accounts for the non-production and production environments, by default, the resources and data that make up a workload environment are separated from other environments and workloads.

## Constrain access to sensitive data
<a name="constrain-access-to-sensitive-data"></a>

 A key benefit of a multi-account architecture is the ability to create distinct data perimeters. By limiting sensitive data stores to dedicated accounts, you can more tightly control access and minimize the number of people and processes that can interact with that data. This simplified access model aligns with the principle of least privilege, as you can restrict permissions at the coarse-grained account level rather than needing to manage fine-grained access within a single broad account.

 Establishing these data perimeters is particularly valuable for highly confidential or regulated information. By segmenting sensitive data into its own secured account, you can drastically reduce the exposure surface and attack vectors. This account-level isolation helps contain potential data breaches and ensures that even in the event of a security incident, the blast radius remains limited to that specific data domain rather than impacting your entire cloud environment.

 For example, designating a set of accounts to house publicly accessible (Amazon S3) buckets enables you to implement policies for all of your other accounts to prohibit making Amazon S3 buckets publicly available.

## Promote innovation and agility
<a name="promote-innovation-and-agility"></a>

 In the early stages of a workload's lifecycle, you can help promote innovation by providing your builders with separate accounts in support of experimentation, development, and early testing.

 These environments often provide greater freedom than more tightly controlled production-like test and production environments by enabling broader access to AWS services while using controls to help prohibit access to and use of sensitive and internal data.
+ **Sandbox accounts** are typically disconnected from your enterprise services and do not provide access to your internal data, but offer the greatest freedom for experimentation.
+ **Development accounts** typically provide limited access to your enterprise services and development data, but can more readily support day-to-day experimentation with your enterprise approved AWS services, formal development, and early testing work.

 In both cases, we recommend security controls and cost budgets so that you limit risks and proactively manage costs.

 In support of later stages of the workload lifecycle, you can use distinct test and production accounts for workloads or groups of related workloads. Having an environment for each set of workloads can enable owning teams to move faster by reducing dependencies on other teams and workloads and minimizing the impact of changes.

## Limit scope of impact from adverse events
<a name="limit-scope-of-impact-from-adverse-events"></a>

 The inherent isolation provided by an AWS account can be leveraged to limit the scope of impact from issues within your cloud environment. By provisioning resources within dedicated accounts, you establish clear security, access, and billing boundaries that prevent problems from spreading between different parts of your infrastructure. This account-level isolation is a key benefit of a multi-account strategy, as it helps ensure that if an application-level problem, misconfiguration, or malicious activity occurs within one account, the impacts can be contained and prevented from impacting workloads in other accounts. Maintaining this resource independence across multiple accounts is a powerful way to manage risk and help ensure failures remain localized, providing a safeguard against wider disruptions that could occur in a single monolithic account environment.

## Support multiple IT operating models
<a name="support-multiple-it-operating-models"></a>

 Organizations often have multiple IT operating models or ways in which they divide responsibilities among parts of the organization to deliver their application workloads and platform capabilities. The following figure shows three example operating models:

![Diagram showing example operating models](http://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/images/example-operating-models.png)

+ In the *Traditional Ops* model, teams who own custom and commercial off-the-shelf (COTS) applications are responsible for engineering their applications, but not for their production operations. A cloud platform engineering team is responsible for engineering the underlying platform capabilities. A separate cloud operations team is responsible for the operations of both applications and platform.
+ In the *CloudOps model*, application teams are also responsible for production operations of their applications. In this model, a common cloud platform engineering team is responsible for both engineering and operations of the underlying platform capabilities.
+ In the *DevOps model*, the application teams take on the additional responsibilities of engineering and operating platform capabilities that are specific to their applications. A cloud platform engineering team is responsible for engineering and operations of shared platform capabilities that are used by multiple applications.

 As a practice, IT Service Management (ITSM) is a common element across all of the models. Your overall goals and requirements of ITSM might not change across these models, but the responsible individuals and solutions for meeting those goals and requirements can vary depending on the model.

 Given the implications of centralized operations versus more distributed operational responsibilities, you will likely benefit from establishing separate groups of accounts in support of different operating models. Use of separate accounts enables you to apply distinct governance and operational controls that are appropriate for each of your operating models. To learn more about operating models and their implications on your cloud adoption, refer to the [AWS Well-Architected Operational Excellence Pillar Operating Model.](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model.html)

## Manage costs
<a name="manage-costs"></a>

 An account is the default means by which AWS costs are allocated. Because of this fact, using different accounts for different business units and groups of workloads can help you more easily report, control, forecast, and budget your cloud expenditures.

 In addition to cost reporting at the account level, AWS has built-in support to consolidate and report costs across your entire set of accounts. When you require fine-grained cost allocation, you can apply cost allocation tags to individual resources in each of your accounts. For more information about cost optimization, see the AWS Well-Architected Cost Optimization Pillar's [Expenditure and Usage Awareness](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/expenditure-and-usage-awareness.html) best practices.

## Distribute AWS Service Quotas and API request rate limits
<a name="distribute-aws-service-quotas-and-api-request-rate-limits"></a>

 [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html), also known as limits, are the maximum number of service resources or operations that apply to an account. For example, the number of Amazon S3 buckets that you can create for each account.

 You can use Service Quotas to help protect you from unexpected excessive provisioning of AWS resources and malicious actions that could dramatically impact your AWS costs.

 AWS services can also throttle or limit the rate of requests made to their API operations. Because Service Quotas and request rate limits are allocated for each account, use of separate accounts for workloads can help distribute the potential impact of the quotas and limits.

 To learn more about managing service quotas, refer to the AWS Well-Architected Reliability Pillar: [Manage Service Quotas and Constraints](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/manage-service-quotas-and-constraints.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

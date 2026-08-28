---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/iam-resources.html
---

# IAM resources
<a name="iam-resources"></a>

Although AWS Identity and Access Management (IAM) is not a service that is included in a traditional architecture diagram, it touches every aspect of the AWS organization, AWS accounts, and AWS services. You cannot deploy any AWS services without creating IAM entities and granting permissions first. A full explanation of IAM is beyond the scope of this document, but this section provides important summaries of best practice recommendations and pointers to additional resources.
+ For IAM best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the AWS documentation, [IAM articles](https://aws.amazon.com/blogs/security/category/security-identity-compliance/aws-identity-and-access-management-iam/) in the AWS Security blog, and [AWS re:Invent presentations](https://www.youtube.com/watch?v=YQsK4MtsELU).
+ The AWS Well-Architected security pillar outlines key steps in the [permissions management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/permissions-management.html) process: define permissions guardrails, grant least privilege access, analyze public and cross-account access, share resources securely, reduce permissions continuously, and establish an emergency access process.
+ The following table and its accompanying notes provide a high-level overview of recommended guidance on types of available IAM permission policies and how to use them in your security architecture. To learn more, see the [AWS re:Invent 2020 video on choosing the right mix of IAM policies](https://www.youtube.com/watch?v=o1bfA0SIxBk).

|
|
| Use case or policy | Effect | Managed by | Purpose | Pertains to | Affects | Deployed in |
| --- |--- |--- |--- |--- |--- |--- |
| **Service control policies (SCPs)** | Restrict | Central team, such as platform or security team [1] | Guardrails, governance | Organization, OU, account | All principals in Organization, OU, and accounts | Org Management account [2] |
| **Resource control policies (RCPs)** | Restrict | Central team, such as platform or security team [1] | Guardrails, governance | Organization, OU, account | Resources in member accounts [12] | Org Management account [2] |
| **Baseline account automation policies**  (the IAM roles used by the platform to operate an account) | Grant and restrict | Central team, such as platform, security, or IAM team [1] | Permissions for (baseline) non-workload automation roles [3] | Single account [4] | Principals used by automation within a member account | Member accounts |
| **Baseline human policies**  (the IAM roles that grant users permissions to perform their work) | Grant and restrict | Central team, such as platform, security, or IAM team [1] | Permissions for human roles [5] | Single account [4] | Federated principals [5] and IAM users [6] | Member accounts |
| **Permissions boundaries**  (maximum permissions that an empowered developer can assign to another principal) | Restrict | Central team, such as platform, security, or IAM team [1] | Guardrails for application roles (must be applied) | Single account [4] | Individual roles for an application or workload in this account [7] | Member accounts |
| **Machine role policies for applications**  (role attached to infrastructure deployed by developers) | Grant and restrict | Delegated to developers [8] | Permission for the application or workload [9] | Single account | A principal in this account | Member accounts |
| **Resource policies** | Grant and restrict | Delegated to developers [8,10] | Permissions to resources | Single account | A principal in an account [11] | Member accounts |
| **Central root user management** | Grant and restrict | Central team, such as platform, security, or IAM team [1] | Centrally manage member account root users at scale | Organization | All root users in member accounts | Org management account, delegated administrator account |

Notes from the table:

1. Enterprises have many centralized teams (such as cloud platform, security operations, or identity and access management teams) that divide the responsibilities of these independent controls, and peer review one another's policies. The examples in the table are placeholders. You will need to determine the most effective separation of duties for your enterprise.

1. To use SCPs, you must [enable all features](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) within AWS Organizations.

1. Common baseline roles and policies are generally needed to enable automation, such as permissions for the pipeline, deployment tools, monitoring tools (for example, AWS Lambda and AWS Config Rules), and other permissions. This configuration is typically delivered when the account is provisioned.

1. Although these pertain to a resource (such as a role or a policy) in a single account, they can be replicated or deployed to multiple accounts by using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

1. Define a core set of baseline human roles and policies that are deployed to all member accounts by a central team (often during account provisioning). Examples include the developers in the platform team, the IAM team, and security audit teams.

1. Use identity federation (instead of local IAM users) whenever possible.

1. Permissions boundaries are used by delegated administrators. This IAM policy defines the maximum permissions and overrides other policies (including `"*:*"` policies that allow all actions on resources). Permissions boundaries should be required in baseline human policies as a condition to create roles (such as workload performance roles) and to attach policies. Additional configurations such as SCPs enforce the attachment of the permissions boundary.

1. This assumes that sufficient guardrails (for example, SCPs and permissions boundaries) have been deployed.

1. These optional policies could be delivered during account provisioning or as part of the application development process. The permission to create and attach these policies will be governed by the application developer's own permissions.

1. In addition to local account permissions, a centralized team (such as the cloud platform team or the security operations team) often manages some resource-based policies to enable cross-account access to operate the accounts (for example, to provide access to S3 buckets for logging).

1. A resource-based IAM policy can refer to any principal in any account to allow or deny access to its resources. It can even refer to anonymous principals to enable public access.

1. RCPs apply to resources for a subset of AWS services. For more information, see [List of AWS services that support RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#rcp-supported-services) in the AWS Organizations documentation.

Ensuring that IAM identities have only those permissions that are necessary for a well-delineated set of tasks is critical for reducing the risk of malicious or unintentional abuse of permissions. Establishing and maintaining a [least privilege model](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) requires a deliberate plan to continually update, evaluate, and mitigate excess privilege. Here are some additional recommendations for that plan:
+ Use your organization's governance model and established risk appetite to establish specific guardrails and permissions boundaries.
+ Implement least privilege through a *continually iterative process*. This is not a one-time exercise.
+ Use SCPs to reduce actionable risk. These are intended to be broad guardrails, not narrowly targeted controls.
+ Use permissions boundaries to delegate IAM administration in a safer way.
  + Make sure that the delegated administrators attach the appropriate IAM boundary policy to the roles and users they create.
+ As a defense-in-depth approach (in conjunction with identity-based policies), use resource-based IAM policies to deny broad access to resources.
+ Use IAM access advisor, AWS CloudTrail, IAM Access Analyzer, and related tooling to regularly analyze historical usage and permissions granted. Immediately remediate obvious over-permissions.
+ Scope broad actions to specific resources where applicable instead of using an asterisk as a wildcard to indicate all resources.
+ Implement a mechanism to quickly identify, review, and approve IAM policy exceptions based upon requests.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

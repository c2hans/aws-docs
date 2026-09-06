---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/engineering-cultural-considerations.html
---

# Engineering cultural considerations
<a name="engineering-cultural-considerations"></a>

One of the pillars of the AWS Well-Architected Framework is Operational Excellence. Teams must understand the [operating model](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model.html) and their part in achieving your business outcomes. Teams can focus on achieving shared goals when they understand their responsibilities, can take ownership, and know how decisions are made.

With early stage companies that are building quickly, everyone on the team performs multiple roles. It isn't uncommon for these users to have highly privileged access to the entire AWS account. As companies grow, they often want to follow the principle of *least privilege* and only grant permissions that are required for the user to do their job. To help you limit scope, you can use [AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to see what permissions a user or IAM role is actually using, allowing you to remove any excess permissions.

It can be challenging to decide who in your company has permissions to create IAM roles. This is commonly a vector for escalating privileges. Escalating privileges is when a user can expand their own permissions or scope of access. For example, if a user has limited permissions but can create new IAM roles, that user could escalate their privileges by creating and assuming a new IAM role that has the `AdministratorAccess` managed policy applied.

Some companies limit IAM role provisioning to a centralized team of trusted individuals. The downside of this approach is that this team can quickly become a bottleneck because almost all AWS services require an IAM role to operate. As an alternative, you can use [permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) to delegate IAM access to only users who are developing, testing, launching, and managing your cloud infrastructure. For example policies, see [Example Permission Boundaries](https://github.com/aws-samples/example-permissions-boundary) (GitHub).

Development operations (DevOps) teams, also known as *platform* teams, often need to balance self-service capabilities for multiple internal development teams against application operational stability. Fostering an engineering culture that embraces autonomy, mastery, and purpose in the workplace can help motivate teams. Engineers want to do their work in a self-directed manner, without relying on others to do things for them. If DevOps teams can implement self-service solutions, this also reduces the amount of time others depend on them to get things done.

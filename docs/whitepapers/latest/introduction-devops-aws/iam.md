---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/iam.html
---

# Identity and Access Management
<a name="iam"></a>

[AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) defines the controls and polices that are used to manage access to AWS resources. Using IAM you can create users and groups and define permissions to various DevOps services.

In addition to the users, various services may also need access to AWS resources. For example, your CodeBuild project might need access to store Docker images in [Amazon Elastic Container Registry](https://aws.amazon.com/ecr) (Amazon ECR) and need permissions to write to Amazon ECR. These types of permissions are defined by a special type role know as service role.

IAM is one component of the AWS security infrastructure. With IAM, you can centrally manage groups, users, service roles and security credentials such as passwords, access keys, and permissions policies that control which AWS services and resources users can access. [IAM Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) lets you define the set of permissions. This policy can then be attached to either a [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html), [user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html), or a [service](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) to define their permission.

You can also use IAM to create roles that are used widely within your desired DevOps strategy. In some cases, it can make perfect sense to programmatically [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) instead of directly getting the permissions. When a service or user assumes roles, they are given temporary credentials to access a service that they normally don’t have access to.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution.html
---

# Provision least-privilege IAM roles by deploying a role vending machine solution
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution"></a>

*Benjamin Morris, Nima Fotouhi, Aman Kaur Gandhi, and Chad Moon, Amazon Web Services*

## Summary
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-summary"></a>

Over-scoped AWS Identity and Access Management (IAM) role permissions for pipelines can introduce unnecessary risk to an organization. Developers sometimes grant broad permissions during development but neglect to scope down permissions after troubleshooting their code. This causes a problem where powerful roles are present without a business need and may have never been reviewed by a security engineer.

This pattern offers a solution to this problem: the role vending machine (RVM). Using a secure and centralized deployment model, the RVM demonstrates how to provision least-privilege IAM roles for individual GitHub repositories’ pipelines with minimal effort from developers. Because the RVM is a central solution, you can configure your security teams as required reviewers to approve changes. This approach allows security to reject over-permissioned pipeline role requests.

The RVM takes Terraform code as input and generates pipeline-ready IAM roles as output. The required inputs are the AWS account ID, GitHub repository name, and permissions policy. The RVM uses these inputs to create the role’s trust policy and permissions policy. The resulting trust policy allows the specified GitHub repository to assume the role and use it for pipeline operations.

The RVM uses an IAM role (configured during bootstrap). This role has permissions to assume a role-provisioning-role in each account in the organization. The role is configured through either AWS Control Tower Account Factory for Terraform (AFT) or AWS CloudFormation StackSets. The role-provisioning-roles are the roles that actually create the pipeline roles for developers.

## Prerequisites and limitations
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ A GitHub organization that is used to deploy infrastructure as code (IaC) through GitHub Actions. (GitHub Enterprise/Premium/Ultimate are *not*** **required.)
+ A multi-account AWS environment. This environment does not need to be part of AWS Organizations.
+ A mechanism for deploying an IAM role in all AWS accounts (for example, AFT or CloudFormation StackSets).
+ Terraform version 1.3 or latter [installed and configured](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).
+ Terraform AWS Provider version 4 or later [installed](https://github.com/hashicorp/terraform-provider-aws/releases) and [configured](https://developer.hashicorp.com/terraform/language/providers/configuration).

**Limitations**
+ This pattern’s code is specific to GitHub Actions and Terraform. However, the pattern’s general concepts can be reused in other continuous integration and delivery (CI/CD) frameworks.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-architecture"></a>

The following diagram illustrates the workflow for this pattern.

![Workflow to automate IAM role creation and deployment by using GitHub Actions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/215c590e-0c84-411d-be6e-b1739f1e19d2/images/82fcdc9f-9576-4e7c-b7fe-b45046ba79d2.png)

The workflow for the typical usage of the role vending machine consists of the following steps:

1. A developer pushes code that contains Terraform code for a newly requested IAM role to the RVM GitHub repository. This action triggers the RVM GitHub Actions pipeline.

1. The pipeline uses an OpenID Connect (OIDC) trust policy to assume the RVM role-assumption role.

1. As the RVM pipeline runs, it assumes the RVM workflow role in the account in which it’s provisioning the developer’s new IAM role. (The RVM workflow role was provisioned by using AFT or CloudFormation StackSets.)

1. The RVM creates the developer’s IAM role with appropriate permissions and trust, so that the role can be assumed by other application pipelines.

1. App developers can configure their app pipelines to assume this RVM-provisioned role.

The created role includes the permissions requested by the developer and a `ReadOnlyAccess` policy. The role is assumable only by pipelines that run against the `main` branch of the developer’s specified repository. This approach helps to ensure that branch protection and reviews can be required to use the role.

**Automation and scale**

Least-privilege permissions require attention to detail for each role being provisioned. This model reduces the complexity required to create these roles, allowing developers to create the roles they need without much additional learning or effort.

## Tools
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-tools"></a>

**AWS services**
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

**Other tools**
+ [Git](https://git-scm.com/docs) is an open source, distributed version control system. It includes the ability to create an [organization account](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts#organization-accounts).
+ [GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.
+ [Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool from HashiCorp that helps you create and manage cloud and on-premises resources.

**Code repository**

The code for this pattern is available in the GitHub [role-vending-machine](https://github.com/aws-samples/role-vending-machine) repository.

## Best practices
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-best-practices"></a>
+ **Make the right way easy and the wrong way hard** – Make it easy to do the right thing. If developers are struggling with the RVM provisioning process, they might attempt to create roles through other means, which undermines the central nature of RVM. Make sure that your security team provides clear guidance about how to use the RVM securely and effectively.

  You should also make it hard for developers to do the wrong thing. Use service control policies (SCPs) or permission boundaries to restrict what roles can create other roles. This approach can help limit role creation to just RVM and other trusted sources.
+ **Provide good examples** – Inevitably, some developers will adapt existing roles in the RVM repository as informal templates for granting permissions to their new roles. If you have least-permissions examples that they can copy from, that can reduce the risk of developers requesting broad, wildcard-heavy permissions. If you start with highly permissioned roles with lots of wildcards, that problem can multiply as time goes on.
+ **Use naming conventions and conditions** – Even if a developer doesn’t know all the resource names that their application will create, they should still limit role permissions by using a naming convention. For example, if they’re creating Amazon S3 buckets, their resource key’s value might look like `arn:aws:s3:::myorg-myapp-dev-*` so that their role doesn’t have permissions beyond buckets matching that name. Enforcing naming convention through an IAM policy has the additional benefit of improving compliance with the naming convention. This improvement occurs because non-matching resources will not be permitted to be created.
+ **Require pull request (PR) reviews** – The value of the RVM solution is that it creates a central location where new pipeline roles can be reviewed. However, this design is only useful if there are guardrails that help ensure secure, high-quality code is committed to the RVM. Protect the branches that are used to deploy code (for example, `main`) from direct pushes and require approvals for any merge requests that target them.
+ **Configure read-only roles** – By default, the RVM provisions a `readonly` version of each requested role. This role can be used in CI/CD pipelines that don’t write data, such as a `terraform plan` pipeline workflow. This approach helps prevent unwanted changes if a read-only workflow misbehaves.

  By default, the AWS managed `ReadOnlyAccess` policy is attached to both the read-only roles and read-write roles. This policy reduces the need for iteration when determining required permissions, but it might be overly permissive for some organizations. If you want, you can remove the policy from the Terraform code.
+ **Grant minimum permissions** – Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-epics"></a>

### Prepare environment
<a name="prepare-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the sample repository to your GitHub organization. | [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this pattern’s repository or [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository to your GitHub organization so that you can adapt it for your needs.+ If you choose to clone this repository, you can use the following command: `git clone https://github.com/aws-samples/role-vending-machine`<br />+ If you choose to fork the repository to your GitHub organization, you can use the following command:<br />`gh repo fork aws-samples/role-vending-machine --org YOUR_ORGANIZATION_NAME` | DevOps engineer |
| Determine the AWS account for the RVM. | Determine which infrastructure deployment AWS account to use for the RVM. Don’t use the management or root account. | Cloud architect |
| (Optional) Allow the organization's pipelines to create PRs. | This step is only necessary if you want to allow the `generate_providers_and_account_vars` workflow to create PRs.To allow your organization’s pipelines to create PRs, use the following steps:1. Go to `https://github.com/organizations/YOUR_ORG/settings/actions`.<br />2. Select **Allow GitHub Actions to create and approve pull requests**.<br />For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/enterprise-server@3.10/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests) in the GitHub documentation. | DevOps engineer |
| Grant read-only permissions to the RVM account. | Create a delegation policy in your management account that grants your RVM account read-only permissions. This allows your RVM GitHub workflows to dynamically pull a list of your AWS organization's accounts when the `generate_providers_and_account_vars.py` script runs. <br />Use the following code and replace `<YOUR RVM Account ID>` with the AWS account ID that you selected in Step 2:<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Sid": "Statement",<br />      "Effect": "Allow",<br />      "Principal": {<br />        "AWS": "arn:aws:iam::<YOUR RVM Account ID>:root"<br />      },<br />      "Action": [<br />        "organizations:ListAccounts",<br />        "organizations:DescribeOrganization",<br />        "organizations:DescribeOrganizationalUnit",<br />        "organizations:ListRoots",<br />        "organizations:ListAWSServiceAccessForOrganization",<br />        "organizations:ListDelegatedAdministrators"<br />      ],<br />      "Resource": "*"<br />    }<br />  ]<br />}</pre> | Cloud administrator |
| Update default values from the sample repo. | To configure the RVM to operate in your specific environment and AWS Region, do the following:1. Update `scripts/generate_providers_and_account_vars.py` and other files (such as the `bootstrap` folder) with the appropriate Region that you operate in.<br />2. Update the `.github/workflows/.env` file with the AWS account ID, Region, and any other variables that you want to specify. | DevOps engineer |

### Initialize infrastructure
<a name="initialize-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bootstrap the RVM repo. | This step is necessary to create the OIDC trust and IAM roles used by the RVM pipeline itself, so that it can start operating and vending other roles.<br />In the context of your RVM account, manually run a `terraform apply` command from the `scripts/bootstrap` directory. Provide any required values based on variable documentation. | DevOps engineer |

### Configure operations
<a name="configure-operations"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the `github-workflow-rvm` and `github-workflow-rvm-readonly` roles to all accounts. | Choose a deployment method that aligns with your organization’s practices, such as AFT or StackSets. Use that method to deploy the two IAM roles in the `scripts/assumed_role/main.tf` file (default names `github-workflow-rvm` and `github-workflow-rvm-readonly`) to each account where you want the RVM to be able to create pipeline roles.<br />These IAM roles have trust policies that allows the RVM account’s role-assumption role (or its `readonly` equivalent) to assume it. The roles also have IAM permission policies that allow them to read and write (unless using the `readonly` role) roles that match `github-workflow-role-*`. | AWS administrator |
| Run the `generate_providers_and_account_vars` workflow. | To configure your RVM so that it’s ready to create pipeline roles, do the following:1. Run the `generate_providers_and_account_vars` workflow by using [workflow\_dispatch](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#workflow_dispatch).<br />2. Merge the PR that the workflow creates.<br />After the workflow completes, the RVM is ready to:+ Accept requests for new pipeline roles.<br />+ Create either read-only or read-write roles as requested.<br />+ Deploy roles to the specified AWS accounts. | DevOps engineer |

## Troubleshooting
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| I created a role by using the RVM, but GitHub isn’t able to assume it. | Verify that the name of the GitHub repository matches the name provided to the `github_workflow_roles` module. Roles are scoped so that only one repository can assume them.<br />Similarly, verify that the branch used in the GitHub pipeline matches the name of the branch provided to the `github_workflow_roles` module. Typically, RVM-created roles with write permissions can only be used by workflows scoped to the `main` branch (that is, deployments sourced from `main`). |
| My read-only role is failing to run its pipeline because it lacks permissions to read a specific resource. | Although the `ReadOnlyAccess` policy provides broad read-only permissions, the policy doesn't have some read actions (for example, certain AWS Security Hub CSPM actions).<br />You can add specific action permissions by using the `inline_policy_readonly` parameter of the `github-workflow-roles` module. |

## Related resources
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-resources"></a>
+ [Best practices for using AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-bestpractices.html)
+ [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
+ [Overview of AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html)
+ [Policy best practices](https://docs.aws.amazon.com/codepipeline/latest/userguide/security_iam_service-with-iam-policy-best-practices.html)

## Additional information
<a name="provision-least-privilege-iam-roles-by-deploying-a-role-vending-machine-solution-additional"></a>

**Using GitHub environments**

GitHub environments are an alternative approach to branch-based restrictions for role access. If you prefer to use a GitHub environment, following is an example of the syntax for an additional condition in the IAM trust policy. This syntax specifies that the role can be used only when the GitHub action is running in the `Production` environment.

```
"StringLike": {
    "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:environment:Production"
}
```

The example syntax uses the following placeholder values:
+ `octo-org` is the GitHub organization name.
+ `octo-repo` is the repository name.
+ `Production` is the specific GitHub environment name.

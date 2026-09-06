---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-custom-checkov-scanning.html
---

# Implement centralized custom Checkov scanning to enforce policy before deploying AWS infrastructure
<a name="centralized-custom-checkov-scanning"></a>

*Benjamin Morris, Amazon Web Services*

## Summary
<a name="centralized-custom-checkov-scanning-summary"></a>

This pattern provides a GitHub Actions framework for writing custom Checkov policies in one repository that can be reused across a GitHub organization. By following this pattern, an information security team can write, add, and maintain custom policies based on company requirements. The custom policies can be pulled into all pipelines in the GitHub organization automatically. This approach can be used to enforce company standards for resources before the resources are deployed.

## Prerequisites and limitations
<a name="centralized-custom-checkov-scanning-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A GitHub organization using GitHub Actions
+ AWS infrastructure deployed with either HashiCorp Terraform or AWS CloudFormation

**Limitations **
+ This pattern is written for GitHub Actions. However, it can be adapted to similar continuous integration and continuous delivery (CI/CD) frameworks such as GitLab. No specific paid version of GitHub is required.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) in the AWS documentation, and choose the link for the service.

## Architecture
<a name="centralized-custom-checkov-scanning-architecture"></a>

This pattern is designed to be deployed as a GitHub repository that contains a GitHub reusable workflow and custom Checkov policies. The reusable workflow can scan both Terraform and CloudFormation infrastructure as code (IaC) repositories.

The following diagram shows the **Reusable GitHub workflows repository** and **Custom Checkov policies repository** as separate icons. However, you can implement these repositories either as separate repositories or a single repository. The example code uses a single repository, with files for workflows (`.github/workflows`) and files for custom policies (`custom_policies` folder and the `.checkov.yml` config file) in the same repository.

![GitHub Actions uses reusable GitHub workflow and custom Checkov policies to evaluate IaC.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6c0c941f-14f9-4569-92da-9f81ab3e525c/images/a1539ce5-0ee6-4af1-bd01-cafad0f71708.png)

The diagram shows the following workflow:

1. A user creates a pull request in a GitHub repository.

1. Pipeline workflows start in GitHub Actions, including a reference to a Checkov reusable workflow.

1. The pipeline workflow downloads the referenced Checkov reusable workflow from an external repository and runs that Checkov workflow by using GitHub Actions.

1. The Checkov reusable workflow downloads the custom policies from an external repository.

1. The Checkov reusable workflow evaluates the IaC in the GitHub repository against both built-in and custom Checkov policies. The Checkov reusable workflow passes or fails based on whether security issues are found.

**Automation and scale**

This pattern allows for central management of Checkov configuration, so that policy updates can be applied in one location. However, this pattern does require that each repository use a workflow that contains a reference to the central reusable workflow. You can add this reference manually or use scripts to push the file to the `.github/workflows` folder for each repository.

## Tools
<a name="centralized-custom-checkov-scanning-tools"></a>

**AWS services**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions. Checkov can scan CloudFormation.

**Other tools**
+ [Checkov](https://www.checkov.io/) is a static code analysis tool that checks IaC for security and compliance misconfigurations.
+ [GitHub Actions](https://github.com/features/actions) is integrated into the GitHub platform to help you create, share, and run workflows within your GitHub repositories. You can use GitHub Actions to automate tasks such as building, testing, and deploying your code.
+ [Terraform](https://www.terraform.io/) is an IaC tool from HashiCorp that helps you create and manage cloud and on-premises resources. Checkov can scan Terraform.

**Code repository**

The code for this pattern is available in the GitHub [centralized-custom-checkov-sast](https://github.com/aws-samples/centralized-custom-checkov-sast) repository.

## Best practices
<a name="centralized-custom-checkov-scanning-best-practices"></a>
+ To maintain a consistent security posture, align your company’s security policies with the Checkov policies.
+ In the early phases of implementing Checkov custom policies, you can use the soft-fail option in your Checkov scan to allow IaC with security issues to be merged. As the process matures, switch from the soft-fail option to the hard-fail option.

## Epics
<a name="centralized-custom-checkov-scanning-epics"></a>

### Create a central Checkov repository for custom policies
<a name="create-a-central-checkov-repository-for-custom-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a central Checkov repository. | Create a repository to store custom Checkov policies that will be used within the organization.<br />For a quick start, you can copy the contents of this pattern’s GitHub [centralized-custom-checkov-sast ](https://github.com/aws-samples/centralized-custom-checkov-sast)repository into your central Checkov repository. | DevOps engineer |
| Create a repository for reusable workflows. | If a repository for reusable workflows already exists, or you plan to include reusable workflow files in the same repository as the custom Checkov policies, you can skip this step.<br />Create a GitHub repository to hold reusable workflows. Other repositories’ pipelines will reference this repository. | DevOps engineer |

### Create reusable and example Checkov workflows
<a name="create-reusable-and-example-checkov-workflows"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add a reusable Checkov workflow. | Create a reusable Checkov GitHub Actions workflow (YAML file) in the reusable workflows repository. You can adapt this reusable workflow from the workflow file provided in this pattern.<br />An example of a change that you might want to make is to change the reusable workflow to use the soft-fail option. Setting `soft-fail` to `true` allows the job to complete successfully even if there is a failed Checkov scan. For instructions, see [Hard and soft fail](https://www.checkov.io/2.Basics/Hard%20and%20soft%20fail.html) in the Checkov documentation. | DevOps engineer |
| Add an example workflow. | Add an example Checkov workflow that references the `reusable` workflow. This will provide a template for how to reuse the `reusable` workflow. In the example repository, `checkov-source.yaml` is the reusable workflow and `checkov-scan.yaml` is the example that consumes `checkov-source`.<br />For more details about writing an example Checkov workflow, see [Additional information](#centralized-custom-checkov-scanning-additional). | DevOps engineer |

### Associate company policies to Checkov custom policies
<a name="associate-company-policies-to-checkov-custom-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Determine policies that can be enforced with Checkov. | 1. Review company policies that are related to infrastructure security and which requirements should be in place.<br />2. Determine which requirements can be implemented by using Checkov custom policies.<br />3. Create a naming convention that maps the policy control to the Checkov custom policy. Typically, Checkov custom policies have an identifier with a Checkov name, the policy source (custom), and a policy number (for example, `CKV2_CUSTOM_123`).For more details about creating Checkov custom policies, see [Custom Policies Overview](https://www.checkov.io/3.Custom%20Policies/Custom%20Policies%20Overview.html) in the Checkov documentation. | Security and Compliance |
| Add Checkov custom policies. | Convert the identified company policies to custom Checkov policies in the central repository. You can write simple Checkov policies in either Python or YAML. | Security |

### Implement centralized Checkov custom policies
<a name="implement-centralized-checkov-custom-policies"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the Checkov reusable workflow to all repositories. | At this point, you should have an example Checkov workflow that references the reusable workflow. Copy the sample Checkov workflow that references the reusable workflow to each repository that requires it. | DevOps engineer |
| Create a mechanism to ensure that Checkov runs before merges. | To ensure that the Checkov workflow gets run for every pull request, create a [status check](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks) that requires a successful Checkov workflow before pull requests can be merged. GitHub allows you to require that specific workflows run before pull requests can be merged. | DevOps engineer |
| Create an organization-wide PAT, and share it as a secret. | If your GitHub organization is publicly visible, you can skip this step.<br />This pattern requires that the Checkov workflow be able to download custom policies from the custom policy repository in your GitHub organization. You must provide permissions such that the Checkov workflow can access those repositories.<br />To do this, [create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token) (PAT) with permissions to read organization repositories. Share this PAT with repositories, either as an organization-wide secret (if on a paid plan) or a secret in each repository (free version). In the sample code, the default name for the secret is `ORG_PAT`. | DevOps engineer |
| (Optional) Protect the Checkov workflow files from modification. | To protect the Checkov workflow files from unwanted changes, you can use a `CODEOWNERS` file. The `CODEOWNERS` file is typically deployed in the root of the directory.<br />For example, to require approvals from your GitHub organization’s `secEng` group when the `checkov-scan.yaml` file is modified, append the following to a repository’s `CODEOWNERS` file:<pre>[Checkov]<br />.github/workflows/checkov-scan.yaml @myOrg/secEng</pre><br />A `CODEOWNERS` file is specific to the repository it lives in. To protect the Checkov workflow used by the repository, you must add (or update) a `CODEOWNERS` file in each repository.<br />For more information about protecting Checkov workflow files, see [Additional information](#centralized-custom-checkov-scanning-additional). For more information about `CODEOWNERS` files, see the official documentation for your CI/CD provider (such as [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)). | DevOps engineer |

## Related resources
<a name="centralized-custom-checkov-scanning-resources"></a>
+ [Checkov Custom Policies Overview](https://www.checkov.io/3.Custom%20Policies/Custom%20Policies%20Overview.html)
+ [CloudFormation Configuration Scanning](https://www.checkov.io/7.Scan%20Examples/Cloudformation.html)
+ [GitHub Actions Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

## Additional information
<a name="centralized-custom-checkov-scanning-additional"></a>

**Writing Checkov workflow files**

When writing `checkov-scan.yaml`, consider when you want it to run. The top-level `on` key determines when the workflow runs. In the example repository, the workflow will run when there is a pull request targeting the `main` branch (and any time that pull request’s source branch is modified). The workflow can also be run as required because of the `workflow_dispatch` key.

You can change the workflow trigger conditions based on how often you want the workflow to run. For example, you could change the workflow to run every time code is pushed to any branch by replacing `pull_request` with `push` and removing the `branches` key.

You can modify the example workflow file that you created within an individual repository. For example, you could adjust the target branch’s name from `main` to `production` if a repository is structured around a `production` branch.

**Protecting Checkov workflow files**

Checkov scanning provides useful information about potential security misconfiguration. However, some developers might perceive it to be a barrier to their productivity and attempt to remove or disable the scanning workflow.

There are several ways to address this problem, including better messaging about the long-term value of security scanning and clearer documentation about how to deploy secure infrastructure. These are important "soft" approaches to DevSecOps collaboration that can be seen as the solution to this problem’s root cause. However, you can also use technical controls such as a `CODEOWNERS` file as guardrails to help keep developers on the right path.

**Testing pattern in a sandbox**

To test this pattern in a sandbox environment, follow these steps:

1. Create a new GitHub organization. Create a token with read-only access to all repositories in the organization. Because this token is for a sandbox environment, not a paid environment, you will not be able to store this token in an organization-wide secret.

1. Create a `checkov` repository to hold the Checkov configuration and a `github-workflows` repository to hold the reusable workflow configuration. Populate the repositories with the contents of the example repository.

1. Create an application repository, and copy and paste the `checkov-scan.yaml` workflow to its `.github/workflows` folder. Add a secret to the repository that contains the PAT you created for organization read-only access. The default secret is `ORG_PAT`.

1. Create a pull request that adds some Terraform or CloudFormation code to the application repository. Checkov should scan and return a result.

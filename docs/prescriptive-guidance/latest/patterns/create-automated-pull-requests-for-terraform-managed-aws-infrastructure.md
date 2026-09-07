---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-automated-pull-requests-for-terraform-managed-aws-infrastructure.html
---

# Create automated pull requests for Terraform-managed AWS infrastructure by using GitHub Actions
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure"></a>

*Matt Padgett, Ashish Bhatt, Ashwin Divakaran, Sandip Gangapadhyay, and Prafful Gupta, Amazon Web Services*

## Summary
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-summary"></a>

This pattern presents an automation utility that’s designed to eliminate the manual, repetitive work involved in managing changes across multiple Terraform repositories. Many organizations use Terraform repositories to manage their infrastructure as code (IaC), often with hundreds of separate repositories representing different environments, services, or teams. Managing these repositories at scale presents a significant operational challenge. Routine tasks such as updating a parameter, upgrading module versions, or applying configuration changes often require creating and managing pull requests (PRs) across many repositories multiple times a day.

Even for simple changes, this repetitive and manual process is time-consuming and error prone. Engineers must consistently apply the same change across all targeted repositories and craft meaningful PR titles and descriptions. In addition, they often must interact with external tools like Jira to fetch or include issue tracking references. These tasks, while necessary, are undifferentiated heavy lifting that consume valuable engineering time and reduce overall efficiency. The lack of automation in this workflow creates friction, slows down delivery, and increases the cognitive burden on teams tasked with maintaining large-scale Terraform infrastructures.

**Solution overview**

To address this challenge, this pattern offers a utility that’s entirely configuration-driven, allowing users to define their desired changes in a structured configuration file. This file specifies the target repositories, modules, parameters, and values using a clearly defined schema.

Once configured, the utility performs the following automated steps:

1. **Reads the user-defined configuration** to determine the scope and nature of changes

1. **Creates a new branch** in each target repository with the required updates applied

1. **Generates a PR** for each change, ensuring consistency across all repositories

1. **Sends Slack notifications** (optional) to alert stakeholders with direct links to the created PRs

By automating these repetitive tasks, the utility significantly reduces the time, effort, and risk associated with managing large-scale infrastructure updates. It enables teams to focus on higher-value engineering work while helping to ensure that changes are applied consistently and can be traced across all repositories.

## Prerequisites and limitations
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Python version 3.8 or later.
+ A GitHub personal access token (PAT). For more information, see [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) in the GitHub documentation.
+ The GitHub PAT can access your target repositories so that the utility can perform operations like creating branches and pull requests. For more information, see this pattern’s GitHub [code repository](https://github.com/aws-samples/sample-terraform-pr-automation-utility?tab=readme-ov-file#repository-access-verification).

**Limitations**
+ **Configuration complexity** presents the primary challenge. The automation's effectiveness is constrained by the capabilities of its configuration file. Although the system handles standard changes efficiently, complex infrastructure modifications might require manual intervention and certain edge cases remain beyond the scope of automated handling.
+ **Security and access** presents significant considerations particularly in managing GitHub access tokens and API rate limits. Organizations must carefully balance the need for automation with secure credential storage and management, ensuring proper access controls while maintaining operational efficiency.
+ **Validation constraints** pose another notable limitation because the automated system has limited ability to validate business logic and environment-specific requirements. Complex dependencies and cross-service interactions often necessitate human oversight because automated validation can’t fully capture all contextual nuances and business rules.
+ **Scale and performance** issues emerge when dealing with large-scale infrastructure changes. The system must operate within GitHub API limits while managing numerous repositories simultaneously. Resource-intensive operations across extensive infrastructure can create performance bottlenecks that require careful management.
+ **Integration boundaries** restrict the system's flexibility because it's primarily designed to work with specific tools like GitHub and Slack. Organizations that use different tools might need custom solutions and the workflow customization options of this pattern are limited to supported integration points.

## Architecture
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-architecture"></a>

The following diagram shows the workflow and components for this solution.

![Workflow to create automated pull requests using GitHub Actions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e211359a-03b1-4e69-b152-eb7c09bdb01a/images/6cee0660-5b44-4abe-970c-c0a3c830a9aa.png)

The workflow consists of the following steps:

1. The developer triggers GitHub Actions by specifying the Terraform repository.

1. The automation utility reads the defined configurations.

1. The automation utility also pulls the provided Terraform repository.

1. The automation utility creates a new branch and makes updates to Terraform templates locally.

1. The automation utility pushes the new branch to the repository and creates a new PR.

1. The automation utility uses Slack notifications that include PR links to notify developers and enables Terraform templates for AWS Cloud deployment.

## Tools
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-tools"></a>
+ [GitHub](https://docs.github.com/) is a developer platform that developers can use to create, store, manage, and share their code.
+ [GitHub Actions](https://docs.github.com/en/actions) is a continuous integration and continuous delivery (CI/CD) platform that’s tightly integrated with GitHub repositories. You can use GitHub Actions to automate your build, test, and deployment pipeline.
+ [HashiCorp Terraform](https://www.terraform.io/) is an infrastructure as code (IaC) tool that helps you create and manage cloud and on-premises resources.
+ [Slack](https://slack.com/help/articles/115004071768-What-is-Slack-), a Salesforce offering, is an AI-powered conversational platform that provides chat and video collaboration, automates processes with no code, and supports information sharing.

**Code repository**

The code for this pattern is available in the GitHub [Automated Terraform Infrastructure Update Workflow using GitHub Actions](https://github.com/aws-samples/sample-terraform-pr-automation-utility?tab=readme-ov-file) repository.

## Best practices
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-best-practices"></a>
+ Effective **change management** is crucial for successful implementation. Organizations should adopt a gradual rollout strategy for large-scale changes. Maintain consistent branch naming conventions and PR descriptions and ensure comprehensive documentation of all changes.
+ **Security controls** must be rigorously implemented, focusing on least-privilege access principles and secure credential management. Enable branch protection rules to prevent unauthorized changes. Conduct regular security audits to maintain system integrity.
+ A robust **testing protocol** should include automated `terraform plan` execution in continuous integration and continuous deployment (CI/CD) pipelines. The protocol should also include pre-commit validation checks, and dedicated review environments for critical changes. This multi-layered testing approach helps catch issues early and ensures infrastructure stability.
+ **Monitoring strategy** needs to encompass comprehensive alerting mechanisms, detailed success/failure metrics tracking, and automated retry mechanisms for failed operations. This strategy helps to ensure operational visibility and enables quick response to any issues that arise.
+ **Configuration standards** should emphasize version control for all configurations, maintaining modularity for reusability and scalability. Clear documentation of schema and examples helps teams understand and use the automation system effectively.

## Epics
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-epics"></a>

### Installation and setup
<a name="installation-and-setup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the repository. | To set up the repository, run the following commands:<pre># Clone the automation tool repository<br />git clone https://github.com/aws-samples/sample-terraform-pr-automation-utility<br />cd sample-terraform-pr-automation-utility<br /><br /># Copy example configuration<br />cp config.example.yaml config.yaml<br /></pre> | AWS DevOps |
| Install dependencies. | To install and verify the Python dependencies, run the following commands:<pre># Install Python dependencies<br />pip3 install -r requirements.txt<br /><br /># Verify installation<br />python3 -c "import github; import hcl2; import yaml; import requests; print('All packages installed successfully')"<br /></pre> | AWS DevOps |
| Configure the GitHub token. | To configure the GitHub token and then verify that it works, run the following commands:<pre># Set GitHub token environment variable<br />export GITHUB_TOKEN="your_github_token_here"<br /><br /># Verify token works<br />curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user<br /></pre> | AWS DevOps |

### Set up configuration file for Terraform changes
<a name="set-up-configuration-file-for-terraform-changes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the `config.yaml` file. | To define your target repositories and desired changes, edit the `config.yam`l file as follows:<pre>repositories:<br />  - owner: "your-org"<br />    repo: "your-terraform-repo"<br />    files:<br />      - path: "variables.tf"<br />        changes:<br />          variables:<br />            - app_version:<br />                default:<br />                  update:<br />                    - from: ["1.0.0"]<br />                      to: "1.1.0"<br /><br />settings:<br />  pr_title_template: "Infrastructure Update - {{timestamp}}"<br />  slack:<br />    username: "Terraform Bot"<br />    icon_emoji: ":terraform:"<br />    notify_on_success: true<br />    notify_on_error: true<br />    notify_batch_summary: true<br /></pre> | AWS DevOps |

### Test and validate
<a name="test-and-validate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Do pre-flight testing. | Always test your configuration before running it on production repositories. Use the following commands:<pre># 1. Test configuration syntax<br />python3 -c "from main import get_config_content; get_config_content()"<br /><br /># 2. Run in dry-run mode first<br />DRY_RUN=true python3 main.py<br /><br /># 3. Test with minimal configuration<br /># Use a simple config.yaml with just one repository and one change</pre> | AWS DevOps |
| Verify repository access. | To verify that the GitHub token can access the repository, run the following command:<pre># Test GitHub token access<br />curl -H "Authorization: token $GITHUB_TOKEN" \<br />  https://api.github.com/repos/owner/repo-name<br /><br /># Should return repository information, not 404</pre> | AWS DevOps |

### Run the automation utility
<a name="run-the-automation-utility"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the automation utility by using the GitHub Actions UI. | To run the automation utility using the GitHub Actions UI, do the following:1. Navigate to your repository on GitHub.<br />2. Choose the **Actions** tab.<br />3. Choose the **Terraform Infrastructure Update Automation** workflow.<br />4. Choose **Run workflow**.<br />5. Configure the following workflow inputs:**Source configuration**:Select the target branch for automation.Specify the path to the configuration file (`config.yaml`) that contains the desired changes.**Preview controls**:Choose the **Preview** option to review changes without applying them.**Branch management**:Enter the base branch for creating new feature branches.Enter the branch prefix configuration.Choose the **Automatically close obsolete pull requests** checkbox.**Notifications setup**:Enter your URL for **Slack webhook URL for rich notifications (overrides repository secret)**.Choose the **Test Slack integration before processing (dry run only)** checkbox.Enter your information for an **Override default Slack channel (e. g., \#infrastructure-test)**.**Advanced settings**:Choose the **Enable debug logging for troubleshooting** checkbox. | AWS DevOps |
| (Alternative) Run the automation utility from the command line. | If you prefer, you can run the automation utility from the command line instead of by using the GitHub Actions UI. Use the following command:<pre># Run actual automation<br />python3 main.py</pre> | AWS DevOps |

### Validate PRs and changes
<a name="validate-prs-and-changes"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review the created PRs and changes. | To monitor the results of the GitHub workflow execution, do the following:+ Check the [workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) for processing status.<br />+ Review the PRs that the automation utility created.<br />+ Monitor Slack notifications (if configured). | AWS DevOps |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Clean up PRs. | Close abandoned or unnecessary PRs. | AWS DevOps |

## Related resources
<a name="create-automated-pull-requests-for-terraform-managed-aws-infrastructure-resources"></a>

**AWS Prescriptive Guidance**
+ [Using Terraform as an IaC tool for the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/choose-iac-tool/terraform.html)

**GitHub documentation**
+ [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
+ [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
+ [Understanding GitHub Actions](https://docs.github.com/en/actions/get-started/understand-github-actions)
+ [Quickstart for GitHub Actions](https://docs.github.com/en/actions/get-started/quickstart)

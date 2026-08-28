---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/manage-projects-domain-administration.html
---

# Manage Projects from Domain Administration
<a name="manage-projects-domain-administration"></a>

The Projects section in domain administration provides centralized management of all projects within your Amazon SageMaker Unified Studio domain. Domain administrators can view project details, monitor project status, create new projects, and manage project configurations.

Projects in Amazon SageMaker Unified Studio enable users to collaborate on various business use cases. Within projects, users can manage data assets, perform data analysis, organize workflows, and develop machine learning models.

From the domain administration perspective, you can oversee all projects in the domain and ensure proper configuration.

Prerequisites:
+ Domain administrator permissions for Amazon SageMaker Unified Studio
+ IAM role or user with the `SageMakerStudioAdminIAMDefaultExecutionPolicy` policy attached

Perform the following procedure:

1. From the domain administration page, choose **Projects** in the left navigation pane.

1. The Projects page displays:
   + Domain details section showing account information, region, domain ID, admin roles, and creation date
   + Projects section listing all projects in the domain with details including:
     + Project name
     + Creation date (UTC-08:00)
     + Status (Active, Creating, Deleting)
     + Project URL
     + Actions menu

1. To view project details, choose the project name from the list.

1. To create a new project, choose **Create project** in the upper right corner of the Projects section.

1. Use the search functionality by entering terms in the **Find** search box to locate specific projects.

1. To perform actions on a project, choose the **Actions** menu (three dots) next to the project name for available options.

1. Monitor project status in the Status column to track project lifecycle states.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

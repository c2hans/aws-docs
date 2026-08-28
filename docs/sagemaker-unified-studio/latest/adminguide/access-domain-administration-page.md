---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/access-domain-administration-page.html
---

# Access the Domain Administration Page
<a name="access-domain-administration-page"></a>

The domain administration page in Amazon SageMaker Unified Studio provides administrators with centralized management capabilities for domains, projects, and settings. Domain administrators can create and manage projects, configure domain-level settings including networking, and oversee the overall domain configuration.

Access to the domain administration page is restricted to the IAM role, specified as the domain login role, used to create the domain. This IAM role is the project member in the default admin project created for the domain.

1. Log in to your Amazon SageMaker Unified Studio IAM-based domain.

1. From the Amazon SageMaker Unified Studio left navigation, choose **Domain management**.

1. Alternatively, from the Amazon SageMaker Unified Studio header, locate the project dropdown menu and choose **Manage projects**.

From the domain administration page, you can access:
+ Projects - Manage existing projects and create new projects
+ Users - Manage user access and permissions
+ Settings - Configure network settings

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/best-practices.html
---

# Best practices for using the Infrastructure Documentation Generator
<a name="best-practices"></a>

This section outlines best practices and key considerations for using the Infrastructure Documentation Generator responsibly and effectively. By following these practices, you can support secure handling of AWS credentials, generate accurate and meaningful infrastructure insights, and collaborate more effectively with your team. This approach helps you leverage the system for security, cost, and performance optimization. At the same time, you can respect organizational policies, protect sensitive data, and maximize the value of the generated documentation and visualizations.

## Using credentials securely
<a name="using-credentials-securely.682bd4c9-d835-57a8-8983-c914aef7d862"></a>

Always provide temporary credentials or assume roles instead of by using long-lived AWS access keys. This minimizes security risks while scanning your environments. Use AWS Identity and Access Management (IAM) users and roles with read-only permissions only, so the tool never modifies resources. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Interpreting reports
<a name="interpreting-reports.03bc89d4-20bd-59f7-b1b1-a08db77b1266"></a>

You can choose from the following types of analysis reports:
+ **Comprehensive** for a full overview
+ **Security** to identify risky configurations
+ **Cost** for optimization opportunities
+ **Performance** to check resource efficiency

You can also add custom prompts for focused checks, for example, "Focus on compute resources and their security posture".

## Managing large environments
<a name="managing-large-environments.1e7ee15f-5a6d-5979-8527-830aaa328ba8"></a>

For big accounts with thousands of resources, the system may chunk data before analysis. Users should expect slightly longer processing times. In such cases, pay special attention to the "Analysis Limitations" section of the report if some chunks were skipped or failed.

## Exploring dependencies
<a name="exploring-dependencies.85ce81ed-4ace-54fc-a455-b862f74ed270"></a>

Use the graph visualization in the UI to explore resource relationships. Filters, search, and zoom capabilities help navigate complex environments. Look for clusters of dependencies that can indicate tightly coupled services or potential single points of failure.

## Maintaining cache awareness
<a name="maintaining-cache-awareness.6d8504d5-ad92-59d7-849b-c3f30b78958f"></a>

The system caches recent analyses to speed up repeated queries. If your infrastructure changes, always trigger a fresh scan instead of relying solely on cached results. This practice helps to ensure that your report reflects the latest state.

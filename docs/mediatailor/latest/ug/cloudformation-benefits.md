---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/cloudformation-benefits.html
---

# Why use CloudFormation for MediaTailor and CDN integration
<a name="cloudformation-benefits"></a>

AWS Elemental MediaTailor automation with AWS CloudFormation provides significant advantages for broadcast professionals managing streaming workflows. Manually configuring MediaTailor with a content delivery network (CDN) can be time-consuming and error-prone. Using CloudFormation automation offers the following advantages.
+ **Consistency**: Ensures the same configuration is deployed every time, reducing human error.
+ **Version control**: Store your infrastructure as code in a version control system for tracking changes.
+ **Rapid deployment**: Deploy complex configurations in minutes instead of hours of manual configuration.
+ **Environment replication**: Easily replicate configurations across development, testing, and production environments.
+ **Documentation**: The template itself serves as documentation of your infrastructure.

Here's how the automated workflow compares to manual configuration:

| Manual setup (multiple steps) | Automated setup (single template) |
| --- | --- |
| Create MediaTailor playback configuration | Deploy one CloudFormation template with parameters |
| Create CloudFront distribution |
| Configure cache behaviors |
| Set up security configurations |

The automated workflow for setting up MediaTailor with CloudFront follows these steps:

1. Deploy the CloudFormation template with your content origin and ad server parameters

1. CloudFormation creates and configures all necessary resources:
   + MediaTailor playback configuration for ad insertion
   + CloudFront distribution with appropriate cache behaviors
   + Security configurations for content protection

1. Use the CloudFormation outputs to access your ad-enabled stream URLs

1. Stream your content with dynamically inserted ads

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

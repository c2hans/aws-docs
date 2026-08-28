---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/jamf-pro-setup.html
---

# Jamf Pro integration configuration
<a name="jamf-pro-setup"></a>

Jamf Pro is the flagship enterprise Mobile Device Management (MDM) and Enterprise Mobility Management (EMM) platform providing centralized lifecycle management for Apple devices across macOS, iOS, iPadOS, and tvOS. It provides structured per-device inventory records including hardware specifications, OS versions, security posture (FileVault, SIP, Gatekeeper), installed software, and user assignments. With CloudWatch Pipelines, you can use the Jamf Pro REST API to retrieve computer inventory data from your Jamf Pro tenant. The API exposes paginated REST endpoints with OAuth2 authentication that allow fetching device inventory records for monitoring and analysis.

**Topics**
+ [Source configuration for Jamf Pro](jamf-pro-source-config.md)
+ [CloudWatch pipelines configuration for Jamf Pro](jamf-pro-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

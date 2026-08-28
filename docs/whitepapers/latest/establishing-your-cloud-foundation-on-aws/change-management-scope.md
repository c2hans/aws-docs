---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/change-management-scope.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Change management scope
<a name="change-management-scope"></a>

Change management is the practice of monitoring resource configurations to establish and manage a baseline. A baseline is a snapshot at a given point in time of a set of configurations. This snapshot enables you to identify different configuration states of a given configuration item (a snapshot of a particular configuration at a point in time). The purpose of your change management should be to control the changes made to the baseline in a safe and controlled method. The scope of your environment baseline needs to be defined so it doesn’t conflict with any DevSecOps practices that deliver their own change management through a release management process. Any configurations that are not managed by a DevSecOps release management process should be tracked as a change management process. You will also need to determine which services and configurations necessitate change control which are outside of the management of templates or CI/CD operations. Common configurations item for change control can be:

1. Enterprise-wide configurations completed one time via manual effort

1. Temporary suspension of enterprise-wide policies

1. User access or membership changes to groups

1. Centralized changes that impact multiple groups

**Note**
DevSecOps is the preferred method to implement change and should follow the general principals of change control. Change management as defined in this capability is inclusive of DevSecOps changes in regard to progressing change fulfillment to an automated process leveraging infrastructure as code.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

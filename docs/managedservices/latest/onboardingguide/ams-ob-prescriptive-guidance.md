---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ams-ob-prescriptive-guidance.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# AMS post-account prescriptive guidance
<a name="ams-ob-prescriptive-guidance"></a>

As organizations adopt distributed operations and DevOps practices, there are a core set of operational capabilities that should be applied to every account prior to deployment of workloads to meet the pillars of Well Architected.

This link downloads a ZIP file containing a Word document, and a ZIP file with scripts and examples. Automated Account Setup is a set of scripts to automate, or bootstrap, the setup of a new application account.

Once a new account is vended, and before any workloads are deployed, in order to make the account ready from an operational, security and management point of view, you setup default backup plans, patch windows, and encryption (and more). To help improve the agility, consistency, and responsiveness for application account setup, the following sample "How To" is provided for your reference.

[Automated Account Setup](samples/automate-account-setup-Bash-Script.zip).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

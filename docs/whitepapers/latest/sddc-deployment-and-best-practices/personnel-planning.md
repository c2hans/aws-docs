---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/personnel-planning.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Personnel planning
<a name="personnel-planning"></a>

 A critical first step in the planning process is to identify personnel that will be involved in the initial account onboarding process, and technical personnel involved in the deployment of the SDDC. The following is a list of common “roles” required to activate the service and deploy an SDDC.

**Note**
 Depending on the organizational structure, a single person may encompass more than one role.
+  **AWS administrator** — Required to ensure that at least one user is created with the permissions necessary to link the VMware Cloud on the AWS service with a new or existing AWS account.
+  **Cloud administrator** — Performs all planning for the deployment of the SDDC. Performs the deployment of the SDDC. Performs the initial account link to the AWS account.
+  **Network administrator** — Allocates IP ranges needed for the deployment of the SDDC and AWS environment. The network administrator will work with the cloud administrator to ensure that the correct network classless inter-domain routing (CIDR) ranges are set during deployment. The network administrator plans and implements connectivity from the on-premises environment to the SDDC.
+  **Security administrator** — Reviews and approves security policy for the SDDC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

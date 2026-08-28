---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cicd-and-orchestration.html
---

# CI/CD and orchestration
<a name="cicd-and-orchestration"></a>

Continuous Integration and Continuous Delivery are part of an overall automation philosophy that comes with the cloud-native architecture and how it applies to 5G. Orchestration is another aspect of this philosophy that is expected to be dynamic and reactive to any changes that happen on the network. Orchestration and CI/CD are expected to be tightly coupled to guarantee a healthy service and minimize service disruption. The integration between CI/CD and orchestration is expected to be on two fronts:
+  Applying patches and upgrades into the system need to be managed and orchestrated in a way that minimizes disruption to any live services. For example, orchestration can dynamically determine the best time an update should be rolled out.
+  CI/CD-aware orchestration allows traffic to be shifted during deployment of upgrades based on the deployment model strategy adopted (canary, linear, or all-at-once).

Typically, orchestration solutions run on top of CI/CD pipelines to allow orchestration to introduce governance phases into those pipelines and to have exposure into ongoing upgrade cycles.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp03.html
---

# MIDASEC09-BP03 Automate patch management for ICS and connected data infrastructure
<a name="midasec09-bp03"></a>

 Patch known vulnerabilities in a timely manner across industrial control systems (ICS), gateways, and cloud services by automating patch management processes.

 **Desired outcome:** Patches are deployed consistently and timely, minimizing exposure to known exploits.

 **Benefits of establishing this best practice:** Reduces manual overhead, enhances system stability, and supports compliance with vulnerability remediation SLAs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-32"></a>

 Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely with OT vendors for ICS-specific patch cycles.

### Implementation steps
<a name="implementation-steps-33"></a>
+  Inventory all patchable assets across OT and IT systems.
+  Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed nodes.
+  Align maintenance windows with production downtime cycles.
+  Monitor patch compliance using AWS Config and AWS Systems Manager reports.

## Resources
<a name="resources-33"></a>
+  [AWS Systems Manager Patch Manager ](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
+  [ Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

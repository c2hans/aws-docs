---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp02.html
---

# MIDASEC06-BP02 Establish clear data ownership and sharing agreements
<a name="midasec06-bp02"></a>

 Define clear ownership responsibilities and data sharing rules to guide access and usage across internal teams and partner organizations.

 **Desired outcome:** Data is shared responsibly, with clarity around who controls, accesses, and governs its lifecycle.

 **Benefits of establishing this best practice:** Improves accountability, supports regulatory compliance, and fosters trusted partnerships in the industrial environment.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-25"></a>

 Document data ownership roles and access conditions as part of your data governance framework and reinforce with access controls.

### Implementation steps
<a name="implementation-steps-26"></a>
+  Identify and document data owners across all domains.
+  Define acceptable use policies and access controls for each dataset.
+  Use AWS Lake Formation and IAM policies to enforce agreements.
+  Review agreements regularly to align with evolving compliance needs.

## Resources
<a name="resources-26"></a>
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
+  [ Policies and permissions in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

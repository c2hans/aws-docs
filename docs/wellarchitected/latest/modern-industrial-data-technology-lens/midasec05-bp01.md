---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp01.html
---

# MIDASEC05-BP01 Define access permissions
<a name="midasec05-bp01"></a>

 Establish clear and granular access permissions to control who can access industrial data, based on job roles and operational responsibilities.

 **Desired outcome:** Only authorized personnel can access specific data resources, reducing the risk of data leakage or misuse.

 **Benefits of establishing this best practice:** Supports principle of least privilege, improves accountability, and reduces insider threats.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-21"></a>

 Use IAM policies and resource tagging strategies to enforce fine-grained permissions aligned to user roles.

### Implementation steps
<a name="implementation-steps-22"></a>
+  Inventory data assets and define roles for access control.
+  Apply IAM roles and permissions based on job functions.
+  Use resource tags to apply conditional access policies.
+  Review and refine permissions regularly using AWS IAM Access Analyzer.

## Resources
<a name="resources-22"></a>
+  [ Policies and permissions in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
+  [ Using IAM Access Analyzer ](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/deployment-validation.html
---

# Deployment Validation
<a name="deployment-validation"></a>

## Verify Stack Status in Console
<a name="verify-stack-status-in-console"></a>

To verify successful deployment:

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/)

1. Select your stack (SpatialDataManagement or the name you choose during deployment steps)

1. Verify the stack status shows **CREATE\_COMPLETE**

1. Review the **Outputs** tab to confirm the PortalURL output is present and copy its value for later use

This console verification is sufficient to confirm deployment success. The following CLI-based validation steps are optional but useful if you want to verify the deployment through multiple layers and ensure everything is configured appropriately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Spatial Data Management on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

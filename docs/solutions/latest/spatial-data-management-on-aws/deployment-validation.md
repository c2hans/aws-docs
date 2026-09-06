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

---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/update-the-solution.html
---

# Update the solution
<a name="update-the-solution"></a>

**Important**
When updating the solution, automated remediation rules may need to be re-enabled manually in the Admin account. Refer to [Enable fully-automated remediations](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/enable-fully-automated-remediations.html).
If you are using the `Reuse Orchestrator Log Group` parameter to retain logs, ensure it is set appropriately during stack update to avoid log group recreation or loss of log retention settings. Refer to [Deploy the solution](https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/deployment.html). If you are performing a stack update to v2.3.0\+ from an earlier version choose "no"

## Upgrading from versions prior to v1.4
<a name="v1.3.0-or-v1.3.1-to-v1.3.2"></a>

If you have previously deployed the solution prior to v1.4.x, uninstall, then install the latest version:

1. Uninstall the previously deployed solution. Refer to [Uninstall the solution](uninstall-the-solution.md).

1. Launch the latest template. Refer to [Deploy the solution](deploy-the-solution.md).
**Note**
If you are upgrading from v1.2.1 or earlier to v1.3.0 or later, set **Use existing Orchestrator Log Group** to `No`. If you are reinstalling v1.3.0 or later, you can select `Yes` for this option. This option allows you to continue to log to the same Log Group for the Orchestrator Step Functions.

## Upgrading from v1.4 and later
<a name="earlier-versions-to-v1.3.2"></a>

If you are upgrading from v1.4.x, update all stacks or StackSets as follows:

1. Update the stack in the Security Hub admin account using the [latest template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template).

1. In each member account, update the permissions from the latest template.

1. In each member account in all Regions where currently deployed, update the member stack from the latest template.

1. If the Web UI is enabled and you updated parameters such as `TicketGenFunctionName`, invalidate the CloudFront cache to reflect changes immediately:

   ```
   aws cloudfront create-invalidation \
     --distribution-id <distribution-id> \
     --paths "/aws-exports.json"
   ```

## Upgrading from v2.0.x
<a name="upgrading-from-v2.0.x"></a>

If you are upgrading from v2.0.x, upgrade to v2.1.2 or later. Updating to v2.1.0 - v2.1.1 will fail in CloudFormation.

## Upgrading from v2.1.4 or earlier
<a name="upgrading-from-v2.1.4"></a>

If you are upgrading from v2.1.4 or earlier, **you must upgrade to v2.3.0 before upgrading to any version higher than v2.3.0.** Otherwise, the stack update operation will fail. Alternatively, you can delete and re-deploy the solution’s stacks rather than performing a stack update.

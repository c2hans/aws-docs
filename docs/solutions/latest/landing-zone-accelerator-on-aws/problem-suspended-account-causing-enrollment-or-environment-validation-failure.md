---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-suspended-account-causing-enrollment-or-environment-validation-failure.html
---

# Problem: Suspended account causing enrollment or environment validation failure
<a name="problem-suspended-account-causing-enrollment-or-environment-validation-failure"></a>

After you suspend accounts from your AWS Organization, the solution environment validation feature still attempts to enroll and validate these suspended accounts in the **Prepare** stage unless you contain them within an ignored OU. You will receive a [Core pipeline error](problem-core-pipeline-failure.md) until you complete the following resolution steps.

## Resolution
<a name="resolution-4"></a>

Follow the steps in [Closing an account](performing-administrator-tasks.md#closing-an-account). The solution then ignores the suspended account.

### For AWS Control Tower-based environments
<a name="for-aws-control-tower-based-environments"></a>

If you run the Core pipeline before ignoring the account, the account might have a tainted Account Factory product associated with it. Use the following procedure to remove that resource:

1. Follow the steps in [Closing an account](performing-administrator-tasks.md#closing-an-account).

1. Sign in to the [Service Catalog console](https://us-east-1.console.aws.amazon.com/servicecatalog) from your Management account.

1. Select **Provisioned products** from the navigation menu.

1. Choose **Account** in the **Access Filter** drop-down menu.

1. Select the Control Tower Account Factory product that failed provisioning. From the drop-down menu, select **Terminate**.

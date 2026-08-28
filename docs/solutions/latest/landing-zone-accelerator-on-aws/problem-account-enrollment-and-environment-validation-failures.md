---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-account-enrollment-and-environment-validation-failures.html
---

# Problem: Account enrollment and environment validation failures
<a name="problem-account-enrollment-and-environment-validation-failures"></a>

When you enroll new or existing accounts in the solution, you can encounter [Core pipeline errors](problem-core-pipeline-failure.md) during the **Prepare** stage of the pipeline. Failures during this stage typically indicate an issue with enrolling the account into AWS Organizations or AWS Control Tower.

The following are potential errors you might see in **Prepare** stage build logs when enrolling accounts:

## General account enrollment failure
<a name="general-account-enrollment-failure"></a>

You might receive the following [Core pipeline error](problem-core-pipeline-failure.md) message when experiencing a general account enrollment failure:

 ` AWSAccelerator-PrepareStack | UPDATE_FAILED | Custom::CreateControlTowerAccounts | CreateCTAccounts/Resource/Default (CreateCTAccounts) Received response status [FAILED] from custom resource. Message returned: Account creation failed. Error: Accounts failed to enroll in Control Tower. Check Service Catalog Console`

### Resolution
<a name="resolution-2"></a>

Complete the following steps when this error occurs:

1. Ensure that the prerequisites listed in [Adding an existing account](performing-administrator-tasks.md#adding-an-existing-account) are complete.

1. Sign in to the [Service Catalog](https://us-east-1.console.aws.amazon.com/servicecatalog) console from your Management account.

1. Select **Provisioned products** from the left-hand navigation pane.

1. Choose **Account** in the **Access Filter** drop-down menu.

1. The screen lists the reason provisioning failed. Select the Control Tower Account Factory product that failed provisioning. From the drop-down menu, select **Terminate**.

1. Sign in to the [AWS CloudFormation](https://us-east-1.console.aws.amazon.com/cloudformation) console.

1. Select the **Prepare** stack, which will be in the `ROLLBACK_FAILED` or `UPDATE_ROLLBACK_FAILED` state after the account enrollment failure.

1. Select **Continue update rollback** from the **Stack actions** dropdown menu. Choose **Advanced troubleshooting**. Select the resource with prefix `CreateCTAccounts*`, then choose **Continue update rollback**.

1. Await rollback completion.

1.  [Retry](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-retry.html) the **Prepare** stage of **AWSAccelerator-Pipeline**.

## Environment validation error
<a name="environment-validation-error"></a>

You might receive a [Core pipeline error](problem-core-pipeline-failure.md) message when experiencing an environment validation error. For example:

 ` AWSAccelerator-PrepareStack | UPDATE_FAILED | Custom::ValidateEnvironmentConfig | ValidateEnvironmentConfig/Resource/Default (ValidateEnvironmentConfig) Received response status [FAILED] from custom resource. Message returned: Error: AWS Control Tower has detected that the managed account <account_ID> has been removed from organization <organization_ID>. `

**Note**
This error message might differ depending on the type of drift detected.

If you have made any changes to your account(s), OU(s), or managed SCPs outside of the AWS Control Tower console, the solution’s drift detection functionality likely caught these changes and caused this error. You can’t run the pipeline until you undo these changes or enroll the changed account(s) or OU(s) in AWS Control Tower.

### Resolution
<a name="resolution-3"></a>

Complete the following steps when this error occurs:

1. Ensure that all account(s), OU(s), and AWS Control Tower-managed SCPs are properly enrolled in Control Tower. For more information, see [Detect and resolve drift in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) in the *AWS Control Tower User Guide*.

1. Sign in to the [Systems Manager Parameter Store console](https://us-east-1.console.aws.amazon.com/systems-manager/parameters) from your Management account.

1. Search for the parameter named `/accelerator/controlTower/driftDetected`.

1. If the value of this parameter is true, select **Edit** and change the parameter value to false.

1. Sign in to the [AWS CloudFormation console](https://us-east-1.console.aws.amazon.com/cloudformation).

1. Select the **Prepare** stack, which will be in the `ROLLBACK_FAILED` or `UPDATE_ROLLBACK_FAILED` state after the environment validation failure.

1. Select the **Stack actions** dropdown menu, then choose **Continue update rollback**. Select **Advanced troubleshooting**. Select the resource with prefix `ValidateEnvironmentConfig*`, then choose **Continue update rollback**.

1. Await rollback completion.

1.  [Retry](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-retry.html) the **Prepare** stage of **AWSAccelerator-Pipeline**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/account-creation-and-drift-detection.html
---

# Account creation and enrollment
<a name="account-creation-and-drift-detection"></a>

The following diagram shows how the solution creates new accounts, optionally quarantines them, and enrolls them with AWS Control Tower.

 **The account creation and enrollment workflow, showing how EventBridge rules, Lambda functions, DynamoDB tables, and Step Functions state machines interact.**

![image4](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image4.png)

1. The **Prepare** stage of the `AWSAccelerator-Pipeline` invokes the account creation workflow when you add a new account to the `accounts-config.yaml` file. The solution validates the environment against the configuration. It records each account to create in an [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table, and then starts account creation. The workflow is the same for AWS Control Tower–based landing zones and AWS Organizations–based landing zones.

1. The solution creates each new account through the AWS Organizations [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html) API (or [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) for AWS GovCloud (US) accounts). An [AWS Step Functions](https://aws.amazon.com/step-functions/) state machine periodically checks the status of each account creation request. It stores the result in DynamoDB tables that hold the state of your multi-account environment.

1. If you enable the `quarantineNewAccounts` option in `organization-config.yaml`, the solution deploys an [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rule. The rule monitors for AWS Organizations CreateAccount events (and CreateGovCloudAccount events, if you configured AWS GovCloud (US) accounts). The rule invokes an [AWS Lambda](https://aws.amazon.com/lambda/) function named `AttachQuarantineScp`. The function waits for account creation to finish, and then attaches the service control policy (SCP) that you specified to the new account. The **Finalize** stage removes the quarantine SCP after the solution finishes configuring the account.

1. For AWS Control Tower–based landing zones, the **Accounts** stage of the pipeline enrolls the new accounts with AWS Control Tower. The solution calls the AWS Control Tower [ListEnabledBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html) API to find registered OUs whose baseline reports inheritance drift. This drift indicates that the OU contains accounts that aren’t yet enrolled. The solution then calls [ResetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ResetEnabledBaseline.html) on each of those OUs and waits for the operation to complete, which enrolls the new accounts. The solution no longer uses the Account Factory Service Catalog portfolio to create or enroll accounts.

1. For AWS Organizations–based landing zones, no enrollment step is required. You specify the type of landing zone in the `global-config.yaml` file.

**Note**
Account creation is an asynchronous process. The state machine periodically checks the status of the Organizations account creation request, and pauses the pipeline stage until account creation succeeds or fails.

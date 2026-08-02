---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/account-creation-and-drift-detection.html
---

# Account creation and drift detection
<a name="account-creation-and-drift-detection"></a>

 **AWS account creation and management workflow with EventBridge, Lambda, DynamoDB, and other services.**

![image4](http://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/images/image4.png)

1. The solution deploys [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules that monitor for AWS Control Tower lifecycle events. These rules invoke AWS Lambda functions that perform different actions based on the lifecycle event. The solution uses the `AttachQuarantineScp` function to attach an AWS Organizations SCP to newly-enrolled accounts, if configured. The solution uses the `ControlTowerOuEvents` function to detect changes made to OUs in the multi-account environment.

1. The Lambda functions have access to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables that contain stateful information about the multi-account environment. The functions use this data to validate changes made to the environment against a known good state.

1. The account creation workflow is invoked by the **Prepare** stage of the `AWSAccelerator-Pipeline` when a new account is added to the `accounts-config.yaml` file. Two [AWS Step Functions](https://aws.amazon.com/step-functions/) state machines handle this workflow: one for AWS Control Tower-based landing zones and the other for AWS Organizations-based landing zones.

1. The state machines have access to DynamoDB tables that contain stateful information about the multi-account environment. This allows the underlying Lambda functions to validate the environment and store the environment’s state in the DynamoDB tables.

1. The state machines initiate the account creation process if a new account is added to the solution configuration. The account creation workflow is dependent on the type of landing zone that the solution has been deployed to. For AWS Control Tower-based landing zones, the solution leverages the [Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) Service Catalog portfolio to provision a new account. For AWS Organizations-based landing zones, the Organizations API invokes account creation. We provide configuration toggles to differentiate the type of landing zone in the `global-config.yaml` file.

**Note**
Account creation is an asynchronous process, so the state machine workflow is used to periodically check the status of the Account Factory or Organizations-based account creation. As such, the state machine pauses the pipeline stage progression until the account creation succeeds or fails.

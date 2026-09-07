---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-cleaner-component.html
---

# Account Cleaner components
<a name="account-cleaner-component"></a>

![Diagram showing the Account Cleaner components including the durable Lambda function and CodeBuild project](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/account-cleaner.drawio.png)

**ISB Account Cleaner components**
The **Account Cleaner** recycles sandbox accounts either during onboarding or after a lease ends. It orchestrates the following sequence using an AWS Lambda durable function:

1.  **Lock acquisition**: The function acquires an exclusive DynamoDB lock on the account, preventing concurrent cleanup executions on the same account. If another cleanup is already in progress, the request exits gracefully.

1.  **Initialization**: The function validates the account, fetches the global cleanup configuration, and verifies that the cleanup spoke role exists in the sandbox account.

1.  **Access revocation**: The function waits for any in-progress lease assignment revocation to complete, then performs an authoritative sweep to remove all remaining IAM Identity Center account assignments from the sandbox account.

1.  **Pre-cleanup resource enumeration**: The function queries [AWS Resource Explorer](https://aws.amazon.com/resource-explorer/) across all ISB-managed regions to capture a baseline count of resource types in the account before cleanup begins.

1.  **Cleanup loop**: An [AWS CodeBuild](https://aws.amazon.com/codebuild/) project assumes into the sandbox account and runs [AWS Nuke](https://github.com/ekristen/aws-nuke) to delete all supported resources (the solution configures AWS Nuke to ignore protected solution assets). The function monitors build completion through an EventBridge callback relay. By default, the solution performs two successful passes of the cleanup loop. Administrators can configure this value in the **Cleanup** section of the **Settings** page in the web UI. For more information, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

1.  **Post-cleanup resource enumeration**: The function queries Resource Explorer again after Nuke completes to capture the post-cleanup resource baseline.

1.  **Account cooldown** (optional): If a cooldown period is configured, the account waits in the CleanUp OU before proceeding to validation. The cooldown doubles as the Resource Explorer staleness buffer, giving deleted resources time to age out of the index. Administrators can skip the remaining cooldown from the account details page. For more information, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

1.  **Post-cleanup validation**: After cooldown (or immediately after the post-cleanup enumeration if cooldown is disabled), the function enumerates resources one final time and checks whether any non-excluded resources remain. If the remaining count is zero, validation passes. For more information, see [Post-cleanup resource validation](#post-cleanup-validation).

1.  **Tag removal**: The function removes the four lease-level cost allocation tags from the account. The `ISB-<namespace>:Status` tag is updated to `Available` during finalization.

1.  **Finalization**: The function releases the lock, updates the account status, and publishes a cleanup success event to the event bus, which moves the account to the **Available** OU.

Throughout each step, the function writes progress to a cleanup summary report in DynamoDB. You can view live cleanup progress and historical reports from the account details page in the web UI. For more information, see [Viewing cleanup details](administrator-guide.md#viewing-cleanup-details).

**Note**
If the cleanup fails at any step, the function releases the lock and publishes a failure event to the event bus, which moves the account to the **Quarantine** OU. If post-cleanup validation detects remaining resources: in `Silent` mode (the default) the account proceeds normally; in `Warn` mode the account proceeds with a warning logged; in `Quarantine` mode the account is quarantined for manual review.

## Post-cleanup resource validation
<a name="post-cleanup-validation"></a>

After AWS Nuke completes, the solution independently verifies that the sandbox account is clean using AWS Resource Explorer. This provides a defense-in-depth safety check against silent Nuke failures (for example, resources protected by SCPs that Nuke silently skips).

The validation step:

1. Queries Resource Explorer across all ISB-managed regions to enumerate remaining resources.

1. Applies the validator exclusion configuration to filter out expected protected resources.

1. Checks whether any non-excluded resources remain (remaining count must be zero to pass).

1. If unexpected resources remain: in `Silent` mode (the default) the account proceeds without action; in `Warn` mode a warning is logged and remaining resources are surfaced in the UI; in `Quarantine` mode the account is quarantined for manual review.

The validator exclusion configuration is stored in AWS AppConfig alongside the AWS Nuke configuration. It defines ARN patterns that are expected to survive cleanup (ISB infrastructure, AWS Control Tower assets, service-linked roles). When you add filters to the AWS Nuke configuration, add corresponding entries to the validator exclusion configuration so that protected resources are not flagged as validation failures. For more information, see [Resolving Account Cleanup Failures](administrator-guide.md#resolving-account-cleanup-failures).

**Note**
AWS Resource Explorer does not index all AWS resource types. Validation provides additional confidence but cannot guarantee complete cleanup. AWS Nuke remains the primary cleanup mechanism.

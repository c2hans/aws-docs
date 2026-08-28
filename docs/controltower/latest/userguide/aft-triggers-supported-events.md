---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-triggers-supported-events.html
---

# Supported event paths
<a name="aft-triggers-supported-events"></a>

The `account_move` trigger fires when AFT receives an `UpdateManagedAccount` AWS Control Tower lifecycle event. This event is emitted when:
+ An account's OU is changed through the AFT account request file (Terraform `ManagedOrganizationalUnit` parameter update).
+ An account is updated through the AWS Control Tower console.
+ An account is moved using the Register OU or Account Factory operations (console or Service Catalog API).

**Important**
Accounts updated through the Auto Enroll feature in AWS Control Tower landing zone do not emit the `UpdateManagedAccount` lifecycle event. The customization trigger does not fire for those operations.

For more information about AWS Control Tower lifecycle events, see [Lifecycle events](https://docs.aws.amazon.com/controltower/latest/userguide/lifecycle-events.html) in the *AWS Control Tower User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

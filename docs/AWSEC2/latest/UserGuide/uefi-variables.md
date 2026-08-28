---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-variables.html
---

# UEFI variables for Amazon EC2 instances
<a name="uefi-variables"></a>

When you launch an instance where the boot mode is set to UEFI, a key-value store for variables is created. The store can be used by UEFI and the instance operating system for storing UEFI variables.

UEFI variables are used by the boot loader and the operating system to configure early system startup. They allow the operating system to manage certain settings of the boot process, like the boot order, or managing the keys for UEFI Secure Boot.

**Warning**
Anyone who can connect to the instance (and potentially any software running on the instance), or anyone with permissions to use the [ GetInstanceUefiData](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceUefiData.html) API on the instance can read the variables. You should never store sensitive data, such as passwords or personally identifiable information, in the UEFI variable store.

**UEFI variable persistence**
+ For instances that were launched on or before May 10, 2022, UEFI variables are wiped on reboot or stop.
+ For instances that are launched on or after May 11, 2022, UEFI variables that are marked as non-volatile are persisted on reboot and stop/start.
+ Bare metal instances don't preserve UEFI non-volatile variables across instance stop/start operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

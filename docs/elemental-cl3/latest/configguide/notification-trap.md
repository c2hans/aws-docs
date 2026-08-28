---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-trap.html
---

# SNMP traps
<a name="notification-trap"></a>

AWS Elemental Conductor Live generates SNMP traps for activity on the cluster. You can set up to receive SNMP traps from Conductor Live. (If you prefer to poll the SNMP interface for messages, see [SNMP polling](notification-polling.md).)

Conductor Live generates SNMP traps for the following events.
+ Type of notification: `ELEMENTAL-MIB::alert`
+ Type of event: Any alert that worker nodes in the cluster generate.
+ Contents of the notification:
  + `ELEMENTAL-MIB::alertSet`. The value is `1` if the alert is being set, `0` if the alert is being cleared.
  + `ELEMENTAL-MIB::alertMessage`. Describes the alert that was set or cleared.

**To set up SNMP traps**

1. On the Conductor Live web interface, go to the **Settings** page and choose **SNMP**.

1. On the **SNMP** page, complete the fields. Use the instructions in the following table as a guide. Choose **Save**:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/configguide/notification-trap.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

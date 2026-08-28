---
source_url: https://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/elpg-run-states.html
---

# 2 Run states
<a name="elpg-run-states"></a>

An ExpressLink module operates as a state machine that moves through a number of internal states (see [figure 2](#elpg-figure2) for a partial representation).

<a name="elpg-figure2"></a>![Figure 2 - ExpressLink internal states diagram (partial)](http://docs.aws.amazon.com/iot-expresslink/archive/v1.0/programmersguide/images/internal-states.png)

The application or host processor is presented with a small command set that is independent from the connectivity solution offered by the specific module (such as ethernet, cellular, and Wi-Fi).

The command interface is designed to be stateless, with all interactions initiated exclusively from the host side. When an asynchronous event occurs (a message is received or an internal error condition occurs), the ExpressLink module queues the event and flags its availability to the host. A host can choose to ignore most event notifications and only periodically poll the receive queue if desired. (See [7.2 Event handling commands](elpg-event-handling.md#elpg-event-handling-commands).)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

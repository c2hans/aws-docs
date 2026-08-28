---
source_url: https://docs.aws.amazon.com/dcv/latest/adminguide/dcv-server-processes.html
---

# Amazon DCV server processes
<a name="dcv-server-processes"></a>

This counter set contains information about the individual Amazon DCV processes.

`agent_type can be one of: session_agent, system_agent, user_agent`

Counters are updated once per second.

| Counter name | Description | Unit | Notes |
| --- | --- | --- | --- |
| % Processor Time | Percentage of processor time used by the process | Percent | Percentage is relative to one CPU core (i.e. 100% means the process is hogging one thread).<br />Same as \\Process(NAME)\\% Processor Time |
| Physical Memory Bytes | Current amount of physical memory used by the process, in bytes | Bytes | Same as \\Process(NAME)\\Working Set |
| Virtual Memory Bytes | Current size of the virtual address space of the process, in bytes | Bytes |  |
| Process Identifier | Numeric process identifier (PID) | - |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

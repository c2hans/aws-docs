---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/complete-the-pids-for-arib.html
---

# PIDs for ARIB
<a name="complete-the-pids-for-arib"></a>

This section applies if you are [setting up ARIB captions](output-embedded-and-more.md) in an  output group that supports a transport stream. For example, UDP or SRT. You must specify the output PID.
+ In the relevant output group, choose the output that has the ARIB captions.
+ For **PID settings**, complete **ARIB captions PID control **and **ARIB captions PID** as shown in the following table.

|  ARIB Captions PID Control  |  ARIB Captions PID  |  Result  |
| --- | --- | --- |
| Auto | Ignore | A PID is automatically assigned during encoding. This value could be any number. |
| Use Configured | Enter a decimal or hexadecimal | This PID is used for the captions. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

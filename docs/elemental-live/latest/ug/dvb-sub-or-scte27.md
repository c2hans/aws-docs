---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/dvb-sub-or-scte27.html
---

# Information for DVB-Sub or SCTE-27
<a name="dvb-sub-or-scte27"></a>

This section provides information specific to DVB-Sub or SCTE-27 input captions. It describes the fields that appear when you choose **DVB-Sub** or **SCTE-27** in the **Source** field in the **Caption Selector** section of the event. For more context, see the steps earlier in this section.

DVB-Sub and SCTE-27 formats are supported only in TS inputs. You must specify the location of the captions.

Complete the **PID** and **Language code** fields in one of the ways described in the following table. Each row in the table describes a valid way to complete these two fields.

| PID | Language code | Result |
| --- | --- | --- |
| Specified | Blank | Extracts the captions from the specified PID. |
| Blank | Specified | Extracts the captions from the first PID that Elemental Live encounters that matches the specified language. This might or might not be the PID with the lowest number. |
| Specified | Specified | Extracts the captions from the specified PID. Elemental Live ignores the language code, therefore we recommend you leave it blank. |
| Blank | Blank | Valid only if the source is DVB-Sub and the output is DVB-Sub. With this combination of PID and Language, all input DVB-Sub PIDs will be included in the output.Not valid for SCTE-27. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

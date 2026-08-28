---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/dvb-sub-or-scte-27.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# DVB-Sub or SCTE-27 Formats
<a name="dvb-sub-or-scte-27"></a>

AWS Elemental Server supports DVB-Sub and SCTE-27 formats only in TS inputs.

In most cases, create one captions selector per track. In each selector, specify which track you want by providing the PID or language code.

**Note**
Don't specify the captions in both the **PID** field and the **Language** dropdown list. Specify one or the other.

If you are doing DVB-sub-to-DVB-sub and you want to pass through all the captions tracks from the input to the output, create one captions selector for all tracks. In this case, keep the **PID **field blank and don't choose any language from the **Language** dropdown list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/input-2110.html
---

# Ingesting SMPTE 2110 content
<a name="input-2110"></a>

You can create a SMPTE 2110 input in AWS Elemental Live in order to ingest a source that is compliant with the SMPTE 2110 specification. You can optionally configure the input to use SMPTE 2022-7, if the source offers it.

You can configure the SMPTE 2110 input by specifying an SDP file that contains information about the SMPTE 2110 content. Or you can configure the input to use NMOS to provide that information.

For more information about SMPTE 2110 video content, SMPTE 2022-7, NMOS, and SDP files, see [Working with SMPTE 2110](SMPTE-ST-2110.md).

**Topics**
+ [Get ready](input-2110-get-ready.md)
+ [Setting up a SMPTE 2110 input using NMOS](setup-2110-input-nmos.md)
+ [Setting up a SMPTE 2110 input without NMOS](setup-input-2110.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

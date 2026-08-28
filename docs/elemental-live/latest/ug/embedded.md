---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/embedded.html
---

# Information for embedded
<a name="embedded"></a>

This section provides information specific to embedded input captions. It describes the fields that appear when you choose **Embedded** in the **Source** field in the **Caption Selector** section of the event. For more context, see the steps earlier in this section.

Read this section if the input captions you have are any of the following: embedded (EIA-608 or CEA-708), embedded\+SCTE-20, SCTE-20\+embedded, or SCTE-20.

**Note**
For captions in VBI data: If you are extracting embedded captions from the input and using embedded captions in the output, and if the input includes VBI data and you want to include all that data in the output, then do not follow this procedure. Instead, see [Passing through VBI data](captions-in-vbi-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/downloading-output-quick-flows.html
---

# Downloading output in Amazon Quick Flows
<a name="downloading-output-quick-flows"></a>

After a flow run completes, you can download one or more step outputs as a Word (.docx) or PDF document. You can save files locally or to a shared Quick space for team collaboration. Downloaded files maintain the original formatting, including markdown structure, visual elements, and data tables.

## Download flow outputs
<a name="download-flow-outputs-procedure"></a>

1. In Run mode, choose the download icon (downward arrow) in the top right.

1. Choose **Download as**.

1. Select which outputs to include:
   + Choose **Select All** to include all steps in chronological order.
   + Use checkboxes to select specific steps.
**Note**
User input and file upload steps cannot be downloaded.

1. Select your preferred file format:
   + **Word (docx)** — Editable document format
   + **PDF** — Fixed-layout document format

1. Choose your download destination:
   + **Download** to save the file locally.
   + **Save to a space** to save to a shared space (requires edit access).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

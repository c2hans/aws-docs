---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/create-caption-selectors.html
---

# Step 2: Create captions selectors
<a name="create-caption-selectors"></a>

After you have created a list of captions selectors, you can create the captions selectors in the event.

**To create the captions selectors**

1. In the event, in the **Input** section, choose **Advanced**.

1. Choose **Add Caption Selector**.

1. For **Source**, choose the format of the source captions.

   To identify SMPTE-TT as the source captions, choose **TTML**. When Elemental Live ingests the captions, it automatically detects that they are SMPTE-TT.

1. For most formats, more fields appear. For details about a field, choose the Info link next to the field. In addition, see extra information about [DVB-Sub or SCTE-27](dvb-sub-or-scte27.md), on [Embedded](embedded.md), on [SCC](captions-input-scc.md), on [SMI, SRT, STL, TTML](captions-input-other-sidecars.md), on [teletext](teletext.md), or on [Null](captions-input-null.md).

1. Create more captions selector, as required.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

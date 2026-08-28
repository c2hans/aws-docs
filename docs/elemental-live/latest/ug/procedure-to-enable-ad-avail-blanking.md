---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/procedure-to-enable-ad-avail-blanking.html
---

# Procedure to enable ad avail blanking
<a name="procedure-to-enable-ad-avail-blanking"></a>

**To enable ad avail blanking**

1. In the Profile or Event screen, click Advanced Avail Controls (in the Input section towards the top of the screen):

1. Select or clear the two restriction fields:
   + **Cleared** (default): Observe the restriction and blank the content for the ad avail event.
   + **Selected**: Ignore the restriction and do *not* blank the content for the ad avail event.

1. Go down to the Global Processors section and complete the following fields:
   + **Ad Avail Blanking**: Click to turn on. The **Blanking Image** field appears.
   + **Blanking Image**: Specify a `.bmp` or `.png` file to use for the blanking. If you leave this field blank, a plain black image is inserted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

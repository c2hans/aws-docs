---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/mov-set-up-event-web-interface.html
---

# Using the web interface
<a name="mov-set-up-event-web-interface"></a>

**To configure the event using the web interface**

1. In the **Global Processors** section, go to the **Image Inserter** field and choose **On**. More fields appear.

1. Complete the fields. You can configure some or all the information in the non-running event, but you must at least set the following fields:
   + **Insertion Mode**
   + **Enable REST Control**

   You must also configure the motion overlay behavior when the event first starts:
   + If you want the motion overlay to appear as soon as the event starts, specify all the fields. Make sure that you check **Active**, and make sure that you leave the **Action Time** empty.
   + If you don't want the motion overlay to appear as soon as the event starts, leave **Active** unchecked.

   You can configure the remaining fields after you've started the event, when you want to run the first motion overlay.

   For detailed information about the fields, see [Fields for a MOV asset](mov-set-up-event-fields.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

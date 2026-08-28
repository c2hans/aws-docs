---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-step-event.html
---

# Step 2: Set up the event
<a name="vips-setup-step-event"></a>

These steps show you how to configure the event with information about the POIS server.

The information in this section assumes that you are familiar with the general steps for creating an event.

**Note**
The information in this section assumes that you are familiar with the general steps for creating an event.

1. On the web interface, open the **Ad Avail Controls** section of the event.

1. Complete the fields as follows:
   + **Ad Avail Trigger**: ESAM.
   + **Acquisition Point Identifier**: The value that you [obtained from the POIS operator](vips-setup-step-coordinate.md).
   + **Zone Identity**: The value that you obtained from the POIS operator.
   + **Signal Conditioner Endpoint**: The URL that you obtained from the POIS operator.
   + **Alternate Signal Conditioner Endpoint**: The URL that you obtained from the POIS operator, if any.
   + **Response Signal Preroll**: The value you obtained from the POIS operator, if any.
   + Other fields: The other fields in this section aren't used for virtual input switching.

1. Complete this field only if you want to enable asynchronous input switching:
   + **Unsolicited ESAM Server**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

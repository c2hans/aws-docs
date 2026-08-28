---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-sdi-dev.html
---

# Add SDI input devices
<a name="config-wrkr-lv-cg-sdi-dev"></a>

*Input devices* are cards that are installed in the hardware unit. The AWS Elemental Live node auto-detects the SDI card and creates an input in Elemental Live as follows:
+ One single-link input for each input on the card (so four inputs). Each input is given a unique numerical ID.
+ One quad-link input, if the SDI card supports quad link.

  The quad-link input is used with 4K quad input. When you're creating a profile or event, select this quad-link input to indicate to Elemental Live that the four inputs on this SDI card are the four parts of a quad-link input.

Once you have cabled the SDI cards, make sure that every input that has a cable appears in the **Settings** > **Input Devices** screen. The following image shows input devices in Elemental Live:

![Input Devices screen showing a list of SDI inputs with their status and settings.](http://docs.aws.amazon.com/elemental-live/latest/configguide/images/inputs-shared-png.png)

**Naming Inputs**
If you want, you can give the device a custom name.

1. On the Elemental Live web interface, hover over **Settings** and choose **Input Devices**. Elemental Live lists all of the detected input cards.

1. Enter a name and choose **Save**.

**Note**
If these input device cards are connected to a router, you need to now follow the procedure for adding the router. See [Add SDI video routers](config-wrkr-lv-cg-sdi-rou.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

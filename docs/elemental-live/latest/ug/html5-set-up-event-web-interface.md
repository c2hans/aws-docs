---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-web-interface.html
---

# Using the web interface
<a name="html5-set-up-event-web-interface"></a>

**To configure the event using the web interface**

1. Obtain the asset URL and user credentials (if required) from the administrator of the authoring system that is publishing the HTML5 asset.

1. In the **Global Processors** section, go to the **Image Inserter** field and choose **On**. More fields appear.

1. Complete these fields:
   + **Insertion Mode**: Choose **HTML**.
   + **Input**: Enter the location of the HTML5 asset.

     If access to your local or mounted directory requires authentication, enter the user name and password.

1. Set the following fields to match the control that you're using.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-web-interface.html)

For detailed information about the fields, see [Fields for an HTML5 asset](html5-set-up-event-fields.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

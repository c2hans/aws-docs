---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/how-to-insert-a-motion-overlay-with-html5.html
---

# How to insert a motion overlay with HTML5
<a name="how-to-insert-a-motion-overlay-with-html5"></a>

You can insert a motion overlay with HTML5. The overlay could be an animated overlay such as a sports scoreboard, a stock price ticker tape, or the current time and temperature. You use an HTML5 *authoring system* to create and publish an HTML asset. This system usually has an authoring component that lets you create the overlay content, and a control component that lets you control how and when the overlay is visible.

You configure the Elemental Live event with all the information about the motion overlay, including the location of the asset. After the event starts, Elemental Live pulls the asset that is being published, and includes the overlay in the video, when appropriate. Elemental Live doesn't provide any features for manipulating the content or position of the overlay.

**Topics**
+ [Step A: Choose the method for show/hide](step-design-controls-html5.md)
+ [Step B: Prepare the HTML5 asset](step-prepare-the-html5-asset.md)
+ [Step C: Set up the event](html5-step-set-up-the-event.md)
+ [Step D: Showing and hiding the motion overlay](html5-step-manage-the-overlay-on-a-running-event.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

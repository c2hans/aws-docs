---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/managing-templates-pacings.html
---

# Understanding template pacing in WhatsApp
<a name="managing-templates-pacings"></a>

Template pacing is a method, used by Meta, that allows time for early customer feedback on new or modified templates. It identifies and pauses templates that receive poor engagement or feedback, giving you time to adjust the template content before sending it to too many customers. This reduces the risk of negative customer feedback impacting the business. For example, if too many customers "block" your message, or if your template has low read rates, then your template quality rating can be lowered.

Template pacing affects newly created templates, templates that have been unpaused, and templates without a high quality rating. Template pacing is often started by a previous history of low quality or paused templates. When a template is paced, messages using that template are sent normally up to a certain threshold determined by Meta. After that, subsequent messages are held to allow time for customer feedback. If the feedback is positive, the template pacing is then scaled up. If the feedback is negative, the template pacing is lowered, allowing you to adjust the template content. For more information, see [Template pacing](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines#template-pacing) in the *WhatsApp Business Platform Cloud API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

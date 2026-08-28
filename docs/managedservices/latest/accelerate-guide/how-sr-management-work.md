---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/how-sr-management-work.html
---

# How service request management works in Accelerate
<a name="how-sr-management-work"></a>

Service requests are handled by the on-call AMS Accelerate operations team.

After your service request is received by the AMS Accelerate operations team, it's reviewed to make sure that it's properly classified as a service request or an incident. If it's reclassified as an incident, the AMS Accelerate incident management process begins and you're sent a notification.

If the AMS Accelerate operator can resolve the service request, steps to do so are taken immediately. For example, if the service request is for architecture advice or other information, then the operator refers you to the appropriate resources or answers the question directly.

If the analysis of your service request identifies a bug or a feature request, then AMS sends you a notification through the service request. Since there is no ETA for feature requests or bug fixes, the original service request is closed. Contact your CSDM for follow up questions related to the original service request.

If the service request is out of scope for AMS Accelerate operations, the operator either sends the request to your cloud service delivery manager, so they can communicate with you, or to the appropriate AWS support team, along with an email to you as to what steps are being taken.

The service request is not resolved until you have indicated that you are satisfied with the outcome.

**Note**
We recommend you provide a contact email, name, and phone number in all cases to facilitate communications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

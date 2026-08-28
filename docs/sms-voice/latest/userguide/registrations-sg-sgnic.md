---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-sg-sgnic.html
---

# Registering a Sender ID with Singapore Network Information Centre (SGNIC)
<a name="registrations-sg-sgnic"></a>

To register a sender ID with Singapore Network Information Centre (SGNIC) there are two steps that must be completed in the following order:

**Register a sender ID with Singapore Network Information Centre (SGNIC)**

1. You must first work with AWS End User Messaging SMS to register your Singapore (SG) Sender ID for your account. After this step is complete you can proceed to the next step.

1. Work with SGNIC to register your sender ID using the process at [SGNIC SMS Sender ID Registry](https://smsregistry.sg/web/login).

   1. When completing the process list AMCS SG Private Limited (Amazon Media Communications Services) as your participating aggregator.

**Warning**
Doing these steps out of order might result in your sender ID being blocked by the service or will prevent your Sender ID from being preserved on the mobile device.

**Note**
Please note that you are required to submit a sender ID registration from each individual AWS account you require to use the sender ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

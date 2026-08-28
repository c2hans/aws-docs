---
source_url: https://docs.aws.amazon.com/iot-expresslink/latest/oemonboardingguide/oemog-summary.html
---

# Summary
<a name="oemog-summary"></a>

To summarize, ExpressLink modules come pre-provisioned with a unique identifier and a certificate signed by the module manufacturer Certificate Authority (CA), ready to authenticate with AWS IoT Core.

Onboarding, the act of binding the module credentials to a [thing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) inside the AWS IoT registry of an customer/OEM's account is accomplished using various mechanisms provided to all devices that connect to AWS IoT Core. This guide describes a novel onboarding-by-claim mechanism specifically created to leverage an ExpressLink module's unique capabilities.

By following the steps in this document, any customer/OEM can take advantage of this new capability to provide their own customers with the best experience, while optimizing the supply chain for security and flexibility.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT ExpressLink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-expresslink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

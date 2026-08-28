---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-licensing.html
---

# Software licensing for service-managed fleets
<a name="smf-licensing"></a>

Deadline Cloud provides usage-based licensing (UBL) for commonly used software packages. Supported software packages are automatically licensed when they run on a service-managed fleet. You don't need to configure or maintain a software license server. Licenses scale so you won't run out for larger jobs.

You can install software packages that support UBL using the built-in Deadline Cloud conda channel, or you can use your own packages. For more information about the conda channel, see [Create a queue environment](create-queue-environment.md).

For a list of supported software packages and information about pricing for UBL, see [AWS Deadline Cloud pricing](https://aws.amazon.com/deadline-cloud/pricing/).

## Bring your own license with service-managed fleets
<a name="bring-your-own"></a>

With Deadline Cloud usage-based licensing (UBL), you don't need to manage separate license agreements with software vendors. However, if you have existing licenses or need to use software that isn't available through UBL, you can use your own software licenses with your Deadline Cloud service-managed fleets. Workers connect to your license server through a VPC resource endpoint, through port forwarding to an instance in your account, or over the internet. The license server can be in another VPC or AWS account, as long as the endpoint or forwarding instance has network access to it.

You can also combine both methods so workers use your existing licenses first and fall back to UBL when they run out.

For a comparison of the licensing options and setup instructions, see [Using software licenses with Deadline Cloud](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/license.html) in the *Deadline Cloud Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ct-internals.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Internal-only change types
<a name="ct-internals"></a>

You can see change types that are for internal use only. This is so you know what actions AMS can, or does, take. If there is an internal-only change type that you would like to have available for your use, submit a service request.

For example, there is a Management \| Monitoring and notification \| CloudWatch alarm suppression \| Update CT that is internal-only. AMS uses it to deploy infrastructure updates (such as patching) to turn off alarm notifications that the updates might erroneously trigger. When this CT is submitted, you will notice the RFC for the CT in your RFC list. Any internal-only CT that is deployed in an RFC appears in your RFC list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

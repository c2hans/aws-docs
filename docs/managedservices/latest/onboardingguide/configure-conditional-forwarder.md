---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/configure-conditional-forwarder.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Configure the conditional forwarder
<a name="configure-conditional-forwarder"></a>

Follow this Microsoft AD article [ Assign a Conditional Forwarder for a Domain Name](https://technet.microsoft.com/en-us/library/cc794735%28v=ws.10%29.aspx), and use these settings and choices:

1. In the AD **DNS Manager -> Create a New Conditional Forwarder**, under **DNS Domain:** Use the domain name AMS supplied to you; for example, {{A523434123.amazonaws.com}}.

1. Under **IP addresses of the master servers:** Add the AMS-supplied IP addresses. Make sure there isn’t a connection problem by validating both addresses.

1. Select **Store this conditional forwarder in Active Directory and replicate as follows: All DNS servers in this domain** and press **OK**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt-con-trust.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Configure the AD trust
<a name="set-up-access-mgmt-con-trust"></a>

Follow this Microsoft AD article [ Create a one-way, incoming, forest trust for one side of the trust](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc756735(v=ws.10)), using the settings and choices described in this section.

1. Open the **Start -> Administrative Tools -> Active Directory Domains and Trusts** dialog. Right-click the domain node for the domain that you want to establish a trust with, and then click **Properties -> Trusts -> New Trust** to open the New Trust Wizard. Enter the domain name provided to you by AMS for the **Trust Name** and press **Next**.

1. Under **Trust Type**, select appropriate trust level (e.g. Forest Trust). Press**Next**.

1. Under **Direction of Trust**, select **One-way: incoming**. Press **Next**.

1. Under **Sides of Trust**, select **This domain only**. Press **Next**.

1. Under **Trust Password**, type a password of your choosing. Press **Next**.

1. For **Trust Selections Completed** and **Trust Creation Complete**, just press **Next**.

1. Under **Confirm Incoming Trust**, select **No**, do not confirm the incoming trust. Press **Next**.

1. Under **Completed the New Trust Wizard**, select **Finish**, and then **OK** to close.

1. Provide the trust password (contact us via your CSDM's phone number for security reasons). AMS will complete the trust configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

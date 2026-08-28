---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ma-verify-console-access.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Verify console access
<a name="ma-verify-console-access"></a>

Once you are set up with ADFS, and have the AMS URL to use for authentication, follow these steps.

With an Active Directory Federated Service (ADFS) configuration, you can follow these steps:

1. Open a browser window and go to the sign in page provided to you for your account. The ADFS **IdpInitiatedSignOn** page for your account opens.

1. Select the radio button next to **Sign in to one of the following sites**. The **Sign in** site picklist becomes active.

1. Choose the **signin.aws.amazon.com** site and click **Sign in**. Options for entering your credentials open.

1. Enter your CORP credentials and click **Sign in**. The AWS Management Console opens.

1. Paste into the location bar the URL of the AMS console and press **Enter**. The AMS console opens.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-leostream-gateway-module.html
---

# Step 4: Enable Leostream Gateway module
<a name="enable-leostream-gateway-module"></a>

Follow these steps to enable the Leostream Broker module.

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

1. Navigate to the MCS web console (see [Launch the stack](launch-the-stack.md) for details).

1. Select **Workstation Management** from the left navigation pane.

1. Choose **Deploy New Module**.

1. For **Select Region**, select the Region where you want the Leostream Broker module. There should be only one hub Region option if you have not deployed any spoke Regions.

1. For **Select Workstation Management module**, select **Gateway with Amazon DCV**, and choose **Next**.

1. For **Configure workstation management settings**, review the parameters for this module and modify them as necessary. This module uses the following default values.
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/enable-leostream-gateway-module.html)

1. For **Configure Tag Settings**, review the tags for this module and modify them as necessary. By default, this module uses tags defined in the main solution stack.

1. Choose **Next**.

1. On the **Review** page, verify all the parameters that you provided and choose **Deploy Module** if you confirm that they are correct.

1. The status of the Leostream Gateway shows as **Enabling in progress**. The deployment of this module takes approximately 1 hour. After the deployment is complete, the status of the Leostream Gateway module shows as **Enabled**.

1. Choose **External Link**. This opens a new window to the Leostream log in page.
**Note**
If you provided a FQDN in the previous steps, you’ll be directed to the domain with the certificate that you provided. If you didn’t provide the information, you’ll be directed to the AWS Global Accelerator using a self-signed certificate. In this case, depending on your browser setting, you might see a privacy error with warnings about your connection not being private.

1. Sign in as a Leostream local admin user ([Step 5: Enable Leostream Broker module](enable-leostream-broker-module.md) step 11) to access the Leostream Connection Broker and manage configurations.

1. To access workstations through Leostream, sign in using your Active Directory credentials ([Step 3: Enable Identity modules](enable-identity-modules.md) step 7 if you created a new AD using MCS). When signing in, use the username format `your-username@mad.mcs.int`.

   Download the Amazon DCV Client from [https://www.amazondcv.com](https://www.amazondcv.com/). After the connection is established, send the Ctrl\+Alt\+Delete command from the Connection menu in the Amazon DCV Client to unlock the workstation and proceed to the login screen.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

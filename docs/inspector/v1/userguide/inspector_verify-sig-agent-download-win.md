---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_verify-sig-agent-download-win.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# (Optional) Verify the signature of the Amazon Inspector Classic agent installation script on Windows-based operating systems
<a name="inspector_verify-sig-agent-download-win"></a>

This topic describes the recommended process of verifying the validity of the Amazon Inspector Classic agent's installations script for Windows-based operating systems.

Whenever you download an application from the internet, we recommend that you authenticate the identity of the software publisher and check that the application is not altered or corrupted since it was published. This protects you from installing a version of the application that contains a virus or other malicious code.

If after running the steps in this topic, you determine that the software for the Amazon Inspector Classic agent is altered or corrupted, do NOT run the installation file. Instead, contact AWS Support.

To verify the validity of the downloaded agent installation script on Windows-based operating systems, make sure that the thumbprint of its Amazon Services LLC signer certificate is equal to this value:

**E8 83 C5 3A F7 8C BA 7C F5 A2 47 E9 B8 86 FC E9 68 EE 0B 36**

To verify this value, perform the following procedure:

1. Right-click the downloaded `AWSAgentInstall.exe`, and open the **Properties** window.

1. Choose the **Digital Signatures** tab.

1. From the **Signature List**, choose **Amazon Web Services, Inc.**, and then choose **Details**.

1. Choose the **General** tab, if not already selected, and then choose **View Certificate**.

1. Choose the **Details** tab, and then choose **All** in the **Show** dropdown list, if not already selected.

1. Scroll down until you see the **Thumbprint** field and then choose **Thumbprint**. This displays the entire thumbprint value in the lower window.
   + If the thumbprint value in the lower window is identical to the following value:

     **E8 83 C5 3A F7 8C BA 7C F5 A2 47 E9 B8 86 FC E9 68 EE 0B 36 **

     then your downloaded agent installation script is authentic and can be safely installed.
   + If the thumbprint value in the lower details window is not identical to the value above, do not run `AWSAgentInstall.exe`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

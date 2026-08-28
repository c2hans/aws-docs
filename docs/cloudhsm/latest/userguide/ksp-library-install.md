---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ksp-library-install.html
---

# Install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5
<a name="ksp-library-install"></a>

Use the following sections to install the Key storage provider (KSP) for AWS CloudHSM Client SDK 5.

**Note**
To run a single HSM cluster with Client SDK 5, you must first manage client key durability settings by setting `disable_key_availability_check` to `True`. For more information, see [Key Synchronization](manage-key-sync.md) and [Client SDK 5 Configure Tool](configure-sdk-5.md).

**To install and configure the Key Storage Provider (KSP)**

1. Install the Key Storage Provider (KSP) for Windows Server on x86\_64 architecture, open PowerShell as an administrator and run the following command:

   ```
   PS C:\> wget https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Windows/AWSCloudHSMKSP-latest.msi -Outfile C:\AWSCloudHSMKSP-latest.msi
   ```

   ```
   PS C:\> Start-Process msiexec.exe -ArgumentList '/i C:\AWSCloudHSMKSP-latest.msi /quiet /norestart /log C:\client-install.txt' -Wait
   ```

1. Use the configure tool to specify the location of the issuing certificate. For instructions, see [Specify the location of the issuing certificate](cluster-connect.md#specify-cert-location).

1. To connect to your cluster, see [Bootstrap the Client SDK](cluster-connect.md#connect-how-to).

1. You can find the Key Storage Provider (KSP) files in the following locations:
   + Windows binaries:

     ```
     C:\Program Files\Amazon\CloudHSM
     ```

     Windows configuration scripts and log files:

     ```
     C:\ProgramData\Amazon\CloudHSM
     ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

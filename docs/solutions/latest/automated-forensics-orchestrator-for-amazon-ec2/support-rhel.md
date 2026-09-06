---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/support-rhel.html
---

# Support for Red Hat Enterprise Linux (RHEL 8.6 and above)
<a name="support-rhel"></a>

Starting from the current version (1.2.0), the Guidance supports Red Hat Enterprise Linux (RHEL) 8.6 and above. To use RHEL as the target, you must build a symbol based on the target RHEL.

**Note**
You will only need to build this once per RHEL version.

To build a symbol:

1. After you deploy the Guidance, navigate to the [AWS Management Console](https://console.aws.amazon.com/) where you have deployed the Guidance.

1. Navigate to **Step Functions**, and select the `Forensic-Profile-Function` step function

1. To initiate the build, add these input parameters.

   ```
   {
       "amiId": "ami-0b6c020bf93af9ce1",
       "distribution": "RHEL8"
   }
   ```

   where `ami-0b6c020bf93af9ce1` is the base image Amazon Machine Image (AMI) for RHEL8
**Note**
You will need a Red Hat subscription before you add this. For more information, refer to the [Linux platforms](https://www.redhat.com/en/store/linux-platforms) page.

The `Forensic-Profile-Function` step function will build the symbol automatically. Once the symbol is built, the Guidance will support RHEL8.

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/user-access-and-remote-desktops.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# User access and remote desktops
<a name="user-access-and-remote-desktops"></a>

 Once users and engineers have the data they need to run flows, enabling access can be accomplished through multiple mechanisms. The same methods that are being used by your engineers to access on-premises systems can also be used for accessing AWS resources. Many engineers login via command line with ssh, or through a web UI for managing job submission and monitoring. These same methods are available on AWS.

 The following figure shows connectivity from on-premises systems to AWS infrastructure. The additional launched services and resources are [AWS Directory Service](https://aws.amazon.com/directoryservice), login server, scheduling server, and a remote desktop using [NICE DCV](https://aws.amazon.com/hpc/dcv). The login and scheduler servers, remote desktop instance, testing, and POC should all use moderately sized [instance types](https://aws.amazon.com/ec2/instance-types/). For example, M5.2xlarge, T2, or T3 instance types should suffice for these applications. We provide additional details about which instances to use in the [Amazon Elastic Compute Cloud (Amazon EC2)](launch-aws-services-needed-to-run-a-poc.md#amazon-elastic-compute-cloud-amazon-ec2) section.

![This diagram shows the user access and remote desktops component of the semiconductor environment on AWS.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-user-access-remote-desktops.png)

**User access and remote desktops **

## Remote Desktops
<a name="remote-desktops"></a>

 Remote desktops are a cost effective way to bring the engineer to the data, rather than bring the data to the engineer. Remote desktops can be used to view waveforms or step through a simulation to identify and resolve register-transfer-level (RTL) regression errors, or it might be necessary to view a 2D or 3D graphical representation of results generated during signal integrity analysis. Some applications, such as printed circuit layout software, are inherently interactive and require a high quality, low latency user experience.

 There are multiple ways to deploy remote desktops on AWS. You have the option of using open-source software such as Virtual Network Computing (VNC), or commercial remote desktop solutions available from AWS partners. You can also make use of AWS solutions, including NICE desktop cloud visualization (NICE DCV).

### NICE DCV
<a name="nice-dcv"></a>

 NICE Desktop Cloud Visualization (NICE DCV)is a remote visualization technology that enables users to securely connect to graphic-intensive 2D and 3D applications hosted on an Amazon EC2 instance. With NICE DCV, you can provide high-performance graphics processing to remote users by creating secure client sessions. NICE DCV was specifically designed for high performance technical applications, and is an excellent choice for semiconductor design workloads. For more information, see [NICE DCV](https://aws.amazon.com/hpc/dcv/).

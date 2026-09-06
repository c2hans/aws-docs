---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/enable-user-access-and-remote-visualization.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enable user access and remote visualization
<a name="enable-user-access-and-remote-visualization"></a>

After connections have been established and data is migrated, user access and tool installation can be performed. User access is enabled either with terminal-based ssh sessions or graphical remote desktops. A remote desktop provides the same user experience on AWS as on the user’s on-premises infrastructure. Tool engineers and chip designers can submit jobs, manage data, and use GUI-driven interactive tools (such as layout, place and route) in a familiar environment that creates a smooth transition to the cloud.

For remote visualization, you can use existing on-premises commercial solutions such as [NoMachine NX](https://www.nomachine.com/) or [OpenText Exceed TurboX](https://www.opentext.com/products-and-solutions/products/specialty-technologies/connectivity/opentext-exceed-turbox). Optionally, AWS offers a remote desktop service called [NICE DCV](https://aws.amazon.com/hpc/dcv/). NICE DCV is a secure, cloud-native solution that provides a robust user interface for engineering and physical design teams, and performs well over varying network conditions. NICE DCV is provided at no additional cost; you just pay for the EC2 instance that it is running on.

Although the details are beyond the scope of this document, you will also need to install tools and other applications that are required by the engineers on your team. This may involve creating, mounting, and configuring several file systems that are accessible across all Amazon EC2 instances. It is also important to work with your ISV or tool provider to ensure your licensing agreements allow you to run the necessary EDA tools on AWS.

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/license-server-setup.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# License server setup
<a name="license-server-setup"></a>

 Application licensing is required for most semiconductor design workloads, both on-premises and on AWS. From a technical standpoint, managing and accessing EDA licenses can remain unchanged when migrating to AWS. Over time, you may choose to augment your existing license management using AWS services, for example using analytics and machine learning services on AWS to monitor and improve license utilization across projects, and across sites. You can also use features of AWS, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling), to improve license server reliability and reduce time to market.

 Because of the connectivity options available, you can run your license servers on AWS using an Amazon EC2 instance or within your own data centers. By allowing connectivity through a VPN or AWS Direct Connect between cloud resources and on-premises license servers, you can seamlessly run workloads in any location without having to dedicate some of your valuable EDA licenses to your AWS computing environments, thereby fragmenting your license pools.

 The following figure shows how to set up your on-premises license servers on AWS, so you can both run your existing on-premises flows using the license servers hosted on AWS, and also use the same servers when migrating your flows over to AWS. As with the other infrastructure support instances, a moderately sized instance (e.g., M5.2xlarge) will suffice for testing and POC environments.

![This diagram shows the services involved for the license server setup component of the semiconductor environment.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-license-server-setup.png)

**License server setup **

## License Server Access
<a name="license-server-access"></a>

 On AWS, each Amazon EC2 instance launched is provided with a unique hostname and hardware address (MAC) using Amazon elastic network interfaces that cannot be cloned or spoofed. Therefore, traditional license server technologies (such as Flexera) work on AWS without any modification. The inability to clone license servers, which is prevented by AWS by not allowing the duplication of MAC addresses, also provides software vendors with the confidence that software can be deployed and used in a secure manner.

 Although you can configure your EDA tools to use on-premises license servers while running in AWS, the latency may adversely affect the run time of the job. For initial tests and POCs, using an on-premises license server is a suitable solution. For production and for like-to-like comparisons, we recommend setting up license servers in AWS. This approach reduces the need to connect back in to on-premises license servers, and eliminates the latency penalty incurred at license check out.

 The following figure shows three license server deployment scenarios – on premises only license server, cloud-only license server, and on-premises and cloud license servers. Your architecture depends on many factors, but these three options can provide guidance to build out a reliable and scalable licensing architecture. If you plan on using an on-premises license server while running on AWS, as many licensed applications are sensitive to network latency from client to server, a dedicated connection from your on-premises network to the nearest AWS Region using AWS Direct Connect can provide a reliable network connection with consistent latency.

![This diagram shows the three license server deployment scenarios: on-premises license server, cloud-only license server, and on-premises and cloud license server.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-license-server-deployments.png)

**License server deployment scenarios **

## Improving License Server Reliability
<a name="improving-license-server-reliability"></a>

 License servers are critical components in all chip design environments. Hosting licenses in the AWS Cloud can provide improved reliability of license services with the use of a floating [elastic network interface](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html). The elastic network interface has a fixed, immutable MAC address that can be associated with software license keys.

 The implementation of this high availability solution begins with the creation of a elastic network interface that is attached to a license server instance. Your license keys are associated with this elastic network interface. If a failure is detected on this instance, you, or your custom automation, can detach the elastic network interface and attach it to a standby license server. Because the elastic network interface maintains its IP and MAC addresses, network traffic begins flowing to the standby instance as soon as you attach the elastic network interface to the replacement instance.

 This unique capability enables license administrators to provide a level of reliability that can be difficult to achieve using on-premises servers in a traditional datacenter.

## Working with Independent Software Vendors (ISVs)
<a name="working-with-independent-software-vendors-isvs"></a>

 AWS works closely with thousands of independent software vendors (ISVs) that deliver solutions to customers on AWS using methods that may include software as a service (SaaS), platform as a service (PaaS), customer self-managed, and bring your own license (BYOL) models. In the semiconductor industry, AWS works closely with the major vendors of EDA software to help optimize performance, scalability, cost, and application security. AWS can assist ISVs and your organization with deployment best practices described in this guide.

 [AWS Partner Programs](https://aws.amazon.com/partners/programs) are designed to support the unique technical and business requirements of AWS Partner Network (APN) members by providing them with increased support from AWS, including access to AWS Partner team members who specialize in design and engineering applications. In addition, AWS has a growing number of [APN Consulting Partners](https://aws.amazon.com/partners/consulting) who can assist vendors and their customers with cloud migration.

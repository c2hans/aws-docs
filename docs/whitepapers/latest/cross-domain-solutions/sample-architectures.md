---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/sample-architectures.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Sample Architectures
<a name="sample-architectures"></a>

 The following sections outline different architectures for transferring data across security domains. These samples focus on where the source security domain data resides and the desired destination security domain. Some of the samples show the use of customer-owned CDS equipment. But as data moves from on-premises to cloud-based models, the needs for these may disappear and allow different architectures to replace the legacy model. The models are organized as follows:
+  Both of the security domains are in the cloud
+  The source security domain is the cloud and the destination domain is on-premises
+  Both the source and the destination domains are in the cloud, but the customer wants to manage and maintain the CDS component at its location

## Both Security Domains are in the Cloud
<a name="both-security-domains-are-in-the-cloud"></a>

 AWS Diode provides a service to allow native cloud-friendly transfer of data from one cloud security domain to another. The advantage of this service is that you do not need to maintain or manage the cross-domain system (which is a costly endeavor both in manpower and time). The AWS Diode service supports moving multiple file types as well as the option to move compiled code in support of CI/CD pipelines. The following image depicts the service architecture:

![Cloud native CDS](http://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/images/cloud-native-cds.png)

 *Figure 1 – Cloud Native CDS*

 This service works entirely within the cloud security domains and provides the added benefit of cloud APIs that move your data when you want it moved. Because it is a cloud-based service, you do not need to worry about scaling it to support your workload or managing all the complexities and auditing needs of CDS devices. The service is interfaced directly to all the standard auditing in the cloud and provides an ease of use like Amazon EC2 or Amazon S3. For customers who are more interested in getting their data moved versus running a CDS, this service provides the high-speed backbone to move your critical data.

 Again, this option is most attractive when your data is in the cloud and needs to move to the cloud in another security domain.

 You can set up your CDS in many ways. The following examples describe some of the more common architectures in use.

## Deploying a CDS through the Internet or AWS Direct Connect
<a name="deploying-a-cds-through-the-internet-or-aws-direct-connect"></a>

 Figure 2 shows two on-premises customer networks that are connected by a CDS using the traditional deployment. In this configuration, Security Domain A is extended to provide connectivity to an Amazon VPC in the AWS Cloud, while Security Domain B exists solely within the customer’s data center. The connectivity between Security Domain A and an Amazon VPC can be done using a secure IPSec tunnel or using AWS Direct Connect as depicted.

![Two on-premises customer networks that are connected by a CDS using the traditional deployment](http://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/images/onprem-networks-cds-connected.png)

 *Figure 2 – Deploying a CDS through the internet*

![Deploying a CDS through IPSEC or Direct Connect](http://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/images/cds-through-ipsec-or-direct-connect.png)

 *Figure 3: Deploying a CDS through IPSEC or Direct Connect*

 A secure IPSEC tunnel encapsulates data crossing the Internet between on-premises infrastructure and the customer’s VPC. Additional security mechanisms, such as a WAF or an intrusion detection system (IDS), can be deployed within Security Domain A for added protection from Internet-facing systems. Because Amazon VPC is an extension of Security Domain A, Amazon EC2 instances launched within Amazon VPC can communicate with resources in Security Domain B through the CDS.

## Deploying a CDS across Multiple Regions
<a name="deploying-a-cds-across-multiple-regions"></a>

 Figure 4 shows two individual security domains connected to two separate AWS Regions. As shown earlier in Figure 2, the security domains are extended by using a combination of Direct Connect and a secure IPSEC VPN tunnel. All data flowing between the security domains flows from AWS to the customer’s data center first, where it is inspected by the CDS before flowing back to AWS.

![Two individual security domains connected to two separate AWS Regions](http://docs.aws.amazon.com/whitepapers/latest/cross-domain-solutions/images/security-domains-connected-to-regions.png)

 *Figure 4: Deploying a CDS across multiple regions*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

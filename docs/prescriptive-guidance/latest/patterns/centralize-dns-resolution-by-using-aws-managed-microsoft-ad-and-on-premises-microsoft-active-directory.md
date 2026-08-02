---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html
---

# Centralize DNS resolution by using AWS Managed Microsoft AD and on-premises Microsoft Active Directory
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory"></a>

*Brian Westmoreland, Amazon Web Services*

## Summary
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-summary"></a>

This pattern provides guidance for centralizing DNS resolution within an AWS multi-account environment by using both AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) and Amazon Route 53. In this pattern the AWS DNS namespace is a subdomain of the on-premises DNS namespace. This pattern also provides guidance on how to configure the on-premises DNS servers to forward queries to AWS when the on-premises DNS solution uses Microsoft Active Directory.

## Prerequisites and limitations
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-prereqs"></a>

**Prerequisites **
+ An AWS multi-account environment set up by using AWS Organizations.
+ Network connectivity established between AWS accounts.
+ Network connectivity established between AWS and the on-premises environment (by using AWS Direct Connect or any type of VPN connection).
+ AWS Command Line Interface (AWS CLI) configured on a local workstation.
+ AWS Resource Access Manager (AWS RAM) used to share Route 53 rules between accounts. Therefore, sharing must be enabled within the AWS Organizations environment, as described in the [Epics](#centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-epics) section.

**Limitations **
+ AWS Managed Microsoft AD Standard Edition has a limit of 5 shares.
+ AWS Managed Microsoft AD Enterprise Edition has a limit of 125 shares.
+ The solution in this pattern is limited to AWS Regions that support sharing through AWS RAM.

**Product versions**
+ Microsoft Active Directory running on Windows Server 2008, 2012, 2012 R2, or 2016.

## Architecture
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-architecture"></a>

**Target architecture **

![Architecture for centralized DNS resolution on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/91430e2a-f7f6-4dbe-9fe7-8abed1f764a7/images/9b5fc51d-590b-468f-80f7-1949f3b3b258.png)

In this design, AWS Managed Microsoft AD is installed in the shared services AWS account. Although it is not a requirement, this pattern assumes this configuration. If you configure AWS Managed Microsoft AD in a different AWS account, you might have to modify the steps in the [Epics](#centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-epics) section accordingly.

This design uses Route 53 Resolvers to support name resolution through the use of Route 53 rules. If the on-premises DNS solution uses Microsoft DNS, creating a conditional forwarding rule for the AWS namespace (`aws.company.com`), which is a subdomain of the company DNS namespace (`company.com`), is not straightforward. If you try to create a traditional conditional forwarder, it will result in an error. This is because Microsoft Active Directory is already considered authoritative for any subdomain of `company.com`. To get around this error, you must first create a delegation for `aws.company.com` to delegate authority of that namespace. You can then create the conditional forwarder.

The virtual private cloud (VPC) for each spoke account can have its own unique DNS namespace based on the root AWS namespace. In this design, each spoke account appends an abbreviation of the account name to the base AWS namespace. After the private hosted zones in the spoke account have been created, the zones are associated with the local VPC in the spoke account as well as with the VPC in the central AWS network account. This enables the central AWS network account to answer DNS queries related to the spoke accounts. This way, both Route 53 and AWS Managed Microsoft AD work together to share the responsibility of managing the AWS namespace (`aws.company.com`).

**Automation and scale**

This design uses Route 53 Resolver endpoints to scale DNS queries between AWS and your on-premises environment. Each Route 53 Resolver endpoint comprises multiple elastic network interfaces (spread across multiple Availability Zones), and each network interface can handle up to 10,000 queries per second. Route 53 Resolver supports up to 6 IP addresses per endpoint, so altogether this design supports up to 60,000 DNS queries per second spread across multiple Availability Zones for high availability.

Additionally, this pattern automatically accounts for future growth within AWS. The DNS forwarding rules configured on premises do not have to be modified to support new VPCs and their associated private hosted zones that are added to AWS.

## Tools
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-tools"></a>

**AWS services**
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts to reduce operational overhead and provide visibility and auditability.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.

**Tools**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell. In this pattern, the AWS CLI is used to configure Route 53 authorizations.

## Epics
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-epics"></a>

### Create and share an AWS Managed Microsoft AD directory
<a name="create-and-share-an-managed-ad-directory"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy AWS Managed Microsoft AD. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html) | AWS administrator |
| Share the directory. | After the directory has been built, share it with other AWS accounts in the AWS organization. For instructions, see [Share your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step2_share_directory.html) in the *AWS Directory Service Administration Guide*.  AWS Managed Microsoft AD Standard Edition has a limit of 5 shares. Enterprise Edition has a limit of 125 shares. | AWS administrator |

### Configure Route 53
<a name="configure-r53"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Route 53 Resolvers. | Route 53 Resolvers facilitate DNS query resolution between AWS and the on-premises data center.  [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html)Although using the central AWS network account VPC isn’t a requirement, the remaining steps assume this configuration. | AWS administrator |
| Create Route 53 rules. | Your specific use case might require a large number of Route 53 rules, but you will need to configure the following rules as a baseline:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html)<br />For more information, see [Managing forwarding rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html) in the *Route 53 Developer Guide*. | AWS administrator |
| Configure a Route 53 Profile. | A Route 53 Profile is used to share the rules with spoke accounts.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html) | AWS administrator |

### Configure on-premises Active Directory DNS
<a name="configure-on-premises-active-directory-dns"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the delegation. | Use the Microsoft DNS snap-in (`dnsmgmt.msc`) to create a new delegation for the `company.com` namespace within Active Directory. The name of the delegated domain should be `aws`. This makes the fully qualified domain name (FQDN) of the delegation `aws.company.com`. Use the IP addresses of the AWS Managed Microsoft AD domain controllers for the name server IP values, and use `server.aws.company.com` for the name. (This delegation is only for redundancy, because a conditional forwarder will be created for this namespace that takes precedence over the delegation.) | Active Directory |
| Create the conditional forwarder. | Use the Microsoft DNS snap-in (`dnsmgmt.msc`) to create a new conditional forwarder for `aws.company.com`.  Use the IP addresses of the AWS inbound Route 53 Resolvers in the central DNS AWS account for the target of the conditional forwarder.   | Active Directory |

### Create Route 53 private hosted zones for spoke AWS accounts
<a name="create-r53-private-hosted-zones-for-spoke-aws-accounts"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Route 53 private hosted zones. | Create a Route 53 private hosted zone in each spoke account. Associate this private hosted zone with the spoke account VPC. For detailed steps, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) in the *Route 53 Developer Guide*. | AWS administrator |
| Create authorizations. | Use the AWS CLI to create an authorization for the central AWS network account VPC. Run this command from the context of each spoke AWS account:<pre>aws route53 create-vpc-association-authorization --hosted-zone-id <hosted-zone-id> \<br />   --vpc VPCRegion=<region>,VPCId=<vpc-id></pre><br />where:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html) | AWS administrator |
| Create associations. | Create the Route 53 private hosted zone association for the central AWS network account VPC by using the AWS CLI. Run this command from the context of the central AWS network account:<pre>aws route53 associate-vpc-with-hosted-zone --hosted-zone-id <hosted-zone-id> \<br />   --vpc VPCRegion=<region>,VPCId=<vpc-id></pre><br />where:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory.html) | AWS administrator |

## Related resources
<a name="centralize-dns-resolution-by-using-aws-managed-microsoft-ad-and-on-premises-microsoft-active-directory-resources"></a>
+ [Simplify DNS management in a multi-account environment with Route 53 Resolver](https://aws.amazon.com/blogs/security/simplify-dns-management-in-a-multiaccount-environment-with-route-53-resolver/) (AWS blog post)
+ [Creating your AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_create_directory.html) (AWS Directory Service documentation)
+ [Sharing an AWS Managed Microsoft AD directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/step2_share_directory.html) (AWS Directory Service documentation)
+ [What is Amazon Route 53 Resolver?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) (Amazon Route 53 documentation)
+ [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) (Amazon Route 53 documentation)
+ [What are Amazon Route 53 Profiles?](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html) (Amazon Route 53 documentation)

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/virtual-interfaces-vif.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Virtual interfaces (VIF)
<a name="virtual-interfaces-vif"></a>

 With these connections, you can create *virtual interfaces* directly to public AWS services (for example, to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) or Amazon Connect) or to Amazon VPC, bypassing internet service providers in your network path. An AWS Direct Connect point-of-presence (AWS DX POP), carrier interconnection, and data center interconnection provides access to AWS in the Region with which it is associated. You can use a single connection in an AWS Region or [AWS GovCloud](https://aws.amazon.com/govcloud-us/) (US) to access public AWS services in all other Regions.

 Create a virtual interface to enable access to AWS services. A public virtual interface (public VIF) enables access to public services such as Amazon S3 or Amazon Connect. A private virtual interface (private VIF) enables access to your VPC and hosted workloads. A transit virtual interface (transit VIF) is used to access one or more Amazon Transit Gateways associated with Direct Connect gateways.

![Reference diagram of VIF propagation over BGP.](http://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/images/vif-propogation.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

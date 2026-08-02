---
source_url: https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/hybrid-cloud-cost-calculation-example.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid cloud cost calculation example
<a name="hybrid-cloud-cost-calculation-example"></a>

 This example is a hybrid cloud use case of AWS Outposts rack, deployed on-premises and connected to AWS Cloud using AWS Direct Connect. Outposts extends the existing VPC from the selected AWS Region to the customer data center. Selected AWS services required to run on-premises (for example, Amazon Elastic Kubernetes Service (Amazon EKS)) are available on Outposts inside the Outpost Availability Zone, deployed inside a separate subnet.

## Hybrid cloud components selection
<a name="hybrid-cloud-components-selection"></a>

 Customers can choose from a range of pre-validated Outposts conﬁgurations (*Figure: Example Outposts architecture*) oﬀering a mix of Amazon EC2 and Amazon EBS capacity designed to meet a variety of application needs. AWS can also work with customers to create a customized conﬁguration designed for their unique application needs.

 To identify the correct conﬁguration, make sure to verify the deployment and operational parameters of the selected physical location for the AWS Outpost rack installation. The following example represents a set of parameters highlighting facility, networking, and power requirements needed for location validation (selected parameter: example value):

 Purchase Option: All Upfront

 Term: 3 Years

 Max on premises power capacity: 20kVA

 Max weight: 2,500lb

 Networking uplink speed: 100Gbps

 Number of Racks: 1

 Average Power Draw per Rack: 9.34

 Constraint (power draw/weight): Power Draw

 Total Outpost vCPU: 480

 Total Outpost Memory: 2,496 GiB

 In addition to minimum parameters, you should make deployment assumptions prior to any order to minimize the performance and security impact on existing infrastructure (selected question: example assumption).

 Question: What is the speed of the uplink ports from your Outposts Network Devices (OND)? Example answer: 40 or 100Gbps.

 Question: How many uplinks per OND will you use to connect the AWS Outpost to your network? Example answer: Four uplinks.

 Question: How will the Outpost service link (the Outpost control plane) access AWS services? Example answer: Service link will access AWS over a Direct Connect public VIF.

 Question: Is there a ﬁrewall between Outposts and the Internet. Example answer: Yes

 Considering these assumptions together with selected components will result in an architecture with a higher granularity of detail and will inﬂuence the overall cost of a hybrid cloud deployment (*Figure AWS Outpost with Amazon EKS Control Plane and Data Plane Architecture*).

![Hybrid cloud architecture deployment example](http://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/images/hybrid-cloud-architecture-deployment-example.png)

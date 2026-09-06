---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hybrid-cloud-best-practices/capacity-planning.html
---

# Capacity planning at the edge
<a name="capacity-planning"></a>

The capacity planning phase involves collecting the vCPU, memory, and storage requirements to deploy your architecture. In the cost optimization pillar of the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html), right-sizing is an ongoing process that starts with planning. You can use AWS tools to define optimizations based on resource consumption within AWS.

Edge capacity planning in Local Zones is the same as in AWS Regions. You should check to make sure that your instances are available in each Local Zone, because some instance types might differ from the types in AWS Regions. For Outposts, you should plan for capacity based on your workload requirements. Outposts are slotted with fixed numbers of instances per host and can be reslotted as needed. If your workloads require spare capacity, take that into consideration when you plan your capacity needs.

## Capacity planning on Outposts
<a name="capacity-outposts"></a>

AWS Outposts capacity planning requires specific inputs for Regional right-sizing, plus edge-specific factors that affect application availability, performance, and growth. For detailed guidance, see [Capacity planning](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/capacity-planning.html) in the AWS whitepaper *AWS Outposts High Availability Design and Architecture Considerations*.

## Capacity planning for Local Zones
<a name="capacity-planning-for-l-zs"></a>

A Local Zone is an extension of an AWS Region that is geographically close to your users. Resources that are created in a Local Zone can serve local users with very low-latency communications. To enable a Local Zone in your AWS account, review [Getting started with AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html) in the AWS documentation. Each Local Zone has different slotting available for families of EC2 instances. Validate the [instances available in each Local Zone](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/) before you use them. To confirm the available EC2 instances, run the following AWS CLI command:

```
aws ec2 describe-instance-type-offerings \
--location-type "availability-zone" \
--filters Name=location,Values=<local-zone-name>
```

Expected output:

```
{
  "InstanceTypeOfferings": [
      {
          "InstanceType": "m5.2xlarge",
          "LocationType": "availability-zone",
          "Location": "<local-zone-name>"
      },
      {
          "InstanceType": "t3.micro",
          "LocationType": "availability-zone",
          "Location": "local.zone-name"
      },
      ...
  ]
}
```

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/hybrid1.html
---

# Public HTTPS egress at the source and private staging area resources
<a name="hybrid1"></a>

The following diagram illustrates the architecture in the hybrid scenario where HTTPS egress traffic is allowed from any source servers and is used to communicate with AWS Transform MGN and Amazon S3 endpoints, whereas the replication data on TCP port 1500 goes over the private channel (AWS VPN or AWS Direct Connect) between the source environment and AWS.

![Application Migration Service communications with public HTTPS and data replication over private channel](http://docs.aws.amazon.com/prescriptive-guidance/latest/rehost-servers-over-private-networks-mgn/images/guide-img/db816b63-918e-424c-861e-0630fc54fedf/images/6cd6b5e0-8d2c-4d21-a256-c7d4b7b20f21.png)

This architecture simplifies the requirements for the staging area subnet, because HTTPS communications from agents don't travel through the private channel. Also, there is no need to create additional Amazon S3 interface VPC endpoints or Amazon Route 53 Profiles inbound resolver endpoints for DNS traffic, because source servers will use their traditional DNS servers to resolve the standard, public DNS names of MGN and Amazon S3 endpoints.

However, in this scenario, staging area subnet resources still run on a private and fully isolated network and have no public access to any HTTPS endpoints, so they need to create both MGN and Amazon EC2 interface endpoints as well as an Amazon S3 gateway endpoint.

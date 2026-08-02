---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html
---

# Properties included in an Amazon ECS service revision
<a name="service-revision-property"></a>

The following properties are included in a service revision.

| Resource | Description |
| --- | --- |
| Service ARN | The ARN that identifies the service. |
| Cluster ARN | The ARN for the cluster that hosts the service. |
| Task definition ARN | The ARN of the task definition used for the service tasks. |
| Service registries | The details for the service registries used for service discovery.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Capacity providers | The capacity provider strategy details.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Container images | The details about the container images. [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Networking | The network configuration for the service.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Launch type | The compute option used for the service. |
| Fargate-specific properties | When using Fargate, this is information about the Fargate version.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Amazon EBS volumes that are configured at deployment | The configuration for a volume specified in the task definition as a volume that is configured at launch time. [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
|  Service Connect | The Service Connect configuration.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Service load balancers | The load balancers that route the service traffic.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |
| Runtime Monitoring | Indicates if Runtime Monitoring is on. |
| Creation date | The date the service revision was created. |
| VPC Lattice | The VPC Lattice configuration for the service revision. |
| Monitoring | The monitoring configuration for the service, which defines the resolution for the service-level `CPUUtilization` and `MemoryUtilization` CloudWatch metrics.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-revision-property.html) |

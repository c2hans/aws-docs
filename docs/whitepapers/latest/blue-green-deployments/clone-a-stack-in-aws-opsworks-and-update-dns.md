---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/clone-a-stack-in-aws-opsworks-and-update-dns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Clone a Stack in AWS OpsWorks and Update DNS
<a name="clone-a-stack-in-aws-opsworks-and-update-dns"></a>

 [AWS OpsWorks](https://aws.amazon.com/opsworks) utilizes the concept of *stacks*, which are logical groupings of AWS resources (EC2 instances, Amazon RDS, Elastic Load Balancing, and so on) that have a common purpose and should be logically managed together. Stacks are made of one or more layers. A layer represents a set of EC2 instances that serve a particular purpose, such as serving applications or hosting a database server. When a data store is part of the stack, you should be aware of certain data management challenges, such as those discussed in the next section.

 To implement this technique in AWS OpsWorks, bring up the blue environment/stack with the current version of the application.

![AWS architecture diagram showing user traffic flow through Route 53, load balancing, and application servers.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/aws-opsworks-stack.png)

* AWS OpsWorks stack *

 Next, create the green environment/stack with the newer version of application. At this point, the green environment is not receiving any traffic. If Elastic Load Balancing needs to be initialized, you can do that at this time.

![Blue-green deployment with Route 53 directing traffic to blue stack while green stack is created.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/clone-stack-to-create-green.png)

* Clone stack to create green environment *

 When it’s time to promote the green environment/stack into production, update DNS records to point to the green environment/stack’s load balancer. You can also do this DNS flip gradually by using the Amazon Route 53 weighted routing policy. This process involves updating DNS, so be aware of DNS issues discussed in the technique in the [Update DNS Routing with Amazon Route 53 section](update-dns-routing-with-amazon-route-53.md).

![Blue stack marked with red X and green stack active, showing DNS routing switch between stacks.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/decommission-blue-stack.png)

* Decommission blue stack *

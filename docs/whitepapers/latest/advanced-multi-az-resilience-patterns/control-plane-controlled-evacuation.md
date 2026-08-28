---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/control-plane-controlled-evacuation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Control plane-controlled evacuation
<a name="control-plane-controlled-evacuation"></a>

 The first pattern uses data plane operations to prevent performing work in an impacted Availability Zone to mitigate the impact of an event. However, you may be using an architecture that doesn’t use load balancers or where configuring a per-host health check isn’t feasible. Or, you may want to prevent new capacity from being deployed into the impacted Availability Zone through Auto Scaling or normal work scheduling.

 To address both situations, control plane actions are required to update the configuration of the resource. The pattern will work for any service whose network configuration can be updated, for example, EC2 Auto Scaling, Amazon ECS, Lambda, and more. It requires writing code for each service, but the business logic follows a standard pattern. The code should be executed locally by an operator responding to the event in order to minimize the dependencies required. The basic flow of the script logic is shown in the following figure.

![Diagram showing control plane update to evacuate an Availability Zone](http://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/control-plane-evacuation.png)

1.  The script lists all of the resources of the specified type, such as Auto Scaling group, ECS service, or Lambda function, and retrieves their subnets from the resource information. The supported resources depend on what the script has been configured to support.

1.  It determines which subnets should be removed by comparing each subnet’s Availability Zone name to its mapped Availability Zone ID that was provided as an input parameter.

1.  The network configuration of the resource is updated to remove the identified subnets.

1.  The details of the update are recorded in a DynamoDB table. The Availability Zone ID is stored as the [partition key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey) and the resource ARN or name is stored as the [sort key](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey). The subnets that were removed are stored as a string array. Finally, the resource type is also stored and used as a hash key for a [Global Secondary Index](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes) (GSI).

 Because step four records the updates that were made, this approach also lends itself to being easily reversible when you’re ready to recover, as shown in the following figure.

![Diagram showing control plane update to recover from Availability Zone evacuation](http://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/images/control-plane-evacuation-recovery.png)

Recovery steps:

1.  Query the GSI to get the subnets removed for each resource of the specified type in the specified Availability Zone (or all Availability Zones if one isn’t specified).

1.  Describe each resource found in the DynamoDB query to get its current network configuration.

1.  Combine the subnets from the current network configuration with those retrieved from the DynamoDB query.

1.  Update the network configuration of the resource with the new subnet set.

1.  Remove the record from the DynamoDB table after the update completes successfully.

 This generalized pattern both prevents routing work to the impacted Availability Zone and prevents new capacity from being deployed there. The following are examples of how this is accomplished for different services.
+  **Lambda** — Update the function’s [VPC configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html) to remove the subnets in the specified Availability Zone.
+  **Auto Scaling Group** — [Remove the subnets from the ASG configuration](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-availability-zone.html#as-remove-az-console) which will replace that capacity in the remaining Availability Zones.
+  **Amazon ECS** — [Update the ECS service VPC configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html) to remove the subnets.
+  **Amazon EKS** — Apply [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to nodes in the impacted Availability Zone to evict existing pods and prevent additional pods from being scheduled there.

 Each service will react differently to the configuration update. For example, Amazon ECS will follow the [service’s deployment configuration after an update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html) and trigger a rolling deployment or blue/green deployment of new tasks.

 These updates may shift work to the healthy Availability Zones too quickly for some workloads. While being configured to be statically stable to the failure (having enough capacity pre-provisioned in the remaining Availability Zones to handle the impacted Availability Zone’s work), you may also want to gradually phase out capacity from the impacted Availability Zone.

**If you plan to update the network configuration of your Auto Scaling group that is a target group for a load balancer with cross-zone load balancing **disabled**, follow this guidance.**
Auto Scaling reacts to this change using its [Availability Zone rebalancing logic](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html). It will launch instances in the other Availability Zones to meet your desired capacity and terminate instances in the Availability Zone you removed. However, the load balancer will continue to split traffic evenly across each Availability Zone, including the one you removed from the ASG, while the instances are being terminated. This could lead to a brown out of the remaining capacity in that Availability Zone until all instances are successfully terminated there. This is the same problem described in *Availability Zone independence* concerning Availability Zone imbalance when cross-zone load balancing is disabled. To prevent this from occurring, you can either:
Always perform your Availability Zone evacuation first so traffic is only being split among the remaining Availability Zones
Specify a [minimum healthy target count with DNS failover](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health.html) to match your required minimum target count for that Availability Zone.
This will help ensure traffic is not sent to the Availability Zone you removed after instances start being terminated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

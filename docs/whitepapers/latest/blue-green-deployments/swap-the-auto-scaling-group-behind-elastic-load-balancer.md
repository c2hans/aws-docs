---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/swap-the-auto-scaling-group-behind-elastic-load-balancer.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Swap the Auto Scaling Group Behind the Elastic Load Balancer
<a name="swap-the-auto-scaling-group-behind-elastic-load-balancer"></a>

 If DNS complexities are prohibitive, consider using load balancing for traffic management to your blue and green environments. This technique uses Auto Scaling to manage the EC2 resources for your blue and green environments, scaling up or down based on actual demand. You can also control the Auto Scaling group size by updating your maximum desired instance counts for your particular group.

 Auto Scaling also integrates with Elastic Load Balancing (ELB), so any new instances are automatically added to the load balancing pool if they pass the health checks governed by the load balancer. ELB tests the health of your registered EC2 instances with a simple ping or a more sophisticated connection attempt or request. Health checks occur at configurable intervals and have defined thresholds to determine whether an instance is identified as healthy or unhealthy. For example, you could have an ELB health check policy that pings port 80 every 20 seconds and, after passing a threshold of 10 successful pings, health check will report the instance as being `InService`. If enough ping requests time out, then the instance is reported to be `OutofService`. With Auto Scaling, an instance that is `OutofService` could be replaced if the Auto Scaling policy dictates. Conversely, for scaled-down activities, the load balancer removes the EC2 instance from the pool and drains current connections before they terminate.

 The following figure shows the environment boundary reduced to the Auto Scaling group. A blue group carries the production load while a green group is staged and deployed with the new code. When it’s time to deploy, you simply attach the green group to the existing load balancer to introduce traffic to the new environment. For HTTP/HTTPS listeners, the load balancer favors the green Auto Scaling group because it uses a least outstanding requests routing algorithm. For more information see, [How Elastic Load Balancing Works](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/how-elb-works.html). You can also control how much traffic is introduced by adjusting the size of your green group up or down.

![Blue-green deployment with traffic shifting from blue Auto Scaling group to green group via load balancer.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/swap-auto-scaling-group.png)

* Swap Auto Scaling group patterns *

 As you scale up the green Auto Scaling group, you can take blue Auto Scaling group instances out of service by either terminating them or putting them in Standby state. For more information see, [Temporarily removing instances from your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html). Standby is a good option because if you need to roll back to the blue environment, you only have to put your [blue server instances back in service](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html) and they're ready to go. As soon as the green group is scaled up without issues, you can decommission the blue group by adjusting the group size to zero. If you need to roll back, detach the load balancer from the green group or reduce the group size of the green group to zero.

![Blue-green deployment with traffic shifting from blue Auto Scaling group to green group.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/blue-auto-scaling-group-nodes.png)

* Blue Auto Scaling group nodes in standby and decommission *

 This pattern’s traffic management capabilities aren’t as granular as the classic DNS, but you could still exercise control through the configuration of the Auto Scaling groups. For example, you could have a larger fleet of smaller instances with finer scaling policies, which would also help control costs of scaling. Because the complexities of DNS are removed, the traffic shift itself is more expedient. In addition, with an already warm load balancer, you can be confident that you’ll have the capacity to support production load.

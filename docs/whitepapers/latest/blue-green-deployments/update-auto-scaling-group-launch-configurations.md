---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/update-auto-scaling-group-launch-configurations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Update Auto Scaling Group launch configurations
<a name="update-auto-scaling-group-launch-configurations"></a>

 A launch configuration contains information like the Amazon Machine Image (AMI) ID, instance type, key pair, one or more security groups, and a block device mapping. Auto Scaling groups have their own launch configurations. You can associate only one launch configuration with an Auto Scaling group at a time, and it can’t be modified after you create it. To change the launch configuration associated with an Auto Scaling group, replace the existing launch configuration with a new one. After a new launch configuration is in place, any new instances that are launched use the new launch configuration parameters, but existing instances are not affected. When Auto Scaling removes instances (referred to as *scaling in*) from the group, the default termination policy is to remove instances with the earliest launch configuration. However, you should know that if the Availability Zones were unbalanced to begin with, then Auto Scaling could remove an instance with a new launch configuration to balance the zones. In such situations, you should have processes in place to compensate for this effect.

 To implement this technique, start with an Auto Scaling group and an Elastic Load Balancing load balancer. The current launch configuration has the blue environment as shown in the following figure.

![AWS architecture diagram showing Auto Scaling group with blue and green launch configs connecting to various AWS services.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/launch-configuration-update.png)

* Launch configuration update pattern *

 To deploy the new version of the application in the green environment, update the Auto Scaling group with the new launch configuration, and then scale the Auto Scaling group to twice its original size.

![AWS architecture diagram showing Auto Scaling group with blue and green launch configurations.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/scale-up-green-launch.png)

* Scale up green launch configuration *

The next step is to shrink the Auto Scaling group back to the original size. By default, instances with the old launch configuration are removed first. You can also utilize a group’s Standby state to [temporarily remove instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html) from an Auto Scaling group. Having the instance in Standby state helps in quick rollbacks, if required. As soon as you’re confident about the newly deployed version of the application, you can permanently remove instances in Standby state.

![AWS architecture diagram showing user traffic flow through Route 53, load balancing, and auto scaling group to various AWS services.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/scale-down-blue-launch.png)

* Scale down blue launch configuration *

 To perform a rollback, update the Auto Scaling group with the old launch configuration. Then, perform the preceding steps in reverse. Or if the instances are in Standby state, bring them back online.

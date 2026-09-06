---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/update-dns-routing-with-amazon-route-53.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Update DNS Routing with Amazon Route 53
<a name="update-dns-routing-with-amazon-route-53"></a>

 DNS routing through record updates is a common approach to blue/green deployments. DNS is used as a mechanism for switching traffic from the blue environment to the green and vice versa when rollback is necessary. This approach works with a wide variety of environment configurations, as long as you can express the endpoint into the environment as a DNS name or IP address.

 Within AWS, this technique applies to environments that are:
+  Single instances, with a public or Elastic IP address
+  Groups of instances behind an Elastic Load Balancing load balancer, or third-party load balancer
+  Instances in an Auto Scaling group with an Elastic Load Balancing load balancer as the front end
+  Services running on an Amazon Elastic Container Service (Amazon ECS) cluster fronted by an Elastic Load Balancing load balancer
+  Elastic Beanstalk environment web tiers
+  Other configurations that expose an IP or DNS endpoint

The following figure shows how Amazon Route 53 manages the DNS hosted zone. By updating the [alias record](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html), you can route traffic from the blue environment to the green environment.

![Blue-green deployment with Route 53 routing traffic from blue to green environment.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/classic-dns.png)

* Classic DNS pattern *

 You can shift traffic all at once or you can do a weighted distribution. For weighted distribution with Amazon Route 53, you can define a percentage of traffic to go to the green environment and gradually update the weights until the green environment carries the full production traffic. This provides the ability to perform canary analysis where a small percentage of production traffic is introduced to a new environment. You can test the new code and monitor for errors, limiting the blast radius if any issues are encountered. It also allows the green environment to scale out to support the full production load if you’re using Elastic Load Balancing(ELB), for example. [ELB automatically scales its request-handling capacity](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) to meet the inbound application traffic; the process of scaling isn’t instant, so we recommend that you test, observe, and understand your traffic patterns. Load balancers can also be pre-warmed (configured for optimum capacity) through a support request.

![Blue-green deployment with Route 53 DNS endpoint directing 80% traffic to blue and 20% to green.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/classic-dns-weighted.png)

* Classic DNS-weighted distribution *

 If issues arise during the deployment, you can roll back by updating the DNS record to shift traffic back to the blue environment. Although DNS routing is simple to implement for blue/green, you should take into consideration how quickly can you complete a rollback. DNS Time to Live (TTL) determines how long clients cache query results. However, with earlier clients and potentially clients that aggressively cache DNS records, certain sessions may still be tied to the previous environment.

 Although rollback can be challenging, this feature has the benefit of enabling a granular transition at your own pace to allow for more substantial testing and for scaling activities. To help manage costs, consider using Auto Scaling instances to scale out the resources based on actual demand. This works well with the gradual shift using Amazon Route 53 weighted distribution. For a full cutover, be sure to tune your Auto Scaling policy to scale as expected and remember that the new Elastic Load Balancing endpoint may need time to scale up as well.

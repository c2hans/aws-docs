---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/ga-request-routing.html
---

# Global Accelerator request routing
<a name="ga-request-routing"></a>

With [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), illustrated in the following diagram, a client looks up the well-known domain name in Route 53. However, instead of getting back an IP address that corresponds to a Regional endpoint, the client gets back an anycast static IP address that routes to the nearest AWS edge location. Starting from that edge location, all traffic gets routed on the private AWS network to some endpoints (Network Load Balancers, Application Load Balancers, EC2 instances, or elastic IP addresses) in a Region chosen by routing rules that are maintained within Global Accelerator. Compared with routing based on Route 53 rules, Global Accelerator request routing has lower latencies because it reduces the amount of traffic on the public internet. In addition, because Global Accelerator doesn't depend on DNS TTL expiration to change routing rules, it can adjust routing more quickly.

![Global Accelerator request routing](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/images/guide-img/a90e395c-d4d5-48a9-a714-90406b23d110/images/da4a0760-d768-4062-b9f4-12589eef97d9.png)

With *write to any Region* mode, or if combined with the compute-layer request routing on the backend, Global Accelerator works seamlessly. The client connects to the nearest edge location and doesn't have to be concerned about which Region receives the request.

With *write to one Region* mode, Global Accelerator routing rules must send requests to the currently active Region. You can use health checks that artificially report a failure on any Region that's not considered by your global system to be the active Region. As with DNS, it's possible to use an alternative DNS domain name for routing read requests, if the requests can be from any Region.

With *write to your Region* mode, it's best to avoid Global Accelerator unless you're also using compute-layer request routing.

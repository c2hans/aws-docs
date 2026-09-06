---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/architecture-selected-by-example-corp.-automotive.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architecture selected by Example Corp. Automotive
<a name="architecture-selected-by-example-corp.-automotive"></a>

 The following diagram illustrates the architecture selected by Example Corp. Automotive after collecting the requirements and navigating the decision trees covered in the previous sections of this whitepaper.

 It uses AWS S2S VPN over the internet terminating on AWS Transit Gateway for development and testing. It then uses AWS Direct Connect with Direct Connect gateway and a second AWS Transit Gateway for the production traffic. AWS Transit Gateway is used for Inter-VPC routing. From a data path perspective, the VPN tunnels for the primary data center are used as primary paths for development and testing, with the tunnels to the secondary data center used as failover paths. For the production traffic, all connections are used simultaneously. Traffic from AWS prefers the most optional network connection based on the data center in which the on-premises system is located. Example Corp. Automotive uses similar route engineering techniques to prefer the appropriate path when traffic is sent to AWS ensuring symmetric traffic paths are used to minimize the use of the corporate network between on-premises primary and secondary data centers.

![Diagram showing Example Corp. Automotive selected hybrid connectivity model](http://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/images/example-hybrid-connectivity-model.png)

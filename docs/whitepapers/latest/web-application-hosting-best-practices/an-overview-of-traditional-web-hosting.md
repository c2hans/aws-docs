---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/an-overview-of-traditional-web-hosting.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# An overview of traditional web hosting
<a name="an-overview-of-traditional-web-hosting"></a>

 Scalable web hosting is a well-known problem space. The following image depicts a traditional web hosting architecture that implements a common three-tier web application model. In this model, the architecture is separated into presentation, application, and persistence layers. Scalability is provided by adding hosts at these layers. The architecture also has built-in performance, failover, and availability features. The traditional web hosting architecture is easily ported to the AWS Cloud with only a few modifications.

![Three-tier web architecture with firewalls, load balancers, web and app server tiers, and data tier with primary and standby databases.](http://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/images/webarchitecture.png)

* A traditional web hosting architecture *

The following sections look at why and how such an architecture should be and could be deployed in the AWS Cloud.

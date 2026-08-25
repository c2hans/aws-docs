---
source_url: https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/swap-the-environment-of-an-elastic-beanstalk-application.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Swap the Environment of an Elastic Beanstalk Application
<a name="swap-the-environment-of-an-elastic-beanstalk-application"></a>

 Elastic Beanstalk enables quick and easier deployment and management of applications without having to worry about the infrastructure that runs those applications. To deploy an application using Elastic Beanstalk, upload an application version in the form of an application bundle (for example, Java `.war` file or `.zip` file), and then provide some information about your application. Based on application information, Elastic Beanstalk deploys the application in the blue environment and provides a URL to access the environment (typically for web server environments).

 Elastic Beanstalk provides several deployment policies that you can configure for use, ranging from policies that perform an in-place update on existing instances, to immutable deployment using a set of new instances. Because Elastic Beanstalk performs an in-place update when you update your application versions, your application may become unavailable to users for a short period of time.

 However, you can avoid this downtime by deploying the new version to a separate environment. The existing environment’s configuration is copied and used to launch the green environment with the new version of the application. The new green environment will have its own URL. When it’s time to promote the green environment to serve production traffic, you can use [Elastic Beanstalk's Swap Environment URLs feature](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html).

 To implement this technique, use Elastic Beanstalk to spin up the blue environment.

![Elastic Beanstalk architecture with Route 53 DNS, load balancer, and auto scaling group.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/elastic-beanstalk-environment.png)

* Elastic Beanstalk environment *

 Elastic Beanstalk provides an environment URL when the application is up and running. The green environment is spun up with its own environment URL. At this time, two environments are up and running, but only the blue environment is serving production traffic.

![Two Elastic Beanstalk environments with load balancers and auto scaling groups behind Route 53.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/prepare-green-elastic.png)

* Prepare green Elastic Beanstalk environment *

 Use the following procedure to promote the green environment to serve production traffic.

1. Navigate to the environment's dashboard in the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk/).

1. In the **Actions** menu, choose **Swap Environment URL.**

   Elastic Beanstalk performs a DNS switch, which typically takes a few minutes. See the [Update DNS Routing with Amazon Route 53](update-dns-routing-with-amazon-route-53.md) section for the factors to consider when performing a DNS switch.

1. Once the DNS changes have propagated, you can terminate the blue environment.

   To perform a rollback, select **Swap Environment URL** again.

![Elastic Beanstalk architecture with Route 53 DNS endpoint routing to two containers in AWS Region.](http://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/images/decommission-blue-elastic.png)

* Decommission blue Elastic Beanstalk environment *

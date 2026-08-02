---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-aspnet-web-services/fig-pattern.html
---

# The strangler fig pattern
<a name="fig-pattern"></a>

The *strangler fig pattern* was introduced by Martin Fowler as a way to manage risk when modernizing or rewriting large, monolithic systems. The pattern is an analogy for a type of plant that begins life as a vine growing alongside an older, established tree. As the vine grows, it spreads to completely consume and ultimately replace the host tree, leaving a new, strangler fig tree in its place. In the context of modernizing ASP.NET web services, this pattern incrementally replaces system functionality by establishing proxies where other systems have dependencies on web services. Initially, you can consider these proxies as having pass-through behavior, because their implementation is fulfilled by the existing monolithic application service. In the natural analog, this is when the strangler fig initially sends a vine up the host tree's trunk. Then, a new service, which is decoupled from the monolith, is created, and the proxy's implementation is deferred to that new service. In the natural analog, this is when the strangler fig vine wraps around one of the tree's branches and overtakes it. This pattern of proxying and then swapping out the proxy implementation with a new service continues until all the legacy system's functions are migrated to new services. At this point, the strangler fig vine completely consumes the tree, and the legacy system can be decommissioned.

Follow these best practices when using the strangler fig pattern, so you can independently scale and deploy your application more smoothly:
+ Select a component that has good test coverage and less technical debt associated with it. Starting with this component can give teams a lot of confidence during the modernization process.
+ Select components that have scalability requirements, and start with one of these components.
+ Select a component that has frequent business requirement changes and frequent deployments.
+ To implement this pattern at scale on AWS, deploy the refactored ASMX services in a Windows container that is running in Amazon Elastic Container Service (Amazon ECS), and publish your modernized REST API by using Amazon API Gateway.

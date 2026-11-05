---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/qualification-strategy-for-life-science-organizations.html
---

# Cloud strategy and planning for life science organizations
<a name="qualification-strategy-for-life-science-organizations"></a>

Life sciences organizations face a critical decision point when adopting cloud technology: how to innovate rapidly while maintaining compliance with stringent GxP regulations. The fundamental challenge lies in transforming from traditional, manual, and document-centric IT processes into what can be termed Regulated Cloud Natives—organizations that operate at the speed of consumer-focused companies while maintaining the quality and compliance standards required by regulatory bodies.

## Three approaches to cloud adoption
<a name="three-approaches-to-cloud-adoption"></a>

**Option 1: Deferring regulatory compliance**

Some organizations attempt to avoid dealing with GxP regulations for as long as possible. While this might be a valid tactic for quickly demonstrating cloud value through small-scale projects, it becomes problematic when extended too long, because retrospectively addressing GxP compliance requires significantly more effort. This approach fails to use the full potential of cloud transformation and can create technical debt that becomes increasingly difficult to remediate.

**Option 2: Extending traditional practices**

Many organizations attempt to simply extend their current ways of working to the cloud, primarily because their existing processes are documented in their quality management system (QMS) and changing them requires significant effort. However, this approach often perpetuates old and inefficient processes that were originally created with very manual controls and haven't evolved as technology and practices have progressed. Organizations taking this route frequently fail to demonstrate the value of cloud and might stall or block further cloud adoption initiatives.

The same basic principles that govern on-premises infrastructure qualification still apply to cloud-based systems. However, replicating on-premises approaches in the cloud without adaptation fails to capture the benefits of cloud-native capabilities and automation.

**Option 3: Becoming regulated cloud natives**

The best approach involves significant transformation to adopt cloud-centered operating practices within a regulated environment where highly regulated customers can operate at a cadence similar to unregulated customers. This approach recognizes that many life sciences organizations constrain themselves with hypercautious interpretations of compliance demands, creating elaborate approval processes that regulatory bodies don't mandate. Tools that aren't directly part of GxP-regulated processes don't require the same level of validation as systems that directly impact product quality or patient safety.

One of the concerns for regulated enterprise customers becomes how to qualify and demonstrate control over a system when so much of the responsibility is now shared with a supplier. Your cloud strategy should directly address this concern. The strategy will employ various tactics to address your regulatory needs.

To better scope the strategy the architecture should be viewed in its entirety. Enterprise scale customers typically define the architecture similar to the following:

![Layered architecture](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/layered-architecture.png)

The preceding diagram illustrates a layered architecture where a large part is delegated to AWS.

From this approach, a strategy can be defined to address four main areas:

1. How to work with AWS as a supplier of services.

1. The qualification of the regulated landing zone.

1. The qualification of building blocks.

1. Supporting the development of GxP applications.

The situation also changes slightly if the customer uses a service provider, like [AWS Managed Services](https://aws.amazon.com/managed-services/), where the build, operation, and maintenance of the landing zone is done by the service provider. Conversely, for workloads that must remain on premises, [AWS Outposts](https://aws.amazon.com/outposts/) extends AWS services including compute, storage, and networking to customer sites. Data can be configured to be stored locally, and customers are responsible for controlling access around AWS Outposts equipment. Data that is processed and stored on premises is accessible over the customer's local network. In this case, customer responsibility extends into the AWS services box, as shown in the following diagram.

![Layered architecture with service provider](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/images/layered-arch-service-provider.png)

In this situation, even more responsibility is delegated by the customer and so the controls that are typically to be put in place by the customer to control their own operations, now need adaptations to check that similar controls are implemented by the service provider. The controls that are inherited from AWS, are shared or that remain with the customer were covered previously in the [Shared Responsibility Model](assessing-aws-as-a-supplier.md#shared-security-responsibility-model) section of this whitepaper.

This section describes these layers at a high level. These layers are expanded upon in later sections of this whitepaper.

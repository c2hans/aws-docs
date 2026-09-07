---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/saas-vs.-managed-service-provider-msp.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS vs. Managed Service Provider (MSP)
<a name="saas-vs.-managed-service-provider-msp"></a>

 There is also some confusion that surrounds the lines between SaaS and the Managed Service Provider (MSP) models. If you look at an MSP model, it can appear to have some similar goals as the SaaS model.

 If you dig a bit more into MSP, however, you’ll find that MSP and SaaS are actually different. The following diagram provides a conceptual view of an MSP environment.

![A diagram depicting the Managed Service Provider (MSP) model.](https://docs.aws.amazon.com/whitepapers/latest/saas-architecture-fundamentals/images/msp-model.png)

 This diagram represents one approach to the MSP model. On the left you’ll see customers that run in the MSP model. Generally, the approach here would be to use whatever automation is available to provision each customer environment, and install the software for that customer.

 On the right is some approximation of the operational footprint that the MSP would provide to support these customer environments.

 It’s important to note that the MSP is often installing and managing a version of the product that a given customer wants to run. All customers could be running the same version, but this is not typically required in an MSP model.

 The general strategy is to simplify the life of a software provider by owning the installation and management of these environments. While this makes life simpler for the provider, it does not map directly to the values and mindset that are essential to a SaaS offering.

 The focus is on offloading the management responsibility. Making that move is not the equivalent of having all customers run on the same version with a single, unified management and operations experience. Instead, MSP often allows for separate versions, and often treats each of these environments as operationally separate.

 There are certainly areas where MSP might begin to overlap with SaaS. If the MSP essentially required all customers to run the same version and the MSP was able to centrally onboard, manage, operation, and bill all the tenants through one experience, that might begin to be more SaaS than MSP.

 The broader theme is that automating the install of environments does not equate to having a SaaS environment. Only when you add all the other caveats previously discussed would this represent more of a true SaaS model.

 If we move back from the technology and operations aspects of this story, the line between MSP and SaaS become even more distinct. Generally, as a SaaS business, the success of your offering relies on your ability to be deeply involved in all the moving parts of the experience.

 This usually means having your finger on the pulse of the onboarding experience, understanding how operational events impact tenants, tracking key metrics and analytics, and being close to your customer. In an MSP model where this is handed over to someone else, you may end up being a level removed from the key details that are core to operating a SaaS business.

---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html
---

# Modules

Modules are components that run inline on your links and act on each bid request as it passes through the link. Depending on the module, it can filter requests, enrich them with additional data, or observe traffic without changing it.

RTB Fabric provides two kinds of modules:
+ Built-in modules for traffic management, such as rate limiting, sampled no-bid responses, and filtering on OpenRTB attributes.
+ Vendor modules from AdTech partners, available through AWS Marketplace, that add partner signals such as invalid traffic detection, device intelligence, inventory quality, and content data. Because vendor modules run inside RTB Fabric, you can use them without building an integration or adding a network call to your bid path.

You attach modules to a link as a *flow*, which sets which modules run on the link's bid requests and in what order.

Built-in modules are available at no additional charge. Vendor modules are billed in two parts: an RTB Fabric fee per invocation, and the vendor's price under your AWS Marketplace agreement. For more information, see [RTB Fabric Pricing](https://aws.amazon.com/rtb-fabric/pricing/).

**Note**
You can configure modules only on active links. Before you configure modules, make sure that both gateways and the link have the `ACTIVE` status.

**Topics**
+ [Discovering and attaching modules](discovering-attaching-modules.md)
+ [Built-in module reference](built-in-modules.md)
+ [Configuring modules with UpdateLinkModuleFlow (legacy)](legacy-update-link-module-flow.md)

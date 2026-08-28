---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/lorawan-networks.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# LoRaWAN networks
<a name="lorawan-networks"></a>

 When architecting an AWS solution based on LoRaWAN connectivity, AWS customers can implement their IoT solutions using public or private LoRaWAN networks.

## Public LoRaWAN networks
<a name="public-lorawan-networks"></a>

 A public LoRaWAN network is used by several customers sharing the same network infrastructure such as LoRaWAN gateways of LoRaWAN network servers. The public LoRaWAN network is operated by a commercial company, although community-owned public LoRaWAN networks exist.

 The network operator designs and maintains necessary gateway infrastructure and LoRaWAN network software components. Some of the providers allow customers to run LoRaWAN application server on the customer’s premises. The LoRaWAN network operator also offers a capability to integrate with customer’s applications.

 Customers of the public LoRaWAN network are entitled to connect their LoRaWAN devices to the network’s network servers through LoRaWAN gateways. After the LoRaWAN device is connected, the data can be exchanges between the LoRaWAN devices and integrates customer’s applications. Using public LoRaWAN networks offers advantages such as reduction of implementation and operation effort and coverage of larger geographic areas.

 Public LoRaWAN networks can be operated as commercial networks and community networks. When using a commercial public LoRaWAN network, the network operator operates and maintains the LoRaWAN gateways and LoRaWAN server components. When using a community public LoRaWAN network, the LoRaWAN gateways are operated and maintained by the members of the community, and the LoRaWAN server components are operated and maintained by the community network operator.

 Using public LoRaWAN networks offers advantages such as reduction of implementation and operation effort, and coverage of larger geographic areas. However, public LoRaWAN networks have limitations. First, customers of commercial public LoRaWAN networks typically have no influence to the positioning and selection of LoRaWAN gateways, which can limit indoor penetration range and make implementation of indoor use cases challenging or impossible. Further considerations to evaluate when selecting if public LoRaWAN network is a right choice are security, and regulatory or cost efficiency requirements. Especially when using community public LoRaWAN networks, additional limitations such as fair-use-policies may apply.

## Private LoRaWAN networks
<a name="private-lorawan-networks"></a>

 A private LoRaWAN network is used by a single enterprise to consume the service themselves or offer the service to their end customers. The enterprise performs hardware selection for and location of LoRaWAN gateways, and controls the network coverage. The enterprise has also a capability to finetune the configuration of a LoRaWAN network for the requirements of the use case.

 A decision for a private deployment mode of LoRaWAN framework is driven by a combination of coverage, mobility, costs, and regulatory and privacy considerations.

 From a coverage standpoint, private LoRaWAN networks can be used in the areas and environments where public LoRaWAN networks do not provide sufficient coverage. Examples include rural areas as well as indoor and underground environments.

 From a mobility standpoint, private LoRaWAN networks are especially beneficial for use cases with either stationary devices or devices having limited range of movement. If your use case requires LoRaWAN network coverage in wide geographical areas (for example, country-wide), a public LoRaWAN network might be a better solution.

 The cost, regulatory, and privacy considerations are not further detailed in this whitepaper.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

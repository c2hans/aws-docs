---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/challenges-with-connected-vehicle-platforms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Challenges with connected vehicle platforms
<a name="challenges-with-connected-vehicle-platforms"></a>

 The customer experience is a key differentiator for OEMs and when it comes to digital technologies, customers expect a fast and responsive user experience. There are some challenges within the automotive landscape to ensure this desired experience is met, including:

 **Scalability** – Massive scalability is required for millions of devices and billions of messages streamed from the vehicles during peak usage. For vehicles, peak demand is morning and evenings, with large periods of limited activity late at night. The platform should be elastic, allowing for expansion and contraction as demand varies, ensuring cost and performance efficiency.

 **Durability** – For fleet operators, connectivity to the cloud is vital portion of their connected vehicle platform. OEMs and fleet operators demand some of the stringent requirements for platform availability and attempt to minimize downtime disruptions from unplanned peaks in demand to ensure revenue and customer experiences are not impacted by these outages.

 **Unreliable networks** – As the vehicles, connected to the cloud via a cellular network, move along in their journey, intermittent connectivity and drops from the network need to be managed by the platform to ensure messages are delivered as required. The communications protocol needs to support use cases around intermittent connectivity.

 **Instantaneous bidirectional communication** – Ensuring the vehicle can receive and execute remote commands in near-real time are vital to the user's experience of interacting with the vehicle's systems, such as unlocking the door or starting the vehicle if a key has been misplaced.

 **Data residency and global availability** – As OEMs continue to expand globally, navigating regulatory requirements like GDPR, CCPA, and UNR 155/156 and ensuring data privacy for their customers is a key concern. Additionally, ensuring the connected vehicle platform can operate at a global scale with local availability of cloud computing as close to the vehicle as possible is vital to the success of a connected vehicle platform.

 **Security** – Securing vehicles requires collaboration across the enterprise. Securing vehicles goes beyond just the vehicle as connectivity proliferates. Security includes all applications and services the vehicle connects to, back-end resources that interact with vehicles, and any other services the vehicle relies on for connectivity. Customers need to consider identity across device, endpoint, and human entities interacting with the vehicle, network and application security of connected applications, detecting and responding to connected vehicle alerts, protecting vehicle data, and compliance.

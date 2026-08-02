---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/securing-iot-with-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Securing Internet of Things (IoT) with AWS
<a name="securing-iot-with-aws"></a>

Publication date: **December 20, 2021** ([Document history](document-revisions.md))

 This whitepaper is a detailed look at how customers can use AWS security services to secure their Internet of Things (IoT) workloads in consumer and industrial environments. This paper is intended for senior-level program owners, decision makers, and security practitioners considering secure enterprise adoption of consumer and industrial IoT (IIoT) solutions.

## Introduction
<a name="introduction"></a>

 IoT technology allows organizations to optimize processes, enhance product offerings, and transform customer experiences in a variety of ways. Although business leaders are excited about the way in which their businesses can benefit from this technology, it is important for them to consider the complexity and security risks associated with deploying IoT solutions. This is due, in part, to a lack of understanding of how to adopt security best practices to the new technologies, as well as a struggle with disparate, incompatible, and sometimes immature security offerings that fail to properly secure deployments, leading to an increased risk for customer or business owner data. This paper provides guidance on how to understand, approach and meet your security, risk and compliance objectives when deploying IoT solutions with AWS.

 Organizations are eager to deliver smart services that can drastically improve the quality of life for populations, business operations and intelligence, quality of care from service providers, smart city resilience, environmental sustainability, and a host of scenarios yet to be imagined. Most recently, AWS has seen an increase in IoT adoption from manufacturing, the healthcare sector and municipalities, with other industries expected to follow in the near term. Many municipalities are early adopters and are taking the lead when it comes to integrating modern technologies, such as IoT. For example:
+  **Kansas City, Missouri** – Kansas City created a unified smart city platform to manage new systems operating along its KC streetcar corridor. Video sensors, pavement sensors, connected street lights, a public Wi-Fi network, and parking and traffic management have supported a 40% reduction in energy costs, $1.7 billion in new downtown development, and 3,247 new residential units.
+  **City of Chicago, Illinois** – Chicago is installing sensors and cameras in intersections to detect pollen count and air quality for its citizens.
+  **City of Catania, Italy** – Catania developed an application to let commuters know where the closest open parking spot is on the way to their destination.
+  **City of Recife, Brazil** – Recife uses tracking devices placed on each waste collection truck and cleaning trolley. The city was able to reduce cleaning costs by $250,000 per month, while improving service reliability and operational efficiency.
+  **City of Newport, Wales, UK** – Newport deployed smart city IoT solutions to improve air quality, flood control, and waste management in just a few months.
+  **Jakarta, Indonesia** – Being a city of 28 million residents that often deals with flooding, Jakarta is harnessing IoT to detect water levels in canals and lowlands, and is using social media to track citizen sentiment. Jakarta is also able to provide early warning and evacuation to targeted neighborhoods so that the government and first responders know which areas are most in need and can coordinate the evacuation process.

 At AWS, security is our highest priority, and this mandate includes supporting AWS IoT services and customers. AWS invests significant resources into ensuring that security is incorporated into every layer of its services, extending that security out to devices with IoT. Helping to protect the confidentiality, integrity, and availability of customer systems and data, while providing a safe, scalable, and secure platform for IoT solutions is a priority for AWS. AWS also provides design principles for deploying IoT securely on AWS. Found in the Security pillar of the [AWS IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html) for the Well-Architected Framework, the design principles are:
+  **Manage device security lifecycle holistically** – Data security starts at the design phase, and ends with the retirement and destruction of the hardware and data. It is important to take a complete approach to the security lifecycle of your IoT solution to maintain your competitive advantage and retain customer trust.
+  **Ensure least privilege permissions** – Devices should all have fine-grained access permissions that limit which topics a device can use for communication. By restricting access, one compromised device will have fewer opportunities to impact any other devices.
+  **Secure device credentials at rest** – Devices should securely store credential information at rest using mechanisms such as a dedicated crypto element or secure flash.
+  **Implement device identity lifecycle management** – Devices maintain a device identity from creation through end of life. A well-designed identity system will keep track of a device’s identity, track the validity of the identity, and proactively extend or revoke IoT permissions over time.
+  **Take a holistic view of data security** – IoT deployments involving a large number of remotely deployed devices present a significant attack surface for data theft and privacy loss. Use a model such as the [Open Trusted Technology Provider Standard](https://en.wikipedia.org/wiki/Open_Trusted_Technology_Provider_Standard) to systemically review your supply chain and solution design for risk and then apply appropriate mitigations.

 Although the IoT Lens provides a checklist and some examples for these design principles, it does not offer prescriptive guidance for securing industrial and consumer IoT applications, which this whitepaper will do.

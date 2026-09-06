---
source_url: https://docs.aws.amazon.com/whitepapers/latest/reactive-systems-on-aws/typical-use-cases-for-reactive-systems.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Typical use-cases for reactive systems
<a name="typical-use-cases-for-reactive-systems"></a>

In the previous section, the essential characteristics of reactive systems was outlined. What do typical use cases for reactive systems have in common? Potentially millions of messages flow into the backend system. The impact of this requirement is a backend system that is able to quickly scale out and is resilient.

 Advertising technology (Ad tech) face an interesting challenge to collect or track a lot of information. Usually this is a tracking pixel on a website that ingests data into a system. Depending on the campaign and its success, the amount of data that needs to be collected and transformed may significantly vary and is not always predictable. The following sections take a closer look at an example implementation for a tracking system for ads.

 For **eCommerce**, it’s a similar situation: if a product goes viral on social media or an advertising campaign is surprisingly successful, a lot of people will visit the eCommerce website and order products.

 For **IoT,** you need to be able to manage millions of connected devices that produce a huge amount of sensor data. This data needs to be collected, stored, and analyzed. Often it is necessary to send additional data back to the connected devices to update the status. The complete system has to be responsive in order to deliver feedback to users or trigger changes in the devices or machines within a short span of time.

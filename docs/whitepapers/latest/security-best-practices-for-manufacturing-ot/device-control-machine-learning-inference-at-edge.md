---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/device-control-machine-learning-inference-at-edge.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Device control / machine learning inference at edge
<a name="device-control-machine-learning-inference-at-edge"></a>

Traditionally, the manufacturing industry has relied on PLCs and industrial software like SCADA / DCS / MES running on-premises for device control and process orchestration or automation. The industry is increasingly adopting cloud technologies to augment these local capabilities.

AI/ML at the edge is one such augmentation. AWS provides a set of tools that make AI/ML readily accessible to any organization. Manufacturers can utilize these advanced tools to solve process control challenges. They can train the model in the cloud and deploy it on the edge to leverage ML for advanced process control. For example, customers can add visual inspection monitored by AI/ML to improve the detection of defects and exceptions.

Process orchestration and control using [AWS IoT Greengrass](https://aws.amazon.com/greengrass/) is another way to augment local control capabilities. Lambda functions and microservices running in docker containers can be deployed via AWS IoT Greengrass. AWS IoT Greengrass provides a centralized way to manage and deploy code from the cloud. This allows you the flexibility to manage code at scale, helping to reduce the dependency for on-site expertise and support. Figure 4 represents an example of process orchestration, as demonstrated in the [“AWS IoT and Industrial Automation at Amazon”](https://www.youtube.com/watch?v=_y9-2VjTw3Y) re:Invent session.

![A diagram showing an example of process orchestration with AWS IoT Greengrass](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/greengrass-process-example.png)

*Example of process orchestration with AWS IoT Greengrass *

[FreeRTOS](https://www.freertos.org/) is a real-time operating system (OS) with built-in libraries to establish a secure connection with AWS services and enable over-the-air updates. It is well suited for industrial control tasks, and as an embedded controller in smart industrial sensors, actuators, pumps, and other components.

In this scenario, the cloud-enabled component could exist in Levels 0-3 of the plant networks. With the ability to write back to the controllers and control industrial equipment, this scenario warrants careful security planning and implementation.

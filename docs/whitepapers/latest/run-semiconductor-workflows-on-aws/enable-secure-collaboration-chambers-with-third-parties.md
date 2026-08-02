---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/enable-secure-collaboration-chambers-with-third-parties.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Enable secure collaboration chambers with third parties
<a name="enable-secure-collaboration-chambers-with-third-parties"></a>

 Across the entire semiconductor industry, the need for collaboration is part of the design process, fabrication, and product manufacturing. AWS allows you to securely collaborate with third-party IP providers, EDA tool vendors, foundries, and contract manufacturers. For example, you might have a requirement to work with a third-party IP provider or contract engineering team to create or validate a portion of your system-on-chip (SoC). Using AWS for collaboration makes it possible to segregate roles and data, lock down the environment to only authorized users, and monitor activity in the environment.

 When trying to create similar collaborative environments in your on-premises data center, you might have the ability to isolate users and groups through existing network policies; however, you are still allowing external access to your internal infrastructure, and the collaboration environment is not scalable. On AWS, you can set up completely separate, secure, and scalable environments that allow you to isolate access to just what is needed for the collaborative effort. This approach can be accomplished in several ways on AWS, but typically starts with a separate [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc) with specific security settings for the level of security and access required. For additional details on VPC settings, see the [Security](security.md) section.

 This section includes three collaboration examples specific to the semiconductor industry:
+  [Collaboration with IP providers and EDA tool vendors (ISVs)](#collaboration-with-ip-providers-and-eda-tool-vendors-isvs)
+  [Collaboration with foundry](#collaboration-with-foundry)
+  [Collaboration with packaging and contract manufactures](#collaboration-with-packaging-and-contract-manufacturers)

 Each of these examples leverages a separate VPC to ensure a secure, isolated chamber that enables fine-grained control that restricts the environment to only the data and applications necessary for that specific project.

## Collaboration with IP providers and EDA tool vendors (ISVs)
<a name="collaboration-with-ip-providers-and-eda-tool-vendors-isvs"></a>

 From customer specifications to silicon, tool vendors and IP providers are a critical part of the entire workflow. Acquiring the latest version of tools and libraries is a manual process, that remains largely unmonitored and untracked.

 The following figure shows a collaboration VPC for test and regressions.

![This image figure shows a collaboration VPC for test and regressions.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-collaboration-ip-isvs.png)

**Collaboration with IP providers and EDA tool vendors (ISVs) **

 In this figure, the collaboration VPC is set up to allow for inbound transfers from both the tool and IP providers. You can allow inbound transfers using any of the [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family) services. This diagram shows [AWS Site-to-Site VPN](https://aws.amazon.com/vpn), [AWS DataSync](https://aws.amazon.com/datasync), and [AWS Transfer for SFTP](https://aws.amazon.com/aws-transfer-family) because these options are typically seen in the semiconductor industry. Once the tool or library is transferred to the Amazon S3 bucket that is in the test and regression VPC, this transfer triggers an [AWS Lambda](https://aws.amazon.com/lambda) function that starts the continuous integration/continuous deployment (CI/CD). One potential example of this workflow is automating IP characterization. When an IP provider sends a new library, characterization is automatically triggered. Regardless of the specific use case (regressions, IP char, software build, and so on), the output data and results are captured and sent to your data lake. This approach ensures data is in the same place for your entire design environment.

## Collaboration with foundry
<a name="collaboration-with-foundry"></a>

 After sending your GDSII file to the foundry, the wafer fabrication process has traditionally been obfuscated from the chip design teams. Launching a separate VPC to enable collaboration with just your foundry can result in robust analytics, a reduction in time-to-market, and increased ROI. The following figure shows the wafer yield analysis from collaboration with your foundry.

![This figure shows the wafer yield analysis from collaboration with your foundry.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-collaboration-foundry.png)

**Collaboration with foundry - wafer yield analysis **

 As shown in the preceding figure, collaboration with your foundry starts with data collection from an AWS IoT board that is installed in the on-premises foundry equipment. The IoT board sends data to [AWS IoT Greengrass](https://aws.amazon.com/greengrass). Using an Edge location, the data is sent to [AWS IoT Core](https://aws.amazon.com/iot-core) located inside the collaboration VPC. In this diagram, the data is used for wafer yield analysis, which should lead to increased yields at the foundry, and help determine if design changes would result in less defects. AWS IoT Greengrass makes it easy to perform machine learning inference locally on devices (located in the foundry), using models that are created, trained, and optimized in the cloud. IoT AWS IoT Greengrass gives you the flexibility to use machine learning models trained in [Amazon SageMaker AI](https://aws.amazon.com/sagemaker) or to bring your own pre-trained model stored in Amazon S3.

 Similar to the collaborative efforts with the IP providers and EDA tool vendors, the resulting wafer data is sent to the same data lake used for the entire semiconductor design workflow.

## Collaboration with packaging and contract manufacturers
<a name="collaboration-with-packaging-and-contract-manufacturers"></a>

 Similar to the way collaboration is enabled with the foundry, you can also enable collaboration with your packaging and contract manufacturers, as well as the devices in the field. The following figure shows the workflow for collaboration with packaging and contract manufacturers.

![This image shows the workflow for collaboration with packaging and contract manufacturers.](http://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-collaboration-packaging.png)

**Collaboration with packaging and contract manufacturers **

 In the preceding figure, data is sent to both AWS IoT Core and AWS IoT SiteWise using an AWS IoT board that is installed in the on-premises manufacturing equipment. [AWS IoT SiteWise](https://aws.amazon.com/iot-sitewise) makes it easy to collect, store, organize, and monitor data from industrial equipment at scale to help you make better, data-driven decisions. From there, machine learning models trained in Amazon SageMaker AI provide real-time inference on the manufacturing floor. Additionally, all incoming data is sent to [Amazon Kinesis](https://aws.amazon.com/kinesis) to stream data to the same data lake that is used throughout the entire environment.

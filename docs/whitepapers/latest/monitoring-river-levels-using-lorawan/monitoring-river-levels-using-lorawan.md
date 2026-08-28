---
source_url: https://docs.aws.amazon.com/whitepapers/latest/monitoring-river-levels-using-lorawan/monitoring-river-levels-using-lorawan.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Monitoring River Levels Using LoRaWAN
<a name="monitoring-river-levels-using-lorawan"></a>

Publication date: **August 10, 2021** ([Document history](document-revisions.md))

 Authorities around the world have the important responsibility of monitoring river and sea levels, so both public institutions and private citizens can be better informed of flood risks. This implementation guide demonstrates how [AWS IoT Core for LoRaWAN](https://aws.amazon.com/iot-core/lorawan/) can be used in conjunction with a qualified gateway device from AWS Advanced Technology Partner Laird Connectivity to install a private [long range wide-area network](https://lora-alliance.org/) (LoRaWAN) capable of collecting environmental monitoring data, such as river levels.

## Overview
<a name="overview"></a>

 Both public and private sector organizations play a crucial role in managing the risk to life and property from flooding. To illustrate the size of the task faced by such authorities, [Flooding in England: national assessment of flood risk](https://www.gov.uk/government/publications/flooding-in-england-national-assessment-of-flood-risk), published by the Environment Agency, identified that one in six properties in England is at risk of flooding. Furthermore, it reported that rising sea levels and increasingly severe and frequent rainstorms caused by climate change mean that the risk of flooding will only increase.

 As part of a comprehensive approach, authorities commonly undertake monitoring of river and sea levels at a finite number of fixed monitoring stations, providing both immediate and longer-term profiling of risk from rising water levels. To facilitate even greater geographical coverage, low-power wide-area networks (LPWAN) technologies such as LoRaWAN give organizations additional flexibility to deploy low-cost, low-power sensors without depending on existing power or telecoms infrastructure.

 This implementation guide demonstrates how [AWS IoT Core for LoRaWAN](https://aws.amazon.com/iot-core/lorawan/) can be leveraged alongside the [Laird Connectivity Sentrius RG1xx LoRaWAN Gateway](https://www.lairdconnect.com/wireless-modules/lorawan-solutions/sentrius-rg1xx-lorawan-gateway-wi-fi-ethernet-optional-lte-us-only) to deploy a private LoRaWAN network capable of collecting environmental sensor readings from a fleet of geographically distributed microcontrollers.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [IoT Lens](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/welcome.html) and [IoT Lens Checklist](https://docs.aws.amazon.com/wellarchitected/latest/iot-lens-checklist/overview.html), we focus on best practices for architecting your IoT applications on AWS.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

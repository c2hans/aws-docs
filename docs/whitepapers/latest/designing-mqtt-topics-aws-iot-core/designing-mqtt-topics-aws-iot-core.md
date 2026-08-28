---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Designing MQTT Topics for AWS IoT Core
<a name="designing-mqtt-topics-aws-iot-core"></a>

Publication date: **December 8, 2021** ([Document History](document-details.md#document-revisions))

## Abstract
<a name="abstract"></a>

This whitepaper focuses on best practices for MQTT topic design in Amazon Web Services (AWS) Internet of Things (IoT). It covers how developing an optimal MQTT topic schema can improve the overall architecture and efficiency of your IoT solutions. It does so by providing greater visibility into cloud to device communication, providing more fine-grained security permissions, and enhancing integration options with other AWS IoT Core services (such as the AWS IoT Rules Engine, AWS IoT Device Shadow, AWS IoT Device Management, and AWS IoT Analytics). This whitepaper is intended for technical architects, IoT cloud engineers, and application architects. This paper assumes that the reader understands fundamental MQTT concepts and terminology.

## Introduction
<a name="introduction"></a>

 AWS IoT Core supports Message Queuing Telemetry Transport (MQTT), a widely adopted lightweight messaging protocol designed for constrained devices. MQTT participants receive information organized through MQTT topics. An MQTT topic acts as a matching mechanism between publishers and subscribers. Conceptually, an MQTT topic behaves like an ephemeral notification channel.

 For AWS IoT, one of the first considerations when using MQTT is the design strategy of your MQTT topics. MQTT topics must balance current device communications, cloud side operations, and future device capabilities. Therefore, it can be challenging to design an ideal MQTT topic structure that creates enough of a schema to enforce least privilege communication but does not create a rigid structure that makes it challenging to support future device deployments.

 This document provides you with MQTT topic design best practices and guidance. It outlines a set of commonly-used MQTT topic structures that can be implemented to solve various device message patterns, then applies several example design patterns using different AWS IoT services.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/overview.html
---

# Overview
<a name="overview"></a>

## Why you need to rethink your observability strategy
<a name="why-observability"></a>

Observability evolved from *monitoring*, which focused on the collection of telemetry signals such as logs, metrics, and traces, to help you debug your applications. Because of this association, observability was often an afterthought and resulted in too much or too little instrumentation, the inability to correlate signals, disconnected visibility, and multiple tools that often did not integrate cohesively. These led to a perceived lack of value and costs that seemed to outweigh the benefits of observability. From a business perspective, these issues meant a longer mean time to identify (MTTI), a longer mean time to recover (MTTR), and a degradation in user experience, trust, brand reputation, and revenue. Observability today is not only about the ability to debug and diagnose an application but also the ability to validate that the application is behaving exactly as intended.

The confluence between businesses that want to provide users with the best experiences and the evolution of observability tooling and features requires a reconsideration and reprioritization of observability.

## Observability tools and frameworks
<a name="tools-frameworks"></a>

Before OpenTelemetry became available in 2019, specialized tools that provided observability solutions for application performance monitoring (APM) and digital experience monitoring (DEM) made the disconnections across the telemetry signals more visible and highlighted poor user experiences.
+ APM tracks and analyzes software application behavior in real time. It measures key metrics such as response times, error rates, and resource usage while monitoring user transactions across application components. APM tools help teams quickly identify performance issues, bottlenecks, and errors before these problems affect users. Their primary goal is to maintain optimal application performance and user experience while reducing the time needed to resolve issues.
+ DEM measures and analyzes the quality of users' interactions with digital services from their perspective. It combines real user monitoring (RUM), synthetic monitoring, and endpoint monitoring to provide a complete view of the user experience. DEM tracks metrics such as page load times, application responsiveness, and user journey completions across different devices, browsers, and locations. This helps organizations understand how users experience their digital services, identify performance issues that affect user satisfaction, and optimize digital touchpoints. The insights enable businesses to make data-driven decisions to improve customer experience and maintain competitive advantage.

The launch of [OpenTelemetry](https://opentelemetry.io/) in 2019  provided an open source, unified standard for generating, collecting, managing, and exporting telemetry data. This framework focuses on bridging the gaps between telemetry signals by adding context, offering better correlation across signals, and providing better derived value. For example, using structured logs with added context helps you derive metrics from the ingested logs and analyze the information in different ways to get to the root cause more quickly. Before OpenTelemetry, signals were viewed in isolation. To add functionality, you had to revise the code to add a new dimension to an existing metric or create a new metric, wait for the code to go through the development lifecycle, and then wait for the metrics to be observed in a suitable environment before you could make deductions. This process delayed visibility and affected your ability to correlate the data to logs or traces if necessary.

The support for OpenTelemetry, and the tooling improvements that stem from this support,  help you derive better value from observability platforms, enhance user experiences, and improve both operational efficiencies and team morale.

If you want to improve and enhance your observability posture, where and how do you actually start? We recommend an approach that consists of three steps, which are discussed in detail in this guide:
+ [Stage 1: Define your North Star](define-north-star.md)
+ [Stage 2: Implement observability](implement-observability.md)
+ [Stage 3: Inspect, adapt, and iterate](inspect-adapt-iterate.md)

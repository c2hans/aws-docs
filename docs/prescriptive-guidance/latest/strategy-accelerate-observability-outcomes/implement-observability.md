---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-observability-outcomes/implement-observability.html
---

# Stage 2: Implement observability
<a name="implement-observability"></a>

At this stage, you start the process for your teams to incrementally work their way to the North Star.

## Choose your observability platform
<a name="platform"></a>

The first step is to identify the right tools to ingest, visualize, and analyze the signals, and to send alerts. When you select a tool, consider its feature set, licensing model, price, skill requirements, and maintenance.

### Feature set
<a name="feature-set.4bdac9e8-589b-544f-96f9-edfba2f5634a"></a>

Here are some of the questions to consider:
+ **Configurability and customization**. Which features does the tool provide to simplify the investigative experience and to help reduce the MTTR? Does the tool provide alarm correlation, metric math, flexibility in handling missing telemetry, or anomaly detection?
+ **Granularity**. What is the supported granularity of telemetry signal ingestion and visualization?
+ **Personas**. Does the tool support the experiences that you want to offer to your developers, platform engineers, and other personas? Does it  work for both technical and business personas?
+ **Widgets**. What kinds of widgets do the dashboards support? Does the tool allow the creation of custom widgets?
+ **Prebuilt solutions**. What kinds of prebuilt observability solutions does the tool offer to reduce the time to value?
+ **Automation and generative AI**. What features does the tool provide that can help automate or reduce toil for you and your team? For example, automatic anomaly detection, predictive analytics, and other generative AI capabilities can help reduce the stress of assumptions and *unknown-unknowns *(that is, things that you're neither aware of nor fully understand). Does the tool support the use of generative AI/ML models to enhance the analysis of the data at scale? Does it provide you with the option to automate and implement AIOps?
+ **Security. **What kinds of authentication and authorization integrations does the tool support? Do the user and login experiences meet the needs of your organization?
+ **OpenTelemetry support.** Do the tool and agent support OpenTelemetry? Most observability platforms support the ingestion of OpenTelemetry-compatible signals, but not all agents provide configuration options to forward these signals to an observability platform.
+ **Integrations.** What integrations does the tool offer? Consider whether you need to send alerts to Slack, page team members, or automate resolution.
+ **Scalability.** How scalable and performant is the tool? The observability solution has to scale as your demands and usage increase, so it can provide diagnoses even if your application is unavailable.
+ **Support.** What support model is offered? Your observability tool has to be available even if your application fails so you can meet your MTTR and application availability targets or service-level agreements (SLAs). Open source solutions might offer limited formal support.

### Licensing and deployment model
<a name="licensing-and-deployment-model.ea5ccc87-25d0-521d-bb39-b6d835c56bb3"></a>

Consider the solution's licensing model (open source or commercial) and deployment model (self-hosted or cloud-based). Open source options often have lower upfront costs but might require more time for deployment, setup and configuration, maintenance, and team upskilling before they provide value. If you are considering open source options, you might need a dedicated team of observability experts. Commercial software typically offers faster time to value with a higher upfront cost, and the need for a dedicated observability team evolves over time as adoption, complexity, and maturity increase. Self-hosted solutions require more time for deployment, setup and configuration, maintenance, and operational overhead in comparison with cloud-based solutions.

### Pricing dimensions
<a name="pricing-dimensions.df6738b9-e90c-5ae9-b4e5-a2700148f921"></a>

How will the tool's pricing model impact your total cost of ownership (TCO) as your application gains new users, a larger architecture footprint, or new features and applications? For example, some typical licensing models are perpetual or based on subscriptions, the number of named users, consumption, or volume. Consider how your application and the observability tool will scale in usage and how the licensing model can impact the cost of the tool.

### Team skills
<a name="team-skills.dda84ec4-7f64-51fe-8539-a453968723d8"></a>

Depending on the current skill set and maturity of your team, you'll need to determine how much upskilling will be required. Consider what kind of support the vendor provides to train your team. Also consider whether your organizational structure supports the configuration and management of the tool that you choose. For example, if you choose OpenTelemetry, you should consider setting up a separate team that specializes in observability.

### Operations and maintenance
<a name="operations-and-maintenance.51efa04d-3a44-5778-9677-43b37b9398fd"></a>

Evaluate the following questions:
+ What deployment options does the observability agent or collector offer? Do those options meet the requirements of your architecture? For example, if you use a containerized deployment for the observability tool, does it support a daemonset or sidecar? What additional steps or tools would the operations team need to take or use to ensure alignment with security and all other processes?
+ What is the effort required to maintain the solution? How simple or automated is the process of updating the agent or collector? Fully managed and cloud-based observability interfaces typically have lower operational overhead compared with self-deployed and hosted applications, although the management of the agent or collector stays the same. Take your team structure into consideration, and factor in the human cost of maintaining the option you choose.

## Instrument your application
<a name="instrumentation"></a>

The answers to the questions in the previous section give you the information you need to instrument your application—that is, to add code to capture telemetry signals to your application and to measure, observe, and validate behaviors. You can use SDKs such as the OpenTelemetry SDK for your application's language to automatically instrument your application. You might still need to add manual instrumentation code to cover any gaps and to ensure end-to-end visibility. Be intentional about the telemetry you add, and make sure that you can connect it back to one or more SLIs and SLOs that you established in the previous stage.

## Collect telemetry
<a name="telemetry"></a>

Configure the telemetry collector or agent to ingest the relevant telemetry signals in alignment with the outcomes that you prioritized in [stage 1](define-north-star.md).

## Implement observability components
<a name="components"></a>

When the telemetry is flowing and ingested into an observability platform, create dashboards, alerts, playbooks, and runbooks.
+ **Dashboards:** Create dashboards that contain relevant information, including a visual representation of current and historical trends associated with your prioritized outcomes. Make these dashboards available to the stakeholders you defined in [stage 1](define-north-star.md). For more information, see [Building dashboards for operational visibility](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/) on the Amazon Builders' Library website.
+ **Alerts:** Define alerts to notify your team when outcomes are at risk or are being breached. Consider adding [alerts for security and performance issues](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.1-automate-alerts-for-security-and-performance-issues.html). Optimize alerts to [reduce alert fatigue](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.9-optimize-alerts-to-prevent-fatigue-and-minimize-monitoring-costs.html) and costs by adopting the following:
  + Use anomaly detection to avoid setting hard thresholds, which require frequent adjustments, and to reduce the occurrence of unknown-unknowns.
  + Use intelligent alert combinations that look at multiple, related metrics together instead of setting up individual alerts for each metric. For example, instead of setting up separate alerts for CPU, memory, and response time, create one meaningful alert that triggers only when these metrics collectively indicate a real problem. This approach significantly reduces alert noise and helps your teams focus on actual service-impacting issues instead of having to respond to isolated metric spikes.
  + Generate alerts only when user experience or outcomes are at risk. For example, avoid getting alerts about a CPU spike that's caused by an automated upgrade when your application has no active users.
+ **Playbooks: **A playbook provides a mental model and context to the person who responds to an incident or alert, and helps them identify the root cause faster. Consider creating playbooks for highly coupled, complex applications and for applications that lack instrumentation but directly impact the outcomes you identified and prioritized in [stage 1](define-north-star.md).
+ **Runbooks: **Use runbooks to define the steps that are required to resolve an incident or alert.

## Validate the observability system
<a name="validation"></a>

Throughout your software development lifecycle (SDLC), validate that dashboards provide the expected behaviors and updates during system tests. Implement [chaos engineering](https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/) and validate the steps that are documented in playbooks and runbooks, to make sure that they are accurate and serve their purpose. You should also validate alert ownership and escalation paths.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

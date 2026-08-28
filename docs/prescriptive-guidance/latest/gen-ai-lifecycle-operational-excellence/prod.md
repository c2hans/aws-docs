---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod.html
---

# GLOE stage 3: Production, deployment, and continuous operation of generative AI applications
<a name="prod"></a>

Moving a generative AI application into production marks a critical transition to real-world value delivery. This stage requires robust systems for deployment, monitoring, and continuous improvement to ensure the application remains reliable, secure, and aligned with business objectives. Rather than viewing production deployment as a destination, organizations must approach it as the beginning of an ongoing optimization journey that includes continuous monitoring. The goal is to make sure that the AI system stays relevant and produces valid results, even as user behaviors evolve, new data patterns emerge, and underlying data distributions gradually drift over time.

The production environment introduces unique challenges that demand specialized operational frameworks. These include detecting and responding to model drift, gathering and acting on user feedback, maintaining security at scale, and establishing governance protocols that address the distinct risks of generative AI systems. Success in this stage requires careful orchestration of technical, operational, and organizational elements to create sustainable systems that consistently deliver business value while managing potential risks.

This chapter is organized into two main sections:
+ [Delivering and sustaining the value of a generative AI application](prod-value.md) – The first section focuses on how to deliver sustained value from generative AI applications in production and how to define success through key business objectives.
+ [Performance monitoring and continuous improvement for generative AI applications](prod-monitoring.md) – The second section describes how to monitor and improve production generative AI applications through performance monitoring, drift detection, feedback loops, and security controls.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

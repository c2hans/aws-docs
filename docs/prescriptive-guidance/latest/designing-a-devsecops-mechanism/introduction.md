---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/introduction.html
---

# Designing a DevSecOps mechanism
<a name="introduction"></a>

*Ryan Griffin, Amazon Web Services*

Organizations are rapidly adopting DevOps and DevSecOps processes for deploying infrastructure. The common patterns often follow a strict binary: [infrastructure as a service](https://aws.amazon.com/what-is/iaas/) (IaaS) compared to [integration platform as a service](https://aws.amazon.com/what-is/ipaas/) (iPaaS). Typically, DevOps mechanism design and implementation follow a similar set of patterns, and there is abundant strategic guidance on [DevOps practices](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html). However, tactical guidance and practical decision-making often rely on the competency of the development team responsible for implementing a DevOps or DevSecOps feature and building the deployment pipeline.

Key questions that arise include:
+ What tools are the team already familiar with?
+ What can be realistically achieved within the expected time frame?

These are important questions, but they are incomplete. This guide seeks to provide additional tactical context for these questions and others. It aims to convert the traditional IaaS and iPaaS binary into more nuanced spectrums for implementation engineers, team leads, directors, and other decision-makers.

Note: This guide provides scenarios that are based on first-hand experiences of large organizations after they implement DevOps mechanisms.

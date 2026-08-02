---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_incident_response_run_game_days.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP07 Run game days
<a name="sec_incident_response_run_game_days"></a>

Game days, also known as simulations or exercises, are internal events that provide a structured opportunity to practice your incident management plans and procedures during a realistic scenario. These events should exercise responders using the same tools and techniques that would be used in a real-world scenario - even mimicking real-world environments. Game days are fundamentally about being prepared and iteratively improving your response capabilities. Some of the reasons you might find value in performing game day activities include:
+ Validating readiness
+ Developing confidence – learning from simulations and training staff
+ Following compliance or contractual obligations
+ Generating artifacts for accreditation
+ Being agile – incremental improvement
+ Becoming faster and improving tools
+ Refining communication and escalation
+ Developing comfort with the rare and the unexpected

For these reasons, the value derived from participating in a simulation activity increases an organization's effectiveness during stressful events. Developing a simulation activity that is both realistic and beneficial can be a difficult exercise. Although testing your procedures or automation that handles well-understood events has certain advantages, it is just as valuable to participate in creative [Security Incident Response Simulations (SIRS)](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/security-incident-response-simulations.html) activities to test yourself against the unexpected and continuously improve.

Create custom simulations tailored to your environment, team, and tools. Find an issue and design your simulation around it. This could be something like a leaked credential, a server communicating with unwanted systems, or a misconfiguration that results in unauthorized exposure. Identify engineers who are familiar with your organization to create the scenario and another group to participate. The scenario should be realistic and challenging enough to be valuable. It should include the opportunity to get hands on with logging, notifications, escalations, and executing runbooks or automation. During the simulation, your responders should exercise their technical and organizational skills, and leaders should be involved to build their incident management skills. At the end of the simulation, celebrate the efforts of the team and look for ways to iterate, repeat, and expand into further simulations.

[AWS has created Incident Response Runbook templates](https://github.com/aws-samples/aws-incident-response-playbooks) that you can use not only to prepare your response efforts, but also as a basis for a simulation. When planning, a simulation can be broken into five phases.

**Evidence gathering: **In this phase, a team will get alerts through various means, such as an internal ticketing system, alerts from monitoring tooling, anonymous tips, or even public news. Teams then start to review infrastructure and application logs to determine the source of the compromise. This step should also involve internal escalations and incident leadership. Once identified, teams move on to containing the incident

**Contain the incident: **Teams will have determined there has been an incident and established the source of the compromise. Teams now should take action to contain it, for example, by disabling compromised credentials, isolating a compute resource, or revoking a role’s permission.

**Eradicate the incident: **Now that they’ve contained the incident, teams will work towards mitigating any vulnerabilities in applications or infrastructure configurations that were susceptible to the compromise. This could include rotating all credentials used for a workload, modifying Access Control Lists (ACLs) or changing network configurations.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Run [game days](https://wa.aws.amazon.com/wat.concept.gameday.en.html): Run simulated [incident](https://wa.aws.amazon.com/wat.concept.incident.en.html) response [events (game days)](https://wa.aws.amazon.com/wat.concept.event.en.html) for different threats that involve key staff and management.
+  Capture lessons learned: Lessons learned from running [game days](https://wa.aws.amazon.com/wat.concept.gameday.en.html) should be part of a feedback loop to improve your processes.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)
+ [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/)

 **Related videos:**
+ [ DIY guide to runbooks, incident reports, and incident response ](https://youtu.be/E1NaYN_fJUo)

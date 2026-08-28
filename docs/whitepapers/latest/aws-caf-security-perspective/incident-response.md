---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/incident-response.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Incident response
<a name="incident-response"></a>

**Note**
 Reduce potential harm by effectively responding to security incidents.

 [Incident Response](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html) (IR), as a structured process to detect, identify, and manage security events, remains largely the same in the cloud. Well-known IR frameworks, such as [NIST SP 800-61 Computer Security Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r2.pdf) and the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html) continue to be effective guides to building and operating IR programs in the cloud. Cloud IR does not exist in isolation. Building and operating an IR capability requires a mesh of security processes and disciplines that span the entirety of the AWS CAF security capability model. In this prescriptive guidance, important dependencies with other security capabilities will be highlighted.

## Start
<a name="incident-response-start"></a>

 **Start with a plan.**

 A written [Incident Response Plan](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_develop_management_plans.html) should define the purpose and response objectives of IR for the organization. Align the response goals to legal and regulatory requirements and the risks to the goals of the organization. Identify both internal stakeholders and important external parties, and establish roles and responsibilities. If you are adapting an existing IR plan to cloud, update the plan to incorporate an understanding of the AWS Shared Responsibility Model. Communicate with stakeholders to educate them on what's different about responding in the cloud.

 **Security governance – inventory *(dependency).***

 Know what is in your cloud environment through continuously [updating and managing your asset inventory](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_pre_deploy_tools.html). Work with security governance teams to help confirm that assets are properly tagged, inventories are up-to-date, and both are [available to incident responders](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_pre_provision_access.html).

 **Prioritize continuous education and training.**

 Incident response is a complex topic, requiring a wide range of technical knowledge about the systems and services that are involved with security incidents. While the incident response process is largely the same in the cloud, you must train your operations and incident response staff on cloud technologies and how your organization uses them.

 **Establish an incident classification framework.**

 Define what a "security incident" is for your organization and develop a method for classifying incidents. A classification framework will assist you in triaging incidents so that both response and preparation activities can be prioritized. You'll be able to collect useful metrics that will help in determining the performance of your incident response program and areas needing improvement. A simple framework may assign incidents to a *category* such as, denial of service, malware, or unauthorized access, along with an impact-based *severity* such as, critical, high, medium, or low. More complex systems may be created that include threat types as well as tactics and techniques. Not having a classification framework in place may result in either over or under reporting of security incidents and lead to inefficiencies as you are unable to easily prioritize your response activities.

 **Build a framework of playbooks.**

 A [playbook](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_playbooks.html) is a written plan for investigating and responding to specific types of incidents. It defines tasks and the detailed procedures for completing them. Start by creating playbooks that focus on specific types of alerts that are common in your environment. Begin with playbooks that capture manual tasks. To discover and capture exception conditions, iterate on the playbook processes to improve the logical flow. The primary aim of the playbook is consistency and repeatability. The [Customer Response Framework](https://github.com/aws-samples/aws-customer-playbook-framework) provides an example framework for customers to create, develop, and integrate security playbooks in preparation for potential attack scenarios when using AWS services. These playbooks can be used as a guide for what detections to build as well as how to effectively respond to each. Continuously manage and expand your playbook library to cover more complex playbooks. The [MITRE ATT&CK](https://attack.mitre.org/) framework can be a useful tool in helping to build playbooks, supporting completeness of investigations, and understanding where you might have gaps in the coverage of your playbooks.

 **Automate responses to incidents.**

 Automation is a force multiplier, which enables your responders to scale efforts to match the organization. It frees up your time to spend improving the security of your cloud environment. For example:
+  [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) automatically collects log data from your AWS resources, and then uses machine learning, statistical analysis, and graph theory to generate visualizations that help you to conduct faster and more efficient security investigations.
+  [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) collects security data across AWS accounts, AWS services, and supported third-party products and helps you analyze your security trends and identify the highest priority security issues.
+  The [Automated Security Response on AWS](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/) solution is an add-on that works with AWS Security Hub CSPM and provides predefined response and remediation actions based on industry compliance standards and best practices for security threats.

 Look for automation opportunities within the incidents you receive frequently. Then, take well-defined and tested manual tasks from your playbooks and [automate them](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_prepare_forensic.html). Start with the most time-consuming tasks first, and build your automation in the cloud in order to match the resilience, scale, and elasticity of your workloads. Your response to incidents should become more frequently expressed as code, either through serverless functions or automatically building response environments through infrastructure code. Start using the security practices of your organization's SDLC and CI/CD pipelines.

 **Implement threat detection *(dependency).***

 The IR team frequently does not directly own detection mechanisms; however, they are critical consumers of them. Many other capabilities in AWS CAF besides threat detection (such as AWS Identity and Access Management, vulnerability management, and data and infrastructure protection) will have detective functions. One of the most significant vulnerabilities in any environment is lack of visibility. Stay connected with these detection capabilities, understand what detections you have, know where the gaps are, and work with your partners in these other areas to improve detection coverage.

## Advance
<a name="incident-response-advance"></a>

 **Define measures and KPIs.**

 Begin by defining incident service level agreements (SLAs). The SLA will form the basis for mean time to respond, an important measurement of performance for the IR program. Introduce additional metrics to further measure performance, such as mean time to detection and mean time to recovery. Regular reporting on these metrics will provide valuable performance data that can help guide IR program improvements and demonstrate effectiveness.

 **Security assurance*(dependency).***

 When developing metrics, measures, and other KPIs or risk indicators, work with security assurance staff. Verify that the data you have about the effectiveness of your cloud IR capability is reported regularly and to the right audience.

 **Incorporate lessons learned into your incident processes.**

 After each security event, establish the practice of learning from what went well, and what could have been better. This step comes *after* returning to normal operations, and should result in a list of improvement actions for IR processes, plans, and playbooks. Some ideas of the kinds of questions you might answer in a *lessons learned* exercise are:
+  **Detection** – Could you improve time to detection? Are there updates to metrics and alarms that would detect the incident sooner?
+  **Diagnosis** – Can you improve the time to diagnosis? Are there updates to your response plans or escalation plans that would engage the correct responders sooner?
+  **Mitigation** – Can you improve the time to mitigation? Are there runbook steps that you could add or improve?
+  **Prevention** – Can you prevent future incidents from occurring? To discover the root causes of an incident, Amazon uses the [5-Whys approach](https://aws.amazon.com/opensearch-service/resources/root-cause-analysis/) in problem investigation.

 To follow through with the implementation of these lessons and assign ownership to the identified tasks, items from lessons learned should be added to a tracked backlog of work.

 **Test your response processes.**

 Periodically test your plans and playbooks with [Security Response Simulations](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/run-regular-simulations.html). Simulations may consist of assembling key IR staff and stakeholders from outside of the IR team, and talking through specific scenarios. Simulations help prepare responders under less stressful conditions so that they may perform better under real conditions. A simulation also details specific response plans and playbooks to validate readiness or expose possible issues. Simulation exercises should likewise conclude with lessons learned, and produce a list of improvement actions to processes, plans, and playbooks.

 **Threat Detection *(dependency).***

 As you consider threat intelligence collection, partner with those responsible for threat detection solutions. These tools may have useful intelligence feeds that come as part of the tool or that can be added for an additional cost. There are both commercial and open source options available for threat intelligence platforms. Choosing the best option for your organization will take a broad understanding of your security technology stack, as well as your IR goals.

## Excel
<a name="incident-response-excel"></a>

 **Integrate your IR processes with a repository of identify indicators of compromise (IoCs), tactics, techniques, and procedures (TTPs) and threat research.**

 Use threat intelligence platforms (TIPs) to aggregate threat data from intelligence feeds, and store in a repository for your own threat data. Create, store, and share IoCs that are relevant to your environment in a centralized repository. This will speed the IR process by improving the accuracy and completeness of investigations. It will enable automated threat analysis using the latest information from threat feeds or collected from a threat analysis. [Amazon GuardDuty](https://aws.amazon.com/guardduty/faqs/) threat intelligence is provided by AWS and third-party providers, such as Proofpoint and CrowdStrike. These threat intelligence feeds are pre-integrated and continuously updated in GuardDuty at no additional cost.

 **Implement threat detection*(dependency)***.

 A Well-Architected logging infrastructure and threat detection model will enable you to [build automated response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_prepare_forensic.html) use cases faster and easier. As you build and improve automated response functions, use response feedback to improve the log data you collect and store, and your protective controls. You will be able to optimize all of the components in your entire security program as you iterate.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

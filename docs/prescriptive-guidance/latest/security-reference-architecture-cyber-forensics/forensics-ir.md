---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-cyber-forensics/forensics-ir.html
---

# Forensics in the context of security incident response
<a name="forensics-ir"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

The incident response (IR) guidance in this section is provided only in the context of forensics and how different services and solutions can improve the IR process.

The [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html) lists best practices for responding to security incidents in the AWS Cloud, based on the experiences of the [AWS Customer Incident Response Team](https://aws.amazon.com/blogs/security/welcoming-the-aws-customer-incident-response-team/) (AWS CIRT). For additional guidance from AWS CIRT, see the [AWS CIRT workshops](https://aws.amazon.com/blogs/security/aws-cirt-announces-the-release-of-five-publicly-available-workshops/) and [lessons from the AWS CIRT](https://aws.amazon.com/blogs/security/two-real-life-examples-of-why-limiting-permissions-works-lessons-from-aws-cirt/).

The [National Institute of Standards and Technology Cybersecurity Framework](https://csrc.nist.gov/pubs/sp/800/61/r2/final) (NIST CSF) defines four steps in the IR lifecycle: preparation; detection and analysis; containment, eradication, and recovery; and post-incident activity. These steps can be implemented sequentially. However, that sequence is often cyclical because some of the steps have to be [repeated after moving to the next step of the cycle](https://docs.aws.amazon.com/security-ir/latest/userguide/introduction.html#incident-response-overview). For example, after containment and eradication, you need to analyze again to confirm that you were successful in removing the adversary from the environment.

This repeated cycle of analysis, containment, eradication, and back to analysis again allows you to gather more information each time new indicators of compromise (IoCs) are detected. Those IoCs are useful from a number of perspectives. They provide you with a story of the steps that were taken by the adversary in order to compromise your environment. Also, by performing proper [post-incident review](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/post-incident-activity.html), you can improve your defenses and detections so that you can prevent the incident in the future or detect the adversary's actions faster and thus reduce the impact of the incident.

Although this IR process isn't the main objective of forensics, many of the tools, techniques, and best practices are shared with IR (especially the analysis step). For example, after the detection of an incident, the forensic collection process gathers the evidence. Next, evidence examination and analysis can help to extract IoCs. At the end, forensic reporting can assist in post-IR activities.

We recommend that you automate the forensic process as much as possible to speed up the response and reduce the load on IR stakeholders. In addition, you can add more automated analyses after the forensic collection process has finished and the evidence has been securely stored to avoid contamination. For more information, see the pattern [Automate incident response and forensics](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-incident-response-and-forensics.html) on the AWS Prescriptive Guidance website.

**Design considerations:**

To improve your security IR preparedness:
+ Enable and securely store logs that might be required during an investigation or incident response.
+ Prebuild queries for known scenarios and provide automated ways to search logs. Consider using Amazon Detective.
+ Prepare your IR tooling by running simulations.
+ Regularly test backup and recovery processes to make sure they are successful.
+ Use scenario-based playbooks, starting with common potential events related to AWS based on Amazon GuardDuty findings. For information about how to build your own playbooks, see the [Playbook resources](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/appendix-b-incident-response-resources.html#playbook-resources) section of the *AWS Security Incident Response Guide*.

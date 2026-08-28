---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/forensic-triage-service.html
---

# Forensic triage service
<a name="forensic-triage-service"></a>

The diagram below represents the logical interaction view of the forensic triage service. A security event (Application security event) is reported by the Threat Detection Engine. The Threat Detection Engine initiates triaging function to determine the severity of threat based on the threat and infrastructure information. The triaging function initiates forensic acquisition and investigation flow for further analysis.

## Interaction view
<a name="interaction-view"></a>

 **Forensic triage workflow**

![forensic triage workflow](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-triage-workflow.png)

## Implementation view
<a name="implementation-view"></a>

 **Forensic triage - implementation view**

![forensic triage implementation view](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-triage-implementation-view.png)

AWS Security Hub operating in AWS application account is reported with details of the compromised instance and the findings get aggregated to AWS Security Hub administrator AWS master Account. . The security administrator initiates one of the following forensic actions in Security Hub.

\+ .. Forensic triage .. Forensic isolation . Amazon EventBridge initiates the *triage* Step Functions flow. . *Get Instance* Lambda function assumes role into compromised application account and retrieves instance information. . The *triage flow* triggers *acquisition flow* in parallel unless the instance tag **IsTriageRequired** is set to `false`.

\+ .. *Forensic memory acquisition flow* initiates the memory acquisition Step Functions. .. *Forensic disk acquisition flow* initiates the disk acquisition Step Functions. . Once completed, the acquisition flow triage results are sent to SNS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

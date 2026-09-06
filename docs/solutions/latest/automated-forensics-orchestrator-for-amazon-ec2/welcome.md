---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/welcome.html
---

# A self-service Guidance to capture and examine data from EC2 instances or EKS clusters and attached volumes for forensic analysis in the event of a potential security issue being detected
<a name="welcome"></a>

Automated Forensics Orchestrator for Amazon EC2 and EKS is a self-service Guidance that customers can deploy to quickly set up and configure a forensics orchestration workflow for their Security Operations Center (SOC). It allows their SOC to capture and examine data from EC2 instances and attached volumes as digital forensics evidence for forensic analysis, in the event a potential security branch. The Guidance currently supports EKS clusters hosted on EC2 instances.

This Guidance provides a framework to orchestrate and automate key forensics processes from the point at which a threat is first detected. This includes isolation of the affected EC2 instances, EKS clusters, data volumes, capture of memory and disk images to secure storage, and initiation of automated actions or tools for investigation and analysis of such artifacts. The Guidance reports findings and provides process notifications. It allows the SOC to continuously discover and analyze patterns of fraudulent activities across multi-account and multi-region environments. The Automated Forensics Orchestrator for Amazon EC2 Guidance leverages AWS services and is underpinned by a highly available, resilient, a serverless architecture, security, and operational monitoring features.

 **Forensic workflow**

![forensic workflow](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/forensic-workflow.png)

Digital forensics is a four-step process of acquisition, isolation, investigation and reporting. The Automated Forensics Orchestrator for Amazon EC2 and EKS Guidance provides the capability to act on security events by imaging or acquisition of breached resources for examination and generating a forensic report about the security breach. In the event of a security breach, it allows customers to automatically capture and store targeted data for forensic examination and analysis, and their SOC to discover and analyze patterns of fraudulent activities. The Guidance supports EC2 instances and EKS clusters on EC2 instances distributed across multiple accounts and regions.

This Guidance is intended for deployment in an enterprise by IT infrastructure and security architects, Incident Response team, security administrators, developers, and SecDevOps professionals who have practical experience with the AWS Cloud.

**Note**
We make no claim as to the suitability of Automated Forensics Orchestrator for Amazon EC2 and EKS in the detection or investigation of crime, nor the ability of data or forensics evidence captured by this Guidance to be used in a court of law. You should independently evaluate the suitability of Automated Forensics Orchestrator for Amazon EC2 and EKS for your use case.

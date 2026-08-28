---
source_url: https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/implementing-iot-security-using-aws-services.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing IoT security using AWS services
<a name="implementing-iot-security-using-aws-services"></a>

 As noted in the previous sections, IoT implementations can have some very unique challenges not present in traditional IT deployments. For example, deploying a consumer IoT device, such as what iRobot has done using AWS to handle scale and spikes, can introduce a new classification of threats to be addressed. Industrial deployments of IoT (IIoT) devices (such as how [SKF](https://aws.amazon.com/solutions/case-studies/skf/) and [Volkswagen](https://aws.amazon.com/solutions/case-studies/volkswagen-group/) have used AWS IoT to optimize its production processes, reduce costs, and provide a better experience to its customers) offer another unique set of security considerations. Lastly, operational technology (OT) or SCADA-based IoT deployments, such as Enel using AWS IoT to get electricity to their customers can require more thought around reliability and anomaly detection. And this is not an exhaustive list. For these use cases there are some common security best practices that can be addressed using AWS services. How enterprises choose to invest in each of these will be based on their risk model.

 The following are 10 best practices to build a secure IoT deployment.

**Topics**
+ [1. Conduct a formal security risk assessment using a common framework](conduct-a-formal-security-risk-assessment.md)
+ [2. Maintain an asset inventory of all IoT assets](maintain-an-asset-inventory-of-all-iot-assets.md)
+ [3. Provision IoT devices and systems with unique identities and credentials](provision-iot-devices-and-systems-with-unique-identities-and-credentials.md)
+ [4. Define appropriate update mechanisms for software and firmware updates.](define-appropriate-update-mechanisms-for-updates.md)
+ [5. Encrypt persistent data at rest](encrypt-persistent-data-at-rest.md)
+ [6. Encrypt all data in transit](encrypt-all-data-in-transit.md)
+ [7. Secure both the IoT environment and supporting IT environments to the same level of criticality](secure-both-the-iot-environment-and-supporting-it-environments.md)
+ [8. Deploy security auditing and monitoring mechanisms across your IoT environment and relevant IT systems.](deploy-security-auditing-and-monitoring.md)
+ [9. Create incident response playbooks, and build automation as your security response matures](create-incident-response-playbooks.md)
+ [10. Create and test business continuity and recovery plans](create-and-test-business-continuity-and-recovery-plans.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

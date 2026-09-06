---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-devops-aws-mainframe-modernization/dev-ops-aws-mainframe-modernization.html
---

# DevOps of AWS Mainframe Modernization
<a name="dev-ops-aws-mainframe-modernization"></a>

Mainframe systems have unique, but common, challenges. Here is how you can extend the DevOps framework to address those unique characteristics:
+ **Legacy technology stack** – Mainframes typically use legacy technology stacks and proprietary software, which can be vastly different from the modern, cloud-native technologies used in DevOps. Integrating these legacy systems into a DevOps pipeline requires specialized tools and expertise.
+ **High complexity** – Mainframe applications tend to be highly complex and monolithic, with extensive interdependencies. Breaking down and modernizing these applications can be more challenging than working with modern, modular code bases. For example, mainframe COBOL applications require a recompile every time, even when there is no change in the program. This is because of their interdependency behavior with copybooks and associated subprograms.
+ **Legacy tooling** – Mainframes often rely on specialized tooling and processes that are not natively compatible with modern DevOps tools. Integration and automation can be more complicated, requiring custom scripts and connectors.
+ **Long release cycles** – Mainframes are known for their long release cycles, which can be a bottleneck in a DevOps context. DevOps for mainframes aims to shorten these cycles while maintaining stability and compliance. Mainframe applications would have a release cycle of 2–3 months, whereas non-mainframe monolith applications could complete theirs in 3–4 weeks. The reason for this is the substantial amount of testing effort needed for evaluating the change request's unaltered interdependent components.
+ **Compliance and security requirements** – Because mainframes are common across markets such as insurance, financials, and healthcare, their applications often handle sensitive data and must adhere to stringent compliance and security standards. The DevOps framework presented in this guide addresses these requirements at every stage of the pipeline.
+ **Skills gap** – There is a skills gap in organizations transitioning from mainframe-centric development and operations to modern DevOps practices. Team members might need training to work effectively in this new environment.
+ **Testing challenges** – Because of the need to emulate the mainframe environment accurately, automated testing in DevOps for mainframes can be complex. Specialized testing tools and frameworks are required. When a COBOL program written on the Z/OS platform is run on the x86 platform (Linux or Windows), compatibility errors are returned. This necessitates the use of suitable toolsets, such as Micro Focus Enterprise Server.
+ **Cultural differences** – Transitioning from a traditional mainframe culture to a DevOps culture can be a significant cultural shift for organizations. DevOps encourages collaboration, automation, and continuous improvement, which might differ from existing practices of mainframe software development lifecycle (SDLC).
+ **Hybrid environments** – Many organizations use a mix of mainframes and modern systems. DevOps for mainframes must integrate seamlessly with these diverse environments.

DevOps in AWS Mainframe Modernization is categorized into three phases: assess, build, and optimize. The following table shows how these phases represent a structured approach to efficiently enable DevOps during the mainframe modernization journey to the AWS Cloud.

|
|
| Phase | Components |
| --- |--- |
| Assess | + Current state analysis+ Target state definition |
| Build | + Toolset configuration+ Continuous integration+ Continuous delivery+ Pipeline orchestration |
| Optimize | + Monitoring and observability enhancements+ Alerting and notification+ Self-healing system |

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/software-bill-of-materials-sbom.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Software Bill of Materials (SBoM)
<a name="software-bill-of-materials-sbom"></a>

 SBoM is a complete, formally structured list of components, libraries and modules that are required to build a given piece of software and the supply chain relationships between them. In the United States, SBoMs are required in government contracts through [Executive Order 14028](https://www.federalregister.gov/documents/2021/05/17/2021-10460/improving-the-nations-cybersecurity).

## Why is SBoM important?
<a name="why-is-sbom-important"></a>

 SBoM serves three main purposes:
+  **Intellectual Property (IP) Management:** IP Management is a process that manages the creations of the mind and human intellect. The main types of IP include but not limited to patents, copyrights, trademarks, trade secrets, and source code. For that reason, export compliance, open-source license compliance and regular audits are core components of the IP Management process.
+  **Software Supply Chain Security:** What goes into your software is quite critical and placing proactive measures avoid managing failures during the production phases. Continuous Vulnerability Management, implementation of End-Of-Life processes for software and building standardized high assurance systems are important steps towards building a Secure Software Supply Chain.
+  **Asset Management:** You cannot manage what you do not see therefore to know and understand what your company has as assets, how they operate and interact individually and with each other is important to make improvements. It is also crucial to monitor and document all the assets to ensure only authorized parts are used to protect the supply chain.

## Software Supply Chain
<a name="software-supply-chain"></a>

 Software Supply Chain represents everything that is part of an application or interacts with it, during the entire software development life cycle (SDLC). It is composed of components, libraries, tools, elements, sources, and processes with subcomponents including but not limited to application dependencies, container (Operating System) packages, application package managers, Operating System package managers, unmanaged source files, unmanaged binaries, and snippets within proprietary code.

 Security Risks towards any of those components will serve as the weakest link to the overall supply chain therefore it is vital to monitor and handle each component vigorously.

 Mitigating all chain threats may not be possible at first but managing the risks and prioritizing them while applying general security practices will have a positive impact to the overall risk. Some of the practices including but not limited to are:
+  Apply least privilege to resources across the software supply chain, enable multi-factor authentication and use strong passwords. Store password in encrypted password vaults and facilitate password-less authentication systems where applicable.
+  Increase employee security awareness with regular trainings, enablement sessions and game days.
+  Continuously monitor, update, and harden your devices. Isolate, prioritize, and maintain systems with critical vulnerabilities.
+  Know, monitor, and assess your suppliers starting with Direct (Tier-1) suppliers and going down the line by covering all of your suppliers.
+  Implement secure coding practices and publish them internally for easy access so that they are used across the board and become as part of a developers’ coding practice.
+  Apply security in every stage of the CI/CD pipeline.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-accelerate-software-dev-lifecycle-gen-ai/generative-ai-capabilities-devsecops.html
---

# Generative AI use cases for DevSecOps
<a name="generative-ai-capabilities-devsecops"></a>

AI-powered DevSecOps tools automate many aspects of the software delivery pipeline. For example, they can perform intelligent code reviews, detect potential bugs, detect security vulnerabilities, and identify performance issues in near real time as developers write code. AI generates and runs comprehensive test suites, and it automatically updates them as the codebase evolves. This AI-augmented approach to DevSecOps accelerates the delivery pipeline and significantly enhances the security and reliability of the software being delivered.

The following table shows DevSecOps use cases that you can enhance with generative AI and the persona responsible for those use cases.

|
|
| **Subcapability: Use case** | **Persona** |
| --- |--- |
| **DevOps and continuous delivery:** Automated entire deployment pipelines | DevOps engineer |
| **DevOps and continuous delivery:** Receive near real-time feedback on code quality and potential issues | Software developer |
| **DevOps and continuous delivery:** Receive near real-time security issues and remediation recommendations | Software developer |
| **DevOps and continuous delivery:** Receive near real-time code and best practice suggestions | Software developer |
| **DevOps and continuous delivery:** Automate repetitive tasks and integrate commands into scripts | DevOps engineer |
| **DevOps and continuous delivery:** Build code and generate artifacts automatically after each code commit | Software developer |
| **DevOps and continuous delivery:** Build code according to the organization's standards and framework | Software developer |
| **DevOps and continuous delivery:** Automatically run unit tests on every commit to catch errors early in the development process | Software developer |
| **DevOps and continuous delivery:** Analyze the coverage of unit tests to make sure that all critical code paths are tested | Software developer |
| **DevOps and continuous delivery:** Manage branches and merge changes | Software developer |
| **DevOps and continuous delivery:** Manage code and artifact versioning | Software developer |
| **DevOps and continuous delivery:** Store and manage build artifacts and dependencies | DevOps engineer |
| **DevOps and continuous delivery:** Resolve and fetch dependencies during the build process | Software developer |
| **DevOps and continuous delivery:** Generate and run integration tests to make sure that components work together as expected | Test engineer |
| **DevOps and continuous delivery:** Use mock services during integration tests to simulate interactions with external systems | Test engineer |
| **DevOps and continuous delivery:** Benchmark application performance under different loads | Performance engineer |
| **DevOps and continuous delivery:** Simulate high-traffic scenarios to test the application's scalability and response times | Performance engineer |
| **DevOps and continuous delivery:** Test the system's ability to recover from failures, such as server crashes or network outages | Site reliability engineer |
| **DevOps and continuous delivery:** Perform chaos engineering | Site reliability engineer |
| **DevOps and continuous delivery:** Run tests to verify that the application meets the business requirements | QA engineer |
| **DevOps and continuous delivery:** Conduct user acceptance testing | Product owner |
| **DevOps and continuous delivery:** Scan dependencies for vulnerabilities and license compliance issues | Security engineer |
| **DevOps and continuous delivery:** Monitor and manage open source dependencies to make sure that they are up to date and secure | Security engineer |
| **DevOps and continuous delivery:** Generate and maintain a software bill of materials (SBOM) to track all components and dependencies | Security engineer |
| **DevOps and continuous delivery:** Use the SBOM to conduct audits for regulatory compliance | Compliance officer |
| **DevOps and continuous delivery:** Create release notes | Release manager |
| **DevOps and continuous delivery:** Plan and coordinate releases | Release manager |
| **DevOps and continuous delivery:** Implement standard operating procedures for rollback and release management | Release manager |
| **DevOps and continuous delivery:** Use feature flags to enable or disable features in production without deploying new code | Product manager |
| **DevOps and continuous delivery:** Run A/B tests using feature flags to measure the impact of different features on user behavior | Product manager |
| **DevOps and continuous delivery:** Analyze and monitor pipeline failures | DevOps engineer |
| **DevOps and continuous delivery:** Create and manage infrastructure resources | DevOps engineer |
| **DevOps and security:** Scan code repositories for hardcoded secrets | DevOps engineer |
| **DevOps and security:** Implement near real-time detection to alert developers immediately if secrets are committed to the repository | DevOps engineer |
| **DevOps and security:** Enforce continuous code quality monitoring | Software developer |
| **DevOps and security:** Detect and flag indicators of potential security vulnerabilities in code | Software developer |
| **DevOps and security:** Implement automated testing for Open Worldwide Application Security Project (OWASP) top 10 security risks to make sure that the application adheres to industry-standard security practices | Security engineer |
| **DevOps and security:** Regularly update and educate developers about OWASP risks by integrating checks into the development process | Security engineer |
| **DevOps and security:** Scan third-party libraries and dependencies for known security vulnerabilities | DevOps engineer |
| **DevOps and security:** Scan application code and infrastructure to detect vulnerabilities | DevOps engineer |
| **DevOps and security:** Analyze code for vulnerabilities before deployment | Security engineer |
| **DevOps and security:** Enforce security policies by preventing code with critical vulnerabilities from being merged | Security engineer |
| **DevOps and security:** Implement role-based access control (RBAC) to restrict access to sensitive systems and data and to make sure that only authorized personnel can access critical resources | Security engineer |
| **DevOps and security:** Adjust access controls based on roles and responsibilities by adapting to changes in the team structure | DevOps engineer |
| **DevOps and security:** Test running applications for security vulnerabilities in near real time by simulating attacks on the production environment | Security engineer |
| **DevOps and security:** Continuously monitor deployed applications for security vulnerabilities | DevOps engineer |
| **DevOps and security:** Schedule regular vulnerability scans across all environments to identify and address security weaknesses | Security engineer |
| **DevOps and security:** Apply patches and updates based on vulnerability scan results to help maintain secure systems | DevOps engineer |
| **Application performance monitoring:** Continuously monitor application performance in near real time to detect and diagnose performance issues before they affect users | Site reliability engineer |
| **Application performance monitoring:** Detect performance anomalies, such as sudden spikes in response times or increased error rates, and initiate alerts | DevOps engineer |
| **Application performance monitoring:** Trace requests as they propagate through a distributed system to identify performance bottlenecks and latency issues | DevOps engineer |
| **Application performance monitoring:** Use distributed tracing to pinpoint the exact service or component that is responsible for failures or performance degradation | DevOps engineer |
| **Log aggregation and analytics:** Aggregate logs from multiple sources into a centralized system for easy searching and analysis in order to identify trends and issues | Site reliability engineer |
| **Log aggregation and analytics:** Implement automated log parsing to extract relevant information and detect patterns or anomalies that might indicate issues | DevOps engineer |
| **Log aggregation and analytics:** Collect and visualize key performance metrics | Site reliability engineer |
| **Log aggregation and analytics:** Monitor metrics against predefined service-level agreements (SLAs) | Product manager |
| **AI operations:** Detect incidents, analyze root causes, and initiate corrective actions without human intervention | DevOps engineer |
| **AI operations:** Predict future resource demands and optimize capacity planning in order to  avoid outages | Site reliability engineer |
| **Continuous improvement:** Monitor real user interactions with the application to gather insights about performance and identify areas for improvement | UX designer |
| **Continuous improvement:** Track application performance across different geographical regions to ensure consistent user experience globally | Product manager |
| **Dashboard monitoring:** Create customizable dashboards to visualize critical metrics, logs, and traces in near real time in order to provide a comprehensive view of system health | Site reliability engineer |
| **Dashboard monitoring:** Create dashboards for different teams (such as development, operations, and product teams) to provide relevant insights based on their focus areas | DevOps engineer |
| **Performance insights:** Conduct detailed analysis of application performance to identify inefficiencies and optimize code or infrastructure | Software developer |
| **Performance insights:** Use performance insights to iteratively improve application performance and optimize the user experience over time | Product manager |

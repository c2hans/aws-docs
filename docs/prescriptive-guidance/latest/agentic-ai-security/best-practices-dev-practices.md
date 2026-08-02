---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-dev-practices.html
---

# 2. Secure development practices for agentic AI systems on AWS
<a name="best-practices-dev-practices"></a>

Agentic AI systems require the same rigorous development practices as traditional applications. However, there are additional considerations for prompt management and AI-specific vulnerabilities.

**This section contains the following best practices:**
+ [2.1 Conduct threat modeling (AI-specific)](#best-practices-2-threat-modeling)
+ [2.2 Treat prompts as code artifacts (AI-specific)](#best-practices-2-prompts-code-artifacts)
+ [2.3 Implement adaptive authentication (AI-specific)](#best-practices-2-adaptive-authentication)
+ [2.4 Implement secure coding standards (General)](#best-practices-2-coding-standards)
+ [2.5 Perform static code analysis and maintain software bill of materials (General)](#best-practices-2-static-code-analysis)
+ [2.6 Enforce Zero Trust principles for all system access (General)](#best-practices-2-zero-trust)
+ [2.7 Balance access control granularity with development efficiency (General)](#best-practices-2-access-control-granularity)

## 2.1 Conduct threat modeling (AI-specific)
<a name="best-practices-2-threat-modeling"></a>

Each agentic AI system has a unique risk profile. Likewise, each organization operates at a unique level of accepted risk. Threat modeling is a critical aspect of system design which must be undertaken with the organization and system context in mind. For more information about the threat modeling process, see the [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html).

Conduct threat modeling during system design to implement mitigations during development. This approach reduces overall development time by identifying security requirements early in the process. You can use specialized tools, such as [Threat Composer](https://github.com/awslabs/threat-composer), to accelerate and scale the threat modeling process. Threat modeling of agentic AI systems should factor in threats that are applicable to traditional distributed systems and those directly related to AI. For more information about common threats to AI systems, see the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/).

## 2.2 Treat prompts as code artifacts (AI-specific)
<a name="best-practices-2-prompts-code-artifacts"></a>

Prompt management throughout the AI solution lifecycle has evolved from an ad-hoc craft into a critical engineering discipline. While the ideal is to manage prompts as rich artefacts in a dedicated registry, many teams find success with a *prompts as code* approach using Git. This method uses existing developer workflows but often creates a bottleneck by excluding non-technical collaborators. The adoption of specialized prompt management platforms is often driven by an organizational need to accelerate development through more inclusive, UI-driven collaboration. The advanced strategy is to move beyond this binary choice and a hybrid model. In this hybrid model, Git serves as the auditable source of truth, and a registry provides the accessible system of engagement.

During the proof-of-concept (PoC) stage, the primary goal is rapid discovery and iteration. Prompts should be managed as formal experiments. This phase involves frequent changes to prompts, models, and configurations. To manage this complexity, use a proper version control system from the outset. Treat each prompt variation as a distinct experiment and track it with its associated metadata. Include the specific model version, configuration parameters like temperature, and the corresponding evaluation results. This disciplined approach creates a reproducible and auditable log of experiments. Teams can systematically compare performance, identify what works, and build an evidence-based foundation for the application.

After a prompt has been validated and proven effective through extensive testing in the PoC stage, the management strategy shifts for the preproduction and production phases. In these later stages, stability and integration with established software development practices are prioritized. The tested and approved prompt can be embedded as a configuration artifact within the application's codebase. This practice is often referred to as *prompts as code*. In this model, prompts are stored in external files, such as YAML or JSON. This separates them from the core application logic but keeps them within the same version control repository. However, you can also embed the prompt into the application logic itself and use Git for version control and management.

This integration means that any modifications to a production prompt are managed through the same developer workflow as any other code change. Use commits and pull requests for version control. This approach ensures that prompts, as critical components of the application, are subject to the same standards of peer review, automated testing, and approval processes before being deployed. This method provides strong governance and a clear audit trail, treating the final, stable prompt with the same importance as the application code it supports.

## 2.3 Implement adaptive authentication (AI-specific)
<a name="best-practices-2-adaptive-authentication"></a>

By design, agents can execute and interact with data sources and with the effective permissions of the authenticated end user through delegation or impersonation. These permission sets may allow for mass export, modification or removal of critical data. Organizations face two perspectives on managing these risks:
+ **Downstream system controls** – Limit the scope of operations when an agent orchestrates the call
+ **Preventive controls** – Prohibit certain operations by agents or humans without additional safeguards

We recommend that you assess [adaptive authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html) (also called *risk-based authentication*) to balance business outcomes with organizational risk tolerance. For these scenarios and other high-risk activities, consider requiring additional authentication factors or implementing a user-approval chain.

## 2.4 Implement secure coding standards (General)
<a name="best-practices-2-coding-standards"></a>

Establish [secure coding standards](https://owasp.org/www-project-developer-guide/) that include [code review processes](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_appsec_manual_code_reviews.html). Insecure application code or incorrect logic can make it easier for a threat actor to move laterally or gain access to confidential data. Consider the adoption of *static application security tooling (SAST)* throughout the development phase to reduce the likelihood of insecure code reaching production. Peer reviews provide additional support to identify security vulnerabilities, logic errors, and potential attack vectors before they reach production environments. Together, these practices provide a solid baseline for your application security posture.

## 2.5 Perform static code analysis and maintain software bill of materials (General)
<a name="best-practices-2-static-code-analysis"></a>

Conduct supply chain inspection through static code analysis (SCA) and maintain software bill of materials (SBOM). Many frameworks commonly used for agentic AI system development are open source, which makes supply chain security critical for system integrity. An up-to-date SBOM can help you determine which application assets might be at risk should an open-source library become compromised. These tools should integrate with Cloud Native Application Protection Platform (CNAPP) capabilities within your organization.

## 2.6 Enforce Zero Trust principles for all system access (General)
<a name="best-practices-2-zero-trust"></a>

Implement [Zero Trust principles](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html) by making sure that tools cannot be called without proper authentication and authorization. This prevents unauthorized access to agentic AI systems. It also ensures that all interactions are properly validated. This becomes even more important as systems form complex interaction patterns across agents with access to varying data and tools.

## 2.7 Balance access control granularity with development efficiency (General)
<a name="best-practices-2-access-control-granularity"></a>

Ensure identity teams are actively involved throughout entitlements and claims definition development. This helps maintain consistency with organizational identity management practices and helps prevent security gaps. Implement access controls with appropriate granularity of claims. Software development should not be overly burdensome, but your organization must maintain an acceptable risk posture. Overly complex or granular access controls can lead to human error through misunderstanding or workarounds that compromise security.

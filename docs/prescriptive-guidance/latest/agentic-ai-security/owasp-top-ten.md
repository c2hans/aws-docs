---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/owasp-top-ten.html
---

# Mapping to OWASP top 10 for LLM applications
<a name="owasp-top-ten"></a>

The following are the suggested control mappings between this guide and the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/).

## LLM01 Prompt injection
<a name="owasp-top-ten-llm01"></a>
+ [1.2 Determine agent scoping](best-practices-system-design.md#best-practices-1-agent-scoping) – Limits the attack surface through agent boundaries
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies injection vectors during design
+ [2.2 Treat prompts as code artifacts](best-practices-dev-practices.md#best-practices-2-prompts-code-artifacts) – Enables prompt review and version control
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies all access attempts
+ [3.2 Use security evaluation suites](best-practices-eval-suites.md#best-practices-3-security-evaluation-suites) – Tests for injection vulnerabilities
+ [4.1 Deploy automated testing suites for prompt validation](best-practices-input-validation.md#best-practices-4-automated-testing-suites) – Validates prompts before execution
+ [4.2 Deploy Amazon Bedrock Guardrails](best-practices-input-validation.md#best-practices-4-bedrock-filters) – Filters malicious input patterns
+ [4.3 Enable prompt logging with metrics](best-practices-input-validation.md#best-practices-4-prompt-logging) – Logs injection attempts for analysis
+ [4.4 Implement multi-layered input sanitization](best-practices-input-validation.md#best-practices-4-input-sanitization) – Sanitizes user inputs
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements proven security patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides layered defense
+ [6.4 Deploy adequate edge protection](best-practices-infrastructure.md#best-practices-6-edge-protection) – Blocks attacks at the perimeter
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects ongoing attacks
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors injection incidents
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans recovery from compromised systems
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores a clean system state

## LLM02 Sensitive information disclosure
<a name="owasp-top-ten-llm02"></a>
+ [1.3 Implement shared memory management](best-practices-system-design.md#best-practices-1-shared-memory) – Isolates sensitive data in memory
+ [1.4 Isolate sessions](best-practices-system-design.md#best-practices-1-isolate-sessions) – Prevents cross-session data leaks
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies data exposure risks
+ [2.3 Implement adaptive authentication](best-practices-dev-practices.md#best-practices-2-adaptive-authentication) – Controls access to sensitive functions
+ [2.6 Enforce Zero Trust principles for all system access](best-practices-dev-practices.md#best-practices-2-zero-trust) – Balances access with security
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies all data access
+ [4.2 Deploy Amazon Bedrock Guardrails](best-practices-input-validation.md#best-practices-4-bedrock-filters) – Blocks sensitive output patterns
+ [5.1 Implement pipelines for fine-tuning data](best-practices-data.md#best-practices-5-data-pipelines) – Controls training data exposure
+ [5.2 Restrict AI operations against sensitive systems](best-practices-data.md#best-practices-5-restrict-ai-operations) – Restricts AI system access to sensitive data
+ [5.3 Establish a data governance framework](best-practices-data.md#best-practices-5-data-governance) – Classifies and protects data
+ [5.4 Prevent data loss](best-practices-data.md#best-practices-5-data-loss) – Prevents data exfiltration
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements data protection patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides multiple protection layers
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects data exposure incidents
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors data access patterns
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to data breaches
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores data protection controls

## LLM03 Supply chain
<a name="owasp-top-ten-llm03"></a>
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies supply chain risks
+ [2.5 Perform static code analysis and maintain software bill of materials](best-practices-dev-practices.md#best-practices-2-static-code-analysis) – Tracks dependencies and vulnerabilities
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies all component access
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements secure architecture patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides defense against compromised components
+ [6.3 Reduce human access to infrastructure](best-practices-infrastructure.md#best-practices-6-human-access) – Reduces human attack vectors
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Monitors for supply chain compromises
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Observes component behavior
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to compromised dependencies
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores a clean component state

## LLM04 Data and model poisoning
<a name="owasp-top-ten-llm04"></a>
+ [1.4 Isolate sessions](best-practices-system-design.md#best-practices-1-isolate-sessions) – Isolates training sessions
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies poisoning attack vectors
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies all data sources
+ [3.1 Conduct model system card reviews](best-practices-eval-suites.md#best-practices-3-model-card-reviews) – Reviews model integrity
+ [5.1 Implement pipelines for fine-tuning data](best-practices-data.md#best-practices-5-data-pipelines) – Curates training data quality
+ [5.3 Establish a data governance framework](best-practices-data.md#best-practices-5-data-governance) – Ensures data integrity
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements secure training patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides multiple validation layers
+ [6.3 Reduce human access to infrastructure](best-practices-infrastructure.md#best-practices-6-human-access) – Reduces manual data manipulation
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects model behavior changes
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors training processes
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to poisoned models
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores a clean model state

## LLM05 Improper output handling
<a name="owasp-top-ten-llm05"></a>
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies output handling risks
+ [2.4 Implement secure coding standards](best-practices-dev-practices.md#best-practices-2-coding-standards) – Implements secure output processing
+ [2.5 Perform static code analysis and maintain software bill of materials](best-practices-dev-practices.md#best-practices-2-static-code-analysis) – Detects vulnerable output code
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies output access controls
+ [4.4 Implement multi-layered input sanitization](best-practices-input-validation.md#best-practices-4-input-sanitization) – Validates output before use
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements secure output patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides layered output validation
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects output handling failures
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors output processing
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to output vulnerabilities
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores secure output handling

## LLM06 Excessive agency
<a name="owasp-top-ten-llm06"></a>
+ [1.1 Use deterministic execution logic unless AI is needed](best-practices-system-design.md#best-practices-1-deterministic-execution-logic) – Limits AI decision-making scope
+ [1.2 Determine agent scoping](best-practices-system-design.md#best-practices-1-agent-scoping) – Constrains agent capabilities
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies over-privileged operations
+ [2.3 Implement adaptive authentication](best-practices-dev-practices.md#best-practices-2-adaptive-authentication) – Verifies user authorization
+ [2.6 Enforce Zero Trust principles for all system access](best-practices-dev-practices.md#best-practices-2-zero-trust) – Appropriately limits system access
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies all privileged operations
+ [5.2 Restrict AI operations against sensitive systems](best-practices-data.md#best-practices-5-restrict-ai-operations) – Restricts AI data operations
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements least-privilege patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides multiple authorization layers
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects unauthorized actions
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors agent behavior
+ [8.2 Establish emergency shutdown capabilities for high-risk scenarios](best-practices-incident-response.md#best-practices-8-emergency-shutdown) – Stops runaway agents
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to agent overreach
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores proper agent constraints

## LLM07 System prompt leakage
<a name="owasp-top-ten-llm07"></a>
+ [1.3 Implement shared memory management](best-practices-system-design.md#best-practices-1-shared-memory) – Protects the system context in memory
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies prompt exposure risks
+ [2.2 Treat prompts as code artifacts](best-practices-dev-practices.md#best-practices-2-prompts-code-artifacts) – Manages prompts as protected assets
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies prompt access controls
+ [4.1 Deploy automated testing suites for prompt validation](best-practices-input-validation.md#best-practices-4-automated-testing-suites) – Tests for prompt extraction
+ [4.3 Enable prompt logging with metrics](best-practices-input-validation.md#best-practices-4-prompt-logging) – Logs prompt access attempts
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements prompt protection patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides layered prompt security
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects prompt extraction attempts
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors prompt access
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to prompt exposure
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores prompt confidentiality

## LLM08 Vector and embedding weakness
<a name="owasp-top-ten-llm08"></a>
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies embedding vulnerabilities
+ [2.4 Implement secure coding standards](best-practices-dev-practices.md#best-practices-2-coding-standards) – Implements secure embedding handling
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies embedding access
+ [3.2 Use security evaluation suites](best-practices-eval-suites.md#best-practices-3-security-evaluation-suites) – Tests embedding security
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements secure embedding patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides layered embedding protection
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects embedding attacks
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors embedding operations
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to embedding compromise
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores embedding integrity

## LLM09 Misinformation
<a name="owasp-top-ten-llm09"></a>
+ [1.1 Use deterministic execution logic unless AI is needed](best-practices-system-design.md#best-practices-1-deterministic-execution-logic) – Uses deterministic logic where possible
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies misinformation risks
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies information sources
+ [3.1 Conduct model system card reviews](best-practices-eval-suites.md#best-practices-3-model-card-reviews) – Reviews model accuracy characteristics
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements accuracy validation patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides multiple validation layers
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects generation of misinformation
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors output accuracy
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to misinformation incidents
+ [8.4 Implement recovery methods within acceptable timeframes](best-practices-incident-response.md#best-practices-8-recovery-methods) – Restores accurate information systems

## LLM10 Unbounded consumption
<a name="owasp-top-ten-llm10"></a>
+ [2.1 Conduct threat modeling](best-practices-dev-practices.md#best-practices-2-threat-modeling) – Identifies resource consumption risks
+ [2.7 Balance access control granularity with development efficiency](best-practices-dev-practices.md#best-practices-2-access-control-granularity) – Verifies resource access controls
+ [6.1 Use the AWS Security Reference Architecture for AI systems](best-practices-infrastructure.md#best-practices-6-sec-ref-arch) – Implements resource management patterns
+ [6.2 Apply defense-in-depth principles](best-practices-infrastructure.md#best-practices-6-defense-in-depth) – Provides layered resource controls
+ [6.4 Deploy adequate edge protection](best-practices-infrastructure.md#best-practices-6-edge-protection) – Implements rate limiting at edge
+ [7.1 Establish continuous security posture management](best-practices-threat-detection.md#best-practices-7-continuous-security-posture-mgmt) – Detects resource abuse
+ [8.1 Implement comprehensive operational observability](best-practices-incident-response.md#best-practices-8-operational-observability) – Monitors resource consumption
+ [8.2 Establish emergency shutdown capabilities for high-risk scenarios](best-practices-incident-response.md#best-practices-8-emergency-shutdown) – Plans emergency shutdown for resource exhaustion
+ [8.3 Maintain business continuity plans for critical operations](best-practices-incident-response.md#best-practices-8-continuity-plans) – Plans response to resource attacks

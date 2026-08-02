---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-security-landscape-genai/threats-and-mitigations.html
---

# Threats and mitigations
<a name="threats-and-mitigations"></a>

 In this section, we discuss the main threats we encountered and mitigation strategies.

## Context window overflow
<a name="context-window-overflow"></a>

 LLMs process a limited amount of information within a fixed context window. Exceeding this limit can cause the model to forget earlier instructions, which adversaries can exploit by flooding the model with excessive or malicious content. This can result in unpredictable system behavior, data leaks, and unauthorized actions.

### Mitigation strategies:
<a name="mitigation-strategies"></a>
+  **Input management.** Limit the size of the input going into the model. Prioritize essential information and sanitize potentially harmful or excessive inputs before they reach the model.
+  **Real-time monitoring.** Use monitoring systems that trigger alerts when the context window is nearing capacity. Proactively manage context overflow by truncating unessential data.

## Agent vulnerabilities
<a name="agent-vulnerabilities"></a>

 Agents extend AI functionality, but are vulnerable to exploitation if not adequately secured. These vulnerabilities can result in unauthorized access, data breaches, and compromised external integrations, which expose sensitive information.

### Mitigation strategies:
<a name="mitigation-strategies-1"></a>
+  **Principle of least privilege.** Implement least privilege for all agents and external integrations to reduce the potential exploit surface.
+  **Regular audits and patching.** Enforce continuous audits, code reviews, and the application of security patches to help protect against known and emerging vulnerabilities.
+  **Agent isolation.** Isolate agents to help prevent them from directly accessing sensitive parts of the system, using sandboxing techniques to minimize the impact of compromised agents.

## Indirect prompt injections
<a name="indirect-prompt-injections"></a>

 Indirect prompt injections occur when adversaries embed malicious commands within seemingly benign user inputs. The AI system might inadvertently execute these instructions, resulting in unauthorized outputs or data manipulation.

### Mitigation strategies:
<a name="mitigation-strategies-2"></a>
+  **Advanced input validation.** Use context-aware input filters to detect and neutralize malicious instructions embedded in user inputs. Traditional methods such as using a WAF do not go far enough. Specialized models trained on potential inputs might be needed to sufficiently mitigate this issue.
+  **Layered defenses.** Implement multi-level checks where inputs are scrutinized at several stages to detect abnormalities.
+  **User education.** Train administrators and users to identify the signs of prompt injections and respond promptly to security breaches.

## Enhance safeguards for adversarial exploits
<a name="enhance-safeguards-for-adversarial-exploits"></a>

 Traditional AI safeguards, such as basic content moderation, struggle against sophisticated exploits that use encoded instructions to bypass filters. This necessitates a rethinking of how AI systems are safeguarded against adversarial exploitation.

### Mitigation strategies:
<a name="mitigation-strategies-3"></a>
+  **Contextual filters.** Go beyond basic keyword detection by using filters that assess the context of inputs to catch more nuanced adversarial techniques.
+  **Adaptive defenses.** Incorporate machine learning-powered filters that continuously learn and adapt to new adversarial techniques.
+  **Defense-in-depth.** Introduce layered security mechanisms, such as refusal classifiers and real-time input monitoring, to fortify AI system integrity.

## Trust and security boundaries
<a name="trust-and-security-boundaries"></a>

 Establishing and managing trust boundaries in AI applications is essential to help prevent unauthorized access and safeguard sensitive data. Rigorous data flow analysis can identify weak points where sensitive information could be inadvertently exposed.

### Best practices:
<a name="best-practices"></a>
+  **Data classification.** Make sure that your data has been properly classified according to sensitivity.
+  **Data flow mapping.** Conduct comprehensive analyses of data flows from input to output to make sure that sensitive data is appropriately safeguarded.
+  **Principle of least privilege.** Make sure that users, agents, and external integrations have the minimal access rights required for their tasks.
+  **Secure APIs.** Secure API endpoints through robust authentication, authorization, and continuous input validation.
+  **Data hygiene.** Introduce standard operating procedures for cleaning and validating data.

## Design AI systems for reliability
<a name="design-ai-systems-for-reliability"></a>

 LLMs, despite their efficiency, can introduce reliability risks that should be addressed up front. Designing systems to minimize risks such as model failures or adversary-controlled outputs should be a key design consideration.

### Strategies for resilience:
<a name="strategies-for-resilience"></a>
+  **Modular architecture.** Adopt a modular system architecture that decouples critical components, allowing isolation of faults and failures.
+  **Validation layers.** Use multiple validation layers to assess model outputs for plausibility and consistency before they reach end users.
+  **Human oversight.** Implement human-in-the-loop systems for reviewing critical decisions and low-confidence outputs to reduce potential errors.

## Isolate sensitive data from AI models
<a name="isolate-sensitive-data-from-ai-models"></a>

 Generative AI systems, particularly LLMs, are at risk for data extraction and leakage, especially when handling sensitive information. Implementing strict data isolation strategies is crucial to help prevent confidential information from being exposed through prompts or model outputs.

### Data isolation strategies:
<a name="data-isolation-strategies"></a>
+  **Data minimization.** Limit the data exposed to the model, providing only what is necessary for the task at hand.
+  **Differential privacy.** Employ differential privacy techniques to make sure that sensitive data cannot be reconstructed from model outputs.
+  **Secure prompt engineering.** Do not include sensitive data in prompts, and verify secure data handling by third-party services.
+  **Use Retrieval Augmented Generation (RAG).** Use RAG with strong AuthZ and AuthN to augment model data over fine tuning.

## Minimize data leaks from overprivileged agents, logging, and caching
<a name="minimize-data-leaks-from-overprivileged-agents-logging-and-caching"></a>

 Overprivileged agents and improper handling of logs or cached data can lead to serious security breaches, allowing adversaries to access sensitive information or manipulate outputs.

### Preventive measures:
<a name="preventive-measures"></a>
+  **Access control.** Limit agent access using strict role-based access control (RBAC).
+  **Anonymized logging.** Make sure that logs do not inadvertently capture sensitive information. Use anonymization techniques when necessary.
+  **Secure caching.** Encrypt cached data and enforce strict expiration policies to help prevent unauthorized access to sensitive cached information.

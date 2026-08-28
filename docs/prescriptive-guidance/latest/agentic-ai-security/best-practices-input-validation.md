---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-input-validation.html
---

# 4. Input validation and guardrails for agentic AI systems on AWS
<a name="best-practices-input-validation"></a>

User inputs represent the primary attack vector for agentic AI systems through prompt injection and manipulation techniques. Multi-layered validation that combines application-level sanitization with model-level guardrails helps defend against malicious inputs.

**This section contains the following best practices:**
+ [4.1 Deploy automated testing suites for prompt validation (AI-specific)](#best-practices-4-automated-testing-suites)
+ [4.2 Deploy Amazon Bedrock Guardrails (AI-specific)](#best-practices-4-bedrock-filters)
+ [4.3 Enable prompt logging with metrics (AI-specific)](#best-practices-4-prompt-logging)
+ [4.4 Implement multi-layered input sanitization (General)](#best-practices-4-input-sanitization)

## 4.1 Deploy automated testing suites for prompt validation (AI-specific)
<a name="best-practices-4-automated-testing-suites"></a>

Use suitable test suites to assess agentic AI systems against various prompt types that range from potentially harmful to valid user inputs. For an example, see [Align and monitor your Amazon Bedrock powered insurance assistance chatbot to responsible AI principles with AWS Audit Manager](https://aws.amazon.com/blogs/machine-learning/align-and-monitor-your-amazon-bedrock-powered-insurance-assistance-chatbot-to-responsible-ai-principles-with-aws-audit-manager/) (AWS blog post). You can use tools, such as [promptfoo](https://www.promptfoo.dev/), to test prompt injection attacks, jailbreaking attempts, and adversarial inputs that could compromise agent behavior or bypass security controls. Each system configuration change or release should be assessed by using standardized test datasets that include both benign user scenarios and malicious attack vectors. Malicious attempts include role confusion, context manipulation, and privilege escalation.

Outputs from the tests should be catalogued for benchmarking because system behavior might change with LLM and application updates. Establish baseline security metrics, including prompt injection detection rates, false positive thresholds, and response consistency scores. These metrics can help you identify security posture regressions. Implement continuous testing pipelines that automatically run security-focused prompt evaluations during development cycles. This validates that new features or model updates don't introduce vulnerabilities. Additionally, maintain separate test suites for different risk scenarios, including multi-turn conversation attacks, context poisoning attempts, and cross-agent prompt propagation exploits. These exploits might compromise the entire agentic AI system through coordinated manipulation.

## 4.2 Deploy Amazon Bedrock Guardrails (AI-specific)
<a name="best-practices-4-bedrock-filters"></a>

The AWS Well-Architected Framework recommends that you [sanitize and validate user inputs to foundation models](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec04-bp02.html). Deploy [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) for all Amazon Bedrock invocations in order to provide filtering capabilities that support AI safety and responsibility. For more information, see [Build responsible AI applications with Guardrails for Amazon Bedrock](https://www.youtube.com/watch?v=DvvypUqdjXo) (YouTube). Enable the [prompt attack filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html) as an essential requirement. These filters specifically target prompt-injection techniques. Amazon Bedrock Guardrails can be a highly effective preventative control for prompt injection attacks; however, you can enhance it by adopting defense-in-depth practices and applying layered controls.

## 4.3 Enable prompt logging with metrics (AI-specific)
<a name="best-practices-4-prompt-logging"></a>

Enable prompt logging and establish metrics to monitor masking and blocking events in Amazon Bedrock Guardrails. For more information, see [Monitor Amazon Bedrock Guardrails using CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html). Identify opportunities for continuous improvement by monitoring metrics. This can reveal previously unidentified trends or risks that require attention. As an example, an identified upward trend in `GuardrailPolicyType` of `SensitiveInformationPolicy` might indicate a threat actor who is trying to manipulate system behavior. In turn, you might adopt a different type of guardrail or logical control to address that specific threat.

## 4.4 Implement multi-layered input sanitization (General)
<a name="best-practices-4-input-sanitization"></a>

Sanitize and normalize user inputs by using application code logic prior to sending inputs to inference engines. While prompts and guardrails reduce the likelihood of successful prompt-injection attacks, systems should not rely on these defenses alone. [Input sanitization](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensec04-bp02.html) should remove unnecessary Unicode characters and unusual or unexpected text patterns and phrases that provide direction to ignore inputs or directives. Prompt obfuscation is a well-known tactic to hide text used in prompt-injection and data-poisoning attacks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

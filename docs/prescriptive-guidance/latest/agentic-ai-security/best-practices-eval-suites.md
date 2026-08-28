---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices-eval-suites.html
---

# 3. Security evaluation suites for agentic AI systems on AWS
<a name="best-practices-eval-suites"></a>

Foundation models form the intelligence core of agentic AI systems. This makes their security characteristics critical to overall system safety. Systematic evaluation and testing of model behavior can help you identify vulnerabilities before deployment.

**This section contains the following best practices:**
+ [3.1 Conduct model system card reviews (AI-specific)](#best-practices-3-model-card-reviews)
+ [3.2 Use security evaluation suites (AI-specific)](#best-practices-3-security-evaluation-suites)

## 3.1 Conduct model system card reviews (AI-specific)
<a name="best-practices-3-model-card-reviews"></a>

Review [model system cards](https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/) thoroughly to understand the security posture, documented safeguards, and known limitations before deployment. *System cards* describe how models handle adversarial inputs and inappropriate requests. Examine documented results for adversarial safety measures and cyber evaluations. These assessments indicate model resilience against attack patterns and help you determine additional control requirements. This information is essential for risk assessment and determining additional security controls for your specific use case. Understanding baseline model security capabilities informs your overall security architecture decisions.

## 3.2 Use security evaluation suites (AI-specific)
<a name="best-practices-3-security-evaluation-suites"></a>

Use model evaluation tools to probe your AI application with adversarial prompts that are designed to elicit security vulnerabilities or responsible AI failures. This [systematic testing approach](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto.html) identifies potential vulnerabilities, such as:
+ Attempts to extract environment variables or credentials from the model
+ Prompts designed to generate malicious code or exploits
+ Information leakage of training data or sensitive information

Libraries and tools to support model evaluation include [fmeval](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib.html) and [SecEval](https://xuanwuai.github.io/SecEval/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp04.html
---

# RAISP02-BP04 Build security protections directly into the core AI system design
<a name="raisp02-bp04"></a>

 Follow "secure by design" and "defense in depth" principles and build security protections into your system from the beginning to protect your system and maintain its intended operation. This means incorporating safeguards like access controls, input validation and sanitization to defend against prompt injections, and robust techniques to mitigate attempts at jailbreaking or bypassing your system's safety guardrails. The specific security measures you choose should directly address the security requirements in your release criteria.

 **Level of risk exposed if this best practice is not established:** High

## Implementation considerations
<a name="implementation-considerations-67"></a>

1.  Build input validation into your model's core processing by checking inputs for unwanted patterns, prompt injections, and attempts to manipulate system behavior. Create filters that detect and block unwanted patterns such as instruction overrides, data extraction attempts, and jailbreaking prompts before they reach your model.

1.  Design access controls directly into your system architecture by requiring authentications for each interaction, limiting what different user types can access, and restricting administrative functions to authorized personnel only. Set up role-based permissions that block unauthorized users from accessing sensitive model capabilities or training data.

1.  Build adversarial robustness into your model by training it to resist attempts to manipulate its outputs through crafted inputs. Include adversarial examples in your training data and design your model architecture to be stable when faced with inputs designed to cause harmful or unexpected behavior.

## Resources
<a name="resources-64"></a>

 **Related documents:**
+  [Detect and filter harmful content by using Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
+  [ISO/IEC 42001:2023 A.6.1.2 Objectives for responsible development of AI system](https://www.iso.org/standard/42001)

 **Related tools**
+  [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

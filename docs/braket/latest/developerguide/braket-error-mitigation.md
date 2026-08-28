---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-error-mitigation.html
---

# Error mitigation techniques
<a name="braket-error-mitigation"></a>

Quantum error mitigation is a set of techniques aimed at reducing the effects of errors in quantum computers.

Quantum devices are subject to environmental noise that degrades the quality of computations performed. While fault-tolerant quantum computing promises a solution to this problem, current quantum devices are limited by the number of qubits and relatively high error rates. To combat this in the near-term, researchers are investigating methods to improve the accuracy of noisy quantum computation. This approach, known as *quantum error mitigation*, involves using various techniques to extract the best signal from noisy measurement data.

**Topics**
+ [Error mitigation techniques on IonQ devices](error-mitigation-ionq.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

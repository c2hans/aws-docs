---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-local-mode.html
---

# Create and debug a hybrid job with local mode
<a name="braket-jobs-local-mode"></a>

When you are building a new hybrid algorithm, local mode helps you to debug and test your algorithm script. Local mode is a feature that allows you to run code you plan to use in Amazon Braket Hybrid Jobs, but without needing Braket to manage the infrastructure for running the hybrid job. Instead, run hybrid jobs locally on your Amazon Braket Notebook instance or on a preferred client, such as a laptop or desktop computer.

In local mode, you can still send quantum tasks to actual devices, but you do not get the performance benefits when running against an actual Quantum processing unit (QPU) while in local mode.

To use local mode, modify `AwsQuantumJob` to `LocalQuantumJob` wherever it occurs inside of your program. For instance, to run the example from [Create your first hybrid job](braket-jobs-first.md), edit the hybrid job script in the code as follows.

```
from braket.jobs.local import LocalQuantumJob

job = LocalQuantumJob.create(
    device="arn:aws:braket:::device/quantum-simulator/amazon/sv1",
    source_module="algorithm_script.py",
    entry_point="algorithm_script:start_here",
)
```

**Note**
Docker, which is already pre-installed in the Amazon Braket notebooks, needs to be installed in your local environment to use this feature. Instructions for installing Docker can be found on the [Get Docker](https://docs.docker.com/get-started/get-docker/) page. In addition, not all parameters are supported in local mode.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

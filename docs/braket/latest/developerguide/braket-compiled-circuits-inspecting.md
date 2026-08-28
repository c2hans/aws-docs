---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-compiled-circuits-inspecting.html
---

# Inspecting compiled circuits
<a name="braket-compiled-circuits-inspecting"></a>

When a quantum circuit needs to be run on a hardware device, such as a quantum processing unit (QPU), the circuit must first be compiled into an acceptable format that the device can understand and process. For example, transpiling the high-level quantum circuit down to the specific native gates supported by the target QPU hardware. Inspecting the actual compiled output of the quantum circuit can be extremely useful for debugging and optimization purposes. This knowledge can help identify potential issues, bottlenecks, or opportunities for improving the performance and efficiency of the quantum application. You can view and analyze the compiled output of your quantum circuits for both Rigetti and IQM quantum computing devices using the code provided below.

```
task = AwsQuantumTask(arn=task_id, aws_session=session)
# After the task has finished running
task_result = task.result()
compiled_circuit = task_result.get_compiled_circuit()
```

**Note**
Currently, viewing the compiled circuit output for IonQ devices is not supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

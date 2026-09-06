---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/performance-considerations.html
---

# Performance considerations
<a name="performance-considerations"></a>

 **SSM command timeout**

For memory acquisition, memory investigation, and disk investigation SSM documents are leveraged. The timeout is set to 4,000 seconds by default. You can modify the value based on the type of compromised instance. For more details, refer to the following documentation:
+  [Handling timeouts in runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-handling-timeouts.html)
+  [Understanding command statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html)

 **Compromised instance memory size and investigation instance mount disk volume**

The investigation instance mount volume must always be greater than the memory of the compromised instance. This ensures that memory loaded into investigation instance does not error out. The Guidance uses `M5.2Xlarge` Amazon EC2 instance type by default.

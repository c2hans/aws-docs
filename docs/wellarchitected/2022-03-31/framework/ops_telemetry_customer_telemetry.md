---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_telemetry_customer_telemetry.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS04-BP03 Implement user activity telemetry
<a name="ops_telemetry_customer_telemetry"></a>

 Instrument your application code to emit information about user activity, for example, click streams, or started, abandoned, and completed transactions. Use this information to help understand how the application is used, patterns of usage, and to determine when a response is required.

 **Common anti-patterns:**
+  Your developers have deployed a new feature without user telemetry, and utilization has increased. You cannot determine if the increased utilization is from use of the new feature, or is an issue introduced with the new code.
+  Your developers have deployed a new feature without user telemetry. You cannot tell if your customers are using it without reaching out and asking them.

 **Benefits of establishing this best practice:** Understand how your customers use your application to identify patterns of usage, unexpected behaviors, and to enable you to respond if necessary.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement user activity telemetry: Design your application code to emit information about user activity (for example, click streams, or started, abandoned, and completed transactions). Use this information to help understand how the application is used, patterns of usage, and to determine when a response is required.

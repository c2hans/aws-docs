---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_operations_health_ops_metric_baselines.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP04 Establish operations metrics baselines
<a name="ops_operations_health_ops_metric_baselines"></a>

 Establish baselines for metrics to provide expected values as the basis for comparison and identification of under and over performing operations activities.

 **Common anti-patterns:**
+  You have been asked what the expected time to deploy is. You have not measured how long it takes to deploy and can not determine expected times.
+  You have been asked what how long it takes to recover from an issue with the application servers. You have no information about time to recovery from first customer contact. You have no information about time to recovery from first identification of an issue through monitoring.
+  You have been asked how many support personnel are required over the weekend. You have no idea how many support cases are typical over a weekend and can not provide an estimate.
+  You have a recovery time objective to restore lost databases within fifteen minutes that was defined when the system was deployed and had no users. You now have ten thousand users and have been operating for two years. You have no information on how the time to restore has changed for your database.

 **Benefits of establishing this best practice:** By defining baseline metric values you are able to evaluate current metric values, and metric trends, to determine if action is required.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Learn expected patterns of activity for operations: Establish patterns of operations activity to determine when behavior is outside of the expected values so that you can respond appropriately if required.

---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/elastic-container-service-ecs.html
---

# Elastic Container Service (ECS)

## CPU and memory utilization
<a name="cpu-and-memory-utilization"></a>
+ The CPU alarm changes state if the average CPU utilization of the Prebid Server service is 72% or more within 1 minute. The memory alarm changes state if the average memory utilization is 55% or more within 1 minute.
+ The scaling policies’ targets are 66% CPU utilization and 50% memory utilization, and each alarm threshold is 10% above its target. If these alarms change state, the solution’s Auto Scaling might not be keeping up with the load.
+ You might need to check if Auto Scaling is turned on or adjust the Auto Scaling settings.
+ Metric: `CPUUtilization` >= 72%, `MemoryUtilization` >= 55%

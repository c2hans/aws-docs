---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/elastic-container-service-ecs.html
---

# Elastic Container Service (ECS)
<a name="elastic-container-service-ecs"></a>

## CPU and memory utilization
<a name="cpu-and-memory-utilization"></a>
+ The alarm changes state if the container CPU utilization or memory utilization exceed 70% within 1 minute.
+ Our scaling policies’ target is 50%. If these alarms change state, it means the solution’s Auto Scaling is not working.
+ You might need to check if Auto Scaling is turned on or adjust the Auto Scaling settings.
+ The alarm returns to the `OK` state if the CPU utilization and memory utilization are within the acceptable threshold for 5 minutes.
+ Metric: `CPUUtilization` > 70%, `MemoryUtilization` > 70%

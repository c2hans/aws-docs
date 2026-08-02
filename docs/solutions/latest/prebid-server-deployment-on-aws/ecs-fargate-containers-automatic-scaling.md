---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/ecs-fargate-containers-automatic-scaling.html
---

# ECS Fargate containers automatic scaling
<a name="ecs-fargate-containers-automatic-scaling"></a>

Automatic scaling is the ability to increase or decrease the desired count of tasks in your Amazon ECS service automatically. The service is configured to use target tracking scaling policies, which increase or decrease the number of tasks that your service runs. These are based on a target value for a specific metric provided by Application Auto Scaling, such as average CPU utilization, memory utilization, and average request count per target. These values are set in the `source/infrastructure/prebid_server/stack_constants.py` file with default values of `CPU_TARGET_UTILIZATION_PCT = 66`, `MEMORY_TARGET_UTILIZATION_PCT = 50`, and `REQUESTS_PER_TARGET = 5000`.

The default minimum and maximum task counts are also set in the file as `TASK_MIN_CAPACITY = 2` and `TASK_COUNT_MAX = 300`, respectively.

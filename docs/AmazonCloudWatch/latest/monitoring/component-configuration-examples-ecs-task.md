---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-ecs-task.html
---

# Amazon ECS tasks
<a name="component-configuration-examples-ecs-task"></a>

The following example shows a component configuration in JSON format for an Amazon ECS task.

```
{
    "logs":[
       {
          "logGroupName":"/ecs/my-task-definition",
          "logType":"APPLICATION",
          "monitor":true
       }
    ],
    "processes" : [
        {
            "processName" : "my_process",
            "alarmMetrics" : [
                {
                    "alarmMetricName" : "procstat cpu_usage",
                    "monitor" : true
                }, {
                    "alarmMetricName" : "procstat memory_rss",
                    "monitor" : true
                }
            ]
        }
    ]
 }
```

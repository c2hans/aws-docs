---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/logging-and-monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Logging and monitoring
<a name="logging-and-monitoring"></a>

 Monitoring is an important part of maintaining the reliability, availability, and performance of your applications running on Amazon ECS. Collect monitoring data from all of the parts of your AWS stack so you can more easily debug a multi-point failure if one occurs. AWS provides several tools for monitoring your Amazon ECS resources and responding to potential incidents. Refer to the following table for details on each service.

* Table 7 — Monitoring services *

|  Service  |  Description  |
| --- | --- |
|  [Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)  |  For clusters with tasks or services using the EC2 launch type, you can use CloudWatch Alarms to scale in and scale out the container instances based on CloudWatch metrics, such as cluster memory reservation.  |
|  [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)  |  Monitor, store, and access the log files from the containers in your Amazon ECS tasks by specifying the awslogs log driver in your task definitions. This is the only supported method for accessing logs for tasks using the Fargate launch type, but also works with tasks using the EC2 launch type.  |
|  [Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)  |  Match events and route them to one or more target functions or streams to make changes, capture state information, and take corrective action.  |
|  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)  |  CloudTrail provides a record of actions taken by a user, role, or an AWS service in Amazon ECS. Using the information collected by CloudTrail, you can determine the request that was made to Amazon ECS, the IP address from which the request was made, who made the request, when it was made, and additional details.  |
|  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)  |  Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps.  |
|  [Amazon ECS events and Amazon EventBridge](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch_event_stream.html)  |  Amazon ECS events for EventBridge receives near real-time notifications regarding the current state of your Amazon ECS clusters. If your tasks are using the Fargate launch type, you can see the state of your tasks. If your tasks are using the EC2 launch type, you can see the state of both the container instances and the current state of all tasks running on those container instances. For services, you can see events related to the health of your service.  |
|  [AWS X-Ray](https://aws.amazon.com/xray/)  |  AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors. <br /> You can use the X-Ray SDK and AWS service integration to instrument requests to your applications that are running locally or on AWS compute services such as Amazon EC2, [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), Amazon ECS, and AWS Lambda.  |

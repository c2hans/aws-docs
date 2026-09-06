---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_compute_hardware_select_best_compute_options.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP01 Select the best compute options for your workload
<a name="perf_compute_hardware_select_best_compute_options"></a>

 Selecting the most appropriate compute option for your workload allows you to improve performance, reduce unnecessary infrastructure costs, and lower the operational efforts required to maintain your workload.

 **Common anti-patterns:**
+  You use the same compute option that was used on premises.
+  You lack awareness of the cloud compute options, features, and solutions, and how those solutions might improve your compute performance.
+  You over-provision an existing compute option to meet scaling or performance requirements when an alternative compute option would align to your workload characteristics more precisely.

 **Benefits of establishing this best practice:** By identifying the compute requirements and evaluating against the options available, you can make your workload more resource efficient.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 To optimize your cloud workloads for performance efficiency, it is important to select the most appropriate compute options for your use case and performance requirements. AWS provides a variety of compute options that cater to different workloads in the cloud. For instance, you can use [Amazon EC2](https://docs.aws.amazon.com/ec2/) to launch and manage virtual servers, [AWS Lambda](https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs) to run code without having to provision or manage servers, [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/) to run and manage containers, or [AWS Batch](https://aws.amazon.com/batch/) to process large volumes of data in parallel. Based on your scale and compute needs, you should choose and configure the optimal compute solution for your situation. You can also consider using multiple types of compute solutions in a single workload, as each one has its own advantages and drawbacks.

 The following steps guide you through selecting the right compute options to match your workload characteristics and performance requirements.

## Implementation steps
<a name="implementation-steps"></a>

1.  Understand your workload compute requirements. Key requirements to consider include processing needs, traffic patterns, data access patterns, scaling needs, and latency requirements.

1.  Learn about different compute options available for your workload on AWS (as outlined in [PERF01-BP01 Learn about and understand available cloud services and features](perf_architecture_understand_cloud_services_and_features.md). Here are some key AWS compute options, their characteristics, and common use cases:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_compute_hardware_select_best_compute_options.html)

1.  Evaluate cost (like hourly charge or data transfer) and management overhead (like patching and scaling) associated to each compute option.

1.  Perform experiments and benchmarking in a non-production environment to identify which compute option can best address your workload requirements.

1.  Once you have experimented and identified your new compute solution, plan your migration and validate your performance metrics.

1.  Use AWS monitoring tools like [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and optimization services like [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to continually optimize your compute resources based on real-world usage patterns.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected)
+  [Amazon EC2 Instance Types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
+  [Amazon EKS Containers: Amazon EKS Worker Nodes ](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
+  [Amazon ECS Containers: Amazon ECS Container Instances ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)
+ [Prescriptive Guidance for Containers](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23containers&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)
+  [Prescriptive Guidance for Serverless](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23serverless&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)

 **Related videos:**
+  [How to choose compute option for startups](https://aws.amazon.com/startups/start-building/how-to-choose-compute-option/)
+  [Optimize performance and cost for your AWS compute ](https://www.youtube.com/watch?v=zt6jYJLK8sg)
+  [Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0&ref=wellarchitected)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system ](https://www.youtube.com/watch?v=rUY-00yFlE4&ref=wellarchitected)
+  [Deploy ML models for inference at high performance and low cost](https://www.youtube.com/watch?v=4FqHt5bmS2o)
+  [Better, faster, cheaper compute: Cost-optimizing Amazon EC2](https://www.youtube.com/watch?v=_dvh4P2FVbw&ref=wellarchitected)

 **Related examples:**
+  [Migrating the Web application to containers](https://application-migration-with-aws.workshop.aws/en/container-migration.html)
+  [Run a Serverless Hello World](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)

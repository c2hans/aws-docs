---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_config_options.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP02 Understand the available compute configuration options
<a name="perf_select_compute_config_options"></a>

 Each compute solution has options and configurations available to you to support your workload characteristics. Learn how various options complement your workload, and which configuration options are best for your application. Examples of these options include instance family, sizes, features (GPU, I/O), bursting, time-outs, function sizes, container instances, and concurrency.

 **Desired outcome:** The workload characteristics including CPU, memory, network throughput, GPU, IOPS, traffic patterns, and data access patterns are documented and used to configure the compute solution to match the workload characteristics. Each of these metrics plus custom metrics specific to your workload are recorded, monitored, and then used to optimize the compute configuration to best meet the requirements.

 **Common anti-patterns:**
+  Using the same compute solution that was being used on premises.
+  Not reviewing the compute options or instance family to match workload characteristics.
+  Oversizing the compute to ensure bursting capability.
+  You use multiple compute management platforms for the same workload.

** Benefits of establishing this best practice:** Be familiar with the AWS compute offerings so that you can determine the correct solution for each of your workloads. After you have selected the compute offerings for your workload, you can quickly experiment with those compute offerings to determine how well they meet your workload needs. A compute solution that is optimized to meet your workload characteristics will increase your performance, lower your cost and increase your reliability.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 If your workload has been using the same compute option for more than four weeks and you anticipate that the characteristics will remain the same in the future, you can use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to provide a recommendation to you based on your compute characteristics. If AWS Compute Optimizer is not an option due to lack of metrics, [a non-supported instance type](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html#requirements-ec2-instances) or a foreseeable change in your characteristics then you must predict your metrics based on load testing and experimentation.

 **Implementation steps:**

1.  Are you running on EC2 instances or containers with the EC2 Launch Type?

   1.  Can your workload use GPUs to increase performance?

      1.  [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Accelerated_Computing) instances are GPU-based instances that provide the highest performance for machine learning training, inference and high performance computing.

   1.  Does your workload run machine learning inference applications?

      1.  [AWS Inferentia (Inf1)](https://aws.amazon.com/ec2/instance-types/inf1/) — Inf1 instances are built to support machine learning inference applications. Using Inf1 instances, customers can run large-scale machine learning inference applications, such as image recognition, speech recognition, natural language processing, personalization, and fraud detection. You can build a model in one of the popular machine learning frameworks, such as TensorFlow, PyTorch, or MXNet and use GPU instances, to train your model. After your machine learning model is trained to meet your requirements, you can deploy your model on Inf1 instances by using [AWS Neuron](https://aws.amazon.com/machine-learning/neuron/), a specialized software development kit (SDK) consisting of a compiler, runtime, and profiling tools that optimize the machine learning inference performance of Inferentia chips.

   1.  Does your workload integrate with the low-level hardware to improve performance?

      1.  [Field Programmable Gate Arrays (FPGA)](https://aws.amazon.com/ec2/instance-types/f1/) — Using FPGAs, you can optimize your workloads by having custom hardware-accelerated operation for your most demanding workloads. You can define your algorithms by leveraging supported general programming languages such as C or Go, or hardware-oriented languages such as Verilog or VHDL.

   1.  Do you have at least four weeks of metrics and can predict that your traffic pattern and metrics will remain about the same in the future?

      1.  Use [Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to get a machine learning recommendation on which compute configuration best matches your compute characteristics.

   1.  Is your workload performance constrained by the CPU metrics?

      1.  [Compute-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Compute_Optimized) instances are ideal for the workloads that require high performing processors.

   1.  Is your workload performance constrained by the memory metrics?

      1.  [Memory-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Memory_Optimized) instances deliver large amounts of memory to support memory intensive workloads.

   1.  Is your workload performance constrained by IOPS?

      1.  [Storage-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Storage_Optimized) instances are designed for workloads that require high, sequential read and write access (IOPS) to local storage.

   1.  Do your workload characteristics represent a balanced need across all metrics?

      1.  Does your workload CPU need to burst to handle spikes in traffic?

         1.  [Burstable Performance](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Instance_Features) instances are similar to Compute Optimized instances except they offer the ability to burst past the fixed CPU baseline identified in a compute-optimized instance.

      1.  [General Purpose](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#General_Purpose) instances provide a balance of all characteristics to support a variety of workloads.

   1.  Is your compute instance running on Linux and constrained by network throughput on the network interface card?

      1.  Review [Performance Question 5, Best Practice 2: Evaluate available networking features](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/network-architecture-selection.html) to find the right instance type and family to meet your performance needs.

   1.  Does your workload need consistent and predictable instances in a specific Availability Zone that you can commit to for a year?

      1.  [Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) confirms capacity reservations in a specific Availability Zone. Reserved Instances are ideal for required compute power in a specific Availability Zone.

   1.  Does your workload have licenses that require dedicated hardware?

      1.  [Dedicated Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) support existing software licenses and help you meet compliance requirements.

   1.  Does your compute solution burst and require synchronous processing?

      1.  [On-Demand Instances](https://aws.amazon.com/ec2/pricing/on-demand/) let you use the compute capacity by the hour or second with no long-term commitment. These instances are good for bursting above performance baseline needs.

   1.  Is your compute solution stateless, fault-tolerant, and asynchronous?

      1.  [Spot Instances](https://aws.amazon.com/ec2/spot/) let you take advantage of unused instance capacity for your stateless, fault-tolerant workloads.

1.  Are you running containers on [Fargate](https://aws.amazon.com/fargate/)?

   1.  Is your task performance constrained by the memory or CPU?

      1.  Use the [Task Size](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-tasksize.html) to adjust your memory or CPU.

   1.  Is your performance being affected by your traffic pattern bursts?

      1.  Use the [Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-autoscaling.html) configuration to match your traffic patterns.

1.  Is your compute solution on [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html)?

   1.  Do you have at least four weeks of metrics and can predict that your traffic pattern and metrics will remain about the same in the future?

      1.  Use [Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to get a machine learning recommendation on which compute configuration best matches your compute characteristics.

   1.  Do you not have enough metrics to use AWS Compute Optimizer?

      1.  If you do not have metrics available to use Compute Optimizer, use [AWS Lambda Power Tuning](https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html) to help select the best configuration.

   1.  Is your function performance constrained by the memory or CPU?

      1.  Configure your [Lambda memory](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console) to meet your performance needs metrics.

   1.  Is your function timing out when running?

      1.  Change the [timeout settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html)

   1.  Is your function performance constrained by bursts of activity and concurrency?

      1.  Configure the [concurrency settings](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) to meet your performance requirements.

   1.  Does your function run asynchronously and is failing on retries?

      1.  Configure the maximum age of the event and the maximum retry limit in the [asynchronous configuration](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) settings.

## Level of effort for the implementation plan:
<a name="level-of-effort-for-the-implementation-plan-to-establish-this-best-practice-you-must-be-aware-of-your-current-compute-characteristics-and-metrics.-gathering-those-metrics-establishing-a-baseline-and-then-using-those-metrics-to-identify-the-ideal-compute-option-is-a-low-to-moderate-level-of-effort.-this-is-best-validated-by-load-tests-and-experimentation."></a>

To establish this best practice, you must be aware of your current compute characteristics and metrics. Gathering those metrics, establishing a baseline and then using those metrics to identify the ideal compute option is a *low* to *moderate* level of effort. This is best validated by load tests and experimentation.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected)
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
+  [EC2 Instance Types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
+  [Processor State Control for Your EC2 Instance ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html?ref=wellarchitected)
+  [EKS Containers: EKS Worker Nodes ](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
+  [Amazon ECS Containers: Amazon ECS Container Instances ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)

 **Related videos:**
+  [Amazon EC2 foundations (CMP211-R2) ](https://www.youtube.com/watch?v=kMMybKqC2Y0&ref=wellarchitected)
+  [Powering next-gen Amazon EC2: Deep dive into the Nitro system ](https://www.youtube.com/watch?v=rUY-00yFlE4&ref=wellarchitected)
+  [Optimize performance and cost for your AWS compute (CMP323-R1) ](https://www.youtube.com/watch?v=zt6jYJLK8sg&ref=wellarchitected)

 **Related examples:**
+  [Rightsizing with Compute Optimizer and Memory utilization enabled](https://www.wellarchitectedlabs.com/cost/200_labs/200_aws_resource_optimization/5_ec2_computer_opt/)
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

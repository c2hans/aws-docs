---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/sample-planning.html
---

# Experiment planning document
<a name="sample-planning"></a>

## Steady state
<a name="planning-steady-state"></a>

|
|
| Process name | Pet adoption site |
| --- |--- |
| Physical architecture | (Link to architecture diagram.) |
| Logical architecture | (Link to logical diagram.) |
| Define steady state | Average page load time, measured by using Largest Contentful Paint (LCP), for the pet adoption site is 2.5 seconds or less with a 99 percentile latency (P99) of 4.0 seconds or less with a baseline of 5000 concurrent users. |
| Steady state metrics | LCP metric captured across user base, and golden metrics (latency, throughput, error rates, saturation). |
| Steady state observability | LCP will be captured by the user's browser, sent to Amazon CloudWatch, and inspected with CloudWatch RUM. Over a 60 second period, the average and P99 LCP time will be aggregated for all requests in that period. Top-level golden metrics are captured by using CloudWatch. |
| Process to achieve steady state | Grafana K6 will be used to create a load that simulates normal production traffic levels of approximately 5K concurrent users. |

## Observability requirements
<a name="observability-reqs"></a>

Teams should be able to view the following:
+ **Steady state**:  What will be observed to verify that the application is under normal conditions?
+ **Failure condition**: How will the failure condition appear in the dashboard? For example:
  + Alarms that should be triggered
  + Logs that should be generated
+ **Failure impact**: What should be observed to view components that are expected to be impacted (scope of impact)?
+ **Recovery**: How will the recovery be viewed and measured to capture MTTR?
+ **Debug**: Troubleshooting details on experiment failures.

The following table provides suggestions and examples for an observability requirements chart. You should define what should be observed based on your specific experiment.

|
|
| What needs to be observed | Link to observability tool | What is being observed |
| --- |--- |--- |
| Source of input | Grafana K6 dashboard | + Running container count+ Requests per second |
| Overall application health | + Pet adoption CloudWatch dashboard<br />+ Pet adoption user experience dashboard (RUM) | + Amazon EKS healthy node count+ Amazon EKS node CPU utilization |
| Workflow health | Pet adoption CloudWatch dashboard | LCP time, golden metrics |
| Traces | Pet adoption X-Ray dashboard | + Request latency+ Request count+ Failure count |
| Logs | Pet adoption CloudWatch Logs | Any errors encountered by the pods will be issued to CloudWatch Logs. |

## Experiment definition
<a name="experiment-definition"></a>

|
|
| Experiment name | Amazon EKS PetSite pod CPU stress |
| --- |--- |
| Experiment source code | (Link to experiment source repository.) |
| Experiment description | This experiment explores how an increase in CPU usage of the PetSite application pod would impact overall customer experience. By injecting CPU stress into each running PetSite pod, we will be able to understand if there is impact to customers and the extent of that impact. |
| Experiment requirements or parameters | Application load: Production average<br />Pod label selector: `app=petsite` |
| Experiment duration | 10 minutes |
| Environment | Alpha test environment |
| Experiment target resources | PetSite application pods |
| Experiment baseline that is introduced through the load generating tool | + 54% of requests have an LCP of <2.5 seconds.<br />+ 46% of requests have an LCP of <4 seconds.<br />+ No errors are observed. |
| Backoff condition | None |

## Hypothesis
<a name="hypothesis"></a>

|
|
| What if | Impact | Recovery |
| --- |--- |--- |
| What would happen to steady state if the PetSite application pods experienced or caused more than 60% CPU utilization for 10 minutes under normal production-level traffic?<br />** ** | LCP times will remain under 2.5 seconds for P50 of users with P99 of 4.0 seconds or less. The consumer should be able to load the PetSite landing page. | Detection:+ CPU stress will be detected by alarms that are configured in CloudWatch.+ LCP metrics will also generate alarms for the degradation of user experience.<br />Self-healing:+ The distributed nature of the microservice architecture means that many instances of pods are running across multiple Availability Zones. + The EKS cluster control plane will shift traffic away from the affected pods, and will launch new pods on worker nodes.<br />Recovery:  <br />When CPU utilization returns to normal, the LCP should recover automatically. |

## Experiment process
<a name="experiment-process"></a>

Tailor the following example step-by-step process to your specific experiment:

1. Validate access to, and functionality of, all Amazon CloudWatch, CloudWatch RUM, and AWS X-Ray dashboards.

1. Validate the health of the application environment:

   1. Confirm that the EKS cluster is healthy by using the CloudWatch dashboard.

   1. Visit the test pet adoption site application deployment at the example URL.

1. Initiate a load to achieve steady state:

   1. Confirm that the load generator is running and sending 5000 requests per second.

   1. Allow 5 minutes for the application to reach its steady state.

   1. Confirm the steady state of the application by using the CloudWatch RUM dashboard.

1. Initiate a fault (experiment):

   1. Open the AWS FIS console.

   1. Run the pet-adoption-pod-stress experiment.

   1. Confirm that the experiment is running in the console.

1. Observe the impact of the fault on your application:

   1. Capture screenshots from the CloudWatch RUM and CloudWatch dashboards, and note any anomalous data points.

   1. After the experiment has completed in AWS FIS, capture additional screenshots to record if the application returns to steady state in the absence of stress, and note any anomalies in the data points.

   1. If the steady state doesn't resume, take steps to recover the application and record the steps taken.

1. Validate that the environment has returned to normal:
   + Review all business, user experience, application, and infrastructure metrics to verify that the system has returned to a known state. Capture dashboard screenshots if helpful.

## Experiment timeline
<a name="experiment-timeline"></a>

Make sure that you capture the timeline of the end-to-end experiment, starting with load generation, injection of the fault, observation of impact, and recovery of the application, and ending when you stop the load generation. This is illustrated in the following example.

![Example timeline for a chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/32d6e719-6d6f-4297-ba77-6af873f4e43e.png)

## Experiment results
<a name="experiment-results"></a>

|
|
| Experiment run ID | Experiment results |
| --- |--- |
| PET-ADOPT-EXP-23 | (Link to experiment results.) |

## Identified defects
<a name="defects"></a>
+ The Kubernetes cluster didn't detect the CPU impairment of the PetSite pods, so it didn't schedule additional deployments.
+ There was no increase in 4XX or 5XX error rates as a result of this experiment.
+ We need to adjust the health check of the pod to account for impact to LCP when there are resource constraints.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/sample-result.html
---

# Experiment result document
<a name="sample-result"></a>

## Configuration
<a name="config"></a>

Document the specific configurations for the experiment. For example:
+ Load generation set to simulate 5K users issuing a total of 85 requests per second.

## Prerequisites
<a name="prereqs"></a>
+ Verified that the pet adoption site was running in the alpha test environment.
+ Verified that the experiment template was configured to apply CPU stress to the PetSite application pods that are running in the EKS cluster.  Application pods were identified by the Kubernetes label `app=petsite`.
+ Load was confirmed to be running and generating 85 requests per second.

## Steady state
<a name="results-steady-state"></a>

Document the steps taken to achieve the steady state and how you verified it. For example:

For the test deployment of pet adoption site, a load of 85 RPS is being generated to simulate steady state. The CloudWatch RUM and CloudWatch dashboards were reviewed to verify that all business and application metrics were within normal ranges previous to the execution of the experiment.

Observability data:

|
|
| Expected | Observed (screenshot) |
| --- |--- |
| LCP is less than 4 seconds for P99 of requests.Response latency is less than 500 ms.There are no 4XX or 5XX errors. | ![Steady state report 1 for chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/ad6aab54-b8c2-476a-8ecf-af25c69f20cd.png)![Steady state report 2 for chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/a71aa9bd-8487-423f-9431-218e181c5e4b.png) |

## Fault injection
<a name="fault-injection"></a>

AWS FIS was used to inject faults by using the experiment template (provide link). The experiment was set to run for 10 minutes, and a rollback was configured if the worker nodes experienced CPU stress over 60 percent.

## Fault observation
<a name="fault-obs"></a>

The CloudWatch RUM and CloudWatch dashboards were reviewed to track the steady state of the application (defined by using LCP metrics).  Screenshots were captured in the following table.

Observability data:

|
|
| Expected | Observed (screenshot) |
| --- |--- |
| LCP should remain under 4 seconds for P99.Response time should remain under 500 ms.No 4XX or 5XX errors should be encountered. | ![Fault observation report 1 for chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/bc050edb-6b1b-41fc-b24f-41bb7c2911ad.png)![Fault observation report 2 for chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/31e90fe3-1dc9-43a1-b980-76fecfc1baea.png) |

## Recovery
<a name="recovery"></a>

After the stress has been removed (the AWS FIS experiment has completed and removed the CPU stress from the pods), the application should resume its normal steady state.  No manual intervention should be required.

Observability data:

|
|
| Expected | Observed (screenshot) |
| --- |--- |
| LCP P99 should be under 4 seconds with the average under 2.5 seconds. |  ![Sample recovery results from chaos experiment.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/5fafa73b-ee67-4d02-8daf-511ae18c44e1.png) |

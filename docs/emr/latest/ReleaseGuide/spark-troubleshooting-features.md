---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/spark-troubleshooting-features.html
---

# Troubleshooting features and capabilities
<a name="spark-troubleshooting-features"></a>

## Supported platforms
<a name="supported-platforms"></a>
+ **Languages**: Python and Scala Spark applications
+ **Target platforms**: EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue

## How troubleshooting works
<a name="how-it-works"></a>

When your Spark application fails, you can use the Troubleshooting Agent to automatically investigate what went wrong. It analyzes your Spark event logs, error messages, and resource usage to pinpoint the exact issue, such as a Spark executor running out of memory, a configuration error, or a code bug.

When you prompt the agent to analyze your Spark workload, it connects to your platform's resources and extracts features. These features include Spark event logs, query plans, executor timelines, log traces, configurations, and metrics.
+ On EMR on EC2: it connects to the [EMR persistent UI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html) for the cluster.
+ On AWS Glue: it builds the context from the Glue Studio [Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html) for the job.
+ On EMR Serverless: it connects to the EMR Serverless [Spark History Server](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html) for the job.
+ On EMR on EKS: it connects to the EMR persistent UI for the job.
+ The agent also analyzes your error stack traces and configuration details to give you actionable insights.

For failed workloads, you get a clear root cause explanation and specific steps to fix it. If the agent detects a code-related issue, it automatically provides code recommendations that show you exactly what to change in your code. You can also request code-level suggestions directly at any time, without the full analysis.

## Available Regions
<a name="available-regions"></a>

The Troubleshooting Agent is available in the following Regions:
+ **Asia Pacific**: Tokyo (ap-northeast-1), Seoul (ap-northeast-2), Singapore (ap-southeast-1), Sydney (ap-southeast-2), Mumbai (ap-south-1), Osaka (ap-northeast-3), Hong Kong (ap-east-1), Taipei (ap-east-2), Hyderabad (ap-south-2), Jakarta (ap-southeast-3), Melbourne (ap-southeast-4), Malaysia (ap-southeast-5), New Zealand (ap-southeast-6), and Thailand (ap-southeast-7)
+ **North America**: Canada (ca-central-1), Calgary (ca-west-1), and Mexico (mx-central-1)
+ **Europe**: Stockholm (eu-north-1), Ireland (eu-west-1), London (eu-west-2), Paris (eu-west-3), Frankfurt (eu-central-1), Zurich (eu-central-2), Milan (eu-south-1), and Spain (eu-south-2)
+ **Middle East**: Tel Aviv (il-central-1)
+ **Africa**: Cape Town (af-south-1)
+ **South America**: São Paulo (sa-east-1)
+ **United States**: N. Virginia (us-east-1), Ohio (us-east-2), Oregon (us-west-2), and N. California (us-west-1)

## Scope of Spark troubleshooting and user requirements
<a name="scope-requirements"></a>
+ **Supported Spark workload states**: The tools support responses for failed Spark workloads only.
+ **EMR persistent UI**: When analyzing EMR on EC2 and EMR on EKS workloads, the analyze tool attempts to connect to the EMR persistent UI to retrieve key Spark information. For EMR persistent UI considerations, see [Spark UI limitations](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html#app-history-spark-UI-limitations).
+ **Glue Studio Spark UI**: When analyzing AWS Glue workloads, the analyze tool attempts to retrieve key Spark information by parsing your Spark event logs from Amazon S3. The maximum supported Spark event log size is 512 MB, and 1 GB for rolling logs. For more information, see [Monitoring with the Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html).
+ **Code recommendations**: Supported only for EMR on EC2, EMR Serverless, EMR on EKS, and AWS Glue PySpark workloads.
+ **Regional resources**: The Troubleshooting Agent is Regional and uses the underlying Amazon EMR resources in that Region for the troubleshooting process. Cross-Region troubleshooting isn't supported.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics.html
---

# Automate ingestion and visualization of Amazon MWAA custom metrics on Amazon Managed Grafana by using Terraform
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics"></a>

*Faisal Abdullah and Satya Vajrapu, Amazon Web Services*

## Summary
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-summary"></a>

This pattern discusses how to use Amazon Managed Grafana to create and monitor custom metrics that are ingested by Amazon Managed Workflows for Apache Airflow (Amazon MWAA). Amazon MWAA serves as the orchestrator for workflows, employing Directed Acyclic Graphs (DAGs) that are scripted in Python. This pattern centers on the monitoring of custom metrics, including the total number of DAGs running within the last hour, the count of passed and failed DAGs each hour, and the average duration of these processes. This analysis shows how Amazon Managed Grafana integrates with Amazon MWAA to enable comprehensive monitoring and insights into the orchestration of workflows within this environment.

## Prerequisites and limitations
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-prereqs"></a>

**Prerequisites**
+ An active AWS account with the necessary user permissions to create and manage the following AWS services:
  + AWS Identity and Access Management (IAM) roles and policies
  + AWS Lambda
  + Amazon Managed Grafana
  + Amazon Managed Workflows for Apache Airflow (Amazon MWAA)
  + Amazon Simple Storage Service (Amazon S3)
  + Amazon Timestream
+ Access to a shell environment which can be a terminal on your local machine or [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html).
+ A shell environment with Git installed and the latest version of the AWS Command Line Interface (AWS CLI) installed and configured. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the AWS CLI documentation.
+ The following Terraform version installed: `required_version = ">= 1.6.1, < 2.0.0"` You can use [tfswitch](https://tfswitch.warrensbox.com/) to switch between different versions of Terraform.
+ Configured identity source in AWS IAM Identity Center for your AWS account. For more information, see [Confirm your identity sources in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/prereq-identity-sources.html) in the IAM Identity Center documentation. You can choose from the default IAM Identity Center directory, Active Directory, or an external Identity provider (IdP) such as Okta. For more information, see [Related resources](#automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-resources).

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Terraform `required_version = ">= 1.6.1, < 2.0.0"`
+ Amazon Managed Grafana version 9.4 or later. This pattern was tested on version 9.4.

## Architecture
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-architecture"></a>

The following architecture diagram highlights the AWS services used in the solution.

![Workflow to automate the ingestion of Amazon MWAA custom metrics.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3458d0a9-aee1-428a-bf2f-c357bb531c64/images/b43ed8d2-94ac-4438-913b-81c7eba8f3e0.png)

The preceding diagram steps through the following workflow:

1. Custom metrics within Amazon MWAA originate from DAGs that are executing within the environment. The metrics upload to the Amazon S3 bucket in a CSV file format. The following DAGs use the database querying capabilities of Amazon MWAA:
   + `run-example-dag` – This DAG contains sample Python code that defines one or more tasks. It runs every 7 minutes and prints the date. After printing the date, the DAG includes a task to sleep, or pause, execution for a specific duration.
   + `other-sample-dag` – This DAG runs every 10 mins and prints the date. After printing the date, the DAG includes a task to sleep, or pause, execution for a specific duration.
   + `data-extract` – This DAG runs every hour and queries the Amazon MWAA database and collects metrics. After the metrics are collected, this DAG writes them to an Amazon S3 bucket for further processing and analysis.

1. To streamline data processing, Lambda functions run when they’re triggered by Amazon S3 events, which facilitates the loading of metrics into Timestream.

1. Timestream is integrated as a data source within Amazon Managed Grafana where all the custom metrics from Amazon MWAA are stored.

1. Users can query the data and construct custom dashboards to visualize key performance indicators and gain insights into the orchestration of workflows within Amazon MWAA.

## Tools
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-tools"></a>

**AWS services**
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use. In this pattern, AWS Lambda runs the Python code in response to Amazon S3 events and manages the compute resources automatically.
+ [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) is a fully managed data visualization service that you can use to query, correlate, and visualize, and alert on your metrics, logs, and traces. This pattern uses Amazon Managed Grafana to create a dashboard for metrics visualization and alerts.
+ [Amazon Managed Workflows for Apache Airflow (Amazon MWAA)](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) is a managed orchestration service for Apache Airflow that you can use to set up and operate data pipelines in the cloud at scale. [Apache Airflow](https://airflow.apache.org/) is an open source tool used to programmatically author, schedule, and monitor sequences of processes and tasks referred to as workflows. In this pattern, sample DAGs and a metrics extractor DAG are deployed in Amazon MWAA.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. In this pattern, Amazon S3 is used to store DAGs, scripts, and custom metrics in CSV format.
+ [Amazon Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html) is is a fast, scalable, fully managed, purpose-built time series database that makes it easy to store and analyze trillions of time series data points per day. Timestream for LiveAnalytics also integrates with commonly used services for data collection, visualization, and machine learning. In this pattern, it’s used to ingest the generated Amazon MWAA custom metrics.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. This pattern uses a Terraform module to automate the provisioning of infrastructure in AWS.

**Code repository**

The code for this pattern is available on GitHub in the [visualize-amazon-mwaa-custom-metrics-grafana](https://github.com/aws-samples/visualize-amazon-mwaa-custom-metrics-grafana) repository. The `stacks/Infra` folder contains the following:
+ Terraform configuration files for all AWS resources
+ Grafana dashboard .json file in the `grafana` folder
+ Amazon Managed Workflows for Apache Airflow DAGs in the `mwaa/dags` folder
+ Lambda code to parse the .csv file and store metrics in the Timestream database in the `src` folder
+ IAM policy .json files in the `templates` folder

## Best practices
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-best-practices"></a>

Terraform must store state about your managed infrastructure and configuration so that it can map real-world resources to your configuration. By default, Terraform stores state locally in a file named `terraform.tfstate`. It's crucial to ensure the safety and integrity of your Terraform state file because it maintains the current state of your infrastructure. For more information, see [Remote State](https://developer.hashicorp.com/terraform/language/state/remote) in the Terraform documentation.

## Epics
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-epics"></a>

### Deploy the infrastructure using Terraform
<a name="deploy-the-infrastructure-using-terraform"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the infrastructure. | To deploy the solution infrastructure, do the following:1. Open a terminal or command prompt on your local computer or by using AWS CloudShell.<br />2. Navigate to the directory where you want to clone the repository.<br />3. To clone the repository, run the following command:<pre>git clone https://github.com/aws-samples/visualize-amazon-mwaa-custom-metrics-grafana</pre><br />4. After the cloning process is finished, run the following command to navigate into the cloned repository directory:<pre>cd visualize-amazon-mwaa-custom-metrics-grafana/stacks/infra</pre><br />5. To download and initialize the required providers, run the following command:<pre>terraform init</pre><br />6. To get a comprehensive view of all the resources that Terraform will create, run the following command:<pre>terraform plan</pre><br />Terraform provisions the following resources:Amazon Virtual Private Cloud (Amazon VPC) and associated networking componentsAmazon S3 resourcesAWS Lambda functionsAmazon Managed Grafana resources (workspace, dashboards, data source)Supporting IAM resources (roles and policies)<br />7. To create the AWS resources from the plan output, run the following command:<pre>terraform apply -auto-approve</pre><br />The infrastructure provisioning completes in approximately 20 minutes.<br />8. To create the specified AWS resources according to the configuration defined in your Terraform files, run the following command:<pre>terraform apply</pre> | AWS DevOps |

### Validate the deployed infrastructure resources
<a name="validate-the-deployed-infrastructure-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the Amazon MWAA environment. | To validate the Amazon MWAA environment, do the following:1. Sign in to the AWS Management Console, navigate to the [Amazon MWAA dashboard console ](https://us-east-1.console.aws.amazon.com/mwaa/home?region=us-east-1#environments)and select **Open Airflow UI**.<br />2. You should see the following three DAGs in **Active** status:data-extractrun-example-dagother-sample-dag<br />3. If a DAG isn’t active, you can activate it by enabling the toggle switch next to the DAG name. | AWS DevOps, Data engineer |
| Verify the DAG schedules. | To view each DAG schedule, go to the **Schedule** tab in the **Airflow UI**.<br />Each of the following DAGs has a pre-configured schedule, which runs in the Amazon MWAA environment and generates custom metrics: + **run-example-dag** - Runs every 7 minutes<br />+ **other-sample-dag** - Runs every 10 minutes<br />+ **data-extract** - Runs every hour<br />You can also see the successful runs of each DAG under the **Runs **column.  | Data engineer, AWS DevOps |

### Configure the Amazon Managed Grafana environment
<a name="configure-the-gra-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure access to the Amazon Managed Grafana workspace. | The Terraform scripts created the required Amazon Managed Grafana workspace, dashboards, and metrics page. To configure access so that you can view them, do the following:1. Open the [Amazon Managed Grafana](https://us-east-1.console.aws.amazon.com/grafana/home?region=us-east-1#/workspaces) console.<br />2. In **Workspaces**, select the workspace `grafana-ws-dev`, and navigate to the **Authentication** tab in the lower pane.<br />3. Choose the **Assign new user or group** button.<br />4. Add either your group in the **Groups** tab or a user in the **Users** tab, and then choose the **Assign user and groups** button.<br />5. After the user (or group) is added, make this user (or group) an admin. Select the user in **Assigned users or group** in the **Assigned user group** tab and choose **Make** **admin** from the dropdown menu. For more information, see [Use AWS IAM Identity Center with your Amazon Managed Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG-SSO.html) in the Amazon Managed Grafana documentation.<br />6. Navigate to **Workspaces**, and then choose the **Grafana workspace URL**. To sign in to Amazon Managed Grafana as an admin, choose **Sign in with AWS IAM Identity Center**. | AWS DevOps |
| Install the Amazon Timestream plugin.  | Amazon MWAA custom metrics are loaded into the Timestream database. You use the Timestream plugin to visualize the metrics with Amazon Managed Grafana dashboards.<br />To install the Timestream plugin, do the following:1. In the Amazon Managed Grafana console, expand the menu in the left navigation pane and go to **Administration, Plugins**.<br />2. Search for and then install latest version of the Amazon Timestream plugin.<br />3. After the plugin is installed, go to **Administration**, **Data sources** to see the Timestream data source. If the data source isn’t listed, refresh the page.<br />For more information, see [Extend your workspace with plugins](https://docs.aws.amazon.com/grafana/latest/userguide/grafana-plugins.html#manage-plugins) in the Amazon Managed Grafana documentation. | AWS DevOps, DevOps engineer |

### Visualize the custom metrics in the Amazon Managed Grafana dashboard
<a name="visualize-the-custom-metrics-in-the-gra-dashboard"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| View the Amazon Managed Grafana dashboard. | To view the metrics that were ingested into the Amazon Managed Grafana workspace, do the following:1. In the Amazon Managed Grafana console, choose **Dashboards** in the left navigation pane.<br />2. To view the metrics, choose **MWAA events dashboards **and then select **mwaa\_metrics**.<br />The dashboard metrics page shows the following information:+ Total DAG runs in the last one hour<br />+ Total successful, failed, and running DAG runs in the last one hour<br />+ Average duration for all, successful, and failed DAG runs | AWS DevOps |
| Customize the Amazon Managed Grafana dashboard. | To customize the dashboards for further future enhancements, do the following:1. On the Amazon Managed Grafana dashboard `mwaa_metrics` page, choose the **Dashboard settings **icon.<br />2. To view the data structure that defines the dashboard, choose **JSON model**. You can customize the dashboard by making edits to this JSON model directly in the console.<br />Alternatively, the source code for this dashboard is available in the `dashboard.json` file in the `stacks/infra/grafana` folder in the [GitHub repository](https://github.com/aws-samples/visualize-amazon-mwaa-custom-metrics-grafana/blob/main/stacks/infra/grafana/dashboard.json). | AWS DevOps |

### Clean up AWS resources
<a name="clean-up-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Pause the Amazon MWAA DAG runs. | To pause the DAG runs, do the following:1. In the Amazon MWAA console, navigate to [Airflow environments](https://us-east-1.console.aws.amazon.com/mwaa/home?region=us-east-1#environments) and choose **Open Airflow UI**.<br />2. To pause the DAG, use the toggle switch next to each DAG.<br />3. Refresh the **Airflow UI** page, which should list three DAGs in the **Paused **section. | AWS DevOps, Data engineer |
| Delete the objects in the Amazon S3 buckets. | To delete the Amazon S3 buckets **mwaa-events-bucket-\*** and **mwaa-metrics-bucket-\***, follow the instructions for using the Amazon S3 console in [Deleting a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html) in the Amazon S3 documentation. | AWS DevOps |
| Destroy the resources created by Terraform. | To destroy the resources created by Terraform and the associated local Terraform state file, do the following:1. (Optional) Before deleting the resources, you can preview the changes that Terraform will make. To generate a plan, run the following command:<pre>terraform plan -destroy</pre><br />The command output shows that the `destroy` command will delete all the AWS resources that were created earlier.<br />2. <pre>terraform destroy -auto-approve</pre>This command takes approximately 20 minutes to destroy the infrastructure.To destroy all resources managed by Terraform, run the following command. : The `-auto-approve` tag doesn’t wait for user confirmation to start destroying the resources.<br />3. To delete the local Terraform state file, run the following commands:<pre>rm .terraform.lock.hcl<br />rm -rf .terraform<br />rm terraform.tfstate*</pre> | AWS DevOps |

## Troubleshooting
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `null_resource.plugin_mgmt (local-exec): aws: error: argument operation: Invalid choice, valid choices are:` | Upgrade your AWS CLI to the [latest version](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). |
| Loading data sources error - <br />`Fetch error: 404 Not Found Instantiating…` | The error is intermittent. Wait a few minutes, and then refresh your data sources to view the listed Timestream data source.  |

## Related resources
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-resources"></a>

**AWS documentation**
+ [Amazon Managed Grafana for dashboarding and visualization](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/amg-dashboarding-visualization.html)
+ [Configure Amazon Managed Grafana to use Okta](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-SAML-providers-okta.html)
+ [Use AWS IAM Identity Center with your Amazon Managed Grafana workspace](https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG-SSO.html)
+ [Working with DAGs on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags.html)

**AWS videos**
+ Configure IAM Identity Center with Amazon Managed Grafana for authentication, as shown in the following [video](https://www.youtube.com/watch?v=XX2Xcz-Ps9U).

[https://www.youtube-nocookie.com/embed/XX2Xcz-Ps9U?controls=0](https://www.youtube-nocookie.com/embed/XX2Xcz-Ps9U?controls=0)
+ If IAM Identity Center isn’t available, you can also integrate the Amazon Managed Grafana authentication by using an external Identity provider (IdP) such as Okta, as shown in the following [video](https://www.youtube.com/watch?v=Z4JHxl2xpOg).

[https://www.youtube-nocookie.com/embed/Z4JHxl2xpOg?controls=0](https://www.youtube-nocookie.com/embed/Z4JHxl2xpOg?controls=0)

## Additional information
<a name="automate-ingestion-and-visualization-of-amazon-mwaa-custom-metrics-additional"></a>

You can create a comprehensive monitoring and alerting solution for your Amazon MWAA environment, enabling proactive management and rapid response to potential issues or anomalies. Amazon Managed Grafana includes the following capabilities:

**Alerting** – You can configure alerts in Amazon Managed Grafana based on predefined thresholds or conditions. Set up email notifications to alert relevant stakeholders when certain metrics exceed or fall below specified thresholds. For more information, see [Grafana alerting](https://docs.aws.amazon.com/grafana/latest/userguide/alerts-overview.html) in the Amazon Managed Grafana documentation.

**Integration** – You can integrate Amazon Managed Grafana with various third-party tools such as OpsGenie, PagerDuty, or Slack for enhanced notification capabilities. For example, you can set up webhooks or integrate with APIs to trigger incidents and notifications in these platforms based on alerts generated in Amazon Managed Grafana. In addition, this pattern provides a [GitHub repository](https://github.com/aws-samples/visualize-amazon-mwaa-custom-metrics-grafana) to create AWS resources. You can further integrate this code with your infrastructure deployment workflows.

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/obs-stack-reference.html
---

# Reference and troubleshooting for observability stacks

Every resource of an observability stack has a name that is derived from the stack name, every setting is a parameter of the stack's AWS CloudFormation stack, and the stack reports its endpoints as outputs. Use this topic to find a stack's resources in each service's console, to see which settings you can change after creation, and to look up the values that you need to send data.

## Resources and names
<a name="obs-stack-reference-resources"></a>

The CloudFormation stack is named `ObsStack-{{stack-name}}`. The names of its resources are derived from the stack name, so you can find them in each service's console.

| Resource | Name | Created for |
| --- | --- | --- |
| Amazon OpenSearch Serverless collection, or OpenSearch Service domain | `obs-{{stack-name}}` | Storage for logs and traces |
| Amazon OpenSearch Ingestion pipeline | `obs-{{stack-name}}-ingest` | The OTLP endpoint |
| Amazon Managed Service for Prometheus workspace | `obs-{{stack-name}}-metrics` | Storage for metrics |
| OpenSearch UI application | `obs-{{stack-name}}-app` | The user interface and its observability workspace |
| Prometheus data source | `{{stack_name}}_prometheus` | Lets OpenSearch UI query the metrics workspace. Hyphens in the stack name become underscores. |
| OpenSearch Serverless encryption, network, and data access policies | `obs-{{stack-name}}-enc`, `obs-{{stack-name}}-net`, `obs-{{stack-name}}-access` | Serverless storage only |
| IAM role for the pipeline | `obs-{{stack-name}}-osi-role` | Lets the pipeline write to storage and to the metrics workspace |
| IAM role for metrics queries | `obs-{{stack-name}}-dq-role` | Lets the Prometheus data source read the metrics workspace |
| Lambda functions and their roles | Names that start with `obs-{{stack-name}}-` | Run once by CloudFormation during creation to connect the data source, set up the workspace, and apply retention or access mappings. They are not invoked afterward except when you update or delete the stack. |
| Amazon EC2 instance, security group, and instance profile | Assigned by CloudFormation | The demo workload, when it is deployed |

Because the IAM role names are derived from the stack name, a stack name can be used only once in an account, across all AWS Regions.

## Settings
<a name="obs-stack-reference-parameters"></a>

The following table lists the settings of a stack, their default values, and whether you can change them after the stack is created. The create page in the console shows the same information for the options that you select, before you create the stack.

| Setting | CloudFormation parameter | Default | Change after creation |
| --- | --- | --- | --- |
| Administrators | `AdminRoleArns` | The role that you are signed in with | Yes |
| Demo workload | `DeployDemoWorkload` | `true` | Yes |
| Ingestion capacity | `MinOCU`, `MaxOCU` | 1–4 OCU | Yes |
| Metrics retention | `MetricsRetentionDays` | 150 days | Yes |
| Log and trace retention (serverless) | `LogRetentionDays` | 30 days | Yes |
| Collection capacity (serverless) | `CollectionMinOCU`, `CollectionMaxOCU` | 0–16 OCU. The collection scales down when it is idle. | Yes |
| Domain instances (domain) | `DomainInstanceType`, `DomainInstanceCount`, `DomainVolumeGB` | One instance with 100 GiB of storage | Yes |
| Storage backend and engine | Chosen by the template | Amazon OpenSearch Serverless with Easy create | No |

The **Change after creation** column applies to stacks created with Standard create, or with Easy create without the demo workload, where each setting is a parameter of the CloudFormation stack. A stack created with Easy create and the demo workload has the default values built into its template: its only parameters are the stack name and the administrators, so the administrators are the only setting that you can change by updating its parameters.

## Stack outputs
<a name="obs-stack-reference-outputs"></a>

The CloudFormation stack reports the following values on its **Outputs** tab.

| Output | Value |
| --- | --- |
| `AppEndpoint` | The URL of the OpenSearch UI application |
| `WorkspaceId` | The ID of the observability workspace in the application |
| `OSISEndpoint` | The OTLP endpoint for logs, metrics, and traces |
| `OSISPipelineArn` | The ARN of the ingestion pipeline, for the `osis:Ingest` permission |
| `AOSSEndpoint` or `DomainEndpoint` | The endpoint of the storage for logs and traces |
| `AMPEndpoint` | The endpoint of the Prometheus workspace |
| `PrometheusDataSourceArn` | The ARN of the Prometheus data source |
| `DemoInstanceId`, `DemoAccessHint` | The demo workload instance, and a command to reach its web page. Present only when the demo workload is deployed. |
| `AlertMonitors` | How many alert monitors the stack created. Present for template version 3.3.0 or later. |
| `TemplateVersion` | The version of the template that created the stack |

The stack has other outputs that this table doesn't list, such as the ARNs of its resources (for example, `AmpWorkspaceArn`) and the ID of the application (`AppId`).

## Quotas and limits
<a name="obs-stack-reference-quotas"></a>

The following limits apply to observability stacks:
+ A stack name must be 3–17 characters. It can contain only lowercase letters, numbers, and hyphens, must start with a letter, and must end with a letter or number.
+ A stack name can be used only once in an AWS account, across all AWS Regions, because the names of the stack's IAM roles are derived from it.

Each resource that a stack creates counts toward the quota of its service in the AWS Region. A stack creates one of each of the following:
+ An Amazon OpenSearch Serverless collection, or an OpenSearch Service domain
+ An Amazon OpenSearch Ingestion pipeline
+ An Amazon Managed Service for Prometheus workspace
+ An OpenSearch UI application
+ A Prometheus data source

For the quotas of Amazon OpenSearch Service, see [Amazon OpenSearch Service quotas](limits.md).

## Troubleshoot an observability stack
<a name="obs-stack-troubleshooting"></a>

Use the following information to resolve common issues with observability stacks.

### Observability stack creation failed
<a name="obs-stack-troubleshooting-failed"></a>

CloudFormation creates the resources of a stack in order, and stops and rolls back if one of them can't be created. The most common causes are a resource name that is already in use, a service quota that has been reached, and missing permissions to create one of the resources, including IAM roles. The following sections describe the first two.

To find out which resource failed, open the stack's page on the Amazon OpenSearch Service console. It shows the resource where creation stopped. For the reason, open the stack in the CloudFormation console and view its **Events** tab. A failed stack can't be updated. Delete it in CloudFormation, and then create the stack again.

### Observability stack rolled back immediately and created no resources
<a name="obs-stack-troubleshooting-renamed"></a>

The template accepts only the stack name that the console fills in, `ObsStack-{{stack-name}}`. If you change the stack name in the CloudFormation console, the stack rolls back without creating any resources. Delete it in CloudFormation, and then create the stack again without changing the name.

### Observability stack resource name already exists
<a name="obs-stack-troubleshooting-name"></a>

Creation fails with a message that a resource, such as an IAM role, already exists. Resource names are derived from the stack name, and IAM role names are unique in an account across all AWS Regions. If a stack with the same name exists in any Region, or a failed stack with that name hasn't been deleted yet, choose a different name or delete the other stack first.

### Observability stack service quota exceeded
<a name="obs-stack-troubleshooting-quota"></a>

A stack creates one resource of each kind, and each counts toward that service's quota in the AWS Region. For example, creation fails at the Prometheus data source with a message that the limit for the number of data sources has been exceeded. Delete resources that you no longer need, or request a quota increase, and then create the stack again. For what a stack creates, see [Quotas and limits](#obs-stack-reference-quotas).

### No telemetry data appears in your observability stack
<a name="obs-stack-troubleshooting-nodata"></a>
+ The demo workload takes a few minutes after the stack is created to start sending data.
+ A new ingestion pipeline can take several minutes after it becomes active before its endpoint accepts data. Make sure that your collector retries.
+ Check that the sender has the `osis:Ingest` permission on the stack's pipeline, signs requests for the `osis` service, and uses the paths in [Find the endpoint](observability-get-started.md#obs-stack-send-data-endpoint).
+ Check the pipeline's status and metrics on its page in the console. The stack's page links to it.

### Can't open the workspace of your observability stack or see its data
<a name="obs-stack-troubleshooting-access"></a>

Only the roles in the stack's `AdminRoleArns` parameter are administrators of the application and can read its data. If you sign in with a different role, add that role to the stack. For more information, see [Add or remove administrators](obs-stack-use.md#obs-stack-manage-admins).

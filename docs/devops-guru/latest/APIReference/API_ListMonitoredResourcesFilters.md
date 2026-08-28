---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ListMonitoredResourcesFilters.html
---

# ListMonitoredResourcesFilters
<a name="API_ListMonitoredResourcesFilters"></a>

 Filters to determine which monitored resources you want to retrieve. You can filter by resource type or resource permission status.

## Contents
<a name="API_ListMonitoredResourcesFilters_Contents"></a>

 ** ResourcePermission **   <a name="DevOpsGuru-Type-ListMonitoredResourcesFilters-ResourcePermission"></a>
 The permission status of a resource.
Type: String
Valid Values: `FULL_PERMISSION | MISSING_PERMISSION`
Required: Yes

 ** ResourceTypeFilters **   <a name="DevOpsGuru-Type-ListMonitoredResourcesFilters-ResourceTypeFilters"></a>
 The type of resource that you wish to retrieve, such as log groups.
Type: Array of strings
Valid Values: `LOG_GROUPS | CLOUDFRONT_DISTRIBUTION | DYNAMODB_TABLE | EC2_NAT_GATEWAY | ECS_CLUSTER | ECS_SERVICE | EKS_CLUSTER | ELASTIC_BEANSTALK_ENVIRONMENT | ELASTIC_LOAD_BALANCER_LOAD_BALANCER | ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER | ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP | ELASTICACHE_CACHE_CLUSTER | ELASTICSEARCH_DOMAIN | KINESIS_STREAM | LAMBDA_FUNCTION | OPEN_SEARCH_SERVICE_DOMAIN | RDS_DB_INSTANCE | RDS_DB_CLUSTER | REDSHIFT_CLUSTER | ROUTE53_HOSTED_ZONE | ROUTE53_HEALTH_CHECK | S3_BUCKET | SAGEMAKER_ENDPOINT | SNS_TOPIC | SQS_QUEUE | STEP_FUNCTIONS_ACTIVITY | STEP_FUNCTIONS_STATE_MACHINE`
Required: Yes

## See Also
<a name="API_ListMonitoredResourcesFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ListMonitoredResourcesFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ListMonitoredResourcesFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ListMonitoredResourcesFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

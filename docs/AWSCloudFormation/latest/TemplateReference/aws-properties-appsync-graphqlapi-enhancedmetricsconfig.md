---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appsync-graphqlapi-enhancedmetricsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::GraphQLApi EnhancedMetricsConfig
<a name="aws-properties-appsync-graphqlapi-enhancedmetricsconfig"></a>

Describes an enhanced metrics configuration.

## Syntax
<a name="aws-properties-appsync-graphqlapi-enhancedmetricsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appsync-graphqlapi-enhancedmetricsconfig-syntax.json"></a>

```
{
  "[DataSourceLevelMetricsBehavior](#cfn-appsync-graphqlapi-enhancedmetricsconfig-datasourcelevelmetricsbehavior)" : {{String}},
  "[OperationLevelMetricsConfig](#cfn-appsync-graphqlapi-enhancedmetricsconfig-operationlevelmetricsconfig)" : {{String}},
  "[ResolverLevelMetricsBehavior](#cfn-appsync-graphqlapi-enhancedmetricsconfig-resolverlevelmetricsbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-appsync-graphqlapi-enhancedmetricsconfig-syntax.yaml"></a>

```
  [DataSourceLevelMetricsBehavior](#cfn-appsync-graphqlapi-enhancedmetricsconfig-datasourcelevelmetricsbehavior): {{String}}
  [OperationLevelMetricsConfig](#cfn-appsync-graphqlapi-enhancedmetricsconfig-operationlevelmetricsconfig): {{String}}
  [ResolverLevelMetricsBehavior](#cfn-appsync-graphqlapi-enhancedmetricsconfig-resolverlevelmetricsbehavior): {{String}}
```

## Properties
<a name="aws-properties-appsync-graphqlapi-enhancedmetricsconfig-properties"></a>

`DataSourceLevelMetricsBehavior`  <a name="cfn-appsync-graphqlapi-enhancedmetricsconfig-datasourcelevelmetricsbehavior"></a>
Controls how data source metrics will be emitted to CloudWatch. Data source metrics include:
+ **Requests**: The number of invocations that occured during a request.
+ **Latency**: The time to complete a data source invocation.
+ **Errors**: The number of errors that occurred during a data source invocation.
These metrics can be emitted to CloudWatch per data source or for all data sources in the request. Metrics will be recorded by API ID and data source name. `dataSourceLevelMetricsBehavior` accepts one of these values at a time:
+ `FULL_REQUEST_DATA_SOURCE_METRICS`: Records and emits metric data for all data sources in the request.
+ `PER_DATA_SOURCE_METRICS`: Records and emits metric data for data sources that have the `MetricsConfig` value set to `ENABLED`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperationLevelMetricsConfig`  <a name="cfn-appsync-graphqlapi-enhancedmetricsconfig-operationlevelmetricsconfig"></a>
 Controls how operation metrics will be emitted to CloudWatch. Operation metrics include:
+ **Requests**: The number of times a specified GraphQL operation was called.
+ **GraphQL errors**: The number of GraphQL errors that occurred during a specified GraphQL operation.
Metrics will be recorded by API ID and operation name. You can set the value to `ENABLED` or `DISABLED`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolverLevelMetricsBehavior`  <a name="cfn-appsync-graphqlapi-enhancedmetricsconfig-resolverlevelmetricsbehavior"></a>
Controls how resolver metrics will be emitted to CloudWatch. Resolver metrics include:
+ **GraphQL errors**: The number of GraphQL errors that occurred.
+ **Requests**: The number of invocations that occurred during a request.
+ **Latency**: The time to complete a resolver invocation.
+ **Cache hits**: The number of cache hits during a request.
+ **Cache misses**: The number of cache misses during a request.
These metrics can be emitted to CloudWatch per resolver or for all resolvers in the request. Metrics will be recorded by API ID and resolver name. `resolverLevelMetricsBehavior` accepts one of these values at a time:
+ `FULL_REQUEST_RESOLVER_METRICS`: Records and emits metric data for all resolvers in the request.
+ `PER_RESOLVER_METRICS`: Records and emits metric data for resolvers that have the `MetricsConfig` value set to `ENABLED`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

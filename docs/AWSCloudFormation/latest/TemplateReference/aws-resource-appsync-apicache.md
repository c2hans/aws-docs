---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-apicache.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::ApiCache
<a name="aws-resource-appsync-apicache"></a>

The `AWS::AppSync::ApiCache` resource represents the input of a `CreateApiCache` operation.

## Syntax
<a name="aws-resource-appsync-apicache-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appsync-apicache-syntax.json"></a>

```
{
  "Type" : "AWS::AppSync::ApiCache",
  "Properties" : {
      "[ApiCachingBehavior](#cfn-appsync-apicache-apicachingbehavior)" : {{String}},
      "[ApiId](#cfn-appsync-apicache-apiid)" : {{String}},
      "[AtRestEncryptionEnabled](#cfn-appsync-apicache-atrestencryptionenabled)" : {{Boolean}},
      "[HealthMetricsConfig](#cfn-appsync-apicache-healthmetricsconfig)" : {{String}},
      "[TransitEncryptionEnabled](#cfn-appsync-apicache-transitencryptionenabled)" : {{Boolean}},
      "[Ttl](#cfn-appsync-apicache-ttl)" : {{Integer}},
      "[Type](#cfn-appsync-apicache-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appsync-apicache-syntax.yaml"></a>

```
Type: AWS::AppSync::ApiCache
Properties:
  [ApiCachingBehavior](#cfn-appsync-apicache-apicachingbehavior): {{String}}
  [ApiId](#cfn-appsync-apicache-apiid): {{String}}
  [AtRestEncryptionEnabled](#cfn-appsync-apicache-atrestencryptionenabled): {{Boolean}}
  [HealthMetricsConfig](#cfn-appsync-apicache-healthmetricsconfig): {{String}}
  [TransitEncryptionEnabled](#cfn-appsync-apicache-transitencryptionenabled): {{Boolean}}
  [Ttl](#cfn-appsync-apicache-ttl): {{Integer}}
  [Type](#cfn-appsync-apicache-type): {{String}}
```

## Properties
<a name="aws-resource-appsync-apicache-properties"></a>

`ApiCachingBehavior`  <a name="cfn-appsync-apicache-apicachingbehavior"></a>
Caching behavior.
+ **FULL\_REQUEST\_CACHING**: All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.
+ **PER\_RESOLVER\_CACHING**: Individual resolvers that you specify are cached.
+ **OPERATION\_LEVEL\_CACHING**: Full requests are cached together and returned without executing resolvers.
*Required*: Yes
*Type*: String
*Allowed values*: `FULL_REQUEST_CACHING | PER_RESOLVER_CACHING | OPERATION_LEVEL_CACHING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiId`  <a name="cfn-appsync-apicache-apiid"></a>
The GraphQL API ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AtRestEncryptionEnabled`  <a name="cfn-appsync-apicache-atrestencryptionenabled"></a>
*This parameter has been deprecated*.
At-rest encryption flag for cache. You cannot update this setting after creation.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HealthMetricsConfig`  <a name="cfn-appsync-apicache-healthmetricsconfig"></a>
Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:
+ **NetworkBandwidthOutAllowanceExceeded**: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.
+ **EngineCPUUtilization**: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.
Metrics will be recorded by API ID. You can set the value to `ENABLED` or `DISABLED`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitEncryptionEnabled`  <a name="cfn-appsync-apicache-transitencryptionenabled"></a>
*This parameter has been deprecated*.
Transit encryption flag when connecting to cache. You cannot update this setting after creation.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Ttl`  <a name="cfn-appsync-apicache-ttl"></a>
TTL in seconds for cache entries.
Valid values are 1–3,600 seconds.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-appsync-apicache-type"></a>
The cache instance type. Valid values are
+  `SMALL`
+  `MEDIUM`
+  `LARGE`
+  `XLARGE`
+  `LARGE_2X`
+  `LARGE_4X`
+ `LARGE_8X` (not available in all regions)
+  `LARGE_12X`
Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.
The following legacy instance types are available, but their use is discouraged:
+ **T2\_SMALL**: A t2.small instance type.
+ **T2\_MEDIUM**: A t2.medium instance type.
+ **R4\_LARGE**: A r4.large instance type.
+ **R4\_XLARGE**: A r4.xlarge instance type.
+ **R4\_2XLARGE**: A r4.2xlarge instance type.
+ **R4\_4XLARGE**: A r4.4xlarge instance type.
+ **R4\_8XLARGE**: A r4.8xlarge instance type.
*Required*: Yes
*Type*: String
*Allowed values*: `T2_SMALL | T2_MEDIUM | R4_LARGE | R4_XLARGE | R4_2XLARGE | R4_4XLARGE | R4_8XLARGE | SMALL | MEDIUM | LARGE | XLARGE | LARGE_2X | LARGE_4X | LARGE_8X | LARGE_12X`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-appsync-apicache--examples"></a>

### ApiCache Creation Example
<a name="aws-resource-appsync-apicache--examples--ApiCache_Creation_Example"></a>

The following example creates an ApiCache for your GraphQL API.

#### YAML
<a name="aws-resource-appsync-apicache--examples--ApiCache_Creation_Example--yaml"></a>

```
Parameters:
  graphQlApiId:
    Type: String
Resources:
  ApiCache:
    Type:  AWS::AppSync::ApiCache
    Properties:
      ApiId: !Ref graphQlApiId
      Type: SMALL
      ApiCachingBehavior: FULL_REQUEST_CACHING
      Ttl: 1200
      TransitEncryptionEnabled: true
      AtRestEncryptionEnabled: true
```

#### JSON
<a name="aws-resource-appsync-apicache--examples--ApiCache_Creation_Example--json"></a>

```
{
  "Parameters": {
    "graphQlApiId": {
      "Type": "String"
    }
  },
  "Resources": {
    "ApiCache": {
      "Type": "AWS::AppSync::ApiCache",
      "Properties": {
        "ApiId": { "Ref": "graphQlApiId" },
        "Type": "SMALL",
        "ApiCachingBehavior": "FULL_REQUEST_CACHING",
        "Ttl": 1200,
        "TransitEncryptionEnabled": true,
        "AtRestEncryptionEnabled": true
      }
    }
  }
}
```

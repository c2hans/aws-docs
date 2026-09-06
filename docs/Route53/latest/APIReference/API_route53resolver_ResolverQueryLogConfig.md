---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfig.html
---

# ResolverQueryLogConfig
<a name="API_route53resolver_ResolverQueryLogConfig"></a>

In the response to a [CreateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverQueryLogConfig.html), [DeleteResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverQueryLogConfig.html), [GetResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfig.html), or [ListResolverQueryLogConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigs.html) request, a complex type that contains settings for one query logging configuration.

## Contents
<a name="API_route53resolver_ResolverQueryLogConfig_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-Arn"></a>
The ARN for the query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** AssociationCount **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-AssociationCount"></a>
The number of VPCs that are associated with the query logging configuration.
Type: Integer
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-CreationTime"></a>
The date and time that the query logging configuration was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-CreatorRequestId"></a>
A unique string that identifies the request that created the query logging configuration. The `CreatorRequestId` allows failed requests to be retried without the risk of running the operation twice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** DestinationArn **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-DestinationArn"></a>
The ARN of the resource that you want Resolver to send query logs: an Amazon S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 600.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-Id"></a>
The ID for the query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-Name"></a>
The name of the query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-OwnerId"></a>
The AWS account ID for the account that created the query logging configuration.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ShareStatus **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-ShareStatus"></a>
An indication of whether the query logging configuration is shared with other AWS accounts, or was shared with the current account by another AWS account. Sharing is configured through AWS Resource Access Manager (AWS RAM).
Type: String
Valid Values: `NOT_SHARED | SHARED_WITH_ME | SHARED_BY_ME`
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-Status"></a>
The status of the specified query logging configuration. Valid values include the following:
+  `CREATING`: Resolver is creating the query logging configuration.
+  `CREATED`: The query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
+  `DELETING`: Resolver is deleting this query logging configuration.
+  `FAILED`: Resolver can't deliver logs to the location that is specified in the query logging configuration. Here are two common causes:
  + The specified destination (for example, an Amazon S3 bucket) was deleted.
  + Permissions don't allow sending logs to the destination.
Type: String
Valid Values: `CREATING | CREATED | DELETING | FAILED`
Required: No

## See Also
<a name="API_route53resolver_ResolverQueryLogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverQueryLogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverQueryLogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverQueryLogConfig)

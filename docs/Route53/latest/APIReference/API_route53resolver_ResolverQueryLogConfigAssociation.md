---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfigAssociation.html
---

# ResolverQueryLogConfigAssociation
<a name="API_route53resolver_ResolverQueryLogConfigAssociation"></a>

In the response to an [AssociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html), [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html), [GetResolverQueryLogConfigAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html), or [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html), request, a complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.

## Contents
<a name="API_route53resolver_ResolverQueryLogConfigAssociation_Contents"></a>

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-CreationTime"></a>
The date and time that the VPC was associated with the query logging configuration, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Error **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-Error"></a>
If the value of `Status` is `FAILED`, the value of `Error` indicates the cause:
+  `DESTINATION_NOT_FOUND`: The specified destination (for example, an Amazon S3 bucket) was deleted.
+  `ACCESS_DENIED`: Permissions don't allow sending logs to the destination.
If the value of `Status` is a value other than `FAILED`, `Error` is null.
Type: String
Valid Values: `NONE | DESTINATION_NOT_FOUND | ACCESS_DENIED | INTERNAL_SERVICE_ERROR`
Required: No

 ** ErrorMessage **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-ErrorMessage"></a>
Contains additional information about the error. If the value or `Error` is null, the value of `ErrorMessage` also is null.
Type: String
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-Id"></a>
The ID of the query logging association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResolverQueryLogConfigId **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-ResolverQueryLogConfigId"></a>
The ID of the query logging configuration that a VPC is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceId **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-ResourceId"></a>
The ID of the Amazon VPC that is associated with the query logging configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-Status"></a>
The status of the specified query logging association. Valid values include the following:
+  `CREATING`: Resolver is creating an association between an Amazon VPC and a query logging configuration.
+  `ACTIVE`: The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
+  `DELETING`: Resolver is deleting this query logging association.
+  `FAILED`: Resolver either couldn't create or couldn't delete the query logging association.
Type: String
Valid Values: `CREATING | ACTIVE | ACTION_NEEDED | DELETING | FAILED`
Required: No

## See Also
<a name="API_route53resolver_ResolverQueryLogConfigAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverQueryLogConfigAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverQueryLogConfigAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverQueryLogConfigAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

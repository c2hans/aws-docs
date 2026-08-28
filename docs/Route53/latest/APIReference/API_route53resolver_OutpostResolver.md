---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_OutpostResolver.html
---

# OutpostResolver
<a name="API_route53resolver_OutpostResolver"></a>

A complex type that contains settings for an existing Resolver on an Outpost.

## Contents
<a name="API_route53resolver_OutpostResolver_Contents"></a>

 ** Arn **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-Arn"></a>
The ARN (Amazon Resource Name) for the Resolver on an Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreationTime **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-CreationTime"></a>
The date and time that the Outpost Resolver was created, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** CreatorRequestId **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-CreatorRequestId"></a>
A unique string that identifies the request that created the Resolver endpoint. The `CreatorRequestId` allows failed requests to be retried without the risk of running the operation twice.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-Id"></a>
The ID of the Resolver on Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** InstanceCount **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-InstanceCount"></a>
Amazon EC2 instance count for the Resolver on the Outpost.
Type: Integer
Required: No

 ** ModificationTime **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-ModificationTime"></a>
The date and time that the Outpost Resolver was modified, in Unix time format and Coordinated Universal Time (UTC).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 40.
Required: No

 ** Name **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-Name"></a>
Name of the Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** OutpostArn **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-OutpostArn"></a>
The ARN (Amazon Resource Name) for the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** PreferredInstanceType **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-PreferredInstanceType"></a>
 The Amazon EC2 instance type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Status **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-Status"></a>
Status of the Resolver.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING | ACTION_NEEDED | FAILED_CREATION | FAILED_DELETION`
Required: No

 ** StatusMessage **   <a name="Route53Resolver-Type-route53resolver_OutpostResolver-StatusMessage"></a>
A detailed description of the Resolver.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## See Also
<a name="API_route53resolver_OutpostResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/OutpostResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/OutpostResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/OutpostResolver)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_LinkedService.html
---

# LinkedService
<a name="API_LinkedService"></a>

If a health check or hosted zone was created by another service, `LinkedService` is a complex type that describes the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53.

## Contents
<a name="API_LinkedService_Contents"></a>

 ** Description **   <a name="Route53-Type-LinkedService-Description"></a>
If the health check or hosted zone was created by another service, an optional description that can be provided by the other service. When a resource is created by another service, you can't edit or delete it using Amazon Route 53.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** ServicePrincipal **   <a name="Route53-Type-LinkedService-ServicePrincipal"></a>
If the health check or hosted zone was created by another service, the service that created the resource. When a resource is created by another service, you can't edit or delete it using Amazon Route 53.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_LinkedService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/LinkedService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/LinkedService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/LinkedService)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

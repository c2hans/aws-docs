---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ServiceFunction.html
---

# ServiceFunction
<a name="API_ServiceFunction"></a>

Represents a logical component of a service.

## Contents
<a name="API_ServiceFunction_Contents"></a>

 ** criticality **   <a name="ngresiliencehub-Type-ServiceFunction-criticality"></a>
The criticality level of the service function.
Type: String
Valid Values: `PRIMARY | SUPPLEMENTAL`
Required: Yes

 ** name **   <a name="ngresiliencehub-Type-ServiceFunction-name"></a>
Entity label (not part of ARN — spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9 _\-]{1,59}`
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-ServiceFunction-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** serviceFunctionId **   <a name="ngresiliencehub-Type-ServiceFunction-serviceFunctionId"></a>
The unique identifier of the service function.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `\S{1,255}`
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-ServiceFunction-createdAt"></a>
The timestamp when the service function was created.
Type: Timestamp
Required: No

 ** description **   <a name="ngresiliencehub-Type-ServiceFunction-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** resourceCount **   <a name="ngresiliencehub-Type-ServiceFunction-resourceCount"></a>
The number of resources associated with the service function.
Type: Integer
Required: No

 ** source **   <a name="ngresiliencehub-Type-ServiceFunction-source"></a>
The source of the service function.
Type: String
Valid Values: `AI_GENERATED | USER`
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-ServiceFunction-updatedAt"></a>
The timestamp when the service function was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ServiceFunction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ServiceFunction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ServiceFunction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ServiceFunction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

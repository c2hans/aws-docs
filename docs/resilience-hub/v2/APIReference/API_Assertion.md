---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Assertion.html
---

# Assertion
<a name="API_Assertion"></a>

Represents a resilience assertion for a service.

## Contents
<a name="API_Assertion_Contents"></a>

 ** assertionId **   <a name="ngresiliencehub-Type-Assertion-assertionId"></a>
The unique identifier of the assertion.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}`
Required: Yes

 ** serviceArn **   <a name="ngresiliencehub-Type-Assertion-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** source **   <a name="ngresiliencehub-Type-Assertion-source"></a>
The source of the assertion, indicating whether it was AI-generated or created by a user.
Type: String
Valid Values: `AI_GENERATED | USER`
Required: Yes

 ** text **   <a name="ngresiliencehub-Type-Assertion-text"></a>
The text content of the assertion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** createdAt **   <a name="ngresiliencehub-Type-Assertion-createdAt"></a>
The timestamp when the assertion was created.
Type: Timestamp
Required: No

 ** updatedAt **   <a name="ngresiliencehub-Type-Assertion-updatedAt"></a>
The timestamp when the assertion was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Assertion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Assertion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Assertion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Assertion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

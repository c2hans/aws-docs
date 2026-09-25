---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AccessGrantSummary.html
---

# AccessGrantSummary
<a name="API_AccessGrantSummary"></a>

Summary of an AccessGrant. Call GetAccessGrant for the full grant.

## Contents
<a name="API_AccessGrantSummary_Contents"></a>

 ** domainId **   <a name="cloudwatchomni-Type-AccessGrantSummary-domainId"></a>
The ID of the domain the grant belongs to.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** grantArn **   <a name="cloudwatchomni-Type-AccessGrantSummary-grantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** grantId **   <a name="cloudwatchomni-Type-AccessGrantSummary-grantId"></a>
The unique ID of the access grant.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** grantType **   <a name="cloudwatchomni-Type-AccessGrantSummary-grantType"></a>
Who manages the grant.
Type: String
Valid Values: `SERVICE_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** permission **   <a name="cloudwatchomni-Type-AccessGrantSummary-permission"></a>
The permission granted.
Type: String
Valid Values: `SPACE_ADMIN | READ | READ_WRITE_DELETE | CUSTOM`
Required: Yes

 ** principal **   <a name="cloudwatchomni-Type-AccessGrantSummary-principal"></a>
The principal receiving the grant.
Type: [AccessGrantPrincipal](API_AccessGrantPrincipal.md) object
Required: Yes

 ** spaceId **   <a name="cloudwatchomni-Type-AccessGrantSummary-spaceId"></a>
The space this grant applies to. Domain-scoped grants are returned by ListDomainAccessGrantsForOrganization instead.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-AccessGrantSummary-name"></a>
A name that identifies the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_AccessGrantSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AccessGrantSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AccessGrantSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AccessGrantSummary)

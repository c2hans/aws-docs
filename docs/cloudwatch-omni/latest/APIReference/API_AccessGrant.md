---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_AccessGrant.html
---

# AccessGrant
<a name="API_AccessGrant"></a>

Full AccessGrant structure returned by API operations.

## Contents
<a name="API_AccessGrant_Contents"></a>

 ** accountId **   <a name="cloudwatchomni-Type-AccessGrant-accountId"></a>
The AWS account ID that owns the grant.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-AccessGrant-createdAt"></a>
The timestamp when the grant was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="cloudwatchomni-Type-AccessGrant-createdBy"></a>
The principal that created the grant.
Type: String
Required: Yes

 ** domainId **   <a name="cloudwatchomni-Type-AccessGrant-domainId"></a>
The ID of the domain the grant belongs to.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

 ** grantArn **   <a name="cloudwatchomni-Type-AccessGrant-grantArn"></a>
The Amazon Resource Name (ARN) of the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** grantId **   <a name="cloudwatchomni-Type-AccessGrant-grantId"></a>
The unique ID of the access grant.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** grantType **   <a name="cloudwatchomni-Type-AccessGrant-grantType"></a>
Who manages the grant.
Type: String
Valid Values: `SERVICE_MANAGED | CUSTOMER_MANAGED`
Required: Yes

 ** permission **   <a name="cloudwatchomni-Type-AccessGrant-permission"></a>
The permission granted.
Type: String
Valid Values: `SPACE_ADMIN | READ | READ_WRITE_DELETE | CUSTOM`
Required: Yes

 ** principal **   <a name="cloudwatchomni-Type-AccessGrant-principal"></a>
The principal receiving the grant.
Type: [AccessGrantPrincipal](API_AccessGrantPrincipal.md) object
Required: Yes

 ** spaceId **   <a name="cloudwatchomni-Type-AccessGrant-spaceId"></a>
The space this grant applies to. Domain-scoped grants are returned by ListDomainAccessGrantsForOrganization instead.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-AccessGrant-updatedAt"></a>
The timestamp when the grant was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-AccessGrant-name"></a>
A name that identifies the access grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** scopedActions **   <a name="cloudwatchomni-Type-AccessGrant-scopedActions"></a>
Groups of actions allowed by the grant, each with the resource scopes and conditions that limit those actions.
Type: Array of [ScopedActions](API_ScopedActions.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

## See Also
<a name="API_AccessGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/AccessGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/AccessGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/AccessGrant)

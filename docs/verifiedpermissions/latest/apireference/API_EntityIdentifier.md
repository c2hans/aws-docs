---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html
---

# EntityIdentifier
<a name="API_EntityIdentifier"></a>

Contains the identifier of an entity, including its ID and type.

This data type is used as a request parameter for [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) operation, and as a response parameter for the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html), [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html), and [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html) operations.

Example: `{"entityId":"string","entityType":"string"}`

## Contents
<a name="API_EntityIdentifier_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** entityId **   <a name="verifiedpermissions-Type-EntityIdentifier-entityId"></a>
The identifier of an entity.
 `"entityId":"identifier"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 612.
Pattern: `.*`
Required: Yes

 ** entityType **   <a name="verifiedpermissions-Type-EntityIdentifier-entityType"></a>
The type of an entity.
Example: `"entityType":"typeName"`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `.*`
Required: Yes

## See Also
<a name="API_EntityIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EntityIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EntityIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EntityIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

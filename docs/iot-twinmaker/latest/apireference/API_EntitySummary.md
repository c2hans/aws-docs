---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_EntitySummary.html
---

# EntitySummary
<a name="API_EntitySummary"></a>

An object that contains information about an entity.

## Contents
<a name="API_EntitySummary_Contents"></a>

 ** arn **   <a name="tm-Type-EntitySummary-arn"></a>
The ARN of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** creationDateTime **   <a name="tm-Type-EntitySummary-creationDateTime"></a>
The date and time when the entity was created.
Type: Timestamp
Required: Yes

 ** entityId **   <a name="tm-Type-EntitySummary-entityId"></a>
The ID of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: Yes

 ** entityName **   <a name="tm-Type-EntitySummary-entityName"></a>
The name of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** status **   <a name="tm-Type-EntitySummary-status"></a>
The current status of the entity.
Type: [Status](API_Status.md) object
Required: Yes

 ** updateDateTime **   <a name="tm-Type-EntitySummary-updateDateTime"></a>
The last date and time when the entity was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="tm-Type-EntitySummary-description"></a>
The description of the entity.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** hasChildEntities **   <a name="tm-Type-EntitySummary-hasChildEntities"></a>
An **eventual** Boolean value that specifies whether the entity has child entities or not.
Type: Boolean
Required: No

 ** parentEntityId **   <a name="tm-Type-EntitySummary-parentEntityId"></a>
The ID of the parent entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$ROOT|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|^[a-zA-Z0-9][a-zA-Z_\-0-9.:]*[a-zA-Z0-9]+`
Required: No

## See Also
<a name="API_EntitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/EntitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/EntitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/EntitySummary)

---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_PolicyAttachedToServiceMetadata.html
---

# PolicyAttachedToServiceMetadata
<a name="API_PolicyAttachedToServiceMetadata"></a>

Contains details about the service that started using the policy, such as the account that owns the service.

## Contents
<a name="API_PolicyAttachedToServiceMetadata_Contents"></a>

 ** accountId **   <a name="ngresiliencehub-Type-PolicyAttachedToServiceMetadata-accountId"></a>
The account that owns the service.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** serviceArn **   <a name="ngresiliencehub-Type-PolicyAttachedToServiceMetadata-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

## See Also
<a name="API_PolicyAttachedToServiceMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/PolicyAttachedToServiceMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/PolicyAttachedToServiceMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/PolicyAttachedToServiceMetadata)

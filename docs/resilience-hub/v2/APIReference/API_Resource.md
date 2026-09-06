---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Represents an AWS resource discovered by Resilience Hub.

## Contents
<a name="API_Resource_Contents"></a>

 ** identifier **   <a name="ngresiliencehub-Type-Resource-identifier"></a>
The identifier of the resource.
Type: String
Required: Yes

 ** awsAccountId **   <a name="ngresiliencehub-Type-Resource-awsAccountId"></a>
The AWS account ID that owns the resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** awsRegion **   <a name="ngresiliencehub-Type-Resource-awsRegion"></a>
The AWS Region where the resource is located.
Type: String
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: No

 ** resourceType **   <a name="ngresiliencehub-Type-Resource-resourceType"></a>
The type of the resource.
Type: String
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/Resource)

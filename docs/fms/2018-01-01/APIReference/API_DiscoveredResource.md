---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DiscoveredResource.html
---

# DiscoveredResource
<a name="API_DiscoveredResource"></a>

A resource in the organization that's available to be associated with a Firewall Manager resource set.

## Contents
<a name="API_DiscoveredResource_Contents"></a>

 ** AccountId **   <a name="fms-Type-DiscoveredResource-AccountId"></a>
The AWS account ID associated with the discovered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

 ** Name **   <a name="fms-Type-DiscoveredResource-Name"></a>
The name of the discovered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Type **   <a name="fms-Type-DiscoveredResource-Type"></a>
The type of the discovered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** URI **   <a name="fms-Type-DiscoveredResource-URI"></a>
The universal resource identifier (URI) of the discovered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_DiscoveredResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/DiscoveredResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/DiscoveredResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/DiscoveredResource)

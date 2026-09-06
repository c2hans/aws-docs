---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Details of a resource that is associated to an Firewall Manager resource set.

## Contents
<a name="API_Resource_Contents"></a>

 ** URI **   <a name="fms-Type-Resource-URI"></a>
The resource's universal resource indicator (URI).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** AccountId **   <a name="fms-Type-Resource-AccountId"></a>
The AWS account ID that the associated resource belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/Resource)

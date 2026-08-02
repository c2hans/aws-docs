---
source_url: https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DomainInfo.html
---

# DomainInfo
<a name="API_DomainInfo"></a>

Contains general information about a domain.

## Contents
<a name="API_DomainInfo_Contents"></a>

 ** name **   <a name="SWF-Type-DomainInfo-name"></a>
The name of the domain. This name is unique within the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** status **   <a name="SWF-Type-DomainInfo-status"></a>
The status of the domain:
+  `REGISTERED` – The domain is properly registered and available. You can use this domain for registering types and creating new workflow executions.
+  `DEPRECATED` – The domain was deprecated using [DeprecateDomain](API_DeprecateDomain.md), but is still in use. You should not create new workflow executions in this domain.
Type: String
Valid Values: `REGISTERED | DEPRECATED`
Required: Yes

 ** arn **   <a name="SWF-Type-DomainInfo-arn"></a>
The ARN of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Required: No

 ** description **   <a name="SWF-Type-DomainInfo-description"></a>
The description of the domain provided through [RegisterDomain](API_RegisterDomain.md).
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_DomainInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/swf-2012-01-25/DomainInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/swf-2012-01-25/DomainInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/swf-2012-01-25/DomainInfo)

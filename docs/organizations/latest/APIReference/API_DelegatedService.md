---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_DelegatedService.html
---

# DelegatedService
<a name="API_DelegatedService"></a>

Contains information about the AWS service for which the account is a delegated administrator.

## Contents
<a name="API_DelegatedService_Contents"></a>

 ** DelegationEnabledDate **   <a name="organizations-Type-DelegatedService-DelegationEnabledDate"></a>
The date that the account became a delegated administrator for this service.
Type: Timestamp
Required: No

 ** ServicePrincipal **   <a name="organizations-Type-DelegatedService-ServicePrincipal"></a>
The name of an AWS service that can request an operation for the specified service. This is typically in the form of a URL, such as: ` servicename.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+=,.@-]*`
Required: No

## See Also
<a name="API_DelegatedService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/DelegatedService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/DelegatedService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/DelegatedService)

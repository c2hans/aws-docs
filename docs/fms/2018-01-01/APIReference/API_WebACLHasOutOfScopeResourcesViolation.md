---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_WebACLHasOutOfScopeResourcesViolation.html
---

# WebACLHasOutOfScopeResourcesViolation
<a name="API_WebACLHasOutOfScopeResourcesViolation"></a>

The violation details for a web ACL that's associated with at least one resource that's out of scope of the Firewall Manager policy.

## Contents
<a name="API_WebACLHasOutOfScopeResourcesViolation_Contents"></a>

 ** OutOfScopeResourceList **   <a name="fms-Type-WebACLHasOutOfScopeResourcesViolation-OutOfScopeResourceList"></a>
An array of Amazon Resource Name (ARN) for the resources that are out of scope of the policy and are associated with the web ACL.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** WebACLArn **   <a name="fms-Type-WebACLHasOutOfScopeResourcesViolation-WebACLArn"></a>
The Amazon Resource Name (ARN) of the web ACL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_WebACLHasOutOfScopeResourcesViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/WebACLHasOutOfScopeResourcesViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/WebACLHasOutOfScopeResourcesViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/WebACLHasOutOfScopeResourcesViolation)

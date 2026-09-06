---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_Scope.html
---

# Scope
<a name="API_Scope"></a>

Defines which resources trigger an evaluation for an AWS Config rule. The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

## Contents
<a name="API_Scope_Contents"></a>

 ** ComplianceResourceId **   <a name="config-Type-Scope-ComplianceResourceId"></a>
The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for `ComplianceResourceTypes`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ComplianceResourceTypes **   <a name="config-Type-Scope-ComplianceResourceTypes"></a>
The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for `ComplianceResourceId`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ServicePrincipals **   <a name="config-Type-Scope-ServicePrincipals"></a>
The service principals of the AWS services for the rule.
The field is populated only if the service-linked rule is created by a service. The field is empty if you create your own rule.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagKey **   <a name="config-Type-Scope-TagKey"></a>
The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** TagValue **   <a name="config-Type-Scope-TagValue"></a>
The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for `TagValue`, you must also specify a value for `TagKey`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Scope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/Scope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/Scope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/Scope)

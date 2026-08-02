---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ConfigurationPolicySummary.html
---

# ConfigurationPolicySummary
<a name="API_ConfigurationPolicySummary"></a>

 An object that contains the details of an AWS Security Hub CSPM configuration policy that’s returned in a `ListConfigurationPolicies` request.

## Contents
<a name="API_ConfigurationPolicySummary_Contents"></a>

 ** Arn **   <a name="securityhub-Type-ConfigurationPolicySummary-Arn"></a>
 The Amazon Resource Name (ARN) of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-ConfigurationPolicySummary-Description"></a>
 The description of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Id **   <a name="securityhub-Type-ConfigurationPolicySummary-Id"></a>
 The universally unique identifier (UUID) of the configuration policy.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-ConfigurationPolicySummary-Name"></a>
 The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: `-, ., !, *, /`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ServiceEnabled **   <a name="securityhub-Type-ConfigurationPolicySummary-ServiceEnabled"></a>
 Indicates whether the service that the configuration policy applies to is enabled in the policy.
Type: Boolean
Required: No

 ** UpdatedAt **   <a name="securityhub-Type-ConfigurationPolicySummary-UpdatedAt"></a>
 The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigurationPolicySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ConfigurationPolicySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ConfigurationPolicySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ConfigurationPolicySummary)

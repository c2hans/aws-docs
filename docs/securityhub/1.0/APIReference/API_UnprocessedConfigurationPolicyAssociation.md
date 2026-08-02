---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UnprocessedConfigurationPolicyAssociation.html
---

# UnprocessedConfigurationPolicyAssociation
<a name="API_UnprocessedConfigurationPolicyAssociation"></a>

 An array of configuration policy associations, one for each configuration policy association identifier, that was specified in a `BatchGetConfigurationPolicyAssociations` request but couldn’t be processed due to an error.

## Contents
<a name="API_UnprocessedConfigurationPolicyAssociation_Contents"></a>

 ** ConfigurationPolicyAssociationIdentifiers **   <a name="securityhub-Type-UnprocessedConfigurationPolicyAssociation-ConfigurationPolicyAssociationIdentifiers"></a>
 Configuration policy association identifiers that were specified in a `BatchGetConfigurationPolicyAssociations` request but couldn’t be processed due to an error.
Type: [ConfigurationPolicyAssociation](API_ConfigurationPolicyAssociation.md) object
Required: No

 ** ErrorCode **   <a name="securityhub-Type-UnprocessedConfigurationPolicyAssociation-ErrorCode"></a>
 An HTTP status code that identifies why the configuration policy association failed.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ErrorReason **   <a name="securityhub-Type-UnprocessedConfigurationPolicyAssociation-ErrorReason"></a>
 A string that identifies why the configuration policy association failed.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_UnprocessedConfigurationPolicyAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UnprocessedConfigurationPolicyAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UnprocessedConfigurationPolicyAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UnprocessedConfigurationPolicyAssociation)

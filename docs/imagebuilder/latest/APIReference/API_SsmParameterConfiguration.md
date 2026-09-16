---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_SsmParameterConfiguration.html
---

# SsmParameterConfiguration
<a name="API_SsmParameterConfiguration"></a>

Configuration for a single Parameter in the AWS Systems Manager (SSM) Parameter Store in a given Region.

## Contents
<a name="API_SsmParameterConfiguration_Contents"></a>

 ** parameterName **   <a name="imagebuilder-Type-SsmParameterConfiguration-parameterName"></a>
This is the name of the Parameter in the target Region or account. The image distribution creates the Parameter if it doesn't already exist. Otherwise, it updates the parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^[a-zA-Z0-9_.\-\/]+$`
Required: Yes

 ** amiAccountId **   <a name="imagebuilder-Type-SsmParameterConfiguration-amiAccountId"></a>
Specify the account that will own the Parameter in a given Region. During distribution, this account must be specified in distribution settings as a target account for the Region.
Type: String
Pattern: `^[0-9]{12}$`
Required: No

 ** dataType **   <a name="imagebuilder-Type-SsmParameterConfiguration-dataType"></a>
The type of value the parameter contains. We recommend the `aws:ec2:image` data type.
Type: String
Valid Values: `text | aws:ec2:image`
Required: No

## See Also
<a name="API_SsmParameterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/SsmParameterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/SsmParameterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/SsmParameterConfiguration)

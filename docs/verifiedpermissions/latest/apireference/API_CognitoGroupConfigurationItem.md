---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoGroupConfigurationItem.html
---

# CognitoGroupConfigurationItem
<a name="API_CognitoGroupConfigurationItem"></a>

The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.

This data type is part of an [CognitoUserPoolConfigurationItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CognitoUserPoolConfigurationDetail.html) structure and is a response parameter to [ListIdentitySources](http://forums.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListIdentitySources.html).

## Contents
<a name="API_CognitoGroupConfigurationItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** groupEntityType **   <a name="verifiedpermissions-Type-CognitoGroupConfigurationItem-groupEntityType"></a>
The name of the schema entity type that's mapped to the user pool group. Defaults to `AWS::CognitoGroup`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `([_a-zA-Z][_a-zA-Z0-9]*::)*[_a-zA-Z][_a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_CognitoGroupConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CognitoGroupConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CognitoGroupConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CognitoGroupConfigurationItem)

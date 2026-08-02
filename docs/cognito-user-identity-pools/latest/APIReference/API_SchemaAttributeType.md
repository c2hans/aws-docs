---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SchemaAttributeType.html
---

# SchemaAttributeType
<a name="API_SchemaAttributeType"></a>

A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a `custom:` prefix, and developer attributes with a `dev:` prefix. For more information, see [User pool attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html).

Developer-only `dev:` attributes are a legacy feature of user pools, and are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_SchemaAttributeType_Contents"></a>

 ** AttributeDataType **   <a name="CognitoUserPools-Type-SchemaAttributeType-AttributeDataType"></a>
The data format of the values for your attribute. When you choose an `AttributeDataType`, Amazon Cognito validates the input against the data type. A custom attribute value in your user's ID token is always a string, for example `"custom:isMember" : "true"` or `"custom:YearsAsMember" : "12"`.
Type: String
Valid Values: `String | Number | DateTime | Boolean`
Required: No

 ** DeveloperOnlyAttribute **   <a name="CognitoUserPools-Type-SchemaAttributeType-DeveloperOnlyAttribute"></a>
You should use [WriteAttributes](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolClientType.html#CognitoUserPools-Type-UserPoolClientType-WriteAttributes) in the user pool client to control how attributes can be mutated for new use cases instead of using `DeveloperOnlyAttribute`.
Specifies whether the attribute type is developer only. This attribute can only be modified by an administrator. Users won't be able to modify this attribute using their access token. For example, `DeveloperOnlyAttribute` can be modified using AdminUpdateUserAttributes but can't be updated using UpdateUserAttributes.
Type: Boolean
Required: No

 ** Mutable **   <a name="CognitoUserPools-Type-SchemaAttributeType-Mutable"></a>
Specifies whether the value of the attribute can be changed.
Any user pool attribute whose value you map from an IdP attribute must be mutable, with a parameter value of `true`. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If an attribute is immutable, Amazon Cognito throws an error when it attempts to update the attribute. For more information, see [Specifying Identity Provider Attribute Mappings for Your User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html).
Type: Boolean
Required: No

 ** Name **   <a name="CognitoUserPools-Type-SchemaAttributeType-Name"></a>
The name of your user pool attribute. When you create or update a user pool, adding a schema attribute creates a custom or developer-only attribute. When you add an attribute with a `Name` value of `MyAttribute`, Amazon Cognito creates the custom attribute `custom:MyAttribute`. When `DeveloperOnlyAttribute` is `true`, Amazon Cognito creates your attribute as `dev:MyAttribute`. In an operation that describes a user pool, Amazon Cognito returns this value as `value` for standard attributes, `custom:value` for custom attributes, and `dev:value` for developer-only attributes..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** NumberAttributeConstraints **   <a name="CognitoUserPools-Type-SchemaAttributeType-NumberAttributeConstraints"></a>
Specifies the constraints for an attribute of the number type.
Type: [NumberAttributeConstraintsType](API_NumberAttributeConstraintsType.md) object
Required: No

 ** Required **   <a name="CognitoUserPools-Type-SchemaAttributeType-Required"></a>
Specifies whether a user pool attribute is required. If the attribute is required and the user doesn't provide a value, registration or sign-in will fail.
Type: Boolean
Required: No

 ** StringAttributeConstraints **   <a name="CognitoUserPools-Type-SchemaAttributeType-StringAttributeConstraints"></a>
Specifies the constraints for an attribute of the string type.
Type: [StringAttributeConstraintsType](API_StringAttributeConstraintsType.md) object
Required: No

## See Also
<a name="API_SchemaAttributeType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SchemaAttributeType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SchemaAttributeType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SchemaAttributeType)

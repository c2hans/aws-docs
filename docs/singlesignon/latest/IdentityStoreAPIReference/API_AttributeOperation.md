---
source_url: https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_AttributeOperation.html
---

# AttributeOperation
<a name="API_AttributeOperation"></a>

An operation that applies to the requested group. This operation might add, replace, or remove an attribute.

## Contents
<a name="API_AttributeOperation_Contents"></a>

 ** AttributePath **   <a name="singlesignon-Type-AttributeOperation-AttributePath"></a>
A string representation of the path to a given attribute or sub-attribute. Supports JMESPath.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:\p{L}+:\p{L}+:\p{L}+(?:\.\p{L}+){0,3}|\p{L}+(?:\.\p{L}+){0,2})`
Required: Yes

 ** AttributeValue **   <a name="singlesignon-Type-AttributeOperation-AttributeValue"></a>
The value of the attribute. This is a `Document` type. This type is not supported by Java V1, Go V1, and older versions of the AWS CLI.
Type: JSON value
Required: No

## See Also
<a name="API_AttributeOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/identitystore-2020-06-15/AttributeOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/identitystore-2020-06-15/AttributeOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/identitystore-2020-06-15/AttributeOperation)

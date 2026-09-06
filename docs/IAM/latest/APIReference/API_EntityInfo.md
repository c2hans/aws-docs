---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_EntityInfo.html
---

# EntityInfo
<a name="API_EntityInfo"></a>

Contains details about the specified entity (user or role).

This data type is an element of the [EntityDetails](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EntityDetails.html) object.

## Contents
<a name="API_EntityInfo_Contents"></a>

 ** Arn **
The Amazon Resource Name (ARN). ARNs are unique identifiers for AWS resources.
For more information about ARNs, go to [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** Id **
The identifier of the entity (user or role).
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w]+`
Required: Yes

 ** Name **
The name of the entity (user or role).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

 ** Type **
The type of entity (user or role).
Type: String
Valid Values: `USER | ROLE | GROUP`
Required: Yes

 ** Path **
The path to the entity (user or role). For more information about paths, see [IAM identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `(\u002F)|(\u002F[\u0021-\u007E]+\u002F)`
Required: No

## See Also
<a name="API_EntityInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/EntityInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/EntityInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/EntityInfo)

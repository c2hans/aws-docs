---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Permission.html
---

# Permission
<a name="API_Permission"></a>

Contains information on the permissions an account has within Amazon Inspector.

## Contents
<a name="API_Permission_Contents"></a>

 ** operation **   <a name="inspector2-Type-Permission-operation"></a>
The operations that can be performed with the given permissions.
Type: String
Valid Values: `ENABLE_SCANNING | DISABLE_SCANNING | ENABLE_REPOSITORY | DISABLE_REPOSITORY`
Required: Yes

 ** service **   <a name="inspector2-Type-Permission-service"></a>
The services that the permissions allow an account to perform the given operations for.
Type: String
Valid Values: `EC2 | ECR | LAMBDA`
Required: Yes

## See Also
<a name="API_Permission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Permission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Permission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Permission)

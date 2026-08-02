---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UserContext.html
---

# UserContext
<a name="API_UserContext"></a>

Information about the user who created or modified a SageMaker resource.

## Contents
<a name="API_UserContext_Contents"></a>

 ** DomainId **   <a name="sagemaker-Type-UserContext-DomainId"></a>
The domain associated with the user.
Type: String
Required: No

 ** IamIdentity **   <a name="sagemaker-Type-UserContext-IamIdentity"></a>
The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.
Type: [IamIdentity](API_IamIdentity.md) object
Required: No

 ** UserProfileArn **   <a name="sagemaker-Type-UserContext-UserProfileArn"></a>
The Amazon Resource Name (ARN) of the user's profile.
Type: String
Required: No

 ** UserProfileName **   <a name="sagemaker-Type-UserContext-UserProfileName"></a>
The name of the user's profile.
Type: String
Required: No

## See Also
<a name="API_UserContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UserContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UserContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UserContext)

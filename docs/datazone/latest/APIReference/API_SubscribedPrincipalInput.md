---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedPrincipalInput.html
---

# SubscribedPrincipalInput
<a name="API_SubscribedPrincipalInput"></a>

The principal that is to be given a subscriptiong grant.

## Contents
<a name="API_SubscribedPrincipalInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="datazone-Type-SubscribedPrincipalInput-group"></a>
The subscribed group.
Type: [SubscribedGroupInput](API_SubscribedGroupInput.md) object
Required: No

 ** iam **   <a name="datazone-Type-SubscribedPrincipalInput-iam"></a>
The subscribed IAM principal.
Type: [SubscribedIamPrincipalInput](API_SubscribedIamPrincipalInput.md) object
Required: No

 ** project **   <a name="datazone-Type-SubscribedPrincipalInput-project"></a>
The project that is to be given a subscription grant.
Type: [SubscribedProjectInput](API_SubscribedProjectInput.md) object
Required: No

 ** user **   <a name="datazone-Type-SubscribedPrincipalInput-user"></a>
The subscribed user.
Type: [SubscribedUserInput](API_SubscribedUserInput.md) object
Required: No

## See Also
<a name="API_SubscribedPrincipalInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedPrincipalInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedPrincipalInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedPrincipalInput)

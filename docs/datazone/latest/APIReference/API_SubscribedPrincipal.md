---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedPrincipal.html
---

# SubscribedPrincipal
<a name="API_SubscribedPrincipal"></a>

The principal that has the subscription grant for the asset.

## Contents
<a name="API_SubscribedPrincipal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="datazone-Type-SubscribedPrincipal-group"></a>
The subscribed group.
Type: [SubscribedGroup](API_SubscribedGroup.md) object
Required: No

 ** iam **   <a name="datazone-Type-SubscribedPrincipal-iam"></a>
The subscribed IAM principal.
Type: [SubscribedIamPrincipal](API_SubscribedIamPrincipal.md) object
Required: No

 ** project **   <a name="datazone-Type-SubscribedPrincipal-project"></a>
The project that has the subscription grant.
Type: [SubscribedProject](API_SubscribedProject.md) object
Required: No

 ** user **   <a name="datazone-Type-SubscribedPrincipal-user"></a>
The subscribed user.
Type: [SubscribedUser](API_SubscribedUser.md) object
Required: No

## See Also
<a name="API_SubscribedPrincipal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedPrincipal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedPrincipal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedPrincipal)

---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceOwner.html
---

# ResourceOwner
<a name="API_ResourceOwner"></a>

Information about the owner of a resource, including the account and organization that the resource belongs to.

## Contents
<a name="API_ResourceOwner_Contents"></a>

 ** Account **   <a name="securityhub-Type-ResourceOwner-Account"></a>
Information about the account that owns the resource, for example, an Azure Subscription or AWS Account.
Type: [ResourceOwnerAccount](API_ResourceOwnerAccount.md) object
Required: No

 ** Org **   <a name="securityhub-Type-ResourceOwner-Org"></a>
Information about the organization that owns the resource, for example, an Azure Tenant.
Type: [ResourceOwnerOrg](API_ResourceOwnerOrg.md) object
Required: No

## See Also
<a name="API_ResourceOwner_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceOwner)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceOwner)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceOwner)

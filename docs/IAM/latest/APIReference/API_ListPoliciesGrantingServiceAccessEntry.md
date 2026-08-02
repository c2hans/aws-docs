---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccessEntry.html
---

# ListPoliciesGrantingServiceAccessEntry
<a name="API_ListPoliciesGrantingServiceAccessEntry"></a>

Contains details about the permissions policies that are attached to the specified identity (user, group, or role).

This data type is used as a response element in the [ListPoliciesGrantingServiceAccess](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListPoliciesGrantingServiceAccess.html) operation.

## Contents
<a name="API_ListPoliciesGrantingServiceAccessEntry_Contents"></a>

 ** Policies.member.N **
The `PoliciesGrantingServiceAccess` object that contains details about the policy.
Type: Array of [PolicyGrantingServiceAccess](API_PolicyGrantingServiceAccess.md) objects
Required: No

 ** ServiceNamespace **
The namespace of the service that was accessed.
To learn the service namespace of a service, see [Actions, resources, and condition keys for AWS services](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) in the *Service Authorization Reference*. Choose the name of the service to view details for that service. In the first paragraph, find the service prefix. For example, `(service prefix: a4b)`. For more information about service namespaces, see [AWS service namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w-]*`
Required: No

## See Also
<a name="API_ListPoliciesGrantingServiceAccessEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListPoliciesGrantingServiceAccessEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListPoliciesGrantingServiceAccessEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListPoliciesGrantingServiceAccessEntry)

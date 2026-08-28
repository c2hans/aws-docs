---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_EntitlementAttribute.html
---

# EntitlementAttribute
<a name="API_EntitlementAttribute"></a>

An attribute associated with an entitlement. Application entitlements work by matching a supported SAML 2.0 attribute name to a value when a user identity federates to a WorkSpaces Applications SAML application.

## Contents
<a name="API_EntitlementAttribute_Contents"></a>

 ** Name **   <a name="WorkSpacesApplications-Type-EntitlementAttribute-Name"></a>
A supported AWS IAM SAML `PrincipalTag` attribute that is matched to the associated value when a user identity federates into a WorkSpaces Applications SAML application.
The following are valid values:
+ roles
+ department
+ organization
+ groups
+ title
+ costCenter
+ userType

Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Value **   <a name="WorkSpacesApplications-Type-EntitlementAttribute-Value"></a>
A value that is matched to a supported SAML attribute name when a user identity federates into a WorkSpaces Applications SAML application.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_EntitlementAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/EntitlementAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/EntitlementAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/EntitlementAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

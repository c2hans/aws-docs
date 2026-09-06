---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_Entitlement.html
---

# Entitlement
<a name="API_Entitlement"></a>

Specifies an entitlement. Entitlements control access to specific applications within a stack, based on user attributes. Entitlements apply to SAML 2.0 federated user identities. WorkSpaces Applications user pool and streaming URL users are entitled to all applications in a stack. Entitlements don't apply to the desktop stream view application, or to applications managed by a dynamic app provider using the Dynamic Application Framework.

## Contents
<a name="API_Entitlement_Contents"></a>

 ** AppVisibility **   <a name="WorkSpacesApplications-Type-Entitlement-AppVisibility"></a>
Specifies whether all or selected apps are entitled.
Type: String
Valid Values: `ALL | ASSOCIATED`
Required: Yes

 ** Attributes **   <a name="WorkSpacesApplications-Type-Entitlement-Attributes"></a>
The attributes of the entitlement.
Type: Array of [EntitlementAttribute](API_EntitlementAttribute.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

 ** Name **   <a name="WorkSpacesApplications-Type-Entitlement-Name"></a>
The name of the entitlement.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** StackName **   <a name="WorkSpacesApplications-Type-Entitlement-StackName"></a>
The name of the stack with which the entitlement is associated.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** CreatedTime **   <a name="WorkSpacesApplications-Type-Entitlement-CreatedTime"></a>
The time when the entitlement was created.
Type: Timestamp
Required: No

 ** Description **   <a name="WorkSpacesApplications-Type-Entitlement-Description"></a>
The description of the entitlement.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** LastModifiedTime **   <a name="WorkSpacesApplications-Type-Entitlement-LastModifiedTime"></a>
The time when the entitlement was last modified.
Type: Timestamp
Required: No

## See Also
<a name="API_Entitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/Entitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/Entitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/Entitlement)

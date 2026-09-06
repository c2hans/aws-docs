---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Link.html
---

# Link
<a name="API_Link"></a>

Describes a link.

## Contents
<a name="API_Link_Contents"></a>

 ** Bandwidth **   <a name="networkmanager-Type-Link-Bandwidth"></a>
The bandwidth for the link.
Type: [Bandwidth](API_Bandwidth.md) object
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-Link-CreatedAt"></a>
The date and time that the link was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-Link-Description"></a>
The description of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-Link-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** LinkArn **   <a name="networkmanager-Type-Link-LinkArn"></a>
The Amazon Resource Name (ARN) of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** LinkId **   <a name="networkmanager-Type-Link-LinkId"></a>
The ID of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** Provider **   <a name="networkmanager-Type-Link-Provider"></a>
The provider of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** SiteId **   <a name="networkmanager-Type-Link-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Link-State"></a>
The state of the link.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Link-Tags"></a>
The tags for the link.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** Type **   <a name="networkmanager-Type-Link-Type"></a>
The type of the link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_Link_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Link)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Link)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Link)

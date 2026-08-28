---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Site.html
---

# Site
<a name="API_Site"></a>

Describes a site.

## Contents
<a name="API_Site_Contents"></a>

 ** CreatedAt **   <a name="networkmanager-Type-Site-CreatedAt"></a>
The date and time that the site was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-Site-Description"></a>
The description of the site.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-Site-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** Location **   <a name="networkmanager-Type-Site-Location"></a>
The location of the site.
Type: [Location](API_Location.md) object
Required: No

 ** SiteArn **   <a name="networkmanager-Type-Site-SiteArn"></a>
The Amazon Resource Name (ARN) of the site.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** SiteId **   <a name="networkmanager-Type-Site-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Site-State"></a>
The state of the site.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Site-Tags"></a>
The tags for the site.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Site_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Site)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Site)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Site)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

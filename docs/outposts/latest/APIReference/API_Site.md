---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Site.html
---

# Site
<a name="API_Site"></a>

Information about a site.

## Contents
<a name="API_Site_Contents"></a>

 ** AccountId **   <a name="outposts-Type-Site-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Description **   <a name="outposts-Type-Site-Description"></a>
The description of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1001.
Pattern: `^[\S ]+$`
Required: No

 ** Name **   <a name="outposts-Type-Site-Name"></a>
The name of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[\S ]+$`
Required: No

 ** Notes **   <a name="outposts-Type-Site-Notes"></a>
 Notes about a site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `^[\S \n]+$`
Required: No

 ** OperatingAddressCity **   <a name="outposts-Type-Site-OperatingAddressCity"></a>
 City where the hardware is installed and powered on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`
Required: No

 ** OperatingAddressCountryCode **   <a name="outposts-Type-Site-OperatingAddressCountryCode"></a>
 The ISO-3166 two-letter country code where the hardware is installed and powered on.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `^[A-Z]{2}$`
Required: No

 ** OperatingAddressStateOrRegion **   <a name="outposts-Type-Site-OperatingAddressStateOrRegion"></a>
 State or region where the hardware is installed and powered on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S[\S ]*$`
Required: No

 ** RackPhysicalProperties **   <a name="outposts-Type-Site-RackPhysicalProperties"></a>
 Information about the physical and logistical details for a rack at the site.
Type: [RackPhysicalProperties](API_RackPhysicalProperties.md) object
Required: No

 ** SiteArn **   <a name="outposts-Type-Site-SiteArn"></a>
The Amazon Resource Name (ARN) of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/(os-[a-f0-9]{17})$`
Required: No

 ** SiteId **   <a name="outposts-Type-Site-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: No

 ** Tags **   <a name="outposts-Type-Site-Tags"></a>
The site tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_Site_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Site)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Site)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Site)

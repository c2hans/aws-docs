---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/APIReference/API_WebContentFilteringPolicy.html
---

# WebContentFilteringPolicy
<a name="API_WebContentFilteringPolicy"></a>

The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.

## Contents
<a name="API_WebContentFilteringPolicy_Contents"></a>

 ** allowedUrls **   <a name="workspacesweb-Type-WebContentFilteringPolicy-allowedUrls"></a>
URLs and domains that are always accessible to end users.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

 ** blockedCategories **   <a name="workspacesweb-Type-WebContentFilteringPolicy-blockedCategories"></a>
Categories of websites that are blocked on the end user’s browsers.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `Cults | Gambling | Nudity | Pornography | SexEducation | Tasteless | Violence | DownloadSites | ImageSharing | PeerToPeer | StreamingMediaAndDownloads | GenerativeAI | CriminalActivity | Hacking | HateAndIntolerance | IllegalDrug | IllegalSoftware | SchoolCheating | SelfHarm | Weapons | Chat | Games | InstantMessaging | ProfessionalNetwork | SocialNetworking | WebBasedEmail | ParkedDomains`
Required: No

 ** blockedUrls **   <a name="workspacesweb-Type-WebContentFilteringPolicy-blockedUrls"></a>
URLs and domains that end users cannot access.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 1000 items.
Pattern: `((([a-zA-Z][a-zA-Z0-9+.-]*):\/\/(\*|[\w%._\-\+~#=@]+)?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?)|(\*|[\w%._\-\+~#=@]+\.[\w%._\-\+~#=@]+)(?::(\d{1,5}))?(\/[^@\s]*)?(?:\?([^*\s]+(?:\*?)))?|(([a-zA-Z][a-zA-Z0-9+.-]*):(\/\/)?\*))`
Required: No

## See Also
<a name="API_WebContentFilteringPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-web-2020-07-08/WebContentFilteringPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-web-2020-07-08/WebContentFilteringPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-web-2020-07-08/WebContentFilteringPolicy)

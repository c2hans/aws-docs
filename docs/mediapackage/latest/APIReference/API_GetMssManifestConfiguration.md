---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetMssManifestConfiguration.html
---

# GetMssManifestConfiguration
<a name="API_GetMssManifestConfiguration"></a>

Configuration details for a Microsoft Smooth Streaming (MSS) manifest associated with an origin endpoint. This includes all the settings and properties that define how the MSS content is packaged and delivered.

## Contents
<a name="API_GetMssManifestConfiguration_Contents"></a>

 ** ManifestName **   <a name="mediapackage-Type-GetMssManifestConfiguration-ManifestName"></a>
The name of the MSS manifest. This name is appended to the origin endpoint URL to create the unique path for accessing this specific MSS manifest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** Url **   <a name="mediapackage-Type-GetMssManifestConfiguration-Url"></a>
The complete URL for accessing the MSS manifest. Client players use this URL to retrieve the manifest and begin streaming the Microsoft Smooth Streaming content.
Type: String
Required: Yes

 ** FilterConfiguration **   <a name="mediapackage-Type-GetMssManifestConfiguration-FilterConfiguration"></a>
Filter configuration includes settings for manifest filtering, start and end times, and time delay that apply to all of your egress requests for this manifest.
Type: [FilterConfiguration](API_FilterConfiguration.md) object
Required: No

 ** ManifestLayout **   <a name="mediapackage-Type-GetMssManifestConfiguration-ManifestLayout"></a>
The layout format of the MSS manifest, which determines how the manifest is structured for client compatibility.
Type: String
Valid Values: `FULL | COMPACT`
Required: No

 ** ManifestWindowSeconds **   <a name="mediapackage-Type-GetMssManifestConfiguration-ManifestWindowSeconds"></a>
The duration (in seconds) of the manifest window. This represents the total amount of content available in the manifest at any given time.
Type: Integer
Required: No

## See Also
<a name="API_GetMssManifestConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetMssManifestConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetMssManifestConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetMssManifestConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

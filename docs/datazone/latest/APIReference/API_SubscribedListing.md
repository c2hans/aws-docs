---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedListing.html
---

# SubscribedListing
<a name="API_SubscribedListing"></a>

The details of the published asset for which the subscription grant is created.

## Contents
<a name="API_SubscribedListing_Contents"></a>

 ** description **   <a name="datazone-Type-SubscribedListing-description"></a>
The description of the published asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** id **   <a name="datazone-Type-SubscribedListing-id"></a>
The identifier of the published asset for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** item **   <a name="datazone-Type-SubscribedListing-item"></a>
The published asset for which the subscription grant is created.
Type: [SubscribedListingItem](API_SubscribedListingItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** name **   <a name="datazone-Type-SubscribedListing-name"></a>
The name of the published asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** ownerProjectId **   <a name="datazone-Type-SubscribedListing-ownerProjectId"></a>
The identifier of the project of the published asset for which the subscription grant is created.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** ownerProjectName **   <a name="datazone-Type-SubscribedListing-ownerProjectName"></a>
The name of the project that owns the published asset for which the subscription grant is created.
Type: String
Required: No

 ** revision **   <a name="datazone-Type-SubscribedListing-revision"></a>
The revision of the published asset for which the subscription grant is created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_SubscribedListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedListing)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

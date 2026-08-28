---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_SpaceData.html
---

# SpaceData
<a name="API_SpaceData"></a>

A structure that contains some information about a private re:Post in the account.

## Contents
<a name="API_SpaceData_Contents"></a>

 ** arn **   <a name="repostprivate-Type-SpaceData-arn"></a>
The ARN of the private re:Post.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** configurationStatus **   <a name="repostprivate-Type-SpaceData-configurationStatus"></a>
The configuration status of the private re:Post.
Type: String
Valid Values: `CONFIGURED | UNCONFIGURED`
Required: Yes

 ** createDateTime **   <a name="repostprivate-Type-SpaceData-createDateTime"></a>
The date when the private re:Post was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="repostprivate-Type-SpaceData-name"></a>
The name for the private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: Yes

 ** randomDomain **   <a name="repostprivate-Type-SpaceData-randomDomain"></a>
The AWS generated subdomain of the private re:Post.
Type: String
Required: Yes

 ** spaceId **   <a name="repostprivate-Type-SpaceData-spaceId"></a>
The unique ID of the private re:Post.
Type: String
Required: Yes

 ** status **   <a name="repostprivate-Type-SpaceData-status"></a>
The creation/deletion status of the private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: Yes

 ** storageLimit **   <a name="repostprivate-Type-SpaceData-storageLimit"></a>
The storage limit of the private re:Post.
Type: Long
Required: Yes

 ** tier **   <a name="repostprivate-Type-SpaceData-tier"></a>
The pricing tier of the private re:Post.
Type: String
Valid Values: `BASIC | STANDARD`
Required: Yes

 ** vanityDomain **   <a name="repostprivate-Type-SpaceData-vanityDomain"></a>
This custom subdomain that you use to access your private re:Post. All custom subdomains must be approved by AWS before use.
Type: String
Required: Yes

 ** vanityDomainStatus **   <a name="repostprivate-Type-SpaceData-vanityDomainStatus"></a>
This approval status of the custom subdomain.
Type: String
Valid Values: `PENDING | APPROVED | UNAPPROVED`
Required: Yes

 ** contentSize **   <a name="repostprivate-Type-SpaceData-contentSize"></a>
The content size of the private re:Post.
Type: Long
Required: No

 ** deleteDateTime **   <a name="repostprivate-Type-SpaceData-deleteDateTime"></a>
The date when the private re:Post was deleted.
Type: Timestamp
Required: No

 ** description **   <a name="repostprivate-Type-SpaceData-description"></a>
The description for the private re:Post. This is used only to help you identify this private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** supportedEmailDomains **   <a name="repostprivate-Type-SpaceData-supportedEmailDomains"></a>

Type: [SupportedEmailDomainsStatus](API_SupportedEmailDomainsStatus.md) object
Required: No

 ** userCount **   <a name="repostprivate-Type-SpaceData-userCount"></a>
The number of onboarded users to the private re:Post.
Type: Integer
Required: No

 ** userKMSKey **   <a name="repostprivate-Type-SpaceData-userKMSKey"></a>
The custom AWS KMS key ARN that’s used for the AWS KMS encryption.
Type: String
Required: No

## See Also
<a name="API_SpaceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/SpaceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/SpaceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/SpaceData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS re:Post Private. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query repostprivate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

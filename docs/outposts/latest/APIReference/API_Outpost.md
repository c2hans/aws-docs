---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_Outpost.html
---

# Outpost
<a name="API_Outpost"></a>

Information about an Outpost.

## Contents
<a name="API_Outpost_Contents"></a>

 ** AvailabilityZone **   <a name="outposts-Type-Outpost-AvailabilityZone"></a>
The Availability Zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^([a-zA-Z]+-){1,3}([a-zA-Z]+)?(\d+[a-zA-Z]?)?$`
Required: No

 ** AvailabilityZoneId **   <a name="outposts-Type-Outpost-AvailabilityZoneId"></a>
The ID of the Availability Zone.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+\d-[a-zA-Z]+\d$`
Required: No

 ** Description **   <a name="outposts-Type-Outpost-Description"></a>
The description of the Outpost.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^[\S ]*$`
Required: No

 ** LifeCycleStatus **   <a name="outposts-Type-Outpost-LifeCycleStatus"></a>
The life cycle status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[ A-Za-z]+$`
Required: No

 ** Name **   <a name="outposts-Type-Outpost-Name"></a>
The name of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\S ]+$`
Required: No

 ** OutpostArn **   <a name="outposts-Type-Outpost-OutpostArn"></a>
The Amazon Resource Name (ARN) of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** OutpostId **   <a name="outposts-Type-Outpost-OutpostId"></a>
 The ID of the Outpost.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: No

 ** OwnerId **   <a name="outposts-Type-Outpost-OwnerId"></a>
The AWS account ID of the Outpost owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** SiteArn **   <a name="outposts-Type-Outpost-SiteArn"></a>
The Amazon Resource Name (ARN) of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/(os-[a-f0-9]{17})$`
Required: No

 ** SiteId **   <a name="outposts-Type-Outpost-SiteId"></a>
The ID of the site.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:site/)?(os-[a-f0-9]{17})$`
Required: No

 ** SupportedHardwareType **   <a name="outposts-Type-Outpost-SupportedHardwareType"></a>
 The hardware type.
Type: String
Valid Values: `RACK | SERVER`
Required: No

 ** Tags **   <a name="outposts-Type-Outpost-Tags"></a>
The Outpost tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^[\S \n]+$`
Required: No

## See Also
<a name="API_Outpost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/Outpost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/Outpost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/Outpost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

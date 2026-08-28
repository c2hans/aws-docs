---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_PackageListItem.html
---

# PackageListItem
<a name="API_PackageListItem"></a>

A package summary.

## Contents
<a name="API_PackageListItem_Contents"></a>

 ** Arn **   <a name="panorama-Type-PackageListItem-Arn"></a>
The package's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** CreatedTime **   <a name="panorama-Type-PackageListItem-CreatedTime"></a>
When the package was created.
Type: Timestamp
Required: No

 ** PackageId **   <a name="panorama-Type-PackageListItem-PackageId"></a>
The package's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_\/]+`
Required: No

 ** PackageName **   <a name="panorama-Type-PackageListItem-PackageName"></a>
The package's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** Tags **   <a name="panorama-Type-PackageListItem-Tags"></a>
The package's tags.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

## See Also
<a name="API_PackageListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/PackageListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/PackageListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/PackageListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

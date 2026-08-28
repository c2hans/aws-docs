---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

This structure contains information about one group.

## Contents
<a name="API_Group_Contents"></a>

 ** Arn **   <a name="synthetics-Type-Group-Arn"></a>
The ARN of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:group:[0-9a-z]+`
Required: No

 ** CreatedTime **   <a name="synthetics-Type-Group-CreatedTime"></a>
The date and time that the group was created.
Type: Timestamp
Required: No

 ** Id **   <a name="synthetics-Type-Group-Id"></a>
The unique ID of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="synthetics-Type-Group-LastModifiedTime"></a>
The date and time that the group was most recently updated.
Type: Timestamp
Required: No

 ** Name **   <a name="synthetics-Type-Group-Name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Tags **   <a name="synthetics-Type-Group-Tags"></a>
The list of key-value pairs that are associated with the canary.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/Group)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_RulesetItem.html
---

# RulesetItem
<a name="API_RulesetItem"></a>

Contains metadata about the ruleset.

## Contents
<a name="API_RulesetItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-RulesetItem-Name"></a>
The name of the ruleset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** TargetArn **   <a name="databrew-Type-RulesetItem-TargetArn"></a>
The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** AccountId **   <a name="databrew-Type-RulesetItem-AccountId"></a>
The ID of the AWS account that owns the ruleset.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** CreateDate **   <a name="databrew-Type-RulesetItem-CreateDate"></a>
The date and time that the ruleset was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="databrew-Type-RulesetItem-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the ruleset.
Type: String
Required: No

 ** Description **   <a name="databrew-Type-RulesetItem-Description"></a>
The description of the ruleset.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** LastModifiedBy **   <a name="databrew-Type-RulesetItem-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last modified the ruleset.
Type: String
Required: No

 ** LastModifiedDate **   <a name="databrew-Type-RulesetItem-LastModifiedDate"></a>
The modification date and time of the ruleset.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="databrew-Type-RulesetItem-ResourceArn"></a>
The Amazon Resource Name (ARN) for the ruleset.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** RuleCount **   <a name="databrew-Type-RulesetItem-RuleCount"></a>
The number of rules that are defined in the ruleset.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Tags **   <a name="databrew-Type-RulesetItem-Tags"></a>
Metadata tags that have been applied to the ruleset.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_RulesetItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/RulesetItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/RulesetItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/RulesetItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

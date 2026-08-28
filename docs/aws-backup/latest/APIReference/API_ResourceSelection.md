---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ResourceSelection.html
---

# ResourceSelection
<a name="API_ResourceSelection"></a>

This contains metadata about resource selection for tiering configurations.

You can specify up to 5 different resource selections per tiering configuration. Data moved to lower-cost tier remains there until deletion (one-way transition).

## Contents
<a name="API_ResourceSelection_Contents"></a>

 ** Resources **   <a name="Backup-Type-ResourceSelection-Resources"></a>
An array of strings that either contains ARNs of the associated resources or contains a wildcard `*` to specify all resources. You can specify up to 100 specific resources per tiering configuration.
Type: Array of strings
Required: Yes

 ** ResourceType **   <a name="Backup-Type-ResourceSelection-ResourceType"></a>
The type of AWS resource; for example, `S3` for Amazon S3. For tiering configurations, this is currently limited to `S3`.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: Yes

 ** TieringDownSettingsInDays **   <a name="Backup-Type-ResourceSelection-TieringDownSettingsInDays"></a>
The number of days after creation within a backup vault that an object can transition to the low cost warm storage tier. Must be a positive integer between 60 and 36500 days.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 36500.
Required: Yes

## See Also
<a name="API_ResourceSelection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ResourceSelection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ResourceSelection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ResourceSelection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TagValues.html
---

# TagValues

The values that are available for a tag.

In operations that support `ABSENT`, such as `GetCostAndUsage`, you can filter on resources with no tags. Set `MatchOptions` to `ABSENT` and omit `Key` and `Values`. Not all operations support `ABSENT`. For example, `GetReservationCoverage` and `GetSavingsPlansCoverage` don't.

To filter on resources without a given tag key, set `MatchOptions` to `ABSENT`, specify the `Key`, and omit `Values`.

A `Key` without `Values` doesn't apply `ABSENT`. In Cost Explorer operations such as `GetCostAndUsage`, unless `MatchOptions` includes `ABSENT`, you must specify both `Key` and `Values`, or the request fails with a `ValidationException`.

If `MatchOptions` includes `ABSENT` and you also specify `Values`, the request fails with a `ValidationException`.

## Contents
<a name="API_TagValues_Contents"></a>

 ** Key **   <a name="awscostmanagement-Type-TagValues-Key"></a>
The key for the tag.
Specify user-defined tag keys without the `user:` prefix. For example, use `team`, not `user:team`. Tag keys that Amazon Web Services generates keep their `aws:` prefix.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** MatchOptions **   <a name="awscostmanagement-Type-TagValues-MatchOptions"></a>
The match options that you can use to filter your results. The supported values depend on the operation. Refer to the documentation for each specific API to see what is supported. For example, `GetCostAndUsage` supports the following values:
+  `EQUALS` - Matches values exactly.
+  `ABSENT` - Matches costs that don't have a value for the key.
+  `CASE_SENSITIVE` - Matches values with case sensitivity.
The default values for `MatchOptions` are `EQUALS` and `CASE_SENSITIVE`.
Type: Array of strings
Valid Values: `EQUALS | ABSENT | STARTS_WITH | ENDS_WITH | CONTAINS | CASE_SENSITIVE | CASE_INSENSITIVE | GREATER_THAN_OR_EQUAL`
Required: No

 ** Values **   <a name="awscostmanagement-Type-TagValues-Values"></a>
The specific value of the tag.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_TagValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/TagValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/TagValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/TagValues)

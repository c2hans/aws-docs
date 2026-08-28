---
source_url: https://docs.aws.amazon.com/mpa/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Contains the filter to apply to requests. You can specify up to 10 filters for a request.

## Contents
<a name="API_Filter_Contents"></a>

 ** FieldName **   <a name="mpa-Type-Filter-FieldName"></a>
Name of the filter to use.
 **Supported filters**
The supported filters for [ListSessions](API_ListSessions.md) are: `ActionName`, `SessionStatus`, and `InitationTime`.
Type: String
Valid Values: `ActionName | ApprovalTeamName | VotingTime | Vote | SessionStatus | InitiationTime`
Required: No

 ** Operator **   <a name="mpa-Type-Filter-Operator"></a>
Operator to use for filtering.
+  `EQ`: Equal to the specified value
+  `NE`: Not equal to the specified value
+  `GT`: Greater than the specified value
+  `LT`: Less than the specified value
+  `GTE`: Greater than or equal to the specified value
+  `LTE`: Less than or equal to the specified value
+  `CONTAINS`: Contains the specified value
+  `NOT_CONTAINS`: Does not contain the specified value
+  `BETWEEN`: Between two values, inclusive of the specified values.
 **Supported operators for each filter**:
+  `ActionName`: `EQ` \| `NE` \| `CONTAINS` \| `NOT_CONTAINS`
+  `SessionStatus`: `EQ` \| `NE`
+  `InitiationTime`: `GT` \| `LT` \| `GTE` \| `LTE` \| `BETWEEN`
Type: String
Valid Values: `EQ | NE | GT | LT | GTE | LTE | CONTAINS | NOT_CONTAINS | BETWEEN`
Required: No

 ** Value **   <a name="mpa-Type-Filter-Value"></a>
Value to use for filtering. For the `BETWEEN` operator, specify values in the format `a AND b` (`AND` is case-insensitive).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mpa-2022-07-26/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mpa-2022-07-26/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mpa-2022-07-26/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Multi-party approval. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mpa` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

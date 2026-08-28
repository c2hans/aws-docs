---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

Contains information about the condition.

## Contents
<a name="API_Condition_Contents"></a>

 ** eq **   <a name="guardduty-Type-Condition-eq"></a>
 *This member has been deprecated.*
Represents the *equal* condition to be applied to a single field when querying for findings.
Max values: 50
Type: Array of strings
Required: No

 ** equals **   <a name="guardduty-Type-Condition-equals"></a>
Represents an *equal* **** condition to be applied to a single field when querying for findings.
Max values: 50
Type: Array of strings
Required: No

 ** greaterThan **   <a name="guardduty-Type-Condition-greaterThan"></a>
Represents a *greater than* condition to be applied to a single field when querying for findings.
Type: Long
Required: No

 ** greaterThanOrEqual **   <a name="guardduty-Type-Condition-greaterThanOrEqual"></a>
Represents a *greater than or equal* condition to be applied to a single field when querying for findings.
Type: Long
Required: No

 ** gt **   <a name="guardduty-Type-Condition-gt"></a>
 *This member has been deprecated.*
Represents a *greater than* condition to be applied to a single field when querying for findings.
Type: Integer
Required: No

 ** gte **   <a name="guardduty-Type-Condition-gte"></a>
 *This member has been deprecated.*
Represents a *greater than or equal* condition to be applied to a single field when querying for findings.
Type: Integer
Required: No

 ** lessThan **   <a name="guardduty-Type-Condition-lessThan"></a>
Represents a *less than* condition to be applied to a single field when querying for findings.
Type: Long
Required: No

 ** lessThanOrEqual **   <a name="guardduty-Type-Condition-lessThanOrEqual"></a>
Represents a *less than or equal* condition to be applied to a single field when querying for findings.
Type: Long
Required: No

 ** lt **   <a name="guardduty-Type-Condition-lt"></a>
 *This member has been deprecated.*
Represents a *less than* condition to be applied to a single field when querying for findings.
Type: Integer
Required: No

 ** lte **   <a name="guardduty-Type-Condition-lte"></a>
 *This member has been deprecated.*
Represents a *less than or equal* condition to be applied to a single field when querying for findings.
Type: Integer
Required: No

 ** matches **   <a name="guardduty-Type-Condition-matches"></a>
Represents the *match* condition to be applied to a single field when querying for findings.
 The *matches* condition is available only for create-filter and update-filter APIs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** neq **   <a name="guardduty-Type-Condition-neq"></a>
 *This member has been deprecated.*
Represents the *not equal* condition to be applied to a single field when querying for findings.
Max values: 50
Type: Array of strings
Required: No

 ** notEquals **   <a name="guardduty-Type-Condition-notEquals"></a>
Represents a *not equal* **** condition to be applied to a single field when querying for findings.
Max values: 50
Type: Array of strings
Required: No

 ** notMatches **   <a name="guardduty-Type-Condition-notMatches"></a>
Represents the *not match* condition to be applied to a single field when querying for findings.
 The *not-matches* condition is available only for create-filter and update-filter APIs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Condition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

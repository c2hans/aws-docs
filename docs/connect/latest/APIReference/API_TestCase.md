---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TestCase.html
---

# TestCase
<a name="API_TestCase"></a>

Contains information about a test case.

## Contents
<a name="API_TestCase_Contents"></a>

 ** Arn **   <a name="connect-Type-TestCase-Arn"></a>
The Amazon Resource Name (ARN) of the test case.
Type: String
Required: No

 ** Content **   <a name="connect-Type-TestCase-Content"></a>
The JSON string that represents the content of the test.
Type: String
Required: No

 ** Description **   <a name="connect-Type-TestCase-Description"></a>
The description of the test case.
Type: String
Required: No

 ** EntryPoint **   <a name="connect-Type-TestCase-EntryPoint"></a>
Defines the starting point for the test, including channel type and parameters.
Type: [TestCaseEntryPoint](API_TestCaseEntryPoint.md) object
Required: No

 ** Id **   <a name="connect-Type-TestCase-Id"></a>
The identifier of the test case.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** InitializationData **   <a name="connect-Type-TestCase-InitializationData"></a>
Defines the test attributes for precise data representation. The value must be a valid JSON string.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-TestCase-LastModifiedRegion"></a>
The region in which the test case was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-TestCase-LastModifiedTime"></a>
The time at which the test case was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-TestCase-Name"></a>
The name of the test case.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Status **   <a name="connect-Type-TestCase-Status"></a>
Indicates the test status as either SAVED or PUBLISHED.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** Tags **   <a name="connect-Type-TestCase-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TestCaseSha256 **   <a name="connect-Type-TestCase-TestCaseSha256"></a>
The SHA256 hash of the test case content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`
Required: No

## See Also
<a name="API_TestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TestCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TestCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TestCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

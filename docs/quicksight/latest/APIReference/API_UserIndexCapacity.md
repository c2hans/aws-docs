---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UserIndexCapacity.html
---

# UserIndexCapacity
<a name="API_UserIndexCapacity"></a>

A summary of a user's index capacity consumption.

## Contents
<a name="API_UserIndexCapacity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** email **   <a name="QS-Type-UserIndexCapacity-email"></a>
The email address of the user.
Type: String
Required: No

 ** kbCount **   <a name="QS-Type-UserIndexCapacity-kbCount"></a>
The number of knowledge bases owned by the user.
Type: Integer
Required: No

 ** role **   <a name="QS-Type-UserIndexCapacity-role"></a>
The role of the user.
Type: String
Required: No

 ** spaceCount **   <a name="QS-Type-UserIndexCapacity-spaceCount"></a>
The number of spaces owned by the user.
Type: Integer
Required: No

 ** totalCapacityBytes **   <a name="QS-Type-UserIndexCapacity-totalCapacityBytes"></a>
The total index capacity consumed by the user in bytes.
Type: Long
Required: No

 ** totalKBCapacityBytes **   <a name="QS-Type-UserIndexCapacity-totalKBCapacityBytes"></a>
The total index capacity consumed by the user's knowledge bases in bytes.
Type: Long
Required: No

 ** totalSpaceCapacityBytes **   <a name="QS-Type-UserIndexCapacity-totalSpaceCapacityBytes"></a>
The total index capacity consumed by the user's spaces in bytes.
Type: Long
Required: No

 ** userArn **   <a name="QS-Type-UserIndexCapacity-userArn"></a>
The ARN of the user.
Type: String
Required: No

 ** userName **   <a name="QS-Type-UserIndexCapacity-userName"></a>
The username of the user.
Type: String
Required: No

## See Also
<a name="API_UserIndexCapacity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UserIndexCapacity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UserIndexCapacity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UserIndexCapacity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

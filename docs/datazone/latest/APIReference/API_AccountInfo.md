---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AccountInfo.html
---

# AccountInfo
<a name="API_AccountInfo"></a>

The account information within an account pool.

## Contents
<a name="API_AccountInfo_Contents"></a>

 ** awsAccountId **   <a name="datazone-Type-AccountInfo-awsAccountId"></a>
The account ID.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** supportedRegions **   <a name="datazone-Type-AccountInfo-supportedRegions"></a>
The regions supported for an account within an account pool.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`
Required: Yes

 ** awsAccountName **   <a name="datazone-Type-AccountInfo-awsAccountName"></a>
The account name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_AccountInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AccountInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AccountInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AccountInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

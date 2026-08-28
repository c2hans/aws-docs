---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AccountSource.html
---

# AccountSource
<a name="API_AccountSource"></a>

The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom AWS Lambda handler.

## Contents
<a name="API_AccountSource_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** accounts **   <a name="datazone-Type-AccountSource-accounts"></a>
The static list of accounts within an account pool.
Type: Array of [AccountInfo](API_AccountInfo.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** customAccountPoolHandler **   <a name="datazone-Type-AccountSource-customAccountPoolHandler"></a>
The custom AWS Lambda handler within an account pool.
Type: [CustomAccountPoolHandler](API_CustomAccountPoolHandler.md) object
Required: No

## See Also
<a name="API_AccountSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AccountSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AccountSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AccountSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

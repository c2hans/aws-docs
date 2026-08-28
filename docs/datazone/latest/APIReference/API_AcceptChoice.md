---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AcceptChoice.html
---

# AcceptChoice
<a name="API_AcceptChoice"></a>

Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be accepted.

## Contents
<a name="API_AcceptChoice_Contents"></a>

 ** predictionTarget **   <a name="datazone-Type-AcceptChoice-predictionTarget"></a>
Specifies the target (for example, a column name) where a prediction can be accepted.
Type: String
Required: Yes

 ** editedValue **   <a name="datazone-Type-AcceptChoice-editedValue"></a>
The edit of the prediction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Required: No

 ** predictionChoice **   <a name="datazone-Type-AcceptChoice-predictionChoice"></a>
Specifies the prediction (aka, the automatically generated piece of metadata) that can be accepted.
Type: Integer
Required: No

## See Also
<a name="API_AcceptChoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AcceptChoice)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AcceptChoice)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AcceptChoice)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

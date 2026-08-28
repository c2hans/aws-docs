---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_Association.html
---

# Association
<a name="API_Association"></a>

The Amazon Braket resource and the association type.

## Contents
<a name="API_Association_Contents"></a>

 ** arn **   <a name="braket-Type-Association-arn"></a>
The Amazon Braket resource arn.
Type: String
Pattern: `arn:aws[a-z\-]*:braket:[a-z0-9\-]*:[0-9]{12}:.*`
Required: Yes

 ** type **   <a name="braket-Type-Association-type"></a>
The association type for the specified Amazon Braket resource arn.
Type: String
Valid Values: `RESERVATION_TIME_WINDOW_ARN`
Required: Yes

## See Also
<a name="API_Association_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/Association)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/Association)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/Association)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

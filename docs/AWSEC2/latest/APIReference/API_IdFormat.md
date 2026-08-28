---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IdFormat.html
---

# IdFormat
<a name="API_IdFormat"></a>

Describes the ID format for a resource.

## Contents
<a name="API_IdFormat_Contents"></a>

 ** deadline **
The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned.
Type: Timestamp
Required: No

 ** resource **
The type of resource.
Type: String
Required: No

 ** useLongIds **
Indicates whether longer IDs (17-character IDs) are enabled for the resource.
Type: Boolean
Required: No

## See Also
<a name="API_IdFormat_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IdFormat)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IdFormat)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IdFormat)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

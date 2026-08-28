---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_PolicyToPath.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# PolicyToPath
<a name="API_PolicyToPath"></a>

Used when a regular object exists in a [Directory](API_Directory.md) and you want to find all of the policies that are associated with that object and the parent to that object.

## Contents
<a name="API_PolicyToPath_Contents"></a>

 ** Path **   <a name="amazoncds-Type-PolicyToPath-Path"></a>
The path that is referenced from the root.
Type: String
Required: No

 ** Policies **   <a name="amazoncds-Type-PolicyToPath-Policies"></a>
List of policy objects.
Type: Array of [PolicyAttachment](API_PolicyAttachment.md) objects
Required: No

## See Also
<a name="API_PolicyToPath_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/PolicyToPath)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/PolicyToPath)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/PolicyToPath)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Directory. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clouddirectory` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

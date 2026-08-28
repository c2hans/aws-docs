---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_AccessKeyLastUsed.html
---

# AccessKeyLastUsed
<a name="API_AccessKeyLastUsed"></a>

Describes the last time an access key was used.

**Note**
This object does not include data in the response of a [CreateBucketAccessKey](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html) action.

## Contents
<a name="API_AccessKeyLastUsed_Contents"></a>

 ** lastUsedDate **   <a name="Lightsail-Type-AccessKeyLastUsed-lastUsedDate"></a>
The date and time when the access key was most recently used.
This value is null if the access key has not been used.
Type: Timestamp
Required: No

 ** region **   <a name="Lightsail-Type-AccessKeyLastUsed-region"></a>
The AWS Region where this access key was most recently used.
This value is `N/A` if the access key has not been used.
Type: String
Required: No

 ** serviceName **   <a name="Lightsail-Type-AccessKeyLastUsed-serviceName"></a>
The name of the AWS service with which this access key was most recently used.
This value is `N/A` if the access key has not been used.
Type: String
Required: No

## See Also
<a name="API_AccessKeyLastUsed_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/AccessKeyLastUsed)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/AccessKeyLastUsed)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/AccessKeyLastUsed)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketState.html
---

# BucketState
<a name="API_BucketState"></a>

Describes the state of an Amazon Lightsail bucket.

## Contents
<a name="API_BucketState_Contents"></a>

 ** code **   <a name="Lightsail-Type-BucketState-code"></a>
The state code of the bucket.
The following codes are possible:
+  `OK` - The bucket is in a running state.
+  `Unknown` - Creation of the bucket might have timed-out. You might want to delete the bucket and create a new one.
Type: String
Pattern: `.*\S.*`
Required: No

 ** message **   <a name="Lightsail-Type-BucketState-message"></a>
A message that describes the state of the bucket.
Type: String
Required: No

## See Also
<a name="API_BucketState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/BucketState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/BucketState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/BucketState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

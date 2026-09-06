---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_Primary.html
---

# Primary
<a name="API_Primary"></a>

The primary Region of the endpoint.

## Contents
<a name="API_Primary_Contents"></a>

 ** HealthCheck **   <a name="eventbridge-Type-Primary-HealthCheck"></a>
The ARN of the health check used by the endpoint to determine whether failover is triggered.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:route53:::healthcheck/[\-a-z0-9]+$`
Required: Yes

## See Also
<a name="API_Primary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/Primary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/Primary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/Primary)

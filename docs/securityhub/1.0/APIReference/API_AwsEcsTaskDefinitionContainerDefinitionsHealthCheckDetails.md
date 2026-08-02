---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails"></a>

The container health check command and associated configuration parameters for the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails_Contents"></a>

 ** Command **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails-Command"></a>
The command that the container runs to determine whether it is healthy.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** Interval **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails-Interval"></a>
The time period in seconds between each health check execution. The default value is 30 seconds.
Type: Integer
Required: No

 ** Retries **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails-Retries"></a>
The number of times to retry a failed health check before the container is considered unhealthy. The default value is 3.
Type: Integer
Required: No

 ** StartPeriod **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails-StartPeriod"></a>
The optional grace period in seconds that allows containers time to bootstrap before failed health checks count towards the maximum number of retries.
Type: Integer
Required: No

 ** Timeout **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails-Timeout"></a>
The time period in seconds to wait for a health check to succeed before it is considered a failure. The default value is 5.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails)

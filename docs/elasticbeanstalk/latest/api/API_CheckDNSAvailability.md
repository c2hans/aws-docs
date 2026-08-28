---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CheckDNSAvailability.html
---

# CheckDNSAvailability
<a name="API_CheckDNSAvailability"></a>

Checks if the specified CNAME is available.

## Request Parameters
<a name="API_CheckDNSAvailability_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CNAMEPrefix **
The prefix used when this CNAME is reserved.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 63.
Required: Yes

## Response Elements
<a name="API_CheckDNSAvailability_ResponseElements"></a>

The following elements are returned by the service.

 ** Available **
Indicates if the specified CNAME is available:
+  `true` : The CNAME is available.
+  `false` : The CNAME is not available.
Type: Boolean

 ** FullyQualifiedCNAME **
The fully qualified CNAME to reserve when [CreateEnvironment](API_CreateEnvironment.md) is called with the provided prefix.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors
<a name="API_CheckDNSAvailability_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CheckDNSAvailability_Examples"></a>

### Example
<a name="API_CheckDNSAvailability_Example_1"></a>

This example illustrates one usage of CheckDNSAvailability.

#### Sample Request
<a name="API_CheckDNSAvailability_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?CNAMEPrefix=sampleapplication
&Operation=CheckDNSAvailability
&AuthParams
```

#### Sample Response
<a name="API_CheckDNSAvailability_Example_1_Response"></a>

```
<CheckDNSAvailabilityResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CheckDNSAvailabilityResult>
    <FullyQualifiedCNAME>sampleapplication.elasticbeanstalk.amazonaws.com</FullyQualifiedCNAME>
    <Available>true</Available>
  </CheckDNSAvailabilityResult>
  <ResponseMetadata>
    <RequestId>12f6701f-f1d6-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CheckDNSAvailabilityResponse>
```

## See Also
<a name="API_CheckDNSAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CheckDNSAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CheckDNSAvailability)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

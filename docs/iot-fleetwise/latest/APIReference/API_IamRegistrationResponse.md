---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_IamRegistrationResponse.html
---

# IamRegistrationResponse
<a name="API_IamRegistrationResponse"></a>

Information about registering an AWS Identity and Access Management (IAM) resource so AWS IoT FleetWise edge agent software can transfer your vehicle data to Amazon Timestream.

## Contents
<a name="API_IamRegistrationResponse_Contents"></a>

 ** registrationStatus **   <a name="iotfleetwise-Type-IamRegistrationResponse-registrationStatus"></a>
The status of registering your IAM resource. The status can be one of `REGISTRATION_SUCCESS`, `REGISTRATION_PENDING`, `REGISTRATION_FAILURE`.
Type: String
Valid Values: `REGISTRATION_PENDING | REGISTRATION_SUCCESS | REGISTRATION_FAILURE`
Required: Yes

 ** roleArn **   <a name="iotfleetwise-Type-IamRegistrationResponse-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to register.
Type: String
Required: Yes

 ** errorMessage **   <a name="iotfleetwise-Type-IamRegistrationResponse-errorMessage"></a>
A message associated with a registration error.
Type: String
Required: No

## See Also
<a name="API_IamRegistrationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/IamRegistrationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/IamRegistrationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/IamRegistrationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

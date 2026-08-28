---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_TimestreamRegistrationResponse.html
---

# TimestreamRegistrationResponse
<a name="API_TimestreamRegistrationResponse"></a>

Information about the registered Amazon Timestream resources or errors, if any.

## Contents
<a name="API_TimestreamRegistrationResponse_Contents"></a>

 ** registrationStatus **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-registrationStatus"></a>
The status of registering your Amazon Timestream resources. The status can be one of `REGISTRATION_SUCCESS`, `REGISTRATION_PENDING`, `REGISTRATION_FAILURE`.
Type: String
Valid Values: `REGISTRATION_PENDING | REGISTRATION_SUCCESS | REGISTRATION_FAILURE`
Required: Yes

 ** timestreamDatabaseName **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-timestreamDatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** timestreamTableName **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-timestreamTableName"></a>
The name of the Timestream database table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** errorMessage **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-errorMessage"></a>
A message associated with a registration error.
Type: String
Required: No

 ** timestreamDatabaseArn **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-timestreamDatabaseArn"></a>
The Amazon Resource Name (ARN) of the Timestream database.
Type: String
Required: No

 ** timestreamTableArn **   <a name="iotfleetwise-Type-TimestreamRegistrationResponse-timestreamTableArn"></a>
The ARN of the Timestream database table.
Type: String
Required: No

## See Also
<a name="API_TimestreamRegistrationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/TimestreamRegistrationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/TimestreamRegistrationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/TimestreamRegistrationResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_AppInstanceUserEndpointSummary.html
---

# AppInstanceUserEndpointSummary
<a name="API_AppInstanceUserEndpointSummary"></a>

Summary of the details of an `AppInstanceUserEndpoint`.

## Contents
<a name="API_AppInstanceUserEndpointSummary_Contents"></a>

 ** AllowMessages **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-AllowMessages"></a>
Boolean that controls whether the `AppInstanceUserEndpoint` is opted in to receive messages. `ALL` indicates the endpoint will receive all messages. `NONE` indicates the endpoint will receive no messages.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** AppInstanceUserArn **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-AppInstanceUserArn"></a>
The ARN of the `AppInstanceUser`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** EndpointId **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-EndpointId"></a>
The unique identifier of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `.*`
Required: No

 ** EndpointState **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-EndpointState"></a>
A read-only field that represent the state of an `AppInstanceUserEndpoint`.
Type: [EndpointState](API_EndpointState.md) object
Required: No

 ** Name **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-Name"></a>
The name of the `AppInstanceUserEndpoint`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Pattern: `.*`
Required: No

 ** Type **   <a name="chimesdk-Type-AppInstanceUserEndpointSummary-Type"></a>
The type of the `AppInstanceUserEndpoint`.
Type: String
Valid Values: `APNS | APNS_SANDBOX | GCM`
Required: No

## See Also
<a name="API_AppInstanceUserEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-identity-2021-04-20/AppInstanceUserEndpointSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-identity-2021-04-20/AppInstanceUserEndpointSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-identity-2021-04-20/AppInstanceUserEndpointSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

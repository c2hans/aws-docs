---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html
---

# GetSMSSandboxAccountStatus
<a name="API_GetSMSSandboxAccountStatus"></a>

Retrieves the SMS sandbox status for the calling AWS account in the target AWS Region.

When you start using Amazon SNS to send SMS messages, your AWS account is in the *SMS sandbox*. The SMS sandbox provides a safe environment for you to try Amazon SNS features without risking your reputation as an SMS sender. While your AWS account is in the SMS sandbox, you can use all of the features of Amazon SNS. However, you can send SMS messages only to verified destination phone numbers. For more information, including how to move out of the sandbox to send messages without restrictions, see [SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) in the *Amazon SNS Developer Guide*.

## Response Elements
<a name="API_GetSMSSandboxAccountStatus_ResponseElements"></a>

The following element is returned by the service.

 ** IsInSandbox **
Indicates whether the calling AWS account is in the SMS sandbox.
Type: Boolean

## Errors
<a name="API_GetSMSSandboxAccountStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

## Examples
<a name="API_GetSMSSandboxAccountStatus_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_GetSMSSandboxAccountStatus_Example_1"></a>

This example illustrates one usage of GetSMSSandboxAccountStatus.

#### Sample Request
<a name="API_GetSMSSandboxAccountStatus_Example_1_Request"></a>

```
https://sns.us-west-2.amazonaws.com/?Action=GetSMSSandboxAccountStatus
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetSMSSandboxAccountStatus_Example_1_Response"></a>

```
<GetSMSSandboxAccountStatusResponse xmlns="https://sns.amazonaws.com/doc/2010-03-31/">
    <GetSMSSandboxAccountStatusResult>
            <IsInSandbox>true</IsInSandbox>
    </GetSMSSandboxAccountStatusResult>
    <ResponseMetadata>
        <RequestId>197f9501-7eca-5151-8d68-cdfb83a62aeb</RequestId>
    </ResponseMetadata>
</GetSMSSandboxAccountStatusResponse>
```

## See Also
<a name="API_GetSMSSandboxAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/GetSMSSandboxAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/GetSMSSandboxAccountStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

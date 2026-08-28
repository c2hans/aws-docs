---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_PutDataProtectionPolicy.html
---

# PutDataProtectionPolicy
<a name="API_PutDataProtectionPolicy"></a>

**Important**
Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see [Amazon SNS message data protection availability change](https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html).

Adds or updates an inline policy document that is stored in the specified Amazon SNS topic.

## Request Parameters
<a name="API_PutDataProtectionPolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DataProtectionPolicy **
The JSON serialization of the topic's `DataProtectionPolicy`.
The `DataProtectionPolicy` must be in JSON string format.
Length Constraints: Maximum length of 30,720.
Type: String
Required: Yes

 ** ResourceArn **
The ARN of the topic whose `DataProtectionPolicy` you want to add or update.
For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the AWS General Reference.
Type: String
Required: Yes

## Errors
<a name="API_PutDataProtectionPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** InvalidSecurity **
The credential signature isn't valid. You must use an HTTPS endpoint and sign your request using Signature Version 4.
HTTP Status Code: 403

 ** NotFound **
Indicates that the requested resource does not exist.
HTTP Status Code: 404

## Examples
<a name="API_PutDataProtectionPolicy_Examples"></a>

The structure of `AUTHPARAMS` depends on the signature of the API request. For more information, see [Examples of the complete Signature Version 4 signing process (Python)](https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html) in the * AWS General Reference*.

### Example
<a name="API_PutDataProtectionPolicy_Example_1"></a>

This example illustrates one usage of `PutDataProtectionPolicy`.

#### Sample Request
<a name="API_PutDataProtectionPolicy_Example_1_Request"></a>

```
https://sns.us-east-2.amazonaws.com/?Action=PutDataProtectionPolicy
&ResourceArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&DataProtectionPolicy=
&Version=2010-03-31
&AUTHPARAMS
```

#### Sample Response
<a name="API_PutDataProtectionPolicy_Example_1_Response"></a>

```
<PutDataProtectionPolicyResponse xmlns="http://sns.amazonaws.com/doc/2010-03-31/">
    <ResponseMetadata>
        <RequestId>e6616aef-1cf0-5c13-b454-31657d8ed10b</RequestId>
    </ResponseMetadata>
</PutDataProtectionPolicyResponse>
```

## See Also
<a name="API_PutDataProtectionPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/PutDataProtectionPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/PutDataProtectionPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SNS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_DecodeAuthorizationMessage.html
---

# DecodeAuthorizationMessage
<a name="API_DecodeAuthorizationMessage"></a>

Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.

For example, if a user is not authorized to perform an operation that he or she has requested, the request returns a `Client.UnauthorizedOperation` response (an HTTP 403 response). Some AWS operations additionally return an encoded message that can provide details about this authorization failure.

**Note**
Only certain AWS operations return an encoded authorization message. The documentation for an individual operation indicates whether that operation returns an encoded message in addition to returning an HTTP code.

The message is encoded because the details of the authorization status can contain privileged information that the user who requested the operation should not see. To decode an authorization status message, a user must be granted permissions through an IAM [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) to request the `DecodeAuthorizationMessage` (`sts:DecodeAuthorizationMessage`) action.

The decoded message includes the following type of information:
+ Whether the request was denied due to an explicit deny or due to the absence of an explicit allow. For more information, see [Determining Whether a Request is Allowed or Denied](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow) in the *IAM User Guide*.
+ The principal who made the request.
+ The requested action.
+ The requested resource.
+ The values of condition keys in the context of the user's request.

## Request Parameters
<a name="API_DecodeAuthorizationMessage_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EncodedMessage **
The encoded message that was returned with the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: Yes

## Response Elements
<a name="API_DecodeAuthorizationMessage_ResponseElements"></a>

The following element is returned by the service.

 ** DecodedMessage **
The API returns a response with the decoded message.
Type: String

## Errors
<a name="API_DecodeAuthorizationMessage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidAuthorizationMessage **
The error returned if the message passed to `DecodeAuthorizationMessage` was invalid. This can happen if the token contains invalid characters, such as line breaks, or if the message has expired.
HTTP Status Code: 400

## Examples
<a name="API_DecodeAuthorizationMessage_Examples"></a>

### Example
<a name="API_DecodeAuthorizationMessage_Example_1"></a>

The following code provides an example snippet of a `DecodeAuthorizationMessage` policy:

```
"Effect": "Allow",
"Action": "sts:DecodeAuthorizationMessage",
"Resource": "*"
```

### Example
<a name="API_DecodeAuthorizationMessage_Example_2"></a>

This example illustrates one usage of DecodeAuthorizationMessage.

#### Sample Request
<a name="API_DecodeAuthorizationMessage_Example_2_Request"></a>

```
POST https://sts.amazonaws.com / HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: sts.amazonaws.com
Content-Length: 1148
Expect: 100-continue
Connection: Keep-Alive
Action=DecodeAuthorizationMessage
&EncodedMessage=<encoded-message>
&Version=2011-06-15
&AUTHPARAMS
```

#### Sample Response
<a name="API_DecodeAuthorizationMessage_Example_2_Response"></a>

```
<?xml version="1.0" encoding="UTF-8"?>
<DecodeAuthorizationMessageResponse xmlns="http://sts.amazonaws.com/doc/2011-06-15/">
    <requestId>6624a9ca-cd25-4f50-b2a5-7ba65bf07453</requestId>
    <DecodedMessage>
    {
      "allowed": "false",
      "explicitDeny": "false",
      "matchedStatements": "",
      "failures": "",
      "context": {
        "principal": {
          "id": "AIDACKCEVSQ6C2EXAMPLE",
          "name": "Bob",
          "arn": "arn:aws:iam::123456789012:user/Bob"
        },
        "action": "ec2:StopInstances",
        "resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-dd01c9bd",
        "conditions": [
          {
            "item": {
              "key": "ec2:Tenancy",
              "values": ["default"]
             },
          {
            "item": {
              "key": "ec2:ResourceTag/elasticbeanstalk:environment-name",
              "values": ["Default-Environment"]
            }
          },
          (Additional items ...)
        ]
      }
    }
    </DecodedMessage>
</DecodeAuthorizationMessageResponse>
```

## See Also
<a name="API_DecodeAuthorizationMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/DecodeAuthorizationMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/DecodeAuthorizationMessage)

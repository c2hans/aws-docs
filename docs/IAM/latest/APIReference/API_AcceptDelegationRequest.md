---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AcceptDelegationRequest.html
---

# AcceptDelegationRequest
<a name="API_AcceptDelegationRequest"></a>

Accepts a delegation request, granting the requested temporary access.

Once the delegation request is accepted, it is eligible to send the exchange token to the partner. The [SendDelegationToken](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html) API has to be explicitly called to send the delegation token.

At the time of acceptance, IAM records the details and the state of the identity that called this API. This is the identity that gets mapped to the delegated credential.

An accepted request may be rejected before the exchange token is sent to the partner.

## Request Parameters
<a name="API_AcceptDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationRequestId **
The unique identifier of the delegation request to accept.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

## Errors
<a name="API_AcceptDelegationRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_AcceptDelegationRequest_Examples"></a>

### Example
<a name="API_AcceptDelegationRequest_Example_1"></a>

This example illustrates one usage of AcceptDelegationRequest.

#### Sample Request
<a name="API_AcceptDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=AcceptDelegationRequest
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_AcceptDelegationRequest_Example_1_Response"></a>

```
<AcceptDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</AcceptDelegationRequestResponse>
```

## See Also
<a name="API_AcceptDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/AcceptDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AcceptDelegationRequest)

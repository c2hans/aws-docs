---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_SendDelegationToken.html
---

# SendDelegationToken
<a name="API_SendDelegationToken"></a>

Sends the exchange token for an accepted delegation request.

The exchange token is sent to the partner via an asynchronous notification channel, established by the partner.

The delegation request must be in the `ACCEPTED` state when calling this API. After the `SendDelegationToken` API call is successful, the request transitions to a `FINALIZED` state and cannot be rolled back. However, a user may reject an accepted request before the `SendDelegationToken` API is called.

 For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_SendDelegationToken_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationRequestId **
The unique identifier of the delegation request for which to send the token.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

## Errors
<a name="API_SendDelegationToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModification **
The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
HTTP Status Code: 409

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

## Examples
<a name="API_SendDelegationToken_Examples"></a>

### Example
<a name="API_SendDelegationToken_Example_1"></a>

This example illustrates one usage of SendDelegationToken.

#### Sample Request
<a name="API_SendDelegationToken_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=SendDelegationToken
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_SendDelegationToken_Example_1_Response"></a>

```
<SendDelegationTokenResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</SendDelegationTokenResponse>
```

## See Also
<a name="API_SendDelegationToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/SendDelegationToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/SendDelegationToken)

---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_RejectDelegationRequest.html
---

# RejectDelegationRequest
<a name="API_RejectDelegationRequest"></a>

Rejects a delegation request, denying the requested temporary access.

Once a request is rejected, it cannot be accepted or updated later. Rejected requests expire after 7 days.

When rejecting a request, an optional explanation can be added using the `Notes` request parameter.

 For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_RejectDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationRequestId **
The unique identifier of the delegation request to reject.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

 ** Notes **
Optional notes explaining the reason for rejecting the delegation request.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

## Errors
<a name="API_RejectDelegationRequest_Errors"></a>

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
<a name="API_RejectDelegationRequest_Examples"></a>

### Example
<a name="API_RejectDelegationRequest_Example_1"></a>

This example illustrates one usage of RejectDelegationRequest.

#### Sample Request
<a name="API_RejectDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=RejectDelegationRequest
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_RejectDelegationRequest_Example_1_Response"></a>

```
<RejectDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</RejectDelegationRequestResponse>
```

## See Also
<a name="API_RejectDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/RejectDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/RejectDelegationRequest)

---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_AssociateDelegationRequest.html
---

# AssociateDelegationRequest
<a name="API_AssociateDelegationRequest"></a>

Associates a delegation request with the current identity.

If the partner that created the delegation request has specified the owner account during creation, only an identity from that owner account can call the `AssociateDelegationRequest` API for the specified delegation request. Once the `AssociateDelegationRequest` API call is successful, the ARN of the current calling identity will be stored as the `ownerId` of the request.

If the partner that created the delegation request has not specified the owner account during creation, any caller from any account can call the `AssociateDelegationRequest` API for the delegation request. Once this API call is successful, the ARN of the current calling identity will be stored as the `ownerId` and the AWS account ID of the current calling identity will be stored as the `ownerAccount` of the request.

 For more details, see [ Managing Permissions for Delegation Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-temporary-delegation.html#temporary-delegation-managing-permissions).

## Request Parameters
<a name="API_AssociateDelegationRequest_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DelegationRequestId **
The unique identifier of the delegation request to associate.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 128.
Pattern: `[\w-]+`
Required: Yes

## Errors
<a name="API_AssociateDelegationRequest_Errors"></a>

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
<a name="API_AssociateDelegationRequest_Examples"></a>

### Example
<a name="API_AssociateDelegationRequest_Example_1"></a>

This example illustrates one usage of AssociateDelegationRequest.

#### Sample Request
<a name="API_AssociateDelegationRequest_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=AssociateDelegationRequest
&DelegationRequestId=e4bdcdae-4f66-11eD-ELEG-ATIONEXAMPLE
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateDelegationRequest_Example_1_Response"></a>

```
<AssociateDelegationRequestResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ResponseMetadata>
    <RequestId>e4bdcdae-4f66-11e4-aefa-bfd6aEXAMPLE</RequestId>
  </ResponseMetadata>
</AssociateDelegationRequestResponse>
```

## See Also
<a name="API_AssociateDelegationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/AssociateDelegationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/AssociateDelegationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

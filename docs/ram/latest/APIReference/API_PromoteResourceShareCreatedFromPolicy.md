---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html
---

# PromoteResourceShareCreatedFromPolicy
<a name="API_PromoteResourceShareCreatedFromPolicy"></a>

When you attach a resource-based policy to a resource, AWS RAM automatically creates a resource share of `featureSet`=`CREATED_FROM_POLICY` with a managed permission that has the same IAM permissions as the original resource-based policy. However, this type of managed permission is visible to only the resource share owner, and the associated resource share can't be modified by using AWS RAM.

This operation promotes the resource share to a `STANDARD` resource share that is fully manageable in AWS RAM. When you promote a resource share, you can then manage the resource share in AWS RAM and it becomes visible to all of the principals you shared it with.

**Important**
Before you perform this operation, you should first run [PromotePermissionCreatedFromPolicy](API_PromotePermissionCreatedFromPolicy.md)to ensure that you have an appropriate customer managed permission that can be associated with this resource share after its is promoted. If this operation can't find a managed permission that exactly matches the existing `CREATED_FROM_POLICY` permission, then this operation fails.

## Request Syntax
<a name="API_PromoteResourceShareCreatedFromPolicy_RequestSyntax"></a>

```
POST /promoteresourcesharecreatedfrompolicy?resourceShareArn={{resourceShareArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_PromoteResourceShareCreatedFromPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceShareArn](#API_PromoteResourceShareCreatedFromPolicy_RequestSyntax) **   <a name="ram-PromoteResourceShareCreatedFromPolicy-request-uri-resourceShareArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share to promote.
Required: Yes

## Request Body
<a name="API_PromoteResourceShareCreatedFromPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_PromoteResourceShareCreatedFromPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "returnValue": boolean
}
```

## Response Elements
<a name="API_PromoteResourceShareCreatedFromPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [returnValue](#API_PromoteResourceShareCreatedFromPolicy_ResponseSyntax) **   <a name="ram-PromoteResourceShareCreatedFromPolicy-response-returnValue"></a>
A return value of `true` indicates that the request succeeded. A value of `false` indicates that the request failed.
Type: Boolean

## Errors
<a name="API_PromoteResourceShareCreatedFromPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** InvalidStateTransitionException **
The operation failed because the requested operation isn't valid for the resource share in its current state.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
The operation failed because a required input parameter is missing.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ResourceShareLimitExceededException **
The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

 ** UnmatchedPolicyPermissionException **
There isn't an existing managed permission defined in AWS RAM that has the same IAM permissions as the resource-based policy attached to the resource. You should first run [PromotePermissionCreatedFromPolicy](API_PromotePermissionCreatedFromPolicy.md) to create that managed permission.
HTTP Status Code: 400

## See Also
<a name="API_PromoteResourceShareCreatedFromPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy)

---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_DeleteDomainForOrganization.html
---

# DeleteDomainForOrganization
<a name="API_DeleteDomainForOrganization"></a>

Removes an organization domain and all of its resources. Call this operation in the Region where the domain was created.

A domain cannot be deleted while it contains spaces.

## Request Parameters
<a name="API_DeleteDomainForOrganization_RequestParameters"></a>

 ** domainId **
The ID of the organization domain to delete.
Type: String
Pattern: `d-[0-9a-z]{1,25}`
Required: Yes

## Errors
<a name="API_DeleteDomainForOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The operation could not be completed because of a conflict with the current state of the resource.
 ** conflictType **
The type of conflict that caused the request to fail. Not always present.
 ** errorCode **
The error code associated with the conflict. Not always present.
 ** message **
A human-readable description of the conflict.
 ** resourceId **
The identifier of the resource that is in conflict. Not always present.
 ** resourceType **
The type of the resource that is in conflict. Not always present.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** errorCode **
The error code associated with the internal error.
HTTP Status Code: 500

 ** ThrottlingException **
The request was throttled due to exceeding the allowed request rate.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request. Not always present.
HTTP Status Code: 429

 ** ValidationException **
A parameter is specified incorrectly.
 ** errorCode **
The error code associated with the validation failure.
HTTP Status Code: 400

## Examples
<a name="API_DeleteDomainForOrganization_Examples"></a>

### Delete an organization domain
<a name="API_DeleteDomainForOrganization_Example_1"></a>

The following example deletes an organization domain in the Region where it was created. The domain must not contain any spaces. A successful response returns an empty body. Payloads are shown as JSON; on the wire they are CBOR-encoded.

#### Sample Request
<a name="API_DeleteDomainForOrganization_Example_1_Request"></a>

```
{
  "domainId": "d-9z8y7x6w5v"
}
```

#### Sample Response
<a name="API_DeleteDomainForOrganization_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteDomainForOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/DeleteDomainForOrganization)

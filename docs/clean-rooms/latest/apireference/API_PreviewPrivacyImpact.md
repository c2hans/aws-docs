---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_PreviewPrivacyImpact.html
---

# PreviewPrivacyImpact
<a name="API_PreviewPrivacyImpact"></a>

An estimate of the number of aggregation functions that the member who can query can run given epsilon and noise parameters.

## Request Syntax
<a name="API_PreviewPrivacyImpact_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/previewprivacyimpact HTTP/1.1
Content-type: application/json

{
   "parameters": { ... }
}
```

## URI Request Parameters
<a name="API_PreviewPrivacyImpact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_PreviewPrivacyImpact_RequestSyntax) **   <a name="API-PreviewPrivacyImpact-request-uri-membershipIdentifier"></a>
A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_PreviewPrivacyImpact_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [parameters](#API_PreviewPrivacyImpact_RequestSyntax) **   <a name="API-PreviewPrivacyImpact-request-parameters"></a>
Specifies the desired epsilon and noise parameters to preview.
Type: [PreviewPrivacyImpactParametersInput](API_PreviewPrivacyImpactParametersInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_PreviewPrivacyImpact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "privacyImpact": { ... }
}
```

## Response Elements
<a name="API_PreviewPrivacyImpact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [privacyImpact](#API_PreviewPrivacyImpact_ResponseSyntax) **   <a name="API-PreviewPrivacyImpact-response-privacyImpact"></a>
An estimate of the number of aggregation functions that the member who can query can run given the epsilon and noise parameters. This does not change the privacy budget.
Type: [PrivacyImpact](API_PrivacyImpact.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_PreviewPrivacyImpact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_PreviewPrivacyImpact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/PreviewPrivacyImpact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/PreviewPrivacyImpact)

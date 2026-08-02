---
source_url: https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_DeletePracticeRunConfiguration.html
---

# DeletePracticeRunConfiguration
<a name="API_DeletePracticeRunConfiguration"></a>

Deletes the practice run configuration for a resource. Before you can delete a practice run configuration for a resource., you must disable zonal autoshift for the resource. Practice runs must be configured for zonal autoshift to be enabled.

## Request Syntax
<a name="API_DeletePracticeRunConfiguration_RequestSyntax"></a>

```
DELETE /configuration/{{resourceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePracticeRunConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceIdentifier](#API_DeletePracticeRunConfiguration_RequestSyntax) **   <a name="zonalshift-DeletePracticeRunConfiguration-request-uri-resourceIdentifier"></a>
The identifier for the resource that you want to delete the practice run configuration for. The identifier is the Amazon Resource Name (ARN) for the resource.
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: Yes

## Request Body
<a name="API_DeletePracticeRunConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePracticeRunConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "name": "string",
   "zonalAutoshiftStatus": "string"
}
```

## Response Elements
<a name="API_DeletePracticeRunConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeletePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-DeletePracticeRunConfiguration-response-arn"></a>
The Amazon Resource Name (ARN) of the resource that you deleted the practice run for.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Pattern: `arn:.*`

 ** [name](#API_DeletePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-DeletePracticeRunConfiguration-response-name"></a>
The name of the resource that you deleted the practice run for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [zonalAutoshiftStatus](#API_DeletePracticeRunConfiguration_ResponseSyntax) **   <a name="zonalshift-DeletePracticeRunConfiguration-response-zonalAutoshiftStatus"></a>
The status of zonal autoshift for the resource.
Type: String
Valid Values: `ENABLED | DISABLED`

## Errors
<a name="API_DeletePracticeRunConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
 ** reason **
The reason for the conflict exception.
 ** zonalShiftId **
The zonal shift ID associated with the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The input requested a resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_DeletePracticeRunConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-zonal-shift-2022-10-30/DeletePracticeRunConfiguration)

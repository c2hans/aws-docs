---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteRouteCalculator.html
---

# DeleteRouteCalculator
<a name="API_DeleteRouteCalculator"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Routes API V2 unless you require Grab data.
 `DeleteRouteCalculator` is part of a previous Amazon Location Service Routes API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The Routes API version 2 has a simplified interface that can be used without creating or managing route calculator resources.
If you are using an AWS SDK or the AWS CLI, note that the Routes API version 2 is found under `geo-routes` or `geo_routes`, not under `location`.
Since Grab is not yet fully supported in Routes API version 2, we recommend you continue using API version 1 when using Grab.
Start your version 2 API journey with the Routes V2 [API Reference](/location/latest/APIReference/API_Operations_Amazon_Location_Service_Routes_V2.html) or the [Developer Guide](/location/latest/developerguide/routes.html).

Deletes a route calculator resource from your AWS account.

**Note**
This operation deletes the resource permanently.

## Request Syntax
<a name="API_DeleteRouteCalculator_RequestSyntax"></a>

```
DELETE /routes/v0/calculators/{{CalculatorName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRouteCalculator_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CalculatorName](#API_DeleteRouteCalculator_RequestSyntax) **   <a name="location-DeleteRouteCalculator-request-uri-CalculatorName"></a>
The name of the route calculator resource to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_DeleteRouteCalculator_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRouteCalculator_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteRouteCalculator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRouteCalculator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRouteCalculator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/DeleteRouteCalculator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DeleteRouteCalculator)

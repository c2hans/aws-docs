---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapStyleDescriptor.html
---

# GetMapStyleDescriptor
<a name="API_GetMapStyleDescriptor"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to [`GetStyleDescriptor`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html) unless you require `Grab` data.
 `GetMapStyleDescriptor` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `GetStyleDescriptor` operation gives a better user experience and is compatible with the remainder of the V2 Maps API.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Retrieves the map style descriptor from a map resource.

The style descriptor contains speciﬁcations on how features render on a map. For example, what data to display, what order to display the data in, and the style for the data. Style descriptors follow the Mapbox Style Specification.

## Request Syntax
<a name="API_GetMapStyleDescriptor_RequestSyntax"></a>

```
GET /maps/v0/maps/{{MapName}}/style-descriptor?key={{Key}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMapStyleDescriptor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_GetMapStyleDescriptor_RequestSyntax) **   <a name="location-GetMapStyleDescriptor-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [MapName](#API_GetMapStyleDescriptor_RequestSyntax) **   <a name="location-GetMapStyleDescriptor-request-uri-MapName"></a>
The map resource to retrieve the style descriptor from.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_GetMapStyleDescriptor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMapStyleDescriptor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}

{{Blob}}
```

## Response Elements
<a name="API_GetMapStyleDescriptor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_GetMapStyleDescriptor_ResponseSyntax) **   <a name="location-GetMapStyleDescriptor-response-CacheControl"></a>
The HTTP Cache-Control directive for the value.

 ** [ContentType](#API_GetMapStyleDescriptor_ResponseSyntax) **   <a name="location-GetMapStyleDescriptor-response-ContentType"></a>
The style descriptor's content type. For example, `application/json`.

The response returns the following as the HTTP body.

 ** [Blob](#API_GetMapStyleDescriptor_ResponseSyntax) **   <a name="location-GetMapStyleDescriptor-response-Blob"></a>
Contains the body of the style descriptor.

## Errors
<a name="API_GetMapStyleDescriptor_Errors"></a>

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
<a name="API_GetMapStyleDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetMapStyleDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetMapStyleDescriptor)

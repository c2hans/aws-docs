---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_DeleteEndpoint.html
---

# DeleteEndpoint
<a name="API_s3outposts_DeleteEndpoint"></a>

Deletes an endpoint.

**Note**
It can take up to 5 minutes for this action to finish.

Related actions include:
+  [CreateEndpoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_CreateEndpoint.html)
+  [ListEndpoints](https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3outposts_ListEndpoints.html)

## Request Syntax
<a name="API_s3outposts_DeleteEndpoint_RequestSyntax"></a>

```
DELETE /S3Outposts/DeleteEndpoint?endpointId={{EndpointId}}&outpostId={{OutpostId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_s3outposts_DeleteEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndpointId](#API_s3outposts_DeleteEndpoint_RequestSyntax) **   <a name="AmazonS3-s3outposts_DeleteEndpoint-request-uri-EndpointId"></a>
The ID of the endpoint.
Pattern: `^[a-zA-Z0-9]{19}$`
Required: Yes

 ** [OutpostId](#API_s3outposts_DeleteEndpoint_RequestSyntax) **   <a name="AmazonS3-s3outposts_DeleteEndpoint-request-uri-OutpostId"></a>
The ID of the AWS Outposts.
Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`
Required: Yes

## Request Body
<a name="API_s3outposts_DeleteEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_s3outposts_DeleteEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_s3outposts_DeleteEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_s3outposts_DeleteEndpoint_Errors"></a>

 ** AccessDeniedException **
Access was denied for this action.
HTTP Status Code: 403

 ** InternalServerException **
There was an exception with the internal server.
HTTP Status Code: 500

 ** OutpostOfflineException **
The service link connection to your Outposts home Region is down. Check your connection and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
There was an exception validating this data.
HTTP Status Code: 400

## See Also
<a name="API_s3outposts_DeleteEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/DeleteEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/DeleteEndpoint)

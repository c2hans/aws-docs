---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEndpoint.html
---

# DescribeEndpoint
<a name="API_DescribeEndpoint"></a>

Returns or creates a unique endpoint specific to the AWS account making the call.

**Note**
The first time `DescribeEndpoint` is called, an endpoint is created. All subsequent calls to `DescribeEndpoint` return the same endpoint.

Requires permission to access the [DescribeEndpoint](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeEndpoint_RequestSyntax"></a>

```
GET /endpoint?endpointType={{endpointType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endpointType](#API_DescribeEndpoint_RequestSyntax) **   <a name="iot-DescribeEndpoint-request-uri-endpointType"></a>
The endpoint type. Valid endpoint types include:
+  `iot:Data` - Returns a VeriSign signed data endpoint.
+  `iot:Data-ATS` - Returns an ATS signed data endpoint.
+  `iot:CredentialProvider` - Returns an AWS IoT credentials provider API endpoint.
+  `iot:Jobs` - Returns an AWS IoT device management Jobs API endpoint.
We strongly recommend that customers use the newer `iot:Data-ATS` endpoint type to avoid issues related to the widespread distrust of Symantec certificate authorities. ATS Signed Certificates are more secure and are trusted by most popular browsers.
Length Constraints: Maximum length of 128.
Pattern: `[\s\S]*`

## Request Body
<a name="API_DescribeEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpointAddress": "string"
}
```

## Response Elements
<a name="API_DescribeEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpointAddress](#API_DescribeEndpoint_ResponseSyntax) **   <a name="iot-DescribeEndpoint-response-endpointAddress"></a>
The endpoint. The format of the endpoint is as follows: *identifier*.iot.*region*.amazonaws.com.
Type: String

## Errors
<a name="API_DescribeEndpoint_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_DescribeEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeEndpoint)

---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListCACertificates.html
---

# ListCACertificates
<a name="API_ListCACertificates"></a>

Lists the CA certificates registered for your AWS account.

The results are paginated with a default page size of 25. You can use the returned marker to retrieve additional results.

Requires permission to access the [ListCACertificates](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListCACertificates_RequestSyntax"></a>

```
GET /cacertificates?isAscendingOrder={{ascendingOrder}}&marker={{marker}}&pageSize={{pageSize}}&templateName={{templateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCACertificates_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ascendingOrder](#API_ListCACertificates_RequestSyntax) **   <a name="iot-ListCACertificates-request-uri-ascendingOrder"></a>
Determines the order of the results.

 ** [marker](#API_ListCACertificates_RequestSyntax) **   <a name="iot-ListCACertificates-request-uri-marker"></a>
The marker for the next set of results.
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

 ** [pageSize](#API_ListCACertificates_RequestSyntax) **   <a name="iot-ListCACertificates-request-uri-pageSize"></a>
The result page size.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [templateName](#API_ListCACertificates_RequestSyntax) **   <a name="iot-ListCACertificates-request-uri-templateName"></a>
The name of the provisioning template.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`

## Request Body
<a name="API_ListCACertificates_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCACertificates_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificates": [
      {
         "certificateArn": "string",
         "certificateId": "string",
         "creationDate": number,
         "status": "string"
      }
   ],
   "nextMarker": "string"
}
```

## Response Elements
<a name="API_ListCACertificates_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificates](#API_ListCACertificates_ResponseSyntax) **   <a name="iot-ListCACertificates-response-certificates"></a>
The CA certificates registered in your AWS account.
Type: Array of [CACertificate](API_CACertificate.md) objects

 ** [nextMarker](#API_ListCACertificates_ResponseSyntax) **   <a name="iot-ListCACertificates-response-nextMarker"></a>
The current position within the list of CA certificates.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[A-Za-z0-9+/]+={0,2}`

## Errors
<a name="API_ListCACertificates_Errors"></a>

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

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

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
<a name="API_ListCACertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListCACertificates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListCACertificates)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

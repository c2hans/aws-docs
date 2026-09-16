---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Lists Amazon Q Business applications.

**Note**
Amazon Q Business applications may securely transmit data for processing across AWS Regions within your geography. For more information, see [Cross region inference in Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html).

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
GET /applications?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="qbusiness-ListApplications-request-uri-maxResults"></a>
The maximum number of Amazon Q Business applications to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="qbusiness-ListApplications-request-uri-nextToken"></a>
If the `maxResults` response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business applications.
Length Constraints: Minimum length of 1. Maximum length of 800.

## Request Body
<a name="API_ListApplications_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applications": [
      {
         "applicationId": "string",
         "createdAt": number,
         "displayName": "string",
         "identityType": "string",
         "quickSightConfiguration": {
            "clientNamespace": "string"
         },
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_ListApplications_ResponseSyntax) **   <a name="qbusiness-ListApplications-response-applications"></a>
An array of summary information on the configuration of one or more Amazon Q Business applications.
Type: Array of [Application](API_Application.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="qbusiness-ListApplications-response-nextToken"></a>
If the response is truncated, Amazon Q Business returns this token. You can use this token in a subsequent request to retrieve the next set of applications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 800.

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/ListApplications)

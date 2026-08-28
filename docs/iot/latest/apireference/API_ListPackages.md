---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListPackages.html
---

# ListPackages
<a name="API_ListPackages"></a>

Lists the software packages associated to the account.

Requires permission to access the [ListPackages](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListPackages_RequestSyntax"></a>

```
GET /packages?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPackages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPackages_RequestSyntax) **   <a name="iot-ListPackages-request-uri-maxResults"></a>
The maximum number of results returned at one time.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPackages_RequestSyntax) **   <a name="iot-ListPackages-request-uri-nextToken"></a>
The token for the next set of results.

## Request Body
<a name="API_ListPackages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPackages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "packageSummaries": [
      {
         "creationDate": number,
         "defaultVersionName": "string",
         "lastModifiedDate": number,
         "packageName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPackages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListPackages_ResponseSyntax) **   <a name="iot-ListPackages-response-nextToken"></a>
The token for the next set of results.
Type: String

 ** [packageSummaries](#API_ListPackages_ResponseSyntax) **   <a name="iot-ListPackages-response-packageSummaries"></a>
The software package summary.
Type: Array of [PackageSummary](API_PackageSummary.md) objects

## Errors
<a name="API_ListPackages_Errors"></a>

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ValidationException **
The request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListPackages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListPackages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListPackages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListPackages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListPackages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListPackages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListPackages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListPackages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListPackages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListPackages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListPackages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

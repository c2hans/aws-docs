---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListApplications.html
---

# ListApplications
<a name="API_ListApplications"></a>

Retrieves a paginated list of existing applications

## Request Syntax
<a name="API_ListApplications_RequestSyntax"></a>

```
GET /applications?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListApplications_RequestSyntax) **   <a name="iotsitewise-ListApplications-request-uri-maxResults"></a>
Maximum number of results to return
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListApplications_RequestSyntax) **   <a name="iotsitewise-ListApplications-request-uri-nextToken"></a>
Next Page Token
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

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
         "arn": "string",
         "createdAt": number,
         "id": "string",
         "name": "string",
         "status": "string",
         "workspaceName": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applications](#API_ListApplications_ResponseSyntax) **   <a name="iotsitewise-ListApplications-response-applications"></a>
List of applications
Type: Array of [ApplicationSummary](API_ApplicationSummary.md) objects

 ** [nextToken](#API_ListApplications_ResponseSyntax) **   <a name="iotsitewise-ListApplications-response-nextToken"></a>
Next Page Token
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_ListApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_ListApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/ListApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListApplications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

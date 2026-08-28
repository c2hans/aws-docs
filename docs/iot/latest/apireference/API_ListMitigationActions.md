---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListMitigationActions.html
---

# ListMitigationActions
<a name="API_ListMitigationActions"></a>

Gets a list of all mitigation actions that match the specified filter criteria.

Requires permission to access the [ListMitigationActions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListMitigationActions_RequestSyntax"></a>

```
GET /mitigationactions/actions?actionType={{actionType}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMitigationActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [actionType](#API_ListMitigationActions_RequestSyntax) **   <a name="iot-ListMitigationActions-request-uri-actionType"></a>
Specify a value to limit the result to mitigation actions with a specific action type.
Valid Values: `UPDATE_DEVICE_CERTIFICATE | UPDATE_CA_CERTIFICATE | ADD_THINGS_TO_THING_GROUP | REPLACE_DEFAULT_POLICY_VERSION | ENABLE_IOT_LOGGING | PUBLISH_FINDING_TO_SNS`

 ** [maxResults](#API_ListMitigationActions_RequestSyntax) **   <a name="iot-ListMitigationActions-request-uri-maxResults"></a>
The maximum number of results to return at one time. The default is 25.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListMitigationActions_RequestSyntax) **   <a name="iot-ListMitigationActions-request-uri-nextToken"></a>
The token for the next set of results.

## Request Body
<a name="API_ListMitigationActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMitigationActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actionIdentifiers": [
      {
         "actionArn": "string",
         "actionName": "string",
         "creationDate": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMitigationActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionIdentifiers](#API_ListMitigationActions_ResponseSyntax) **   <a name="iot-ListMitigationActions-response-actionIdentifiers"></a>
A set of actions that matched the specified filter criteria.
Type: Array of [MitigationActionIdentifier](API_MitigationActionIdentifier.md) objects

 ** [nextToken](#API_ListMitigationActions_ResponseSyntax) **   <a name="iot-ListMitigationActions-response-nextToken"></a>
The token for the next set of results.
Type: String

## Errors
<a name="API_ListMitigationActions_Errors"></a>

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

## See Also
<a name="API_ListMitigationActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListMitigationActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListMitigationActions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

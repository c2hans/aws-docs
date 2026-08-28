---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListThingsInBillingGroup.html
---

# ListThingsInBillingGroup
<a name="API_ListThingsInBillingGroup"></a>

Lists the things you have added to the given billing group.

Requires permission to access the [ListThingsInBillingGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListThingsInBillingGroup_RequestSyntax"></a>

```
GET /billing-groups/{{billingGroupName}}/things?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListThingsInBillingGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [billingGroupName](#API_ListThingsInBillingGroup_RequestSyntax) **   <a name="iot-ListThingsInBillingGroup-request-uri-billingGroupName"></a>
The name of the billing group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** [maxResults](#API_ListThingsInBillingGroup_RequestSyntax) **   <a name="iot-ListThingsInBillingGroup-request-uri-maxResults"></a>
The maximum number of results to return per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [nextToken](#API_ListThingsInBillingGroup_RequestSyntax) **   <a name="iot-ListThingsInBillingGroup-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise **null** to receive the first set of results.

## Request Body
<a name="API_ListThingsInBillingGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListThingsInBillingGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "things": [ "string" ]
}
```

## Response Elements
<a name="API_ListThingsInBillingGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListThingsInBillingGroup_ResponseSyntax) **   <a name="iot-ListThingsInBillingGroup-response-nextToken"></a>
The token to use to get the next set of results. Will not be returned if operation has returned all results.
Type: String

 ** [things](#API_ListThingsInBillingGroup_ResponseSyntax) **   <a name="iot-ListThingsInBillingGroup-response-things"></a>
A list of things in the billing group.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_ListThingsInBillingGroup_Errors"></a>

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListThingsInBillingGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListThingsInBillingGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListThingsInBillingGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListCommands.html
---

# ListCommands
<a name="API_ListCommands"></a>

List all commands in your account.

## Request Syntax
<a name="API_ListCommands_RequestSyntax"></a>

```
GET /commands?commandParameterName={{commandParameterName}}&maxResults={{maxResults}}&namespace={{namespace}}&nextToken={{nextToken}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCommands_RequestParameters"></a>

The request uses the following URI parameters.

 ** [commandParameterName](#API_ListCommands_RequestSyntax) **   <a name="iot-ListCommands-request-uri-commandParameterName"></a>
A filter that can be used to display the list of commands that have a specific command parameter name.
Length Constraints: Minimum length of 1. Maximum length of 192.
Pattern: `^[.$a-zA-Z0-9_-]+$`

 ** [maxResults](#API_ListCommands_RequestSyntax) **   <a name="iot-ListCommands-request-uri-maxResults"></a>
The maximum number of results to return in this operation. By default, the API returns up to a maximum of 25 results. You can override this default value to return up to a maximum of 100 results for this operation.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [namespace](#API_ListCommands_RequestSyntax) **   <a name="iot-ListCommands-request-uri-namespace"></a>
The namespace of the command. By default, the API returns all commands that have been created for both `AWS-IoT` and `AWS-IoT-FleetWise` namespaces. You can override this default value if you want to return all commands that have been created only for a specific namespace.
Valid Values: `AWS-IoT | AWS-IoT-FleetWise`

 ** [nextToken](#API_ListCommands_RequestSyntax) **   <a name="iot-ListCommands-request-uri-nextToken"></a>
To retrieve the next set of results, the `nextToken` value from a previous response; otherwise `null` to receive the first set of results.

 ** [sortOrder](#API_ListCommands_RequestSyntax) **   <a name="iot-ListCommands-request-uri-sortOrder"></a>
Specify whether to list the commands that you have created in the ascending or descending order. By default, the API returns all commands in the descending order based on the time that they were created.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListCommands_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCommands_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "commands": [
      {
         "commandArn": "string",
         "commandId": "string",
         "createdAt": number,
         "deprecated": boolean,
         "displayName": "string",
         "lastUpdatedAt": number,
         "pendingDeletion": boolean
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCommands_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [commands](#API_ListCommands_ResponseSyntax) **   <a name="iot-ListCommands-response-commands"></a>
The list of commands.
Type: Array of [CommandSummary](API_CommandSummary.md) objects

 ** [nextToken](#API_ListCommands_ResponseSyntax) **   <a name="iot-ListCommands-response-nextToken"></a>
The token to use to get the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListCommands_Errors"></a>

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
<a name="API_ListCommands_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListCommands)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListCommands)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListCommands)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListCommands)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListCommands)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListCommands)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListCommands)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListCommands)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListCommands)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListCommands)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

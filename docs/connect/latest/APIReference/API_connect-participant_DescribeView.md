---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_DescribeView.html
---

# DescribeView
<a name="API_connect-participant_DescribeView"></a>

Retrieves the view for the specified view token.

For security recommendations, see [Connect Customer Chat security best practices](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html#bp-security-chat).

## Request Syntax
<a name="API_connect-participant_DescribeView_RequestSyntax"></a>

```
GET /participant/views/{{ViewToken}} HTTP/1.1
X-Amz-Bearer: {{ConnectionToken}}
```

## URI Request Parameters
<a name="API_connect-participant_DescribeView_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectionToken](#API_connect-participant_DescribeView_RequestSyntax) **   <a name="connect-connect-participant_DescribeView-request-ConnectionToken"></a>
The connection token.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [ViewToken](#API_connect-participant_DescribeView_RequestSyntax) **   <a name="connect-connect-participant_DescribeView-request-uri-ViewToken"></a>
An encrypted token originating from the interactive message of a ShowView block operation. Represents the desired view.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

## Request Body
<a name="API_connect-participant_DescribeView_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-participant_DescribeView_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "View": {
      "Arn": "string",
      "Content": {
         "Actions": [ "string" ],
         "InputSchema": "string",
         "Template": "string"
      },
      "Id": "string",
      "Name": "string",
      "Version": number
   }
}
```

## Response Elements
<a name="API_connect-participant_DescribeView_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [View](#API_connect-participant_DescribeView_ResponseSyntax) **   <a name="connect-connect-participant_DescribeView-response-View"></a>
A view resource object. Contains metadata and content necessary to render the view.
Type: [View](API_connect-participant_View.md) object

## Errors
<a name="API_connect-participant_DescribeView_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the Amazon Connect service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource was not found.
 ** ResourceId **
The identifier of the resource.
 ** ResourceType **
The type of Connect Customer resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by Amazon Connect.
HTTP Status Code: 400

## See Also
<a name="API_connect-participant_DescribeView_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectparticipant-2018-09-07/DescribeView)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/DescribeView)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

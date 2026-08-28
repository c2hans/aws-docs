---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_UpdateLink.html
---

# UpdateLink
<a name="API_UpdateLink"></a>

Use this operation to change what types of data are shared from a source account to its linked monitoring account sink. You can't change the sink or change the monitoring account with this operation.

When you update a link, you can optionally specify filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.

To update the list of tags associated with the sink, use [TagResource](https://docs.aws.amazon.com/OAM/latest/APIReference/API_TagResource.html).

## Request Syntax
<a name="API_UpdateLink_RequestSyntax"></a>

```
POST /UpdateLink HTTP/1.1
Content-type: application/json

{
   "Identifier": "{{string}}",
   "IncludeTags": {{boolean}},
   "LinkConfiguration": {
      "LogGroupConfiguration": {
         "Filter": "{{string}}"
      },
      "MetricConfiguration": {
         "Filter": "{{string}}"
      }
   },
   "ResourceTypes": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateLink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Identifier](#API_UpdateLink_RequestSyntax) **   <a name="OAM-UpdateLink-request-Identifier"></a>
The ARN of the link that you want to update.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

 ** [IncludeTags](#API_UpdateLink_RequestSyntax) **   <a name="OAM-UpdateLink-request-IncludeTags"></a>
Set `IncludeTags` to `true` to receive tags in the response, or `false` to exclude them.
The default value is `true`.
Type: Boolean
Required: No

 ** [LinkConfiguration](#API_UpdateLink_RequestSyntax) **   <a name="OAM-UpdateLink-request-LinkConfiguration"></a>
Use this structure to filter which metric namespaces and which log groups are to be shared from the source account to the monitoring account.
Type: [LinkConfiguration](API_LinkConfiguration.md) object
Required: No

 ** [ResourceTypes](#API_UpdateLink_RequestSyntax) **   <a name="OAM-UpdateLink-request-ResourceTypes"></a>
An array of strings that define which types of data that the source account will send to the monitoring account.
Your input here replaces the current set of data types that are shared.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor | AWS::ApplicationSignals::Service | AWS::ApplicationSignals::ServiceLevelObjective`
Required: Yes

## Response Syntax
<a name="API_UpdateLink_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Id": "string",
   "Label": "string",
   "LabelTemplate": "string",
   "LinkConfiguration": {
      "LogGroupConfiguration": {
         "Filter": "string"
      },
      "MetricConfiguration": {
         "Filter": "string"
      }
   },
   "ResourceTypes": [ "string" ],
   "SinkArn": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_UpdateLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-Arn"></a>
The ARN of the link that you have updated.
Type: String

 ** [Id](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-Id"></a>
The random ID string that AWS generated as part of the sink ARN.
Type: String

 ** [Label](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-Label"></a>
The label assigned to this link, with the variables resolved to their actual values.
Type: String

 ** [LabelTemplate](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-LabelTemplate"></a>
The exact label template that was specified when the link was created, with the template variables not resolved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [LinkConfiguration](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-LinkConfiguration"></a>
This structure includes filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.
Type: [LinkConfiguration](API_LinkConfiguration.md) object

 ** [ResourceTypes](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-ResourceTypes"></a>
The resource types now supported by this link.
Type: Array of strings

 ** [SinkArn](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-SinkArn"></a>
The ARN of the sink that is used for this link.
Type: String

 ** [Tags](#API_UpdateLink_ResponseSyntax) **   <a name="OAM-UpdateLink-response-Tags"></a>
The tags assigned to the link.
Type: String to string map

## Errors
<a name="API_UpdateLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## See Also
<a name="API_UpdateLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/UpdateLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/UpdateLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/UpdateLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/UpdateLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/UpdateLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/UpdateLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/UpdateLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/UpdateLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/UpdateLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/UpdateLink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Observability Access Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query OAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

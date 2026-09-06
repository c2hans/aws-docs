---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateLink.html
---

# CreateLink
<a name="API_CreateLink"></a>

Creates a link between a source account and a sink that you have created in a monitoring account. After the link is created, data is sent from the source account to the monitoring account. When you create a link, you can optionally specify filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.

Before you create a link, you must create a sink in the monitoring account and create a sink policy in that account. The sink policy must permit the source account to link to it. You can grant permission to source accounts by granting permission to an entire organization or to individual accounts.

For more information, see [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html) and [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html).

Each monitoring account can be linked to as many as 100,000 source accounts.

Each source account can be linked to as many as five monitoring accounts.

## Request Syntax
<a name="API_CreateLink_RequestSyntax"></a>

```
POST /CreateLink HTTP/1.1
Content-type: application/json

{
   "LabelTemplate": "{{string}}",
   "LinkConfiguration": {
      "LogGroupConfiguration": {
         "Filter": "{{string}}"
      },
      "MetricConfiguration": {
         "Filter": "{{string}}"
      }
   },
   "ResourceTypes": [ "{{string}}" ],
   "SinkIdentifier": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateLink_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLink_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [LabelTemplate](#API_CreateLink_RequestSyntax) **   <a name="OAM-CreateLink-request-LabelTemplate"></a>
Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.
You can use a custom label or use the following variables:
+  `$AccountName` is the name of the account
+  `$AccountEmail` is the globally unique email address of the account
+  `$AccountEmailNoDomain` is the email address of the account without the domain name
In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, the only supported option is to use custom labels, and the `$AccountName`, `$AccountEmail`, and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [LinkConfiguration](#API_CreateLink_RequestSyntax) **   <a name="OAM-CreateLink-request-LinkConfiguration"></a>
Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.
Type: [LinkConfiguration](API_LinkConfiguration.md) object
Required: No

 ** [ResourceTypes](#API_CreateLink_RequestSyntax) **   <a name="OAM-CreateLink-request-ResourceTypes"></a>
An array of strings that define which types of data that the source account shares with the monitoring account.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `AWS::CloudWatch::Metric | AWS::Logs::LogGroup | AWS::XRay::Trace | AWS::ApplicationInsights::Application | AWS::InternetMonitor::Monitor | AWS::ApplicationSignals::Service | AWS::ApplicationSignals::ServiceLevelObjective`
Required: Yes

 ** [SinkIdentifier](#API_CreateLink_RequestSyntax) **   <a name="OAM-CreateLink-request-SinkIdentifier"></a>
The ARN of the sink to use to create this link. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.
For more information about sinks, see [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html).
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

 ** [Tags](#API_CreateLink_RequestSyntax) **   <a name="OAM-CreateLink-request-Tags"></a>
Assigns one or more tags (key-value pairs) to the link.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateLink_ResponseSyntax"></a>

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
<a name="API_CreateLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-Arn"></a>
The ARN of the link that is newly created.
Type: String

 ** [Id](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-Id"></a>
The random ID string that AWS generated as part of the link ARN.
Type: String

 ** [Label](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-Label"></a>
The label that you assigned to this link. If the `labelTemplate` includes variables, this field displays the variables resolved to their actual values.
Type: String

 ** [LabelTemplate](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-LabelTemplate"></a>
The exact label template that you specified, with the variables not resolved.
Type: String

 ** [LinkConfiguration](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-LinkConfiguration"></a>
This structure includes filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.
Type: [LinkConfiguration](API_LinkConfiguration.md) object

 ** [ResourceTypes](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-ResourceTypes"></a>
The resource types supported by this link.
Type: Array of strings

 ** [SinkArn](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-SinkArn"></a>
The ARN of the sink that is used for this link.
Type: String

 ** [Tags](#API_CreateLink_ResponseSyntax) **   <a name="OAM-CreateLink-response-Tags"></a>
The tags assigned to the link.
Type: String to string map

## Errors
<a name="API_CreateLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
A resource was in an inconsistent state during an update or a deletion.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 429

## See Also
<a name="API_CreateLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/CreateLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/CreateLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/CreateLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/CreateLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/CreateLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/CreateLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/CreateLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/CreateLink)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/CreateLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/CreateLink)

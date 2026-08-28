---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Subscribe.html
---

# Subscribe
<a name="API_Subscribe"></a>

Creates an association between a notification rule and an Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client so that the associated target can receive notifications when the events described in the rule are triggered.

## Request Syntax
<a name="API_Subscribe_RequestSyntax"></a>

```
POST /subscribe HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "Target": {
      "TargetAddress": "{{string}}",
      "TargetType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_Subscribe_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_Subscribe_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_Subscribe_RequestSyntax) **   <a name="codestarnotifications-Subscribe-request-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule for which you want to create the association.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`
Required: Yes

 ** [ClientRequestToken](#API_Subscribe_RequestSyntax) **   <a name="codestarnotifications-Subscribe-request-ClientRequestToken"></a>
An enumeration token that, when provided in a request, returns the next batch of the results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w:/-]+$`
Required: No

 ** [Target](#API_Subscribe_RequestSyntax) **   <a name="codestarnotifications-Subscribe-request-Target"></a>
Information about the Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients associated with a notification rule.
Type: [Target](API_Target.md) object
Required: Yes

## Response Syntax
<a name="API_Subscribe_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_Subscribe_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_Subscribe_ResponseSyntax) **   <a name="codestarnotifications-Subscribe-response-Arn"></a>
The Amazon Resource Name (ARN) of the notification rule for which you have created assocations.
Type: String
Pattern: `^arn:aws[^:\s]*:codestar-notifications:[^:\s]+:\d{12}:notificationrule\/(.*\S)?$`

## Errors
<a name="API_Subscribe_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConfigurationException **
Some or all of the configuration is incomplete, missing, or not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 AWS CodeStar Notifications can't find a resource that matches the provided ARN.
HTTP Status Code: 404

 ** ValidationException **
One or more parameter values are not valid.
HTTP Status Code: 400

## See Also
<a name="API_Subscribe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codestar-notifications-2019-10-15/Subscribe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/Subscribe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeStar Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codestar-notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

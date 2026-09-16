---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ListExtensions.html
---

# ListExtensions
<a name="API_ListExtensions"></a>

Lists all custom and AWS authored AWS AppConfig extensions in the account. For more information about extensions, see [Extending workflows](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) in the * AWS AppConfig User Guide*.

## Request Syntax
<a name="API_ListExtensions_RequestSyntax"></a>

```
GET /extensions?max_results={{MaxResults}}&name={{Name}}&next_token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExtensions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListExtensions_RequestSyntax) **   <a name="appconfig-ListExtensions-request-uri-MaxResults"></a>
The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [Name](#API_ListExtensions_RequestSyntax) **   <a name="appconfig-ListExtensions-request-uri-Name"></a>
The extension name.
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [NextToken](#API_ListExtensions_RequestSyntax) **   <a name="appconfig-ListExtensions-request-uri-NextToken"></a>
A token to start the list. Use this token to get the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListExtensions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExtensions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "Arn": "string",
         "Description": "string",
         "Id": "string",
         "Name": "string",
         "VersionNumber": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListExtensions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListExtensions_ResponseSyntax) **   <a name="appconfig-ListExtensions-response-Items"></a>
The list of available extensions. The list includes AWS authored and user-created extensions.
Type: Array of [ExtensionSummary](API_ExtensionSummary.md) objects

 ** [NextToken](#API_ListExtensions_ResponseSyntax) **   <a name="appconfig-ListExtensions-response-NextToken"></a>
The token for the next set of items to return. Use this token to get the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListExtensions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

## Examples
<a name="API_ListExtensions_Examples"></a>

### Example
<a name="API_ListExtensions_Example_1"></a>

This example illustrates one usage of ListExtensions.

#### Sample Request
<a name="API_ListExtensions_Example_1_Request"></a>

```
GET /extensions HTTP/1.1
Host: appconfig.us-west-2.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.7.19 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/appconfig.list-extensions
X-Amz-Date: 20220803T215314Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220803/us-west-2/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
```

#### Sample Response
<a name="API_ListExtensions_Example_1_Response"></a>

```
{
	"Items": [{
		"Arn": "arn:aws:appconfig:us-west-2:111122223333:extension/6czExample/1",
		"Description": null,
		"Id": "6czExampmle",
		"Name": "my-test-extension",
		"VersionNumber": 1
	}, {
		"Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.FeatureFlags/1",
		"Description": "Validates AppConfig feature flag data automatically against a JSON schema that includes structure and constraints. Also transforms feature flag data prior to sending to the client. This extension is automatically associated to configuration profiles with type \"AWS.AppConfig.FeatureFlags\".",
		"Id": "AWS.AppConfig.FeatureFlags",
		"Name": "AppConfig Feature Flags Helper",
		"VersionNumber": 1
	}, {
		"Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.JiraIntegration/1",
		"Description": "Exports feature flag data from AWS AppConfig into Jira. The lifecycle of each feature flag in AppConfig is tracked in Jira as an individual issue. Customers can see in Jira when flags are updated, turned on or off. Works in conjunction with the AppConfig app in the Atlassian Marketplace and is automatically associated to configuration profiles configured within that app.",
		"Id": "AWS.AppConfig.JiraIntegration",
		"Name": "AppConfig integration with Atlassian Jira",
		"VersionNumber": 1
	}, {
		"Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.DeploymentNotificationsToEventBridge/1",
		"Description": "Sends events to Amazon EventBridge when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile.",
		"Id": "AWS.AppConfig.DeploymentNotificationsToEventBridge",
		"Name": "AppConfig deployment events to Amazon EventBridge",
		"VersionNumber": 1
	}, {
		"Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.DeploymentNotificationsToSqs/1",
		"Description": "Sends messages to the configured Amazon SQS queue when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile.",
		"Id": "AWS.AppConfig.DeploymentNotificationsToSqs",
		"Name": "AppConfig deployment events to Amazon SQS",
		"VersionNumber": 1
	}, {
		"Arn": null,
		"Description": "Sends events to the configured Amazon SNS topic when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile.",
		"Id": "AWS.AppConfig.DeploymentNotificationsToSns",
		"Name": "AppConfig deployment events to Amazon SNS",
		"VersionNumber": 1
	}],
	"NextToken": null
}
```

## See Also
<a name="API_ListExtensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/ListExtensions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ListExtensions)

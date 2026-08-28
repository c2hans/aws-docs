---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_GetSubscription.html
---

# GetSubscription
<a name="API_GetSubscription"></a>

Returns information about the AWS account used for billing purposes and the billing plan for the space.

## Request Syntax
<a name="API_GetSubscription_RequestSyntax"></a>

```
GET /v1/spaces/{{spaceName}}/subscription HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceName](#API_GetSubscription_RequestSyntax) **   <a name="codecatalyst-GetSubscription-request-uri-spaceName"></a>
The name of the space.
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`
Required: Yes

## Request Body
<a name="API_GetSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSubscription_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "awsAccountName": "string",
   "pendingSubscriptionStartTime": "string",
   "pendingSubscriptionType": "string",
   "subscriptionType": "string"
}
```

## Response Elements
<a name="API_GetSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [awsAccountName](#API_GetSubscription_ResponseSyntax) **   <a name="codecatalyst-GetSubscription-response-awsAccountName"></a>
The display name of the AWS account used for billing for the space.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-zA-Z0-9]+(?:[-_\.][a-zA-Z0-9]+)*`

 ** [pendingSubscriptionStartTime](#API_GetSubscription_ResponseSyntax) **   <a name="codecatalyst-GetSubscription-response-pendingSubscriptionStartTime"></a>
The day and time the pending change will be applied to the space, in coordinated universal time (UTC) timestamp format as specified in [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).
Type: Timestamp

 ** [pendingSubscriptionType](#API_GetSubscription_ResponseSyntax) **   <a name="codecatalyst-GetSubscription-response-pendingSubscriptionType"></a>
The type of the billing plan that the space will be changed to at the start of the next billing cycle. This applies only to changes that reduce the functionality available for the space. Billing plan changes that increase functionality are applied immediately. For more information, see [Pricing](https://codecatalyst.aws/explore/pricing).
Type: String

 ** [subscriptionType](#API_GetSubscription_ResponseSyntax) **   <a name="codecatalyst-GetSubscription-response-subscriptionType"></a>
The type of the billing plan for the space.
Type: String

## Errors
<a name="API_GetSubscription_Errors"></a>

 ** AccessDeniedException **
The request was denied because you don't have sufficient access to perform this action. Verify that you are a member of a role that allows this action.
HTTP Status Code: 403

 ** ConflictException **
The request was denied because the requested operation would cause a conflict with the current state of a service resource associated with the request. Another user might have updated the resource. Reload, make sure you have the latest data, and then try again.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was denied because the specified resource was not found. Verify that the spelling is correct and that you have access to the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request was denied because one or more resources has reached its limits for the tier the space belongs to. Either reduce the number of resources, or change the tier if applicable.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request was denied because an input failed to satisfy the constraints specified by the service. Check the spelling and input requirements, and then try again.
HTTP Status Code: 400

## See Also
<a name="API_GetSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codecatalyst-2022-09-28/GetSubscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/GetSubscription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

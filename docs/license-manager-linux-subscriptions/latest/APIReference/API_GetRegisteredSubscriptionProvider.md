---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_GetRegisteredSubscriptionProvider.html
---

# GetRegisteredSubscriptionProvider
<a name="API_GetRegisteredSubscriptionProvider"></a>

Get details for a Bring Your Own License (BYOL) subscription that's registered to your account.

## Request Syntax
<a name="API_GetRegisteredSubscriptionProvider_RequestSyntax"></a>

```
POST /subscription/GetRegisteredSubscriptionProvider HTTP/1.1
Content-type: application/json

{
   "SubscriptionProviderArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetRegisteredSubscriptionProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRegisteredSubscriptionProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SubscriptionProviderArn](#API_GetRegisteredSubscriptionProvider_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-request-SubscriptionProviderArn"></a>
The Amazon Resource Name (ARN) of the BYOL registration resource to get details for.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,510}/[a-z0-9-\.]{1,510}`
Required: Yes

## Response Syntax
<a name="API_GetRegisteredSubscriptionProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastSuccessfulDataRetrievalTime": "string",
   "SecretArn": "string",
   "SubscriptionProviderArn": "string",
   "SubscriptionProviderSource": "string",
   "SubscriptionProviderStatus": "string",
   "SubscriptionProviderStatusMessage": "string"
}
```

## Response Elements
<a name="API_GetRegisteredSubscriptionProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastSuccessfulDataRetrievalTime](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-LastSuccessfulDataRetrievalTime"></a>
The timestamp from the last time License Manager retrieved subscription details from your registered third-party Linux subscription provider.
Type: String

 ** [SecretArn](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-SecretArn"></a>
The Amazon Resource Name (ARN) of the third-party access secret stored in AWS Secrets Manager for the BYOL registration resource specified in the request.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:secretsmanager:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:secret:[^/]{1,1023}`

 ** [SubscriptionProviderArn](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-SubscriptionProviderArn"></a>
The Amazon Resource Name (ARN) for the BYOL registration resource specified in the request.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{1,510}/[a-z0-9-\.]{1,510}`

 ** [SubscriptionProviderSource](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-SubscriptionProviderSource"></a>
The subscription provider for the BYOL registration resource specified in the request.
Type: String
Valid Values: `RedHat`

 ** [SubscriptionProviderStatus](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-SubscriptionProviderStatus"></a>
The status of the Linux subscription provider access token from the last successful subscription data request.
Type: String
Valid Values: `ACTIVE | INVALID | PENDING`

 ** [SubscriptionProviderStatusMessage](#API_GetRegisteredSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-GetRegisteredSubscriptionProvider-response-SubscriptionProviderStatusMessage"></a>
The detailed message from your subscription provider token status.
Type: String

## Errors
<a name="API_GetRegisteredSubscriptionProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Unable to find the requested AWS resource.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_GetRegisteredSubscriptionProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/GetRegisteredSubscriptionProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

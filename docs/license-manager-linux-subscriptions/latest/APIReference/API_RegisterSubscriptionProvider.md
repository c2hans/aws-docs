---
source_url: https://docs.aws.amazon.com/license-manager-linux-subscriptions/latest/APIReference/API_RegisterSubscriptionProvider.html
---

# RegisterSubscriptionProvider
<a name="API_RegisterSubscriptionProvider"></a>

Register the supported third-party subscription provider for your Bring Your Own License (BYOL) subscription.

## Request Syntax
<a name="API_RegisterSubscriptionProvider_RequestSyntax"></a>

```
POST /subscription/RegisterSubscriptionProvider HTTP/1.1
Content-type: application/json

{
   "SecretArn": "{{string}}",
   "SubscriptionProviderSource": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_RegisterSubscriptionProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterSubscriptionProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SecretArn](#API_RegisterSubscriptionProvider_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-request-SecretArn"></a>
The Amazon Resource Name (ARN) of the secret where you've stored your subscription provider's access token. For RHEL subscriptions managed through the Red Hat Subscription Manager (RHSM), the secret contains your Red Hat Offline token.
Type: String
Pattern: `arn:[a-z0-9-\.]{1,63}:secretsmanager:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:secret:[^/]{1,1023}`
Required: Yes

 ** [SubscriptionProviderSource](#API_RegisterSubscriptionProvider_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-request-SubscriptionProviderSource"></a>
The supported Linux subscription provider to register.
Type: String
Valid Values: `RedHat`
Required: Yes

 ** [Tags](#API_RegisterSubscriptionProvider_RequestSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-request-Tags"></a>
The metadata tags to assign to your registered Linux subscription provider resource.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_RegisterSubscriptionProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "SubscriptionProviderArn": "string",
   "SubscriptionProviderSource": "string",
   "SubscriptionProviderStatus": "string"
}
```

## Response Elements
<a name="API_RegisterSubscriptionProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SubscriptionProviderArn](#API_RegisterSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-response-SubscriptionProviderArn"></a>
The Amazon Resource Name (ARN) of the Linux subscription provider resource that you registered.
Type: String

 ** [SubscriptionProviderSource](#API_RegisterSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-response-SubscriptionProviderSource"></a>
The Linux subscription provider that you registered.
Type: String
Valid Values: `RedHat`

 ** [SubscriptionProviderStatus](#API_RegisterSubscriptionProvider_ResponseSyntax) **   <a name="licensemanagerlinuxsubscriptions-RegisterSubscriptionProvider-response-SubscriptionProviderStatus"></a>
Indicates the status of the registration action for the Linux subscription provider that you requested.
Type: String
Valid Values: `ACTIVE | INVALID | PENDING`

## Errors
<a name="API_RegisterSubscriptionProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An exception occurred with the service.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_RegisterSubscriptionProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-linux-subscriptions-2018-05-10/RegisterSubscriptionProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for License Manager Linux Subscriptions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager-linux-subscriptions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeleteConfigurationProfile.html
---

# DeleteConfigurationProfile
<a name="API_DeleteConfigurationProfile"></a>

Deletes a configuration profile.

To prevent users from unintentionally deleting actively-used configuration profiles, enable [deletion protection](https://docs.aws.amazon.com/appconfig/latest/userguide/deletion-protection.html).

## Request Syntax
<a name="API_DeleteConfigurationProfile_RequestSyntax"></a>

```
DELETE /applications/{{ApplicationId}}/configurationprofiles/{{ConfigurationProfileId}} HTTP/1.1
x-amzn-deletion-protection-check: {{DeletionProtectionCheck}}
```

## URI Request Parameters
<a name="API_DeleteConfigurationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationId](#API_DeleteConfigurationProfile_RequestSyntax) **   <a name="appconfig-DeleteConfigurationProfile-request-uri-ApplicationId"></a>
The ID or name of the application that includes the configuration profile you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ConfigurationProfileId](#API_DeleteConfigurationProfile_RequestSyntax) **   <a name="appconfig-DeleteConfigurationProfile-request-uri-ConfigurationProfileId"></a>
The ID or name of the configuration profile you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [DeletionProtectionCheck](#API_DeleteConfigurationProfile_RequestSyntax) **   <a name="appconfig-DeleteConfigurationProfile-request-DeletionProtectionCheck"></a>
A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile if your application has called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for the configuration profile during the specified interval.
This parameter supports the following values:
+  `BYPASS`: Instructs AWS AppConfig to bypass the deletion protection check and delete a configuration profile even if deletion protection would have otherwise prevented it.
+  `APPLY`: Instructs the deletion protection check to run, even if deletion protection is disabled at the account level. `APPLY` also forces the deletion protection check to run against resources created in the past hour, which are normally excluded from deletion protection checks.
+  `ACCOUNT_DEFAULT`: The default setting, which instructs AWS AppConfig to implement the deletion protection value specified in the `UpdateAccountSettings` API.
Valid Values: `ACCOUNT_DEFAULT | APPLY | BYPASS`

## Request Body
<a name="API_DeleteConfigurationProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteConfigurationProfile_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteConfigurationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteConfigurationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_DeleteConfigurationProfile_Examples"></a>

### Example
<a name="API_DeleteConfigurationProfile_Example_1"></a>

This example illustrates one usage of DeleteConfigurationProfile.

#### Sample Request
<a name="API_DeleteConfigurationProfile_Example_1_Request"></a>

```
DELETE /applications/339ohji/configurationprofiles/ur8hx2f HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.delete-configuration-profile
X-Amz-Date: 20210920T221708Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_DeleteConfigurationProfile_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_DeleteConfigurationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/DeleteConfigurationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeleteConfigurationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

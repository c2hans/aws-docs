---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdatePublicSharingSettings.html
---

# UpdatePublicSharingSettings
<a name="API_UpdatePublicSharingSettings"></a>

**Important**
This API controls public sharing settings for your entire Quick Sight account, affecting data security and access. When you enable public sharing:
Dashboards can be shared publicly
This setting affects your entire AWS account and all Quick Sight users
 **Before proceeding:** Ensure you understand the security implications and have proper IAM permissions configured.

Use the `UpdatePublicSharingSettings` operation to turn on or turn off the public sharing settings of an Amazon Quick Sight dashboard.

To use this operation, turn on session capacity pricing for your Amazon Quick Sight account.

Before you can turn on public sharing on your account, make sure to give public sharing permissions to an administrative user in the AWS Identity and Access Management (IAM) console. For more information on using IAM with Amazon Quick Sight, see [Using Quick with IAM](https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html) in the *Amazon Quick Sight User Guide*.

## Request Syntax
<a name="API_UpdatePublicSharingSettings_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/public-sharing-settings HTTP/1.1
Content-type: application/json

{
   "PublicSharingEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdatePublicSharingSettings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_UpdatePublicSharingSettings_RequestSyntax) **   <a name="QS-UpdatePublicSharingSettings-request-uri-AwsAccountId"></a>
The AWS account ID associated with your Amazon Quick Sight subscription.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdatePublicSharingSettings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PublicSharingEnabled](#API_UpdatePublicSharingSettings_RequestSyntax) **   <a name="QS-UpdatePublicSharingSettings-request-PublicSharingEnabled"></a>
A Boolean value that indicates whether public sharing is turned on for an Quick account.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdatePublicSharingSettings_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdatePublicSharingSettings_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdatePublicSharingSettings_ResponseSyntax) **   <a name="QS-UpdatePublicSharingSettings-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_UpdatePublicSharingSettings_ResponseSyntax) **   <a name="QS-UpdatePublicSharingSettings-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdatePublicSharingSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedPricingPlanException **
This error indicates that you are calling an embedding operation in Amazon Quick Sight without the required pricing plan on your AWS account. Before you can use embedding for anonymous users, a Quick Suite administrator needs to add capacity pricing to Quick Sight. You can do this on the **Manage Quick Suite** page.
After capacity pricing is added, you can use the ` [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html) ` API operation with the `--identity-type ANONYMOUS` option.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdatePublicSharingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdatePublicSharingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdatePublicSharingSettings)

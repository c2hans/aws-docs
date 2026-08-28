---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListAssetsForLicenseAssetGroup.html
---

# ListAssetsForLicenseAssetGroup
<a name="API_ListAssetsForLicenseAssetGroup"></a>

Lists assets for a license asset group.

## Request Syntax
<a name="API_ListAssetsForLicenseAssetGroup_RequestSyntax"></a>

```
{
   "AssetType": "{{string}}",
   "LicenseAssetGroupArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAssetsForLicenseAssetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetType](#API_ListAssetsForLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-request-AssetType"></a>
Asset type. The possible values are `Instance` \| `License` \| `LicenseConfiguration`.
Type: String
Required: Yes

 ** [LicenseAssetGroupArn](#API_ListAssetsForLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-request-LicenseAssetGroupArn"></a>
Amazon Resource Name (ARN) of the license asset group.
Type: String
Required: Yes

 ** [MaxResults](#API_ListAssetsForLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-request-MaxResults"></a>
Maximum number of results to return in a single call.
Type: Integer
Required: No

 ** [NextToken](#API_ListAssetsForLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-request-NextToken"></a>
Token for the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_ListAssetsForLicenseAssetGroup_ResponseSyntax"></a>

```
{
   "Assets": [
      {
         "AssetArn": "string",
         "LatestAssetDiscoveryTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAssetsForLicenseAssetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Assets](#API_ListAssetsForLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-response-Assets"></a>
Assets.
Type: Array of [Asset](API_Asset.md) objects

 ** [NextToken](#API_ListAssetsForLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-ListAssetsForLicenseAssetGroup-response-NextToken"></a>
Token for the next set of results.
Type: String

## Errors
<a name="API_ListAssetsForLicenseAssetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_ListAssetsForLicenseAssetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/ListAssetsForLicenseAssetGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

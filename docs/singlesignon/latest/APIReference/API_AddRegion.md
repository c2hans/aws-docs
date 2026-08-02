---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html
---

# AddRegion
<a name="API_AddRegion"></a>

Adds a Region to an IAM Identity Center instance. This operation initiates an asynchronous workflow to replicate the IAM Identity Center instance to the target Region. The Region status is set to ADDING at first and changes to ACTIVE when the workflow completes.

To use this operation, your IAM Identity Center instance and the target Region must meet the requirements described in the [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html#multi-region-prerequisites).

The following actions are related to `AddRegion`:
+  [RemoveRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html)
+  [DescribeRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html)
+  [ListRegions](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html)

## Request Syntax
<a name="API_AddRegion_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "RegionName": "{{string}}"
}
```

## Request Parameters
<a name="API_AddRegion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_AddRegion_RequestSyntax) **   <a name="singlesignon-AddRegion-request-InstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance to replicate to the target Region.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [RegionName](#API_AddRegion_RequestSyntax) **   <a name="singlesignon-AddRegion-request-RegionName"></a>
The name of the AWS Region to add to the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of AWS Region names (for example, us-east-1).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: Yes

## Response Syntax
<a name="API_AddRegion_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements
<a name="API_AddRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_AddRegion_ResponseSyntax) **   <a name="singlesignon-AddRegion-response-Status"></a>
The status of the Region after the Add operation. The status is ADDING when the asynchronous workflow is in progress and changes to ACTIVE when complete.
Type: String
Valid Values: `ACTIVE | ADDING | REMOVING`

## Errors
<a name="API_AddRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure with an internal server.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Indicates that the principal has crossed the permitted number of resources that can be created.
HTTP Status Code: 400

 ** ThrottlingException **
Indicates that the principal has crossed the throttling limits of the API operations.
 ** Reason **
The reason for the throttling exception.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_AddRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/AddRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/AddRegion)

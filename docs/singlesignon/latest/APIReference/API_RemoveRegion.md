---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html
---

# RemoveRegion
<a name="API_RemoveRegion"></a>

Removes an additional Region from an IAM Identity Center instance. This operation initiates an asynchronous workflow to clean up IAM Identity Center resources in the specified additional Region. The Region status is set to REMOVING and the Region record is deleted when the workflow completes. The request must be made from the primary Region. The target Region cannot be the primary Region, and no other add or remove Region workflows can be in progress.

The following actions are related to `RemoveRegion`:
+  [ AddRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html)
+  [DescribeRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html)
+  [ListRegions](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html)

## Request Syntax
<a name="API_RemoveRegion_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "RegionName": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveRegion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_RemoveRegion_RequestSyntax) **   <a name="singlesignon-RemoveRegion-request-InstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [RegionName](#API_RemoveRegion_RequestSyntax) **   <a name="singlesignon-RemoveRegion-request-RegionName"></a>
The name of the AWS Region to remove from the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of AWS Region names (for example, us-east-1). The primary Region cannot be removed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: Yes

## Response Syntax
<a name="API_RemoveRegion_ResponseSyntax"></a>

```
{
   "Status": "string"
}
```

## Response Elements
<a name="API_RemoveRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Status](#API_RemoveRegion_ResponseSyntax) **   <a name="singlesignon-RemoveRegion-response-Status"></a>
The status of the Region after the remove operation. The status is REMOVING when the asynchronous workflow is in progress. The Region record is deleted when the workflow completes.
Type: String
Valid Values: `ACTIVE | ADDING | REMOVING`

## Errors
<a name="API_RemoveRegion_Errors"></a>

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

 ** ResourceNotFoundException **
Indicates that a requested resource is not found.
 ** Reason **
The reason for the resource not found exception.
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
<a name="API_RemoveRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/RemoveRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/RemoveRegion)

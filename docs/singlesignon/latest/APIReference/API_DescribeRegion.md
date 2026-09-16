---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_DescribeRegion.html
---

# DescribeRegion
<a name="API_DescribeRegion"></a>

Retrieves details about a specific Region enabled in an IAM Identity Center instance. Details include the Region name, current status (ACTIVE, ADDING, or REMOVING), the date when the Region was added, and whether it is the primary Region. The request must be made from one of the enabled Regions of the IAM Identity Center instance.

The following actions are related to `DescribeRegion`:
+  [ AddRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_AddRegion.html)
+  [RemoveRegion](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_RemoveRegion.html)
+  [ListRegions](https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListRegions.html)

## Request Syntax
<a name="API_DescribeRegion_RequestSyntax"></a>

```
{
   "InstanceArn": "{{string}}",
   "RegionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRegion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceArn](#API_DescribeRegion_RequestSyntax) **   <a name="singlesignon-DescribeRegion-request-InstanceArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: Yes

 ** [RegionName](#API_DescribeRegion_RequestSyntax) **   <a name="singlesignon-DescribeRegion-request-RegionName"></a>
The name of the AWS Region to retrieve information about. The Region name must be 1-32 characters long and follow the pattern of AWS Region names (for example, us-east-1).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: Yes

## Response Syntax
<a name="API_DescribeRegion_ResponseSyntax"></a>

```
{
   "AddedDate": number,
   "IsPrimaryRegion": boolean,
   "RegionName": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AddedDate](#API_DescribeRegion_ResponseSyntax) **   <a name="singlesignon-DescribeRegion-response-AddedDate"></a>
The timestamp when the Region was added to the IAM Identity Center instance. For the primary Region, this is the IAM Identity Center instance creation time.
Type: Timestamp

 ** [IsPrimaryRegion](#API_DescribeRegion_ResponseSyntax) **   <a name="singlesignon-DescribeRegion-response-IsPrimaryRegion"></a>
Indicates whether this is the primary Region where the IAM Identity Center instance was originally enabled. For more information on the difference between the primary Region and additional Regions, see [IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/multi-region-iam-identity-center.html)
Type: Boolean

 ** [RegionName](#API_DescribeRegion_ResponseSyntax) **   <a name="singlesignon-DescribeRegion-response-RegionName"></a>
The AWS Region name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`

 ** [Status](#API_DescribeRegion_ResponseSyntax) **   <a name="singlesignon-DescribeRegion-response-Status"></a>
The current status of the Region. Valid values are ACTIVE (Region is operational), ADDING (Region replication workflow is in progress), or REMOVING (Region removal workflow is in progress).
Type: String
Valid Values: `ACTIVE | ADDING | REMOVING`

## Errors
<a name="API_DescribeRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 ** Reason **
The reason for the access denied exception.
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
<a name="API_DescribeRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sso-admin-2020-07-20/DescribeRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/DescribeRegion)

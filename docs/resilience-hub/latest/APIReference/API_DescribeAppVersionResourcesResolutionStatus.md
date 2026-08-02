---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_DescribeAppVersionResourcesResolutionStatus.html
---

# DescribeAppVersionResourcesResolutionStatus
<a name="API_DescribeAppVersionResourcesResolutionStatus"></a>

Returns the resolution status for the specified resolution identifier for an application version. If `resolutionId` is not specified, the current resolution status is returned.

## Request Syntax
<a name="API_DescribeAppVersionResourcesResolutionStatus_RequestSyntax"></a>

```
POST /describe-app-version-resources-resolution-status HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "appVersion": "{{string}}",
   "resolutionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeAppVersionResourcesResolutionStatus_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeAppVersionResourcesResolutionStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_DescribeAppVersionResourcesResolutionStatus_RequestSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [appVersion](#API_DescribeAppVersionResourcesResolutionStatus_RequestSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-request-appVersion"></a>
The version of the application.
Type: String
Pattern: `\S{1,50}`
Required: Yes

 ** [resolutionId](#API_DescribeAppVersionResourcesResolutionStatus_RequestSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-request-resolutionId"></a>
The identifier for a specific resolution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appVersion": "string",
   "errorMessage": "string",
   "resolutionId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeAppVersionResourcesResolutionStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-response-appVersion"></a>
The version of the application.
Type: String
Pattern: `\S{1,50}`

 ** [errorMessage](#API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-response-errorMessage"></a>
The returned error message for the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [resolutionId](#API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-response-resolutionId"></a>
The identifier for a specific resolution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [status](#API_DescribeAppVersionResourcesResolutionStatus_ResponseSyntax) **   <a name="resiliencehub-DescribeAppVersionResourcesResolutionStatus-response-status"></a>
Status of the action.
Type: String
Valid Values: `Pending | InProgress | Failed | Success`

## Errors
<a name="API_DescribeAppVersionResourcesResolutionStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** InternalServerException **
This exception occurs when there is an internal failure in the AWS Resilience Hub service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This exception occurs when the specified resource could not be found.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 404

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAppVersionResourcesResolutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/DescribeAppVersionResourcesResolutionStatus)

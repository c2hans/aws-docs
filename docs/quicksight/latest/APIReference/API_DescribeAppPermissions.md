---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAppPermissions.html
---

# DescribeAppPermissions
<a name="API_DescribeAppPermissions"></a>

Describes the resource permissions for an app.

## Request Syntax
<a name="API_DescribeAppPermissions_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/apps/{{AppId}}/permissions HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAppPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AppId](#API_DescribeAppPermissions_RequestSyntax) **   <a name="QS-DescribeAppPermissions-request-uri-AppId"></a>
The ID of the app.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [AwsAccountId](#API_DescribeAppPermissions_RequestSyntax) **   <a name="QS-DescribeAppPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the app.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_DescribeAppPermissions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAppPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppId": "string",
   "Arn": "string",
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeAppPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppId](#API_DescribeAppPermissions_ResponseSyntax) **   <a name="QS-DescribeAppPermissions-response-AppId"></a>
The ID of the app.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [Arn](#API_DescribeAppPermissions_ResponseSyntax) **   <a name="QS-DescribeAppPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the app.
Type: String

 ** [Permissions](#API_DescribeAppPermissions_ResponseSyntax) **   <a name="QS-DescribeAppPermissions-response-Permissions"></a>
The resource permissions for the app.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Minimum number of 1 item. Maximum number of 64 items.

 ** [RequestId](#API_DescribeAppPermissions_ResponseSyntax) **   <a name="QS-DescribeAppPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_DescribeAppPermissions_Errors"></a>

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

 ** InvalidParameterException **
One or more parameter has a value that isn't valid.
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

## See Also
<a name="API_DescribeAppPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAppPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAppPermissions)

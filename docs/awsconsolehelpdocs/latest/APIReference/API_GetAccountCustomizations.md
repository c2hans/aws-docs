---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_GetAccountCustomizations.html
---

# GetAccountCustomizations
<a name="API_GetAccountCustomizations"></a>

Returns the current account customization settings, including account color, visible services, and visible Regions. Settings that you have not configured return their default values: visible Regions and visible services return `null`, and account color returns `none`.

**Note**
The `visibleServices` and `visibleRegions` settings control only the appearance of services and Regions in the AWS Management Console. They do not restrict access through the AWS CLI, SDKs, or other APIs.

## Request Syntax
<a name="API_GetAccountCustomizations_RequestSyntax"></a>

```
GET /v1/account-customizations HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAccountCustomizations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetAccountCustomizations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAccountCustomizations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountColor": "string",
   "visibleRegions": [ "string" ],
   "visibleServices": [ "string" ]
}
```

## Response Elements
<a name="API_GetAccountCustomizations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountColor](#API_GetAccountCustomizations_ResponseSyntax) **   <a name="uxc-GetAccountCustomizations-response-accountColor"></a>
The account color preference. A value of `none` indicates that you have not set a color.
Type: String
Valid Values: `none | pink | purple | darkBlue | lightBlue | teal | green | yellow | orange | red`

 ** [visibleRegions](#API_GetAccountCustomizations_ResponseSyntax) **   <a name="uxc-GetAccountCustomizations-response-visibleRegions"></a>
The list of AWS Region codes that are visible to the account in the AWS Management Console. A value of `null` indicates that you have not configured this feature and all Regions are visible. For a list of valid Region codes, see [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[a-z]{2}(-[a-z]{1,10}){1,2}-[1-9]`

 ** [visibleServices](#API_GetAccountCustomizations_ResponseSyntax) **   <a name="uxc-GetAccountCustomizations-response-visibleServices"></a>
The list of AWS service identifiers that are visible to the account in the AWS Management Console. A value of `null` indicates that you have not configured this feature and all services are visible. For valid service identifiers, call [ListServices](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`

## Errors
<a name="API_GetAccountCustomizations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. Verify that your IAM policy includes the required `uxc:` permissions for the operation that you are calling. For more information on IAM permissions, see [AWS managed policies for AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.html).
HTTP Status Code: 403

 ** InternalServerException **
The service encountered an internal error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling. Reduce the frequency of your requests.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that are invalid.
HTTP Status Code: 400

## Examples
<a name="API_GetAccountCustomizations_Examples"></a>

### Retrieve account customizations when all settings are configured
<a name="API_GetAccountCustomizations_Example_1"></a>

The following example retrieves the current account customization settings. In this example, all three settings have been previously configured.

#### Sample Request
<a name="API_GetAccountCustomizations_Example_1_Request"></a>

```
GET /v1/account-customizations HTTP/1.1
Host: uxc.us-east-1.amazonaws.com
Content-type: application/json
```

#### Sample Response
<a name="API_GetAccountCustomizations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-type: application/json

{
   "accountColor": "teal",
   "visibleServices": ["s3", "ec2", "lambda"],
   "visibleRegions": ["us-east-1", "us-west-2"]
}
```

### Retrieve account customizations when some settings are not configured
<a name="API_GetAccountCustomizations_Example_2"></a>

The following example retrieves the current account customization settings. In this example, account color and visible Regions have not been configured, so they return `null`.

#### Sample Request
<a name="API_GetAccountCustomizations_Example_2_Request"></a>

```
GET /v1/account-customizations HTTP/1.1
Host: uxc.us-east-1.amazonaws.com
Content-type: application/json
```

#### Sample Response
<a name="API_GetAccountCustomizations_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-type: application/json

{
   "accountColor": "none",
   "visibleServices": ["s3", "ec2", "lambda"],
   "visibleRegions": null
}
```

## See Also
<a name="API_GetAccountCustomizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/uxc-2024-07-01/GetAccountCustomizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/uxc-2024-07-01/GetAccountCustomizations)

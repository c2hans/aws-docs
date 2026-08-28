---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.html
---

# UpdateAccountCustomizations
<a name="API_UpdateAccountCustomizations"></a>

Updates one or more account customization settings. You can update account color, visible services, and visible Regions in a single request. Only the settings that you include in the request body are modified. Omitted settings remain unchanged. To reset a setting to its default behavior, set the value to `null` for visible Regions and visible services, or `none` for account color. This operation is idempotent.

**Note**
The `visibleServices` and `visibleRegions` settings control only the appearance of services and Regions in the AWS Management Console. They do not restrict access through the AWS CLI, SDKs, or other APIs.

## Request Syntax
<a name="API_UpdateAccountCustomizations_RequestSyntax"></a>

```
PATCH /v1/account-customizations HTTP/1.1
Content-type: application/json

{
   "accountColor": "{{string}}",
   "visibleRegions": [ "{{string}}" ],
   "visibleServices": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateAccountCustomizations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateAccountCustomizations_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountColor](#API_UpdateAccountCustomizations_RequestSyntax) **   <a name="uxc-UpdateAccountCustomizations-request-accountColor"></a>
The account color preference to set. Set to `none` to reset to the default (no color).
Type: String
Valid Values: `none | pink | purple | darkBlue | lightBlue | teal | green | yellow | orange | red`
Required: No

 ** [visibleRegions](#API_UpdateAccountCustomizations_RequestSyntax) **   <a name="uxc-UpdateAccountCustomizations-request-visibleRegions"></a>
The list of AWS Region codes to make visible in the AWS Management Console. Set to `null` to reset to the default, which makes all Regions visible. For a list of valid Region codes, see [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[a-z]{2}(-[a-z]{1,10}){1,2}-[1-9]`
Required: No

 ** [visibleServices](#API_UpdateAccountCustomizations_RequestSyntax) **   <a name="uxc-UpdateAccountCustomizations-request-visibleServices"></a>
The list of AWS service identifiers to make visible in the AWS Management Console. Set to `null` to reset to the default, which makes all services visible. For valid service identifiers, call [ListServices](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`
Required: No

## Response Syntax
<a name="API_UpdateAccountCustomizations_ResponseSyntax"></a>

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
<a name="API_UpdateAccountCustomizations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountColor](#API_UpdateAccountCustomizations_ResponseSyntax) **   <a name="uxc-UpdateAccountCustomizations-response-accountColor"></a>
The current account color preference after the update.
Type: String
Valid Values: `none | pink | purple | darkBlue | lightBlue | teal | green | yellow | orange | red`

 ** [visibleRegions](#API_UpdateAccountCustomizations_ResponseSyntax) **   <a name="uxc-UpdateAccountCustomizations-response-visibleRegions"></a>
The current list of visible Region codes after the update.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Pattern: `[a-z]{2}(-[a-z]{1,10}){1,2}-[1-9]`

 ** [visibleServices](#API_UpdateAccountCustomizations_ResponseSyntax) **   <a name="uxc-UpdateAccountCustomizations-response-visibleServices"></a>
The current list of visible service identifiers after the update.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`

## Errors
<a name="API_UpdateAccountCustomizations_Errors"></a>

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
<a name="API_UpdateAccountCustomizations_Examples"></a>

### Update all account customization settings
<a name="API_UpdateAccountCustomizations_Example_1"></a>

The following example sets the account color, visible services, and visible Regions in a single request. The response returns the current state of all settings after the update.

#### Sample Request
<a name="API_UpdateAccountCustomizations_Example_1_Request"></a>

```
PATCH /v1/account-customizations HTTP/1.1
Host: uxc.us-east-1.amazonaws.com
Content-type: application/json

{
   "accountColor": "teal",
   "visibleServices": ["s3", "ec2", "lambda"],
   "visibleRegions": ["us-east-1", "us-west-2"]
}
```

#### Sample Response
<a name="API_UpdateAccountCustomizations_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-type: application/json

{
   "accountColor": "teal",
   "visibleServices": ["s3", "ec2", "lambda"],
   "visibleRegions": ["us-east-1", "us-west-2"]
}
```

### Reset a setting to its default behavior
<a name="API_UpdateAccountCustomizations_Example_2"></a>

The following example resets the account color to its default (no color) by setting the value to `none`. The visible services and visible Regions settings are omitted from the request, so they remain unchanged.

#### Sample Request
<a name="API_UpdateAccountCustomizations_Example_2_Request"></a>

```
PATCH /v1/account-customizations HTTP/1.1
Host: uxc.us-east-1.amazonaws.com
Content-type: application/json

{
   "accountColor": "none"
}
```

#### Sample Response
<a name="API_UpdateAccountCustomizations_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Content-type: application/json

{
   "accountColor": "none",
   "visibleServices": ["s3", "ec2", "lambda"],
   "visibleRegions": ["us-east-1", "us-west-2"]
}
```

## Example service identifiers
<a name="w2aab7c14c21"></a>

The following list shows examples of valid service identifiers. For a complete list, call [ListServices](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html).
+  `bedrock` – Amazon Bedrock
+  `cloudformation` – AWS CloudFormation
+  `cloudwatch` – Amazon CloudWatch
+  `connect` – Amazon Connect
+  `dynamodb` – Amazon DynamoDB
+  `ec2` – Amazon Elastic Compute Cloud (Amazon EC2)
+  `ecs` – Amazon Elastic Container Service (Amazon ECS)
+  `eks` – Amazon Elastic Kubernetes Service (Amazon EKS)
+  `events` – Amazon EventBridge
+  `iot` – AWS IoT Core
+  `kinesisvideo` – Amazon Kinesis Video Streams
+  `lambda` – AWS Lambda
+  `lightsail` – Amazon Lightsail
+  `rds` – Amazon Relational Database Service (Amazon RDS)
+  `s3` – Amazon Simple Storage Service (Amazon S3)
+  `sagemaker` – Amazon SageMaker AI
+  `secretsmanager` – AWS Secrets Manager
+  `ssm` – AWS Systems Manager
+  `states` – AWS Step Functions
+  `vpc` – Amazon Virtual Private Cloud (Amazon VPC)

## See Also
<a name="API_UpdateAccountCustomizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/uxc-2024-07-01/UpdateAccountCustomizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/uxc-2024-07-01/UpdateAccountCustomizations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Experience Customization Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awsconsolehelpdocs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AssociateIamRoleToResource.html
---

# AssociateIamRoleToResource
<a name="API_AssociateIamRoleToResource"></a>

Associates an AWS Identity and Access Management (IAM) service role with a specified resource to enable AWS service integration.

## Request Syntax
<a name="API_AssociateIamRoleToResource_RequestSyntax"></a>

```
{
   "awsIntegration": "{{string}}",
   "iamRoleArn": "{{string}}",
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateIamRoleToResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [awsIntegration](#API_AssociateIamRoleToResource_RequestSyntax) **   <a name="odb-AssociateIamRoleToResource-request-awsIntegration"></a>
The AWS integration configuration settings for the AWS Identity and Access Management (IAM) service role association.
Type: String
Valid Values: `KmsTde`
Required: Yes

 ** [iamRoleArn](#API_AssociateIamRoleToResource_RequestSyntax) **   <a name="odb-AssociateIamRoleToResource-request-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role to associate with the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: Yes

 ** [resourceArn](#API_AssociateIamRoleToResource_RequestSyntax) **   <a name="odb-AssociateIamRoleToResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the target resource to associate with the AWS Identity and Access Management (IAM) service role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-[a-z]?|aws-iso):odb:[a-z0-9-]+:\d{12}:(?:cloud-vm-cluster|cloud-autonomous-vm-cluster|exadb-vm-cluster)/[a-z0-9-_]+`
Required: Yes

## Response Elements
<a name="API_AssociateIamRoleToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateIamRoleToResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_AssociateIamRoleToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/AssociateIamRoleToResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AssociateIamRoleToResource)

---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RegisterResource.html
---

# RegisterResource
<a name="API_RegisterResource"></a>

Registers the resource as managed by the Data Catalog.

To add or update data, AWS Lake Formation needs read/write access to the chosen data location. Choose a role that you know has permission to do this, or choose the AWSServiceRoleForLakeFormationDataAccess service-linked role. When you register the first Amazon S3 path, the service-linked role and a new inline policy are created on your behalf. Lake Formation adds the first path to the inline policy and attaches it to the service-linked role. When you register subsequent paths, Lake Formation adds the path to the existing policy.

The following request registers a new location and gives Lake Formation permission to use the service-linked role to access that location.

 `ResourceArn = arn:aws:s3:::my-bucket/ UseServiceLinkedRole = true`

If `UseServiceLinkedRole` is not set to true, you must provide or set the `RoleArn`:

 `arn:aws:iam::12345:role/my-data-access-role`

## Request Syntax
<a name="API_RegisterResource_RequestSyntax"></a>

```
POST /RegisterResource HTTP/1.1
Content-type: application/json

{
   "ExpectedResourceOwnerAccount": "{{string}}",
   "HybridAccessEnabled": {{boolean}},
   "ResourceArn": "{{string}}",
   "RoleArn": "{{string}}",
   "UseServiceLinkedRole": {{boolean}},
   "WithFederation": {{boolean}},
   "WithPrivilegedAccess": {{boolean}}
}
```

## URI Request Parameters
<a name="API_RegisterResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExpectedResourceOwnerAccount](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-ExpectedResourceOwnerAccount"></a>
The AWS account that owns the AWS Glue tables associated with specific Amazon S3 locations.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** [HybridAccessEnabled](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-HybridAccessEnabled"></a>
 Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies.
Type: Boolean
Required: No

 ** [ResourceArn](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to register.
Type: String
Required: Yes

 ** [RoleArn](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-RoleArn"></a>
The identifier for the role that registers the resource.
Type: String
Pattern: `arn:aws:iam::[0-9]*:role/.*`
Required: No

 ** [UseServiceLinkedRole](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-UseServiceLinkedRole"></a>
Designates an AWS Identity and Access Management (IAM) service-linked role by registering this role with the Data Catalog. A service-linked role is a unique type of IAM role that is linked directly to Lake Formation.
For more information, see [Using Service-Linked Roles for Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/service-linked-roles.html).
Type: Boolean
Required: No

 ** [WithFederation](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-WithFederation"></a>
Whether or not the resource is a federated resource.
Type: Boolean
Required: No

 ** [WithPrivilegedAccess](#API_RegisterResource_RequestSyntax) **   <a name="lakeformation-RegisterResource-request-WithPrivilegedAccess"></a>
Grants the calling principal the permissions to perform all supported Lake Formation operations on the registered data location.
Type: Boolean
Required: No

## Response Syntax
<a name="API_RegisterResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_RegisterResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RegisterResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 403

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_RegisterResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/RegisterResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/RegisterResource)

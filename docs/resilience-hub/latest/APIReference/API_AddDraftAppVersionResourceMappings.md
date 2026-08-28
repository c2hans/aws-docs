---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_AddDraftAppVersionResourceMappings.html
---

# AddDraftAppVersionResourceMappings
<a name="API_AddDraftAppVersionResourceMappings"></a>

Adds the source of resource-maps to the draft version of an application. During assessment, AWS Resilience Hub will use these resource-maps to resolve the latest physical ID for each resource in the application template. For more information about different types of resources supported by AWS Resilience Hub and how to add them in your application, see [Step 2: How is your application managed?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/how-app-manage.html) in the AWS Resilience Hub User Guide.

## Request Syntax
<a name="API_AddDraftAppVersionResourceMappings_RequestSyntax"></a>

```
POST /add-draft-app-version-resource-mappings HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "resourceMappings": [
      {
         "appRegistryAppName": "{{string}}",
         "eksSourceName": "{{string}}",
         "logicalStackName": "{{string}}",
         "mappingType": "{{string}}",
         "physicalResourceId": {
            "awsAccountId": "{{string}}",
            "awsRegion": "{{string}}",
            "identifier": "{{string}}",
            "type": "{{string}}"
         },
         "resourceGroupName": "{{string}}",
         "resourceName": "{{string}}",
         "terraformSourceName": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_AddDraftAppVersionResourceMappings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AddDraftAppVersionResourceMappings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_AddDraftAppVersionResourceMappings_RequestSyntax) **   <a name="resiliencehub-AddDraftAppVersionResourceMappings-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [resourceMappings](#API_AddDraftAppVersionResourceMappings_RequestSyntax) **   <a name="resiliencehub-AddDraftAppVersionResourceMappings-request-resourceMappings"></a>
Mappings used to map logical resources from the template to physical resources. You can use the mapping type `CFN_STACK` if the application template uses a logical stack name. Or you can map individual resources by using the mapping type `RESOURCE`. We recommend using the mapping type `CFN_STACK` if the application is backed by a CloudFormation stack.
Type: Array of [ResourceMapping](API_ResourceMapping.md) objects
Required: Yes

## Response Syntax
<a name="API_AddDraftAppVersionResourceMappings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appVersion": "string",
   "resourceMappings": [
      {
         "appRegistryAppName": "string",
         "eksSourceName": "string",
         "logicalStackName": "string",
         "mappingType": "string",
         "physicalResourceId": {
            "awsAccountId": "string",
            "awsRegion": "string",
            "identifier": "string",
            "type": "string"
         },
         "resourceGroupName": "string",
         "resourceName": "string",
         "terraformSourceName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AddDraftAppVersionResourceMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_AddDraftAppVersionResourceMappings_ResponseSyntax) **   <a name="resiliencehub-AddDraftAppVersionResourceMappings-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_AddDraftAppVersionResourceMappings_ResponseSyntax) **   <a name="resiliencehub-AddDraftAppVersionResourceMappings-response-appVersion"></a>
The version of the application.
Type: String
Pattern: `\S{1,50}`

 ** [resourceMappings](#API_AddDraftAppVersionResourceMappings_ResponseSyntax) **   <a name="resiliencehub-AddDraftAppVersionResourceMappings-response-resourceMappings"></a>
List of sources that are used to map a logical resource from the template to a physical resource. You can use sources such as AWS CloudFormation, Terraform state files, AppRegistry applications, or Amazon EKS.
Type: Array of [ResourceMapping](API_ResourceMapping.md) objects

## Errors
<a name="API_AddDraftAppVersionResourceMappings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions.
HTTP Status Code: 403

 ** ConflictException **
This exception occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
 ** resourceId **
The identifier of the resource that the exception applies to.
 ** resourceType **
The type of the resource that the exception applies to.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
This exception occurs when you have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_AddDraftAppVersionResourceMappings_Examples"></a>

### Example CloudFormation Request
<a name="API_AddDraftAppVersionResourceMappings_Example_1"></a>

The following is an example request payload.

#### Sample Request
<a name="API_AddDraftAppVersionResourceMappings_Example_1_Request"></a>

```
{
  "appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/dd058443-7e2f-410d-bee6-c634cb3edb39",
  "resourceMappings": [
    {
      "logicalStackName": "my-stack-name",
      "mappingType": "CfnStack",
      "physicalResourceId": {
        "identifier": "arn:aws:cloudformation:us-west-2:444455556666:stack/my-stack-name/fe0e1e00-03eb-11ee-8796-02038f8a9691",
        "type": "Arn"
      }
    }
  ]
}
```

### Sample CloudFormation Response
<a name="API_AddDraftAppVersionResourceMappings_Example_2"></a>

The following is an example response payload.

#### Sample Response
<a name="API_AddDraftAppVersionResourceMappings_Example_2_Response"></a>

```
{
  "appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/dd058443-7e2f-410d-bee6-c634cb3edb39",
  "appVersion": "draft",
  "resourceMappings": [
    {
      "logicalStackName": "my-stack-name",
      "mappingType": "CfnStack",
      "physicalResourceId": {
        "identifier": "arn:aws:cloudformation:us-west-2:444455556666:stack/my-stack-name/fe0e1e00-03eb-11ee-8796-02038f8a9691",
        "type": "Arn"
      }
    }
  ]
}
```

### Example Terraform Request
<a name="API_AddDraftAppVersionResourceMappings_Example_3"></a>

The following is an example request payload.

#### Sample Request
<a name="API_AddDraftAppVersionResourceMappings_Example_3_Request"></a>

```
{
"appArn": " arn:aws:resiliencehub:us-west-2:444455556666:app/4019253a-0c99-4d30-be32-b14dd46d1c3d",
   "resourceMappings": [
      {
"mappingType": "Terraform",
         "physicalResourceId": {
            "awsAccountId": "444455556666",
            "awsRegion": "us-west-2",
            "identifier": "s3://my-terraform-bucket/my/path/application-state-file.tfstate",
            "type": "Native"
         },

      }
   ]
}
```

### Sample Terraform Response
<a name="API_AddDraftAppVersionResourceMappings_Example_4"></a>

The following is an example response payload.

#### Sample Response
<a name="API_AddDraftAppVersionResourceMappings_Example_4_Response"></a>

```
{
  "appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/4019253a-0c99-4d30-be32-b14dd46d1c3d",
  "resourceMappings": [
    {
      "terraformSourceName": "application-state-file.tfstate",
      "mappingType": "Terraform",
      "physicalResourceId": {
        "identifier": "s3://terraform-bucket/web-app/latest/application-state-file.tfstate",
        "type": "Native",
        "awsRegion": "us-west-2",
        "awsAccountId": "444455556666"
      }
    }
  ]
}
```

### Sample AppRegistry Request
<a name="API_AddDraftAppVersionResourceMappings_Example_5"></a>

The following is an example request payload.

#### Sample Request
<a name="API_AddDraftAppVersionResourceMappings_Example_5_Request"></a>

```
{
"appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/4019253a-0c99-4d30-be32-b14dd46d1c3d",
"resourceMappings": [
      {
         "appRegistryAppName": "MyWebApp",
         "mappingType": "AppRegistryApp",
         "physicalResourceId": {
            "identifier": "arn:aws:servicecatalog:us-west-2:444455556666:/applications/123456789012abcdefghijklmnop",
            "type": "ARN"
         },
      }
   ]
}
```

### Sample AppRegistry Response
<a name="API_AddDraftAppVersionResourceMappings_Example_6"></a>

The following is an example response payload.

#### Sample Response
<a name="API_AddDraftAppVersionResourceMappings_Example_6_Response"></a>

```
{
  "appArn": "aws:resiliencehub:us-west-2:444455556666:app/4019253a-0c99-4d30-be32-b14dd46d1c3d",
  "resourceMappings": [
    {
      "appRegistryAppName": "MyWebApp",
      "mappingType": "AppRegistryApp",
      "physicalResourceId": {
        "identifier": "arn:aws:servicecatalog:us-west-2:444455556666:/applications/123456789012abcdefghijklmnop",
        "type": "Arn"
      }
    }
  ]
}
```

### Sample Amazon EKS Request
<a name="API_AddDraftAppVersionResourceMappings_Example_7"></a>

The following is an example request payload.

#### Sample Request
<a name="API_AddDraftAppVersionResourceMappings_Example_7_Request"></a>

```
{
"appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/98f97a67-228f-40b3-8b2b-29da919c68cc",
   "resourceMappings": [
      {
         "eksSourceName": "my-cluster/my-namespace",
         "mappingType": "EKS",
         "physicalResourceId": {
            "identifier": "arn:aws:eks:us-west-2:444455556666:cluster/my-cluster/my-namespace",
            "type": "Arn"
         },
      }
   ]
}
```

### Sample Amazon EKS Response
<a name="API_AddDraftAppVersionResourceMappings_Example_8"></a>

The following is an example response payload.

#### Sample Response
<a name="API_AddDraftAppVersionResourceMappings_Example_8_Response"></a>

```
{
"appArn": "arn:aws:resiliencehub:us-west-2:444455556666:app/98f97a67-228f-40b3-8b2b-29da919c68cc",
   "resourceMappings": [
      {
"eksSourceName": "my-cluster/my-namespace",
         "mappingType": "EKS",
         "physicalResourceId": {
"identifier": "arn:aws:eks:us-west-2:444455556666:cluster/my-cluster/my-namespace",
            "type": "Arn"
         },
      }
   ]
}
```

## See Also
<a name="API_AddDraftAppVersionResourceMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/AddDraftAppVersionResourceMappings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

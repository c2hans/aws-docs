---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_PutDraftAppVersionTemplate.html
---

# PutDraftAppVersionTemplate
<a name="API_PutDraftAppVersionTemplate"></a>

Adds or updates the app template for an AWS Resilience Hub application draft version.

**Note**
 AWS Resilience Hub blocks manual grouping and automatically groups certain resources based on their dependencies and configurations to prevent configuration errors and ensure accurate resilience assessment results. For more information, see [Managing Application Components](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.html).

## Request Syntax
<a name="API_PutDraftAppVersionTemplate_RequestSyntax"></a>

```
POST /put-draft-app-version-template HTTP/1.1
Content-type: application/json

{
   "appArn": "{{string}}",
   "appTemplateBody": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutDraftAppVersionTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutDraftAppVersionTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appArn](#API_PutDraftAppVersionTemplate_RequestSyntax) **   <a name="resiliencehub-PutDraftAppVersionTemplate-request-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [appTemplateBody](#API_PutDraftAppVersionTemplate_RequestSyntax) **   <a name="resiliencehub-PutDraftAppVersionTemplate-request-appTemplateBody"></a>
A JSON string that provides information about your application structure. To learn more about the `appTemplateBody` template, see the sample template provided in the *Examples* section.
The `appTemplateBody` JSON string has the following structure:
+  ** `resources` **

  The list of logical resources that must be included in the AWS Resilience Hub application.

  Type: Array
**Note**
Don't add the resources that you want to exclude.

  Each `resources` array item includes the following fields:
  +  * `logicalResourceId` *

    Logical identifier of the resource.

    Type: Object

    Each `logicalResourceId` object includes the following fields:
    +  `identifier`

      Identifier of the resource.

      Type: String
    +  `logicalStackName`

      The name of the AWS CloudFormation stack this resource belongs to.

      Type: String
    +  `resourceGroupName`

      The name of the resource group this resource belongs to.

      Type: String
    +  `terraformSourceName`

      The name of the Terraform S3 state file this resource belongs to.

      Type: String
    +  `eksSourceName`

      Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
**Note**
This parameter accepts values in "eks-cluster/namespace" format.

      Type: String
  +  * `type` *

    The type of resource.

    Type: string
  +  * `name` *

    The name of the resource.

    Type: String
  +  `additionalInfo`

    Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
+  ** `appComponents` **

  List of AppComponents that this resource belongs to. If an AppComponent is not part of the AWS Resilience Hub application, it will be added.

  Type: Array

  Each `appComponents` array item includes the following fields:
  +  `name`

    Name of the AppComponent.

    Type: String
  +  `type`

    Type of AppComponent. For more information about the types of AppComponent, see [Grouping resources in an AppComponent](https://docs.aws.amazon.com/resilience-hub/latest/userguide/AppComponent.grouping.html).

    Type: String
  +  `resourceNames`

    The list of included resources that are assigned to the AppComponent.

    Type: Array of strings
  +  `additionalInfo`

    Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
+  ** `excludedResources` **

  The list of logical resource identifiers to be excluded from the application.

  Type: Array
**Note**
Don't add the resources that you want to include.

  Each `excludedResources` array item includes the following fields:
  +  * `logicalResourceIds` *

    Logical identifier of the resource.

    Type: Object
**Note**
You can configure only one of the following fields:
 `logicalStackName`
 `resourceGroupName`
 `terraformSourceName`
 `eksSourceName`

    Each `logicalResourceIds` object includes the following fields:
    +  `identifier`

      Identifier of the resource.

      Type: String
    +  `logicalStackName`

      The name of the AWS CloudFormation stack this resource belongs to.

      Type: String
    +  `resourceGroupName`

      The name of the resource group this resource belongs to.

      Type: String
    +  `terraformSourceName`

      The name of the Terraform S3 state file this resource belongs to.

      Type: String
    +  `eksSourceName`

      Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
**Note**
This parameter accepts values in "eks-cluster/namespace" format.

      Type: String
+  ** `version` **

   AWS Resilience Hub application version.
+  `additionalInfo`

  Additional configuration parameters for an AWS Resilience Hub application. If you want to implement `additionalInfo` through the AWS Resilience Hub console rather than using an API call, see [Configure the application configuration parameters](https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html).
**Note**
Currently, this parameter accepts a key-value mapping (in a string format) of only one failover region and one associated account.
Key: `"failover-regions"`
Value: `"[{"region":"<REGION>", "accounts":[{"id":"<ACCOUNT_ID>"}]}]"`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 409600.
Pattern: `[\w\s:,-\.'\/{}\[\]:"\\]+`
Required: Yes

## Response Syntax
<a name="API_PutDraftAppVersionTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appVersion": "string"
}
```

## Response Elements
<a name="API_PutDraftAppVersionTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_PutDraftAppVersionTemplate_ResponseSyntax) **   <a name="resiliencehub-PutDraftAppVersionTemplate-response-appArn"></a>
Amazon Resource Name (ARN) of the AWS Resilience Hub application. The format for this ARN is: arn:`partition`:resiliencehub:`region`:`account`:app/`app-id`. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference* guide.
Type: String
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [appVersion](#API_PutDraftAppVersionTemplate_ResponseSyntax) **   <a name="resiliencehub-PutDraftAppVersionTemplate-response-appVersion"></a>
The version of the application.
Type: String
Pattern: `\S{1,50}`

## Errors
<a name="API_PutDraftAppVersionTemplate_Errors"></a>

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

 ** ThrottlingException **
This exception occurs when you have exceeded the limit on the number of requests per second.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **
This exception occurs when a request is not valid.
HTTP Status Code: 400

## Examples
<a name="API_PutDraftAppVersionTemplate_Examples"></a>

### Sample appTemplateBody template
<a name="API_PutDraftAppVersionTemplate_Example_1"></a>

This example illustrates one usage of PutDraftAppVersionTemplate.

```
{
	"resources": [{
		"logicalResourceId": {
			"identifier": "testResourceID1",
			"logicalStackName": "testResourceStack1",
			"resourceGroupName": null
		},
		"type": "AWS::RDS::DBInstance",
		"name": "testResourceName"
	}],
	"appComponents": [{
			"name": "testappcomponent-test",
			"type": "AWS::ResilienceHub::AppComponent",
			"resourceNames": [
				"testResourceName"
			]
		},
		{
			"name": "testappcommon",
			"type": "AWS::ResilienceHub::AppComponent",
			"resourceNames": "[testResourceName]"
		}
	],
	"excludedResources": {
		"logicalResourceIds": [{
			"identifier": "testResourceID2",
			"logicalStackName": "testResourceStack2",
			"resourceGroupName": ""
		}]
	},
	"version": 2.0
}
```

## See Also
<a name="API_PutDraftAppVersionTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/PutDraftAppVersionTemplate)

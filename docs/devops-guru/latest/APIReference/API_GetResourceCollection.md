---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_GetResourceCollection.html
---

# GetResourceCollection
<a name="API_GetResourceCollection"></a>

 Returns lists of AWS resources that are of the specified resource collection type. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.

## Request Syntax
<a name="API_GetResourceCollection_RequestSyntax"></a>

```
GET /resource-collections/{{ResourceCollectionType}}?NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourceCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_GetResourceCollection_RequestSyntax) **   <a name="DevOpsGuru-GetResourceCollection-request-uri-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ResourceCollectionType](#API_GetResourceCollection_RequestSyntax) **   <a name="DevOpsGuru-GetResourceCollection-request-uri-ResourceCollectionType"></a>
 The type of AWS resource collection to return. You can use AWS CloudFormation stacks or AWS tags as a resource collection. You can use your resource collection to specify the resources you want DevOps Guru to analyze.
Valid Values: `AWS_CLOUD_FORMATION | AWS_SERVICE | AWS_TAGS`
Required: Yes

## Request Body
<a name="API_GetResourceCollection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ResourceCollection": {
      "CloudFormation": {
         "StackNames": [ "string" ]
      },
      "Tags": [
         {
            "AppBoundaryKey": "string",
            "TagValues": [ "string" ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetResourceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetResourceCollection_ResponseSyntax) **   <a name="DevOpsGuru-GetResourceCollection-response-NextToken"></a>
The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`

 ** [ResourceCollection](#API_GetResourceCollection_ResponseSyntax) **   <a name="DevOpsGuru-GetResourceCollection-response-ResourceCollection"></a>
 The requested list of AWS resource collections. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.
Type: [ResourceCollectionFilter](API_ResourceCollectionFilter.md) object

## Errors
<a name="API_GetResourceCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource could not be found
 ** ResourceId **
 The ID of the AWS resource that could not be found.
 ** ResourceType **
 The type of the AWS resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to a request throttling.
 ** QuotaCode **
 The code of the quota that was exceeded, causing the throttling exception.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the throttling exception can be retried.
 ** ServiceCode **
 The code of the service that caused the throttling exception.
HTTP Status Code: 429

 ** ValidationException **
 Contains information about data passed in to a field during a request that is not valid.
 ** Fields **
 An array of fields that are associated with the validation exception.
 ** Message **
 A message that describes the validation exception.
 ** Reason **
 The reason the validation exception was thrown.
HTTP Status Code: 400

## See Also
<a name="API_GetResourceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/GetResourceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/GetResourceCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

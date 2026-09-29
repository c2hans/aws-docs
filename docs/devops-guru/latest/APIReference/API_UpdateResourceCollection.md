---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateResourceCollection.html
---

# UpdateResourceCollection
<a name="API_UpdateResourceCollection"></a>

**Note**
End of support notice: On September 30, 2027, AWS will end support for Amazon DevOps Guru. After September 30, 2027, you will no longer be able to access the Amazon DevOps Guru console or Amazon DevOps Guru resources. For more information, see [Amazon DevOps Guru end of support](https://docs.aws.amazon.com/devops-guru/latest/userguide/devops-guru-end-of-support.html).

 Updates the collection of resources that DevOps Guru analyzes. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks. This method also creates the IAM role required for you to use DevOps Guru.

## Request Syntax
<a name="API_UpdateResourceCollection_RequestSyntax"></a>

```
PUT /resource-collections HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "ResourceCollection": {
      "CloudFormation": {
         "StackNames": [ "{{string}}" ]
      },
      "Tags": [
         {
            "AppBoundaryKey": "{{string}}",
            "TagValues": [ "{{string}}" ]
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_UpdateResourceCollection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateResourceCollection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_UpdateResourceCollection_RequestSyntax) **   <a name="DevOpsGuru-UpdateResourceCollection-request-Action"></a>
 Specifies if the resource collection in the request is added or deleted to the resource collection.
Type: String
Valid Values: `ADD | REMOVE`
Required: Yes

 ** [ResourceCollection](#API_UpdateResourceCollection_RequestSyntax) **   <a name="DevOpsGuru-UpdateResourceCollection-request-ResourceCollection"></a>
 Contains information used to update a collection of AWS resources.
Type: [UpdateResourceCollectionFilter](API_UpdateResourceCollectionFilter.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateResourceCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateResourceCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateResourceCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 403

 ** ConflictException **
 An exception that is thrown when a conflict occurs.
 ** ResourceId **
 The ID of the AWS resource in which a conflict occurred.
 ** ResourceType **
 The type of the AWS resource in which a conflict occurred.
HTTP Status Code: 409

 ** InternalServerException **
An internal failure in an Amazon service occurred.
 ** RetryAfterSeconds **
 The number of seconds after which the action that caused the internal server exception can be retried.
HTTP Status Code: 500

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
<a name="API_UpdateResourceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devops-guru-2020-12-01/UpdateResourceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/UpdateResourceCollection)

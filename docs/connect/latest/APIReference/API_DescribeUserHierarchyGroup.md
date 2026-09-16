---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUserHierarchyGroup.html
---

# DescribeUserHierarchyGroup
<a name="API_DescribeUserHierarchyGroup"></a>

Describes the specified hierarchy group.

## Request Syntax
<a name="API_DescribeUserHierarchyGroup_RequestSyntax"></a>

```
GET /user-hierarchy-groups/{{InstanceId}}/{{HierarchyGroupId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeUserHierarchyGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [HierarchyGroupId](#API_DescribeUserHierarchyGroup_RequestSyntax) **   <a name="connect-DescribeUserHierarchyGroup-request-uri-HierarchyGroupId"></a>
The identifier of the hierarchy group.
Required: Yes

 ** [InstanceId](#API_DescribeUserHierarchyGroup_RequestSyntax) **   <a name="connect-DescribeUserHierarchyGroup-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeUserHierarchyGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeUserHierarchyGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "HierarchyGroup": {
      "Arn": "string",
      "HierarchyPath": {
         "LevelFive": {
            "Arn": "string",
            "Id": "string",
            "LastModifiedRegion": "string",
            "LastModifiedTime": number,
            "Name": "string"
         },
         "LevelFour": {
            "Arn": "string",
            "Id": "string",
            "LastModifiedRegion": "string",
            "LastModifiedTime": number,
            "Name": "string"
         },
         "LevelOne": {
            "Arn": "string",
            "Id": "string",
            "LastModifiedRegion": "string",
            "LastModifiedTime": number,
            "Name": "string"
         },
         "LevelThree": {
            "Arn": "string",
            "Id": "string",
            "LastModifiedRegion": "string",
            "LastModifiedTime": number,
            "Name": "string"
         },
         "LevelTwo": {
            "Arn": "string",
            "Id": "string",
            "LastModifiedRegion": "string",
            "LastModifiedTime": number,
            "Name": "string"
         }
      },
      "Id": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "LevelId": "string",
      "Name": "string",
      "Tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_DescribeUserHierarchyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HierarchyGroup](#API_DescribeUserHierarchyGroup_ResponseSyntax) **   <a name="connect-DescribeUserHierarchyGroup-response-HierarchyGroup"></a>
Information about the hierarchy group.
Type: [HierarchyGroup](API_HierarchyGroup.md) object

## Errors
<a name="API_DescribeUserHierarchyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeUserHierarchyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeUserHierarchyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeUserHierarchyGroup)

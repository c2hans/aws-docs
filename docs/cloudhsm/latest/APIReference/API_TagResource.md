---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds or overwrites one or more tags for the specified AWS CloudHSM cluster.

 **Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM resource in a different AWS account.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceId](#API_TagResource_RequestSyntax) **   <a name="CloudHSMV2-TagResource-request-ResourceId"></a>
The cluster identifier (ID) for the cluster that you are tagging. To find the cluster ID, use [DescribeClusters](API_DescribeClusters.md).
Type: String
Pattern: `(?:cluster|backup)-[2-7a-zA-Z]{11,16}`
Required: Yes

 ** [TagList](#API_TagResource_RequestSyntax) **   <a name="CloudHSMV2-TagResource-request-TagList"></a>
A list of one or more tags.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CloudHsmAccessDeniedException **
The request was rejected because the requester does not have permission to perform the requested operation.
HTTP Status Code: 400

 ** CloudHsmInternalFailureException **
The request was rejected because of an AWS CloudHSM internal failure. The request can be retried.
HTTP Status Code: 500

 ** CloudHsmInvalidRequestException **
The request was rejected because it is not a valid request.
HTTP Status Code: 400

 ** CloudHsmResourceLimitExceededException **
The request was rejected because it exceeds an AWS CloudHSM limit.
HTTP Status Code: 400

 ** CloudHsmResourceNotFoundException **
The request was rejected because it refers to a resource that cannot be found.
HTTP Status Code: 400

 ** CloudHsmServiceException **
The request was rejected because an error occurred.
HTTP Status Code: 400

 ** CloudHsmTagException **
The request was rejected because of a tagging failure. Verify the tag conditions in all applicable policies, and then retry the request.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/TagResource)

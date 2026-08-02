---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Deletes specified tags from a resource.

**Note**
The WorkloadArn parameter can be a workload ARN, a custom lens ARN, a profile ARN, or review template ARN.

To specify multiple tags, use separate **tagKeys** parameters, for example:

 `DELETE /tags/WorkloadArn?tagKeys=key1&tagKeys=key2`

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{WorkloadArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="wellarchitected-UntagResource-request-uri-TagKeys"></a>
A list of tag keys. Existing tags of the resource whose keys are members of this list are removed from the resource.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [WorkloadArn](#API_UntagResource_RequestSyntax) **   <a name="wellarchitected-UntagResource-request-uri-WorkloadArn"></a>
The ARN for the workload.
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource was not found.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 404

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/UntagResource)

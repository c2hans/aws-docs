---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribeObjects.html
---

# DescribeObjects
<a name="API_DescribeObjects"></a>

Gets the object definitions for a set of objects associated with the pipeline. Object definitions are composed of a set of fields that define the properties of the object.

## Request Syntax
<a name="API_DescribeObjects_RequestSyntax"></a>

```
{
   "evaluateExpressions": {{boolean}},
   "marker": "{{string}}",
   "objectIds": [ "{{string}}" ],
   "pipelineId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeObjects_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [evaluateExpressions](#API_DescribeObjects_RequestSyntax) **   <a name="DP-DescribeObjects-request-evaluateExpressions"></a>
Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.
Type: Boolean
Required: No

 ** [marker](#API_DescribeObjects_RequestSyntax) **   <a name="DP-DescribeObjects-request-marker"></a>
The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call `DescribeObjects` with the marker value from the previous call to retrieve the next set of results.
Type: String
Required: No

 ** [objectIds](#API_DescribeObjects_RequestSyntax) **   <a name="DP-DescribeObjects-request-objectIds"></a>
The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to `DescribeObjects`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [pipelineId](#API_DescribeObjects_RequestSyntax) **   <a name="DP-DescribeObjects-request-pipelineId"></a>
The ID of the pipeline that contains the object definitions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

## Response Syntax
<a name="API_DescribeObjects_ResponseSyntax"></a>

```
{
   "hasMoreResults": boolean,
   "marker": "string",
   "pipelineObjects": [
      {
         "fields": [
            {
               "key": "string",
               "refValue": "string",
               "stringValue": "string"
            }
         ],
         "id": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeObjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [hasMoreResults](#API_DescribeObjects_ResponseSyntax) **   <a name="DP-DescribeObjects-response-hasMoreResults"></a>
Indicates whether there are more results to return.
Type: Boolean

 ** [marker](#API_DescribeObjects_ResponseSyntax) **   <a name="DP-DescribeObjects-response-marker"></a>
The starting point for the next page of results. To view the next page of results, call `DescribeObjects` again with this marker value. If the value is null, there are no more results.
Type: String

 ** [pipelineObjects](#API_DescribeObjects_ResponseSyntax) **   <a name="DP-DescribeObjects-response-pipelineObjects"></a>
An array of object definitions.
Type: Array of [PipelineObject](API_PipelineObject.md) objects

## Errors
<a name="API_DescribeObjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineDeletedException **
The specified pipeline has been deleted.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_DescribeObjects_Examples"></a>

### Example
<a name="API_DescribeObjects_Example_1"></a>

This example illustrates one usage of DescribeObjects.

#### Sample Request
<a name="API_DescribeObjects_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.DescribeObjects
Content-Length: 98
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE",
 "objectIds":
  ["Schedule"],
 "evaluateExpressions": true}
```

#### Sample Response
<a name="API_DescribeObjects_Example_1_Response"></a>

```
x-amzn-RequestId: 4c18ea5d-0777-11e2-8a14-21bb8a1f50ef
Content-Type: application/x-amz-json-1.1
Content-Length: 1488
Date: Mon, 12 Nov 2012 17:50:53 GMT

{"hasMoreResults": false,
 "pipelineObjects":
  [
    {"fields":
      [
        {"key": "startDateTime",
         "stringValue": "2012-12-12T00:00:00"},
        {"key": "parent",
         "refValue": "Default"},
        {"key": "@sphere",
         "stringValue": "COMPONENT"},
        {"key": "type",
         "stringValue": "Schedule"},
        {"key": "period",
         "stringValue": "1 hour"},
        {"key": "endDateTime",
         "stringValue": "2012-12-21T18:00:00"},
        {"key": "@version",
         "stringValue": "1"},
        {"key": "@status",
         "stringValue": "PENDING"},
        {"key": "@pipelineId",
         "stringValue": "df-06372391ZG65EXAMPLE"}
      ],
     "id": "Schedule",
     "name": "Schedule"}
  ]
}
```

## See Also
<a name="API_DescribeObjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/DescribeObjects)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/DescribeObjects)

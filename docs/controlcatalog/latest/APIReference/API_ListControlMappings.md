---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListControlMappings.html
---

# ListControlMappings
<a name="API_ListControlMappings"></a>

Returns a paginated list of control mappings from the Control Catalog. Control mappings show relationships between controls and other entities, such as common controls or compliance frameworks.

## Request Syntax
<a name="API_ListControlMappings_RequestSyntax"></a>

```
POST /list-control-mappings?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "Filter": {
      "CommonControlArns": [ "{{string}}" ],
      "ControlArns": [ "{{string}}" ],
      "MappingTypes": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_ListControlMappings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListControlMappings_RequestSyntax) **   <a name="controlcatalog-ListControlMappings-request-uri-MaxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListControlMappings_RequestSyntax) **   <a name="controlcatalog-ListControlMappings-request-uri-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_ListControlMappings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Filter](#API_ListControlMappings_RequestSyntax) **   <a name="controlcatalog-ListControlMappings-request-Filter"></a>
An optional filter that narrows the results to specific control mappings based on control ARNs, common control ARNs, or mapping types.
Type: [ControlMappingFilter](API_ControlMappingFilter.md) object
Required: No

## Response Syntax
<a name="API_ListControlMappings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ControlMappings": [
      {
         "ControlArn": "string",
         "Mapping": { ... },
         "MappingType": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListControlMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ControlMappings](#API_ListControlMappings_ResponseSyntax) **   <a name="controlcatalog-ListControlMappings-response-ControlMappings"></a>
The list of control mappings that the ListControlMappings API returns.
Type: Array of [ControlMapping](API_ControlMapping.md) objects

 ** [NextToken](#API_ListControlMappings_ResponseSyntax) **   <a name="controlcatalog-ListControlMappings-response-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_ListControlMappings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_ListControlMappings_Examples"></a>

### Retrieve information about control mappings
<a name="API_ListControlMappings_Example_1"></a>

Use this operation to retrieve information about a control, including common controls and compliance frameworks.

#### Sample Request
<a name="API_ListControlMappings_Example_1_Request"></a>

```
aws controlcatalog list-control-mappings --filter "{\"ControlArns\":[\"arn:aws:controlcatalog:::control/br8o4lzgtvz3he7f8sxg76k7q\"],\"MappingTypes\": [\"FRAMEWORK\"]}" --max-results 2 --region us-east-1
```

#### Sample Response
<a name="API_ListControlMappings_Example_1_Response"></a>

```
    {
        "ControlMappings": [
            {
                "ControlArn": "arn:aws:controlcatalog:::control/br8o4lzgtvz3he7f8sxg76k7q",
                "MappingType": "FRAMEWORK",
                "Mapping": {
                    "Framework": {
                        "Name": "FedRAMP-r4",
                        "Item": "SC-7"
                    }
                }
            },
            {
                "ControlArn": "arn:aws:controlcatalog:::control/br8o4lzgtvz3he7f8sxg76k7q",
                "MappingType": "FRAMEWORK",
                "Mapping": {
                    "Framework": {
                        "Name": "ISO-IEC-27001:2013-Annex-A",
                        "Item": "A.9.1.2"
                    }
                }
            }
        ],
        "NextToken": "AAQA-EFRSURBSGkyaGRScGRQSmM5bnVFTUJMeFlHTHJqajdJSnFvSzkwb2ZscUR5TGs2UzNBR05BUUJZbmJjdEk2Y2tWRC9nWldjdkFBQUFmakI4QmdrcWhraUc5dzBCQndhZ2J6QnRBZ0VBTUdnR0NTcUdTSWIzRFFFSEFUQWVCZ2xnaGtnQlpRTUVBUzR3RVFRTXBmbEdBVWxERXl6R0MzUy9BZ0VRZ0R0VzNTZUlBdktBUHl5WmhnZG9zYVdhWDY4MDM0ZXd3SlYvb3ovQ09Ebmt1K0UvZWI4ZlNzV1VqMUkycG83ZEhSN3BBNmROOEF2Z1VJU0E5dz09ZqxBPRvCSvgdsbQ68I5yAK16M2Lf6p3OEiZ8zWjF41Byzd7h-r4eCDqFszhxe-Jtbl9EGekKLY06VXgEgQ=="
    }
```

## See Also
<a name="API_ListControlMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/ListControlMappings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ListControlMappings)

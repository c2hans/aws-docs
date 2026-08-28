---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchPredefinedAttributes.html
---

# SearchPredefinedAttributes
<a name="API_SearchPredefinedAttributes"></a>

Searches predefined attributes that meet certain criteria. A *predefined attribute* is made up of a name and a value. You can use predefined attributes for:
+ Routing proficiency (for example, agent certification) that has predefined values (for example, a list of possible certifications). For more information, see [Create predefined attributes for routing contacts to agents](https://docs.aws.amazon.com/connect/latest/adminguide/predefined-attributes.html).
+ Contact information that varies between transfers or conferences, such as the name of the business unit handling the contact. For more information, see [Use contact segment attributes](https://docs.aws.amazon.com/connect/latest/adminguide/use-contact-segment-attributes.html).

For the predefined attributes per instance quota, see [Connect Customer quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#connect-quotas).

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_SearchPredefinedAttributes_RequestSyntax"></a>

```
POST /search-predefined-attributes HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "PredefinedAttributeSearchCriteria"
      ],
      "OrConditions": [
         "PredefinedAttributeSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchPredefinedAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchPredefinedAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchPredefinedAttributes_RequestSyntax) **   <a name="connect-SearchPredefinedAttributes-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchPredefinedAttributes_RequestSyntax) **   <a name="connect-SearchPredefinedAttributes-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchPredefinedAttributes_RequestSyntax) **   <a name="connect-SearchPredefinedAttributes-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchPredefinedAttributes_RequestSyntax) **   <a name="connect-SearchPredefinedAttributes-request-SearchCriteria"></a>
The search criteria to be used to return predefined attributes.
Type: [PredefinedAttributeSearchCriteria](API_PredefinedAttributeSearchCriteria.md) object
Required: No

## Response Syntax
<a name="API_SearchPredefinedAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "PredefinedAttributes": [
      {
         "AttributeConfiguration": {
            "EnableValueValidationOnAssociation": boolean,
            "IsReadOnly": boolean
         },
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "Name": "string",
         "Purposes": [ "string" ],
         "Values": { ... }
      }
   ]
}
```

## Response Elements
<a name="API_SearchPredefinedAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchPredefinedAttributes_ResponseSyntax) **   <a name="connect-SearchPredefinedAttributes-response-ApproximateTotalCount"></a>
The approximate number of predefined attributes which matched your search query.
Type: Long

 ** [NextToken](#API_SearchPredefinedAttributes_ResponseSyntax) **   <a name="connect-SearchPredefinedAttributes-response-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [PredefinedAttributes](#API_SearchPredefinedAttributes_ResponseSyntax) **   <a name="connect-SearchPredefinedAttributes-response-PredefinedAttributes"></a>
Predefined attributes matched by the search criteria.
Type: Array of [PredefinedAttribute](API_PredefinedAttribute.md) objects

## Errors
<a name="API_SearchPredefinedAttributes_Errors"></a>

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

## Examples
<a name="API_SearchPredefinedAttributes_Examples"></a>

### Example
<a name="API_SearchPredefinedAttributes_Example_1"></a>

The following example shows a request and response.

```
POST https://connect.us-west-2.amazonaws.com/search-predefined-attributes HTTP/1.1
Content-type: application/json
{
    "InstanceId": "InstanceId",
    "MaxResults": 5,
    "SearchCriteria": {
        "StringCondition": {
            "ComparisonType": "EXACT",
            "FieldName": "purposes",
            "Value": "proficiency"
        }
    }
}

Response:
{
    "ApproximateTotalCount": 20,
    "NextToken": "nextToken,
    "PredefinedAttributes": [
        {
            "AttributeConfiguration": {
                "EnableValueValidationOnAssociation": false,
                "IsReadOnly": false
            },
            "LastModifiedRegion": null,
            "LastModifiedTime": null,
            "Name": "Name1",
            "Purposes": [
                "proficiency"
            ],
            "Values": {
                "StringList": [
                    "value1",
                    "value2"
                ]
            }
        },
        {
            "AttributeConfiguration": {
                "EnableValueValidationOnAssociation": false,
                "IsReadOnly": false
            },
            "LastModifiedRegion": null,
            "LastModifiedTime": null,
            "Name": "Name2",
            "Purposes": [
                "contact-attributes-search",
                "proficiency"
            ],
            "Values": {
                "StringList": [
                    "value1",
                    "value2"
                ]
            }
        }
    ]
}
```

## See Also
<a name="API_SearchPredefinedAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchPredefinedAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchPredefinedAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

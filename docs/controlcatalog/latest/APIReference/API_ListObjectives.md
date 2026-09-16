---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListObjectives.html
---

# ListObjectives
<a name="API_ListObjectives"></a>

Returns a paginated list of objectives from the Control Catalog.

You can apply an optional filter to see the objectives that belong to a specific domain. If you don’t provide a filter, the operation returns all objectives.

## Request Syntax
<a name="API_ListObjectives_RequestSyntax"></a>

```
POST /objectives?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "ObjectiveFilter": {
      "Domains": [
         {
            "Arn": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_ListObjectives_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListObjectives_RequestSyntax) **   <a name="controlcatalog-ListObjectives-request-uri-MaxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListObjectives_RequestSyntax) **   <a name="controlcatalog-ListObjectives-request-uri-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_ListObjectives_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ObjectiveFilter](#API_ListObjectives_RequestSyntax) **   <a name="controlcatalog-ListObjectives-request-ObjectiveFilter"></a>
An optional filter that narrows the results to a specific domain.
This filter allows you to specify one domain ARN at a time. Passing multiple ARNs in the `ObjectiveFilter` isn’t supported.
Type: [ObjectiveFilter](API_ObjectiveFilter.md) object
Required: No

## Response Syntax
<a name="API_ListObjectives_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Objectives": [
      {
         "Arn": "string",
         "CreateTime": number,
         "Description": "string",
         "Domain": {
            "Arn": "string",
            "Name": "string"
         },
         "LastUpdateTime": number,
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListObjectives_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListObjectives_ResponseSyntax) **   <a name="controlcatalog-ListObjectives-response-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Objectives](#API_ListObjectives_ResponseSyntax) **   <a name="controlcatalog-ListObjectives-response-Objectives"></a>
The list of objectives that the `ListObjectives` API returns.
Type: Array of [ObjectiveSummary](API_ObjectiveSummary.md) objects

## Errors
<a name="API_ListObjectives_Errors"></a>

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
<a name="API_ListObjectives_Examples"></a>

### Filtering objectives by domain
<a name="API_ListObjectives_Example_1"></a>

You can use the `ListObjectives` operation to return a filtered list of objectives. For example, you can see all of the objectives that fall under a specific domain such as *Asset management*.

**To filter results by domain**

1. Use the `ListDomains` operation to see the domains that you can use as filters.

1. Find the domain that you want to use as a filter, and take note of its ARN.

1. Use the `ListObjectives` operation and include the `Domains` parameter. For the `ARN` attribute value, specify the domain ARN from step 2.
**Note**
Keep in mind that you can only filter by one domain at a time. Specifying multiple domain ARNs isn’t supported.
If you want to filter by more than one ARN, we recommend that you run the `ListObjectives` operation separately for each ARN.

The sample request below uses the following domain ARN as a filter: `arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq`. This ARN represents the *Asset management* domain.

The sample response shows the result that the `ListObjectives` operation might return if five objectives matched the filter criteria of *Asset management*.

#### Sample Request
<a name="API_ListObjectives_Example_1_Request"></a>

```
{
    "ObjectiveFilter": {
        "Domains": [{
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq"
        }]
    }
}
```

#### Sample Response
<a name="API_ListObjectives_Example_1_Response"></a>

```
{
    "Objectives": [{
        "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
        "CreateTime": 1.710288E9,
        "Description": "This control objective focuses on maintaining an accurate and up-to-date inventory of assets, including hardware, software, and data, to protect organization investments from harm or loss.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset inventory management"
    }, {
        "Arn": "arn:aws:controlcatalog:::objective/90gifwthorhxhxq7m0rtss98u",
        "CreateTime": 1.710288E9,
        "Description": "This control objective focuses on classifying assets based on their value, sensitivity, and criticality to the organization to manage investment risk and unauthorized access to assets and information.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset classification"
    }, {
        "Arn": "arn:aws:controlcatalog:::objective/3frxxgl64u9kzttiuheywykf7",
        "CreateTime": 1.710288E9,
        "Description": "This control objective focuses on maintaining the availability and integrity of assets, including performance management, regular maintenance, and repairs to protect and extract the maximum value of the organization's IT investments.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset maintenance"
    }, {
        "Arn": "arn:aws:controlcatalog:::objective/5ve4jodybrg8wnky75fp50sbf",
        "CreateTime": 1.710288E9,
        "Description": "This control objective focuses on managing assets throughout their entire lifecycle, including acquisition, deployment, use, and retirement. This helps manage risks associated with asset costs by ensuring optimum asset productivity, performance, efficiency, and profitability.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset lifecycle management"
    }, {
        "Arn": "arn:aws:controlcatalog:::objective/ags5wgkyvwriix77zegtwhyo9",
        "CreateTime": 1.710288E9,
        "Description": "This control objective focuses on preventing asset loss, and responding to and recovering lost, stolen, or damaged assets to contribute to the organization's profitability by reducing losses.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset loss prevention, response, and recovery"
    }]
}
```

## See Also
<a name="API_ListObjectives_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/ListObjectives)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ListObjectives)

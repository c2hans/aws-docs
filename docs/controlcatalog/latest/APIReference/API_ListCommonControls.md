---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListCommonControls.html
---

# ListCommonControls
<a name="API_ListCommonControls"></a>

Returns a paginated list of common controls from the AWS Control Catalog.

You can apply an optional filter to see common controls that have a specific objective. If you don’t provide a filter, the operation returns all common controls.

## Request Syntax
<a name="API_ListCommonControls_RequestSyntax"></a>

```
POST /common-controls?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "CommonControlFilter": {
      "Objectives": [
         {
            "Arn": "{{string}}"
         }
      ]
   }
}
```

## URI Request Parameters
<a name="API_ListCommonControls_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListCommonControls_RequestSyntax) **   <a name="controlcatalog-ListCommonControls-request-uri-MaxResults"></a>
The maximum number of results on a page or for an API request call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListCommonControls_RequestSyntax) **   <a name="controlcatalog-ListCommonControls-request-uri-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Request Body
<a name="API_ListCommonControls_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CommonControlFilter](#API_ListCommonControls_RequestSyntax) **   <a name="controlcatalog-ListCommonControls-request-CommonControlFilter"></a>
An optional filter that narrows the results to a specific objective.
This filter allows you to specify one objective ARN at a time. Passing multiple ARNs in the `CommonControlFilter` isn’t supported.
Type: [CommonControlFilter](API_CommonControlFilter.md) object
Required: No

## Response Syntax
<a name="API_ListCommonControls_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CommonControls": [
      {
         "Arn": "string",
         "CreateTime": number,
         "Description": "string",
         "Domain": {
            "Arn": "string",
            "Name": "string"
         },
         "LastUpdateTime": number,
         "Name": "string",
         "Objective": {
            "Arn": "string",
            "Name": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCommonControls_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CommonControls](#API_ListCommonControls_ResponseSyntax) **   <a name="controlcatalog-ListCommonControls-response-CommonControls"></a>
The list of common controls that the `ListCommonControls` API returns.
Type: Array of [CommonControlSummary](API_CommonControlSummary.md) objects

 ** [NextToken](#API_ListCommonControls_ResponseSyntax) **   <a name="controlcatalog-ListCommonControls-response-NextToken"></a>
The pagination token that's used to fetch the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

## Errors
<a name="API_ListCommonControls_Errors"></a>

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
<a name="API_ListCommonControls_Examples"></a>

### Filtering common controls by objective
<a name="API_ListCommonControls_Example_1"></a>

You can use the `ListCommonControls` operation to return a filtered list of common controls. For example, you can see a list of all common controls that have the objective of *Asset inventory management*.

**To filter results by objective**

1. Use the `ListObjectives` operation to see the objectives that you can use as filters.

1. Find the objective that you want to use as a filter, and take note of its ARN.

1. Use the `ListCommonControls` operation and include the `ControlObjectives` parameter. For the `ARN` attribute value, specify the objective ARN from step 2.
**Note**
Keep in mind that you can only filter by one objective at a time. Specifying multiple objective ARNs isn’t supported.
If you want to filter by more than one ARN, we recommend that you run the `ListCommonControls` operation separately for each ARN.

The sample request below uses the following objective ARN as a filter: `arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn`. This ARN represents the *Asset inventory management* objective.

The sample response shows the result that the `ListCommonControls` operation might return if seven common controls matched the filter criteria of *Asset inventory management*.

#### Sample Request
<a name="API_ListCommonControls_Example_1_Request"></a>

```
{
    "CommonControlFilter": {
        "Objectives": [{
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn"
        }]
    }
}
```

#### Sample Response
<a name="API_ListCommonControls_Example_1_Response"></a>

```
{
    "CommonControls": [{
        "Arn": "arn:aws:controlcatalog:::common-control/d4s7ik8fgv8082v3x31hifzcc",
        "CreateTime": 1.710288E9,
        "Description": "Reconcile the organization's asset inventory with other data sources, and conduct asset audits to verify the accuracy of the asset inventory.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset inventory reconciliation and audit",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/1ukpmkewk4i92tjmhsvewi4y7",
        "CreateTime": 1.710288E9,
        "Description": "Maintain an asset inventory of organization authorized and existing hardware, software, and media. Where possible, utilize automated tools to facilitate the discovery and ongoing tracking of such assets.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Inventory of authorized assets and automated discovery",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/c0qrxhefhmxkbq22tiejp3enn",
        "CreateTime": 1.710288E9,
        "Description": "Take appropriate actions to identify and resolve unauthorized assets within the network environment on a periodic and consistent basis. Appropriate actions include, but are not limited to, removing the asset from the network, quarantining the asset, or denying connectivity to the asset.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Unauthorized asset management",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/5u2qgwuw3z1y0lrof60yf6264",
        "CreateTime": 1.710288E9,
        "Description": "Track all physical and digital assets to ensure proper use and protection. Monitor status of digital assets like systems, devices, software, applications, and data throughout their lifecycle. Use real-time location tracking for physical assets through technologies like GPS and RFID where possible.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset tracking",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/1tejgq26c0djpzgskw31uscm4",
        "CreateTime": 1.710288E9,
        "Description": "Regularly analyze hardware and software assets to assess criticality, usage, value, and other key metrics. Generate comprehensive reports on the asset inventory.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset inventory analysis and reporting",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/eg1hxxu2e77a7w2wv79quwaxl",
        "CreateTime": 1.710288E9,
        "Description": "Define asset owners, including who has responsibility for managing each asset.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset ownership",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }, {
        "Arn": "arn:aws:controlcatalog:::common-control/ec1fxlvgtcxlf2nzremqcca7r",
        "CreateTime": 1.710288E9,
        "Description": "Track and monitor asset status, including whether they are operational, in maintenance, or out of service.",
        "Domain": {
            "Arn": "arn:aws:controlcatalog:::domain/d4msesd9vvmzmmuvlv06m92uq",
            "Name": "Asset management"
        },
        "LastUpdateTime": 1.710288E9,
        "Name": "Asset status tracking",
        "Objective": {
            "Arn": "arn:aws:controlcatalog:::objective/ad11p1961s8erra9m185wa1nn",
            "Name": "Asset inventory management"
        }
    }]
}
```

## See Also
<a name="API_ListCommonControls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/ListCommonControls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ListCommonControls)
